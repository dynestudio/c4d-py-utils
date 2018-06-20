import c4d
 
def GetNextObject(op):
    if op == None: return None
 
    if op.GetDown(): return op.GetDown()
 
    while not op.GetNext() and op.GetUp():
        op = op.GetUp()
 
    return op.GetNext()
 
def main():

    print 'checkpoint 01'
    # get first obj
    first_obj = doc.GetFirstObject()
    if first_obj == None: return

    # make the scene obj list
    list_objs = []

    list_objs.append(first_obj)

    print 'checkpoint 02'

    while first_obj:            
        first_obj = GetNextObject(first_obj)
        list_objs.append(first_obj)
        
    c4d.EventAdd() # update the scene

    print 'checkpoint 03'
 
    print list_objs
    print len(list_objs)

if __name__=='__main__':
    main()