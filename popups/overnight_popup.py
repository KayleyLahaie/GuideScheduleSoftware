# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogwindow.ui'
#
# Created: Mon Feb 18 18:32:39 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import create_schedule
from create_schedule import schedule_dictionaries

import manage_staff
from manage_staff import staff_util

class Ui_overnight_popup(object):

    def setupUi(self, overnight_popup, num_guides, current_date, trip_role_assignment, DialogBox):

        self.DialogBox = DialogBox
        print(self.DialogBox)

        self.comboBoxes = [0,0,0,0]
        self.labels = [0,0,0,0]

        self.num_guides = num_guides

        self.trip_role_assignment = trip_role_assignment

        print(num_guides)

        overnight_popup.setObjectName("overnight_popup")
        overnight_popup.resize(700, 500)
        overnight_popup.setStyleSheet("color: #ee7838;\n"
                                      "background-color: white;")

        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")

        self.main_label = QtGui.QLabel(overnight_popup)
        self.main_label.setGeometry(QtCore.QRect(25, 25, 650, 50))
        self.main_label.setFont(font)
        self.main_label.setStyleSheet( " background-color: #006898;\n"
                                            " border-radius: 5%;\n"
                                            "padding-left: 15px;")
        self.main_label.setObjectName("main_label")


        x_text = 175
        y_text = 112.5

        x_label = 25
        y_label = 94

        for n in range(num_guides):
            print("n = ", n)

            guides_available = manage_staff.staff_util.get_guides_can_work(
                                    4,
                                    create_schedule.schedule_dictionaries.guide_roles_converter[n]
                                )

            self.comboBoxes[n] = QtGui.QComboBox(overnight_popup)
            self.comboBoxes[n].setGeometry(QtCore.QRect(x_text, y_text, 200, 30))
            self.comboBoxes[n].setObjectName("comboBox")

            self.comboBoxes[n].addItem("Choose Guide...")

            for m in range(len(guides_available)):
                self.comboBoxes[n].addItem(guides_available[m])

            self.labels[n] = QtGui.QLabel(overnight_popup)
            self.labels[n].setGeometry(QtCore.QRect(x_label, y_label, 125, 60))
            self.labels[n].setStyleSheet("")
            self.labels[n].setObjectName(
                create_schedule.schedule_dictionaries.overnight_dialog_guide_label_name[n]
            )

            y_text += 50
            y_label += 62.5


        if(num_guides == 1):

            guides_available = manage_staff.staff_util.get_guides_can_work(
                                    4,
                                    create_schedule.schedule_dictionaries.guide_roles_converter[4]
                                )

            self.safety_name = QtGui.QComboBox(overnight_popup)
            self.safety_name.setGeometry(QtCore.QRect(x_text, y_text, 200, 30))
            self.safety_name.setObjectName("comboBox")

            self.safety_name.addItem("Choose Guide...")

            for m in range(len(guides_available)):
                self.safety_name.addItem(guides_available[m])

            self.safety_label = QtGui.QLabel(overnight_popup)
            self.safety_label.setGeometry(QtCore.QRect(x_label, y_label, 81, 41))
            self.safety_label.setStyleSheet("")
            self.safety_label.setObjectName("safety_label")

        self.submit = QtGui.QPushButton(overnight_popup)
        self.submit.setGeometry(QtCore.QRect(575, 400, 100, 35))
        self.submit.setStyleSheet("  border: none;\n"
                                "  padding: 0.5%;\n"
                                "  cursor: pointer;\n"
                                "  font-family: special_font;\n"
                                "  font-size: 12pt;\n"
                                "  border-radius: 3%;\n"
                                "  opacity: 0.9;\n"
                                "  background-color: #006898;\n"
                                "  color: #ee7838;")
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.submit_staff)
        self.submit.show()

        self.retranslateUi(overnight_popup, num_guides, self.labels, current_date)
        QtCore.QMetaObject.connectSlotsByName(overnight_popup)

    def retranslateUi(self, overnight_popup, num_guides, labels, current_date):

        overnight_popup.setWindowTitle(QtGui.QApplication.translate(
            "overnight_popup",
            "Create a New Temporary Guide",
            None,
            QtGui.QApplication.UnicodeUTF8)
        )

        self.main_label.setText(QtGui.QApplication.translate(
            "Form",
            "<html><body><p><span style=\" font-size:18pt;\">Choose Staff for "
            +current_date
            +" Ticket to Ride</span></p></body></html>",
            None,
            QtGui.QApplication.UnicodeUTF8)
        )

        self.submit.setText(QtGui.QApplication.translate(
            "overnight_popup",
            "Submit",
            None,
            QtGui.QApplication.UnicodeUTF8)
        )

        for n in range(num_guides):

            self.labels[n].setText(QtGui.QApplication.translate(
                "overnight_popup",
                "<html><body><p><span style=\" font-size:14pt;\">"
                +create_schedule.schedule_dictionaries.overnight_dialog_guide_labels[n]
                +": </span></p></body></html>",
                None,
                QtGui.QApplication.UnicodeUTF8)
            )

        if num_guides == 1:

            self.safety_label.setText(QtGui.QApplication.translate(
                "overnight_popup",
                "<html><body><p><span style=\" font-size:14pt;\">Safety: </span></p></body></html>",
                None,
                QtGui.QApplication.UnicodeUTF8)
            )

    def submit_staff(self):

        for n in range(self.num_guides):

            print("role assignment: ", create_schedule.schedule_dictionaries.role_switch[n]+create_schedule.schedule_dictionaries.trip_types[4])

            self.trip_role_assignment[
                create_schedule.schedule_dictionaries.role_switch[n]
                +create_schedule.schedule_dictionaries.trip_types[4]
            ] = self.comboBoxes[n].currentText()

        if self.num_guides == 1:

            print("safety assignment: ", create_schedule.schedule_dictionaries.role_switch[4]+create_schedule.schedule_dictionaries.trip_types[4])

            self.trip_role_assignment[
                create_schedule.schedule_dictionaries.role_switch[4]
                +create_schedule.schedule_dictionaries.trip_types[4]
            ] = self.safety_name.currentText()

        print(self.trip_role_assignment)

        self.DialogBox.accept()

################################################################################


    def return_data(self):
        return self.trip_role_assignment
