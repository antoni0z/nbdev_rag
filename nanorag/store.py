# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_store.ipynb.

# %% auto 0
__all__ = ['BaseDocumentStore', 'DocumentStore', 'PostgresDocumentStore']

# %% ../nbs/03_store.ipynb 3
from .base import Document, abstractmethod, ABC
from .context import ModelContext
from .loaders import PDFLoader, DocumentBridge
from typing import Union, List, Dict, Optional
from uuid import UUID
import os
import psycopg2
from collections import defaultdict
from psycopg2.extensions import AsIs
import json


# %% ../nbs/03_store.ipynb 5
class BaseDocumentStore(ABC):
    """
    Base class for document storage"""
    def __init__(self, documents : Dict[str, Document] = {}):
        pass
    @abstractmethod    
    def add(self, document: Document):
        pass
    @abstractmethod 
    def ids(self):
        pass
    @abstractmethod    
    def delete(self, ids: Union[List, str]):
        pass
    @abstractmethod
    def get(self, ids: Union[UUID, List]):
        pass
        

# %% ../nbs/03_store.ipynb 6
class DocumentStore(BaseDocumentStore):
    """Key value type document store that store documents by their id in a dictionary.
    Also checks for duplicates via hashing and doesn't admit them. Compatible with both nodes and documents."""
    def __init__(self, documents : Union[List[Document], Document]= []):
        if isinstance(documents, list):
            self.documents = {document.id: document for document in documents}
        elif isinstance(documents, Document):
            self.documents = {documents.id: documents}

        
    def add(self, document: Union[List[Document], Document]) -> str:
        doc_ids = []
        if isinstance(document, list):
            for doc in document:
                self.add(doc)
                doc_ids.append(doc.id)
        else:
            for stored_document in self.documents:
                if self.documents[stored_document].hash == document.hash:
                    return f"You tried to add a duplicate document: {document.hash}"
                elif self.documents[stored_document].id == document.id:
                    self.documents[document.id] = document
                    return f"Document with id {document.id} has been updated"
            self.documents[document.id] =  document
        return f"The following documents have been added: {doc_ids}"

    def ids(self):
        doc_ids = [doc for doc in self.documents]
        return doc_ids

    def delete(self, documents: Union[List[Document], Document]):
        deleted_docs = []
        if isinstance(documents, List):
            for document in documents:
                deleted_doc = self.documents.pop(document.id, None)
                if deleted_doc is not None:
                    deleted_docs.append(deleted_doc)
        elif isinstance(documents, Document):
            deleted_doc = self.documents.pop(documents.id, None)
            if deleted_doc is not None:
                deleted_docs.append(deleted_doc)
        return f"The following docs have been deleted: {deleted_docs}"
        
    def get(self, ids: Optional[Union[List[UUID], UUID]] = None) -> Optional[Union[Document, List[Document]]]:
        if ids == None:
            ids = self.ids()
            if isinstance(ids, List):
                if len(ids) == 0:
                    return None
        if isinstance(ids, List):
            docs = [self.documents[id] for id in ids if id in self.documents]
            if len(docs) == 0:
                return None
            return docs
        elif isinstance(ids, UUID):
            doc = self.documents.get(ids, None)
            if doc is None:
                return None
            return doc
        return None
    def group_by_source_id(self, source_id = None): #Other type of filters can be added
        grouped_documents = defaultdict(list)
        for doc in self.documents.values():
            if source_id == None:
                grouped_documents[doc.source_id].append(doc)
            elif doc.source_id not in grouped_documents or doc.source_id == source_id:
                grouped_documents[doc.source_id].append(doc)
        if source_id != None:
            return grouped_documents[source_id]
        return dict(grouped_documents)
#NOTE: Could I store both nodes and docs in same store? 

