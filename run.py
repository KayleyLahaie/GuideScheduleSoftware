from PySide2 import QtCore, QtGui, QtWidgets
import sys
import stack_gui



app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = stack_gui.Ui_Form()
ui.setupUi(Form)
Form.show()

sys.exit(app.exec_())
