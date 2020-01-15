import c4d

def tag_copy(obj_origin, tag_type, obj_target):
    obj_tags = obj_origin.GetTags()
    for tag in obj_tags:
        if tag.CheckType(tag_type):
            tag = tag.GetClone()
            obj_target.InsertTag(tag)
            return tag
        else:
            None

def main():
    obj = op
    obj2 = obj.GetNext()

    tag_copy(obj, c4d.Tvertexmap, obj2)

    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()