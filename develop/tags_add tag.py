import c4d

def addTag(obj, tag_ID):
    # get obj tags
    obj_tags = obj.GetTags()

    if not obj_tags:
        tag = obj.MakeTag(tag_ID) # new tag
    else:
        obj_tags_types = [] # list of tag types
        for t in obj_tags:
            obj_tags_types.append(t.GetType())
            if t.GetType() == tag_ID:
                tag = t

        if not tag_ID in obj_tags_types:
            tag = obj.MakeTag(tag_ID)

    c4d.EventAdd() ; return tag

def main():

    obj = doc.SearchObject('Cube')

    tag = addTag(obj, c4d.Tcompositing)


if __name__=='__main__':
    main()