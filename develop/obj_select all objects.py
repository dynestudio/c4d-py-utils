import c4d
 
def GetNextObject(op): # object manager iteration
    if not op:
        return None
 
    if op.GetDown():
        return op.GetDown()
 
    while not op.GetNext() and op.GetUp():
        op = op.GetUp()
 
    return op.GetNext()
 
def main():
    # get first obj
    frist_obj = doc.GetFirstObject()
    # list of all objects in the scene
    list_objs = []
    # add the first obj
    list_objs.append(frist_obj)

    # obj loop iteration
    while frist_obj:          
        obj = GetNextObject(frist_obj)
        list_objs.append(obj)
        
    print len(list_objs)
    print list_objs

if __name__=='__main__':
    main()