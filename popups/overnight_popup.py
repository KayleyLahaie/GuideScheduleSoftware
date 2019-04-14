# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogwindow.ui'
#
# Created: Mon Feb 18 18:32:39 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import create_schedule
from create_schedule import schedule_dictionaries

import manage_staff
from manage_staff import staff_util

class Ui_overnight_popup(object):
    """
    Produces the ui for a pop up window that provides functionality for
    selecting the staff members to work on an overnight trip

    Methods
    -------
    setupUi(self, not_enough_guides_popup, DialogBox)
        Sets up all of the objects and adds them to the DialogBox

    retranslateUi(self, not_enough_guides_popup)
        Translates the string properties of the form

    submit_staff(self)
        Inserts selected staff into the trip_role_assignment dictionary

    return_data(self)
        Return the selected staff to the main window
    """

    def setupUi(self, overnight_popup, num_guides, current_date, trip_role_assignment, DialogBox):
        """Sets up all of the objects and adds them to the DialogBox

        Parameters
        ----------
        overnight_popup: QDialog
            A QDialog object created in create_schedule_day() that allows the
            dialog to be created by the method when needed
        num_guides: int
            The number of guides needed for the trip
        current_date : date
            A date object representing the date for which a schedule must be
            created
        trip_role_assignment: dict
            An empty dictionary to be filled with the names of the staff members
            assigned to each role
        DialogBox: QDialog
            A QDialog object created in create_schedule_day() that allows the
            dialog to be created by the method when needed

        Method Calls
        ------------
            -retranslateUi()
        """

        self.DialogBox = DialogBox
        self.num_guides = num_guides
        self.trip_role_assignment = trip_role_assignment

        self.comboBoxes = [0,0,0,0]
        self.labels = [0,0,0,0]

        overnight_popup.setObjectName("overnight_popup")
        overnight_popup.resize(700, 500)
        overnight_popup.setStyleSheet("color: #ee7838;\n"
                                      "background-color: white;")

        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")

        self.main_label = QtWidgets.QLabel(overnight_popup)
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
            guides_available = manage_staff.staff_util.get_guides_can_work(
                                    4,
                                    create_schedule.schedule_dictionaries.guide_roles_converter[n]
                                )

            self.comboBoxes[n] = QtWidgets.QComboBox(overnight_popup)
            self.comboBoxes[n].setGeometry(QtCore.QRect(x_text, y_text, 200, 30))
            self.comboBoxes[n].setObjectName("comboBox")

            self.comboBoxes[n].addItem("Choose Guide...")

            for m in range(len(guides_available)):
                self.comboBoxes[n].addItem(guides_available[m])

            self.labels[n] = QtWidgets.QLabel(overnight_popup)
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

            self.safety_name = QtWidgets.QComboBox(overnight_popup)
            self.safety_name.setGeometry(QtCore.QRect(x_text, y_text, 200, 30))
            self.safety_name.setObjectName("comboBox")

            self.safety_name.addItem("Choose Guide...")

            for m in range(len(guides_available)):
                self.safety_name.addItem(guides_available[m])

            self.safety_label = QtWidgets.QLabel(overnight_popup)
            self.safety_label.setGeometry(QtCore.QRect(x_label, y_label, 81, 41))
            self.safety_label.setStyleSheet("")
            self.safety_label.setObjectName("safety_label")

        self.submit = QtWidgets.QPushButton(overnight_popup)
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
        """Sets up all of the objects and adds them to the DialogBox

        Parameters
        ----------
        overnight_popup: QDialog
            A QDialog object created in create_schedule_day() that allows the
            dialog to be created by the method when needed
        num_guides: int
            The number of guides needed for the trip
        labels: list
            A list of QLabel widgets
        current_date : date
            A date object representing the date for which a schedule must be
            created
        """

        overnight_popup.setWindowTitle(QtWidgets.QApplication.translate(
            "overnight_popup",
            "Create a New Temporary Guide",
            None,
            0)
        )

        self.main_label.setText(QtWidgets.QApplication.translate(
            "Form",
            "<html><body><p><span style=\" font-size:18pt;\">Choose Staff for "
            +current_date
            +" Ticket to Ride</span></p></body></html>",
            None,
            0)
        )

        self.submit.setText(QtWidgets.QApplication.translate(
            "overnight_popup",
            "Submit",
            None,
            0)
        )

        for n in range(num_guides):

            self.labels[n].setText(QtWidgets.QApplication.translate(
                "overnight_popup",
                "<html><body><p><span style=\" font-size:14pt;\">"
                +create_schedule.schedule_dictionaries.overnight_dialog_guide_labels[n]
                +": </span></p></body></html>",
                None,
                0)
            )

        if num_guides == 1:

            self.safety_label.setText(QtWidgets.QApplication.translate(
                "overnight_popup",
                "<html><body><p><span style=\" font-size:14pt;\">Safety: </span></p></body></html>",
                None,
                0)
            )

    def submit_staff(self):
        """Inserts selected staff into the trip_role_assignment dictionary

        Selects the staff chosen by the user for each of the combo boxes and
        adds them to the trip_role_assignment dictionary

        # TODO: Check to make sure the same guide is not chosen for multiple
        # roles
        """

        for n in range(self.num_guides):
            self.trip_role_assignment[
                create_schedule.schedule_dictionaries.role_switch[n]
                +create_schedule.schedule_dictionaries.trip_types[4]
            ] = self.comboBoxes[n].currentText()

        if self.num_guides == 1:
            self.trip_role_assignment[
                create_schedule.schedule_dictionaries.role_switch[4]
                +create_schedule.schedule_dictionaries.trip_types[4]
            ] = self.safety_name.currentText()

        self.DialogBox.accept()

    def return_data(self):
        """Returns the trip_role_assignment dictionary to the main setWindowTitle

        Returns
        -------
        dict
            An dictionary containing the names of the staff members assigned to
            each role on the overnight trip

        """
        return self.trip_role_assignment
