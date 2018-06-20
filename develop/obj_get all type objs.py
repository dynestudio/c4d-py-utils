def get_all_objects(op, filter, output):  #get all objects from each type
    while op:
        if filter(op):
            output.append(op)
        get_all_objects(op.GetDown(), filter, output)
        op = op.GetNext()
    return output

aovs = get_all_objects(doc.GetFirstObject(), lambda x: x.CheckType(ARNOLD_AOV), []) # get all cameras from the scene