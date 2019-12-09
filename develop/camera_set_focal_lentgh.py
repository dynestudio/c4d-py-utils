import c4d
from c4d import gui

class OptionsDialog(gui.GeDialog):
    IDC_LABELNAME = 10000
    IDC_GROUP_01  = 10001
    IDC_LIST      = 10002
    IDC_INPUT_00  = 10003
    IDC_INPUT_01  = 10004
    IDC_INPUT_02  = 10005
    IDC_INPUT_03  = 10006
    IDC_INPUT_04  = 10007
    IDC_INPUT_05  = 10008
    IDC_INPUT_06  = 10009
    IDC_INPUT_07  = 10010
    IDC_INPUT_08  = 10011


    def CreateLayout(self):
        #title
        self.SetTitle('Set camera focal lentgh')

        # group colums
        self.GroupBegin(self.IDC_GROUP_01, c4d.BFH_CENTER, 2, 2, "Main Group", 0, 100, 10)

        #statics text - description UI
        self.AddStaticText(self.IDC_LABELNAME, c4d.BFH_LEFT, name = 'Focal Lentgh:') 

        #combo box UI - user inputs
        self.AddComboBox(self.IDC_LIST, c4d.BFH_CENTER, initw = 100, inith = 10, specialalign = False)
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_00, "100 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_01, "75 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_02, "55 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_03, "40 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_04, "35 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_05, "29 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_06, "24 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_07, "17 mm")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_08, "14 mm")

        # close group
        self.GroupEnd()

        # Ok/Cancel buttons
        self.AddDlgGroup(c4d.DLG_OK|c4d.DLG_CANCEL)
        self.ok = False

        # set dialog default values
        self.SetInt32(self.IDC_LIST , self.IDC_INPUT_02)

        return True

    def Command(self, id, msg):
        if id == c4d.IDC_OK:
            self.ok = True
            self.get_input = self.GetInt32(self.IDC_LIST)
            self.Close()

        elif id == c4d.IDC_CANCEL:
            self.Close()

        return True

def main():
    # Open the options dialog to let users choose their options.
    dlg = OptionsDialog()
    dlg.Open(c4d.DLG_TYPE_MODAL, defaultw = 100, defaulth = 55)
    if not dlg.ok:
        return

    if dlg.get_input == dlg.IDC_INPUT_00:
        dlg_cam_fl = 100
    elif dlg.get_input == dlg.IDC_INPUT_01:
        dlg_cam_fl = 75
    elif dlg.get_input == dlg.IDC_INPUT_02:
        dlg_cam_fl = 55
    elif dlg.get_input == dlg.IDC_INPUT_03:
        dlg_cam_fl = 40
    elif dlg.get_input == dlg.IDC_INPUT_04:
        dlg_cam_fl = 35
    elif dlg.get_input == dlg.IDC_INPUT_05:
        dlg_cam_fl = 29
    elif dlg.get_input == dlg.IDC_INPUT_06:
        dlg_cam_fl = 24
    elif dlg.get_input == dlg.IDC_INPUT_07:
        dlg_cam_fl = 17
    else:
        dlg_cam_fl = 14

    #---------------------------------------
    # get active camera
    bd = doc.GetActiveBaseDraw()
    camera = bd.GetSceneCamera(doc)
    # change focal lentgh
    camera[c4d.CAMERA_FOCUS] = dlg_cam_fl

    # update scene
    c4d.EventAdd()

if __name__=='__main__':
    main()