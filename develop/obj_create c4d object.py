def create_c4d_obj(Obj_ID, name): # create custom objects
    obj = c4d.BaseObject(Obj_ID)
    obj[c4d.ID_BASELIST_NAME] = name
    doc.InsertObject(obj)
    c4d.EventAdd() ; return obj