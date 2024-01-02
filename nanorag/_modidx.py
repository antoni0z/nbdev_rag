# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/nanorag',
                'doc_host': 'https://antoni0z.github.io',
                'git_url': 'https://github.com/antoni0z/nanorag',
                'lib_path': 'nanorag'},
  'syms': { 'nanorag.base': { 'nanorag.base.BaseNode': ('base.html#basenode', 'nanorag/base.py'),
                              'nanorag.base.BaseNode.__init__': ('base.html#basenode.__init__', 'nanorag/base.py'),
                              'nanorag.base.BaseNode.__repr__': ('base.html#basenode.__repr__', 'nanorag/base.py'),
                              'nanorag.base.BaseNode.__set_id': ('base.html#basenode.__set_id', 'nanorag/base.py'),
                              'nanorag.base.BaseNode.create_embedding': ('base.html#basenode.create_embedding', 'nanorag/base.py'),
                              'nanorag.base.BaseNode.get_embedding': ('base.html#basenode.get_embedding', 'nanorag/base.py'),
                              'nanorag.base.Document': ('base.html#document', 'nanorag/base.py'),
                              'nanorag.base.Document.__calculate_hash': ('base.html#document.__calculate_hash', 'nanorag/base.py'),
                              'nanorag.base.Document.__chunk_text': ('base.html#document.__chunk_text', 'nanorag/base.py'),
                              'nanorag.base.Document.__init__': ('base.html#document.__init__', 'nanorag/base.py'),
                              'nanorag.base.Document.__repr__': ('base.html#document.__repr__', 'nanorag/base.py'),
                              'nanorag.base.Document.__set_id': ('base.html#document.__set_id', 'nanorag/base.py'),
                              'nanorag.base.Document.__update_hash': ('base.html#document.__update_hash', 'nanorag/base.py'),
                              'nanorag.base.Document.copy': ('base.html#document.copy', 'nanorag/base.py'),
                              'nanorag.base.Document.create_nodes_from_doc': ( 'base.html#document.create_nodes_from_doc',
                                                                               'nanorag/base.py'),
                              'nanorag.base.Document.delete': ('base.html#document.delete', 'nanorag/base.py'),
                              'nanorag.base.Document.get_embedding': ('base.html#document.get_embedding', 'nanorag/base.py'),
                              'nanorag.base.Document.metadata': ('base.html#document.metadata', 'nanorag/base.py'),
                              'nanorag.base.Document.name': ('base.html#document.name', 'nanorag/base.py'),
                              'nanorag.base.Document.save': ('base.html#document.save', 'nanorag/base.py'),
                              'nanorag.base.Document.source_id': ('base.html#document.source_id', 'nanorag/base.py'),
                              'nanorag.base.Document.text': ('base.html#document.text', 'nanorag/base.py'),
                              'nanorag.base.TextNode': ('base.html#textnode', 'nanorag/base.py'),
                              'nanorag.base.TextNode.__calculate_hash': ('base.html#textnode.__calculate_hash', 'nanorag/base.py'),
                              'nanorag.base.TextNode.__init__': ('base.html#textnode.__init__', 'nanorag/base.py'),
                              'nanorag.base.TextNode.__repr__': ('base.html#textnode.__repr__', 'nanorag/base.py'),
                              'nanorag.base.TextNode.create_embedding': ('base.html#textnode.create_embedding', 'nanorag/base.py'),
                              'nanorag.base.TextNode.get_embedding': ('base.html#textnode.get_embedding', 'nanorag/base.py')},
            'nanorag.context': { 'nanorag.context.ModelContext': ('context.html#modelcontext', 'nanorag/context.py'),
                                 'nanorag.context.ModelContext.__init__': ('context.html#modelcontext.__init__', 'nanorag/context.py'),
                                 'nanorag.context.ModelContext.set_default': ( 'context.html#modelcontext.set_default',
                                                                               'nanorag/context.py')},
            'nanorag.llm': { 'nanorag.llm.LLM': ('llm.html#llm', 'nanorag/llm.py'),
                             'nanorag.llm.LLM.__call__': ('llm.html#llm.__call__', 'nanorag/llm.py'),
                             'nanorag.llm.LLM.__init__': ('llm.html#llm.__init__', 'nanorag/llm.py'),
                             'nanorag.llm.PromptTemplate': ('llm.html#prompttemplate', 'nanorag/llm.py'),
                             'nanorag.llm.PromptTemplate.__call__': ('llm.html#prompttemplate.__call__', 'nanorag/llm.py'),
                             'nanorag.llm.PromptTemplate.__init__': ('llm.html#prompttemplate.__init__', 'nanorag/llm.py')},
            'nanorag.loaders': { 'nanorag.loaders.DocumentBridge': ('loaders.html#documentbridge', 'nanorag/loaders.py'),
                                 'nanorag.loaders.DocumentBridge.__init__': ('loaders.html#documentbridge.__init__', 'nanorag/loaders.py'),
                                 'nanorag.loaders.DocumentBridge.to_doc': ('loaders.html#documentbridge.to_doc', 'nanorag/loaders.py'),
                                 'nanorag.loaders.DocumentBridge.to_nodes': ('loaders.html#documentbridge.to_nodes', 'nanorag/loaders.py'),
                                 'nanorag.loaders.DocumentBridge.to_subdocuments': ( 'loaders.html#documentbridge.to_subdocuments',
                                                                                     'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader': ('loaders.html#pdfloader', 'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader.__generate_id': ('loaders.html#pdfloader.__generate_id', 'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader.__init__': ('loaders.html#pdfloader.__init__', 'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader.get_documents': ('loaders.html#pdfloader.get_documents', 'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader.get_images': ('loaders.html#pdfloader.get_images', 'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader.load_pdf': ('loaders.html#pdfloader.load_pdf', 'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader.load_random_pdf': ( 'loaders.html#pdfloader.load_random_pdf',
                                                                                'nanorag/loaders.py'),
                                 'nanorag.loaders.PDFLoader.pdf_validator': ('loaders.html#pdfloader.pdf_validator', 'nanorag/loaders.py')},
            'nanorag.store': { 'nanorag.store.BaseDocumentStore': ('store.html#basedocumentstore', 'nanorag/store.py'),
                               'nanorag.store.BaseDocumentStore.__init__': ('store.html#basedocumentstore.__init__', 'nanorag/store.py'),
                               'nanorag.store.BaseDocumentStore.add': ('store.html#basedocumentstore.add', 'nanorag/store.py'),
                               'nanorag.store.BaseDocumentStore.delete': ('store.html#basedocumentstore.delete', 'nanorag/store.py'),
                               'nanorag.store.BaseDocumentStore.get': ('store.html#basedocumentstore.get', 'nanorag/store.py'),
                               'nanorag.store.BaseDocumentStore.ids': ('store.html#basedocumentstore.ids', 'nanorag/store.py'),
                               'nanorag.store.DocumentStore': ('store.html#documentstore', 'nanorag/store.py'),
                               'nanorag.store.DocumentStore.__init__': ('store.html#documentstore.__init__', 'nanorag/store.py'),
                               'nanorag.store.DocumentStore.add': ('store.html#documentstore.add', 'nanorag/store.py'),
                               'nanorag.store.DocumentStore.delete': ('store.html#documentstore.delete', 'nanorag/store.py'),
                               'nanorag.store.DocumentStore.get': ('store.html#documentstore.get', 'nanorag/store.py'),
                               'nanorag.store.DocumentStore.group_by_source_id': ( 'store.html#documentstore.group_by_source_id',
                                                                                   'nanorag/store.py'),
                               'nanorag.store.DocumentStore.ids': ('store.html#documentstore.ids', 'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore': ('store.html#postgresdocumentstore', 'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.__create_if_not_exists': ( 'store.html#postgresdocumentstore.__create_if_not_exists',
                                                                                               'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.__enter__': ( 'store.html#postgresdocumentstore.__enter__',
                                                                                  'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.__exit__': ( 'store.html#postgresdocumentstore.__exit__',
                                                                                 'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.__init__': ( 'store.html#postgresdocumentstore.__init__',
                                                                                 'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.add': ('store.html#postgresdocumentstore.add', 'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.close': ('store.html#postgresdocumentstore.close', 'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.delete': ( 'store.html#postgresdocumentstore.delete',
                                                                               'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.get': ('store.html#postgresdocumentstore.get', 'nanorag/store.py'),
                               'nanorag.store.PostgresDocumentStore.ids': ('store.html#postgresdocumentstore.ids', 'nanorag/store.py')},
            'nanorag.utils': {'nanorag.utils.hash_input': ('utils.html#hash_input', 'nanorag/utils.py')}}}
