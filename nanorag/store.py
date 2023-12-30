# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_store.ipynb.

# %% auto 0
__all__ = ['BaseDocumentStore', 'DocumentStore']

# %% ../nbs/03_store.ipynb 2
from .base import Document, abstractmethod, ABC
from .context import ModelContext
from typing import Union, List, Dict, Optional
from uuid import UUID

# %% ../nbs/03_store.ipynb 3
class BaseDocumentStore(ABC):
    """
    Base class for document storage"""
    def __init__(self, documents : Dict[str, Document] = {}):
        pass
    @abstractmethod
    def __call__(self, db): #Connect to backend and specific collection parameters
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
        

# %% ../nbs/03_store.ipynb 4
class DocumentStore(BaseDocumentStore):
    """Key value type document store that store documents by their id in a dictionary.
    Also checks for duplicates via hashing and doesn't admit them. Compatible with both nodes and documents."""
    def __init__(self, documents : Union[List[Document], Document]= []):
        if isinstance(documents, list):
            self.documents = {document.id: document for document in documents}
        elif isinstance(documents, Document):
            self.documents = {documents.id: documents}

    def __call__(self, db): #Connect to backend and specific collection parameters
        pass
        
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

    def delete(self, ids: Union[List, str]):
        deleted_docs = []
        if isinstance(ids, List):
            for id in ids:
                deleted_doc = self.documents.pop(id, None)
                if deleted_doc != None:
                    deleted_docs.append(deleted_doc)
        elif isinstance(ids, UUID):
            deleted_doc = self.documents.pop(ids, None)
            print(f'Ids are: {ids} and theoretically deleted doc is {deleted_doc}')
            if deleted_doc != None:
                deleted_docs.append(deleted_doc)
        return f"The following docs have been deleted {deleted_docs}"
        
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
#NOTE: Could I store both nodes and docs in same store? 
