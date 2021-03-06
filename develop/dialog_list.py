import c4d
from c4d import gui

IDC_LABELNAME           = 10000
IDC_POINTS              = 10007
IDC_POINTSOP01          = 10008
IDC_POINTSOP02          = 10009

IDC_LIST                = 10002
IDC_CRYPTOUSERINPUT_00  = 10003
IDC_CRYPTOUSERINPUT_01  = 10004
IDC_CRYPTOUSERINPUT_02  = 10005
IDC_CRYPTOUSERINPUT_03  = 10006

class OptionsDialog(gui.GeDialog):

    def CreateLayout(self):
        #title
        self.SetTitle('Crypto User AOV')
        #statics text - description UI
        self.AddStaticText(IDC_LABELNAME, c4d.BFH_LEFT, name = 'Which Cryptomatte user input are you going to use?') 
        #radiogroup UI - objects IDs definition
        self.AddRadioGroup(IDC_POINTS, c4d.BFV_SCALEFIT, 2, 1)
        self.AddChild(IDC_POINTS, IDC_POINTSOP01, "Different IDs")
        self.AddChild(IDC_POINTS, IDC_POINTSOP02, "Same ID")
        #combo box UI - cryptomatte user input
        self.AddComboBox(IDC_LIST, c4d.BFH_SCALEFIT, initw = 200, inith = 10, specialalign = True)
        self.AddChild(IDC_LIST, IDC_CRYPTOUSERINPUT_00, "input 0")
        self.AddChild(IDC_LIST, IDC_CRYPTOUSERINPUT_01, "input 1")
        self.AddChild(IDC_LIST, IDC_CRYPTOUSERINPUT_02, "input 2")
        self.AddChild(IDC_LIST, IDC_CRYPTOUSERINPUT_03, "input 3")
        # Ok/Cancel buttons
        self.AddDlgGroup(c4d.DLG_OK|c4d.DLG_CANCEL)
        self.ok = False
        return True

    def Command(self, id, msg):

        if id == c4d.IDC_OK:
            self.ok = True
            self.findPName = self.GetInt32(IDC_POINTS)
            self.findCName = self.GetInt32(IDC_LIST)
            self.Close()

        elif id == c4d.IDC_CANCEL:
            self.Close()
            gui.MessageDialog('Please select a user Cryptomatte input user data.')

        return True

def main():
    # Open the options dialog to let users choose their options.
    dlg = OptionsDialog()
    dlg.Open(c4d.DLG_TYPE_MODAL, defaultw = 300, defaulth = 50)
    if not dlg.ok:
        return

    dialog = dlg.findCName
    pdialog = dlg.findPName

    if pdialog == IDC_POINTSOP01:
        pdialog = True
    else:
        pdialog = False

    print dialog
    print pdialog

if __name__=='__main__':
 main()