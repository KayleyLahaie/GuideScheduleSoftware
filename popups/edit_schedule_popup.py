from PySide2 import QtCore, QtGui, QtWidgets
import manage_staff
from manage_staff import staff_util
import create_schedule
from create_schedule import schedule_dictionaries

from manage_staff import driver
from manage_staff import guide

session_guide = guide.guide_session()
session_driver = driver.driver_session()


class Ui_edit_schedule_popup(object):

    def setupUi(self, edit_schedule_popup, name, trip_role, DialogBox):

        self.trip_role_original = trip_role

        self.DialogBox = DialogBox

        edit_schedule_popup.setObjectName("edit_schedule_popup")
        edit_schedule_popup.resize(400, 200)
        edit_schedule_popup.setStyleSheet("background-color: white;")

        self.change_guide = QtWidgets.QLabel(edit_schedule_popup)
        self.change_guide.setGeometry(QtCore.QRect(25, 50, 150, 30))
        self.change_guide.setObjectName("choose_saved")

        self.comboBox = QtWidgets.QComboBox(edit_schedule_popup)
        self.comboBox.setGeometry(QtCore.QRect(187.5, 50, 187.5, 22))
        self.comboBox.setObjectName("comboBox")

        selected_role = ""
        selected_trip = ""
        for  i, role in enumerate(create_schedule.schedule_dictionaries.role_switch):

            if create_schedule.schedule_dictionaries.role_switch[i] in trip_role:
                selected_role = i

        for i, trip in enumerate(create_schedule.schedule_dictionaries.trip_switch_numerical):
            if create_schedule.schedule_dictionaries.trip_switch_numerical[trip] in trip_role:
                selected_trip = i

        print(selected_role)
        print(selected_trip)

        if selected_role >= 0 and selected_role <= 4:
            staff_list = manage_staff.staff_util.get_guides_can_work(session_guide, selected_trip, selected_role)
        else:
            staff_list = manage_staff.staff_util.get_drivers_can_work(session_driver, selected_trip)

        for x, y in enumerate(staff_list):
            print(y)
            self.comboBox.addItem(y)

        self.submit_changes = QtWidgets.QPushButton(edit_schedule_popup)
        self.submit_changes.setGeometry(QtCore.QRect(139.5, 125, 121, 28))
        self.submit_changes.setStyleSheet("  border: none;\n"
                                          "  padding: 0.5%;\n"
                                          "  cursor: pointer;\n"
                                          "  font-family: special_font;\n"
                                          "  font-size: 130%;\n"
                                          "  border-radius: 3%;\n"
                                          "  opacity: 0.9;\n"
                                          "  background-color: #006898;\n"
                                          "  color: #ee7838;")
        self.submit_changes.setObjectName("submit_changes")
        self.submit_changes.clicked.connect(self.submit_new_staff)


        self.retranslateUi(edit_schedule_popup)
        QtCore.QMetaObject.connectSlotsByName(edit_schedule_popup)

    def retranslateUi(self, edit_schedule_popup):
        """Translates the string properties of the form

        Parameters
        ----------
        not_enough_drivers_popup : QDialog
            A QDialog object created in create_schedule_day() that allows the
            dialog to be created by the method when needed
        """

        edit_schedule_popup.setWindowTitle(QtWidgets.QApplication.translate(
            "edit_schedule_popup",
            "Choose a new Staff Member",
            None,
            0)
        )

        self.change_guide.setText(QtWidgets.QApplication.translate(
            "edit_schedule_popup",
            "<html><body><p><span style=\" font-size:10pt;\">Select a Guide:</span></p></body></html>",
            None,
            0)
        )
        self.submit_changes.setText(QtWidgets.QApplication.translate(
            "edit_schedule_popup", "Submit", None, 0))

    def submit_new_staff(self):
        """Inserts selected staff into the trip_role_assignment dictionary

        Selects the staff chosen by the user for each of the combo boxes and
        adds them to the trip_role_assignment dictionary

        # TODO: Check to make sure the same guide is not chosen for multiple
        # roles
            """
        name = self.comboBox.currentText()

        self.new_staff = [name, self.trip_role_original]


        self.DialogBox.accept()

    def return_new_staff(self):
        """Return the selected driver to the main window

        Returns
        -------
        str
            The string representation of the name of the temporary driver chosen
        """

        return self.new_staff
