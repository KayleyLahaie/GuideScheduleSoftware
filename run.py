from PySide import QtCore, QtGui
import sys
import stack_gui



app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = stack_gui.Ui_Form()
ui.setupUi(Form)
Form.show()

sys.exit(app.exec_())
