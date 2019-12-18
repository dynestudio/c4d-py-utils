import c4d
from c4d import gui
# Welcome to the world of Python
# Author: Mike Udin, 
# Tutorial here http://mikeudin.net/2018/02/28/cinema-4d-python-grouping/
# 2018

def main():
    
    obs = doc.GetActiveObjects(0)
    
    if not obs:
        gui.MessageDialog('Please select some objects!')
        return
    
    if len(obs) == 1:
        nullm = obs[0].GetMg()
    else:
        nullm = c4d.Matrix()
        nullm.off = sum([ob.GetMg().off for ob in obs])/ len(obs)
    
    doc.StartUndo()
    null = c4d.BaseObject(c4d.Onull)
    null.InsertBefore(obs[0])
    doc.AddUndo(c4d.UNDOTYPE_NEW, null)
    null.SetBit(c4d.BIT_ACTIVE)
    null.SetMg(nullm)
    
    for ob in obs:
        m = ob.GetMg()
        doc.AddUndo(c4d.UNDOTYPE_HIERARCHY_PSR, ob)
        ob.InsertUnderLast(null)
        ob.DelBit(c4d.BIT_ACTIVE)
        ob.SetMg(m)
    
    doc.EndUndo()
    c4d.EventAdd()
    

if __name__=='__main__':
    main()