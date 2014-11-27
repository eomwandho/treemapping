from PyQt4 import QtGui
from ui_tree_mapping_dialog import Ui_TreeMappingDialogBase


class TreeMappingDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_TreeMappingDialogBase()
        self.ui.setupUi(self)