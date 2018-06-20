import c4d
from c4d import gui, documents
#Welcome to the world of Python
 
def GetNextObject(op):
    if op == None: return None
 
    if op.GetDown(): return op.GetDown()
 
    while not op.GetNext() and op.GetUp():
        op = op.GetUp()
 
    return op.GetNext()
 
def main():
    obj = doc.GetActiveObject()

    myobject = doc.GetFirstObject()
    if myobject == None: return

    list_objs = []

    while myobject:            
        myobject = GetNextObject(myobject)
        list_objs.append(myobject)
        
    c4d.EventAdd()
 
    print list_objs
    print len(list_objs)

if __name__=='__main__':
    main()