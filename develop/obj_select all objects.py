import c4d
 
def GetNextObject(op): # object manager iteration
    if not op: return None
    if op.GetDown(): return op.GetDown()
    while not op.GetNext() and op.GetUp(): op = op.GetUp()
    return op.GetNext()
 
def main():
    # get first obj
    first_obj = doc.GetFirstObject()
    # list of all objects in the scene
    list_objs = []
    # add the first obj
    list_objs.append(first_obj) 

    # obj loop iteration
    while first_obj:          
        first_obj = GetNextObject(first_obj)
        if first_obj:
            list_objs.append(first_obj)
        
    # update the scene
    c4d.EventAdd()

if __name__=='__main__':
    main()