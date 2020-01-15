import c4d
from c4d import utils

def make_editable(obj):
    obj_next = obj.GetNext()
    obj_list = [obj]
    # make obj editable
    obj_poly = c4d.utils.SendModelingCommand(c4d.MCOMMAND_MAKEEDITABLE,obj_list)
    # return obj only
    obj_new = obj_poly[0] ; doc.InsertObject(obj_new)
    # organize new obj in obj manager
    firstObj = doc.GetFirstObject() # get new editable object
    firstObj.InsertBefore(obj_next)

    return obj_new

def main():
    make_editable(op)

    c4d.EventAdd()

if __name__=='__main__':
    main()