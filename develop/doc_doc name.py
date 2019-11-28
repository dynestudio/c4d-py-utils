import c4d

def get_doc_path():

    doc     = c4d.documents.GetActiveDocument()
    docname=doc.GetDocumentName()
    print docname

if __name__=='__main__':
    get_doc_path()