import os

def getDoc(doc_file_name):
    
    
    doc_path = os.path.dirname(__file__)
    docfilepath = os.path.join(doc_path, doc_file_name)
    
    
    with open(docfilepath, 'r') as f:
        res = f.readlines()
        
        
    return res