# %% ../nbs/03_store.ipynb 7
#TODO: Handle doc modifications and sync with nodes.
#TODO: Support for relationships in Store. 
class PostgresDocumentStore(BaseDocumentStore):
    
    def __init__(self,db_uri, table_name = 'documents'):
        self.table_name = table_name
        self.schema_name = 'public'
        self.conn = psycopg2.connect(db_uri)
        self.cur = self.conn.cursor()
        self.__create_if_not_exists()

    def add(self, documents: Union[List[Document], Document]):
        """This method adds documents or list of documents to the Database. By default it upsert and 
        doesn't admit duplicates. A duplicate is defined as a document with the same hash. Which as
        of now is calculated with the name, text, metadata and source. """
        if isinstance(documents, Document):
            documents = [documents]

        if isinstance(documents, list):
            docs_to_insert = [
            (
                str(doc.id), 
                str(doc.source_id), 
                doc.name, 
                doc.text.replace('\x00', ''),  # Remove null bytes
                json.dumps(doc.metadata), 
                doc.hash,
                doc.metadata.get('category', 'UNCATEGORIZED'),
                doc.doc_separator
            ) 
            for doc in documents
            ]
            try:
                self.cur.executemany(f"""
                INSERT INTO {self.table_name} (id, source_id, name, text, metadata, hash, category, doc_separator)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET text = EXCLUDED.text, metadata = EXCLUDED.metadata, hash = EXCLUDED.hash, category = EXCLUDED.category, doc_separator = EXCLUDED.doc_separator, name = EXCLUDED.name;
                """,docs_to_insert)
                self.conn.commit()
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None
        doc_ids = [doc[0] for doc in docs_to_insert]
        return f"The following documents have been added: {doc_ids}"
        #For now not including any relationship
    def ids(self):
        try:
            self.cur.execute(f"""
            SELECT id
            FROM {self.schema_name}.{self.table_name};
            """)
            result = self.cur.fetchall()
            if len(result) == 0:
                return None
            return [doc[0] for doc in result]
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
    def delete(self, documents: Union[List[Document], Document]):
        """Deletes documents from the database. """
        if isinstance(documents, Document):
            documents = [documents]
        if isinstance(documents, list):
            doc_ids = [str(doc.id) for doc in documents]
            try:
                self.cur.execute(f"""
                DELETE FROM {self.schema_name}.{self.table_name}
                WHERE id = ANY(%s::uuid[]);
                """, (doc_ids,))
                self.conn.commit()
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None
            return f"The following documents have been deleted: {doc_ids}"
        return None
    def get(self, ids : Optional[Union[str, List[str]]] = None):
        def convert_to_doc(result): 
            id, source_id, name, text, metadata, category, doc_separator = result
            doc = Document(id = id if id else None, 
                        source_id = source_id if source_id else None, 
                        name = name if name else None, 
                        text = text if text else None, 
                        metadata = metadata if metadata else None, 
                        doc_separator = doc_separator if doc_separator else None, 
                        store = self)
            doc.metadata['category'] = category if category else None
            return doc
        if ids:
            try:
                if isinstance(ids, str):
                    ids = [ids]
                if isinstance(ids, list):
                    ids = ids
                self.cur.execute(f"""SELECT id, source_id, name, text, metadata, category, doc_separator
                                    FROM {self.schema_name}.{self.table_name}
                                    WHERE id = ANY(%s::uuid[]);""", (ids,))
                result = self.cur.fetchall()
                if len(result) == 0:
                    return None
                documents = [convert_to_doc(doc) for doc in result]
                return documents
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None
        else:
            try:
                self.cur.execute(f"""
                SELECT id, source_id, name, text, metadata, category, doc_separator
                FROM {self.schema_name}.{self.table_name};
                """)
                result = self.cur.fetchall()
                if len(result) == 0:
                    return None
                documents = [convert_to_doc(doc) for doc in result]
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None
            return documents

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __create_if_not_exists(self):
        """
        Creates a table for storing documents if it doesn't exist in the database,
        returns True if the table already exists and False if it was just created. 
        """
        try:
            self.cur.execute(f"""
                SELECT EXISTS (
                SELECT FROM pg_tables
                WHERE  schemaname = '{self.schema_name}'
                AND    tablename  = '{self.table_name}'
                );
                """)

            table_exists = self.cur.fetchone()[0]

            if not table_exists:
                print('Does not exist')
                self.cur.execute(f"""
                CREATE TABLE {self.table_name} (
                    id UUID PRIMARY KEY,
                    source_id UUID NOT NULL,
                    name TEXT,
                    text TEXT NOT NULL,
                    metadata JSONB,
                    hash TEXT UNIQUE NOT NULL,
                    prev_node UUID,
                    next_node UUID,
                    category VARCHAR(255),
                    doc_separator VARCHAR(255),
                    FOREIGN KEY (prev_node) REFERENCES {self.table_name}(id),
                    FOREIGN KEY (next_node) REFERENCES {self.table_name}(id));
                """)
                self.conn.commit()
                return False
            else:
                return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
        
    def close(self): #To use the syntax, with PostgresDocumentStore(db_uri) as store:
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
#TODO: Great HTML loader. Test diff approaches. 
            
#TODO: Great Markdown loader. Test diff approaches.
