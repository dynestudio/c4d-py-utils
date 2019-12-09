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

    def CreateLayout(self):
        #title
        self.SetTitle('Title')

        # group colums
        self.GroupBegin(self.IDC_GROUP_01, c4d.BFH_CENTER, 2, 2, "Main Group", 0, 100, 10)

        #statics text - description UI
        self.AddStaticText(self.IDC_LABELNAME, c4d.BFH_LEFT, name = 'What do you want to do with this dialog?') 

        #combo box UI - user inputs
        self.AddComboBox(self.IDC_LIST, c4d.BFH_CENTER, initw = 200, inith = 10, specialalign = False)
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_00, "input 0")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_01, "input 1")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_02, "input 2")
        self.AddChild(self.IDC_LIST, self.IDC_INPUT_03, "input 3")

        # close group
        self.GroupEnd()

        # Ok/Cancel buttons
        self.AddDlgGroup(c4d.DLG_OK|c4d.DLG_CANCEL)
        self.ok = False

        # set dialog default values
        self.SetInt32(self.IDC_LIST , self.IDC_INPUT_00)

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
    dlg.Open(c4d.DLG_TYPE_MODAL, defaultw = 100, defaulth = 50)
    if not dlg.ok:
        return

    print dlg.get_input



if __name__=='__main__':
 main()