from PySide2 import QtCore, QtGui, QtWidgets
import manage_staff
from manage_staff import staff_util

from manage_staff import driver

session_driver = driver.driver_session()

class Ui_not_enough_drivers_popup(object):
    """
    Produces the ui for a pop up window that provides functionality for
    selecting or creating a temporary driver when more drivers are needed than
    are currently on staff

    Methods
    -------
    setupUi(self, not_enough_drivers_popup, DialogBox)
        Sets up all of the objects and adds them to the DialogBox

    retranslateUi(self, not_enough_drivers_popup)
        Translates the string properties of the form

    choose_temporary_driver(self)
        Choose a temporary driver from a list or create a new one using the
        fields provided

    return_temp_driver(self)
        Return the selected driver to the main window
    """

    def setupUi(self, not_enough_drivers_popup, DialogBox):
        """Sets up all of the objects and adds them to the DialogBox

        Parameters
        ----------
        not_enough_driver_popup : QDialog
            A QDialog object created in create_schedule_day() that allows the
            dialog to be created by the method when needed
        DialogBox : QDialog
            A QDialog object created in create_schedule_day() that allows the
            dialog to be created by the method when needed

        Method Calls
        ------------
            -retranslateUi()
        """

        self.DialogBox = DialogBox
        self.temp_driver = ""

        not_enough_drivers_popup.setObjectName("not_enough_drivers_popup")
        not_enough_drivers_popup.resize(600, 600)
        not_enough_drivers_popup.setStyleSheet("background-color: white;")

        self.choose_saved = QtWidgets.QLabel(not_enough_drivers_popup)
        self.choose_saved.setGeometry(QtCore.QRect(100, 50, 150, 30))
        self.choose_saved.setObjectName("choose_saved")

        self.comboBox = QtWidgets.QComboBox(not_enough_drivers_popup)
        self.comboBox.setGeometry(QtCore.QRect(300, 50, 201, 22))
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItem("Choose driver...")
        self.comboBox.addItem("Unknown")

        num_temp_drivers = manage_staff.staff_util.get_total_temp_drivers(session_driver)

        for x, y in enumerate(num_temp_drivers):
            self.comboBox.addItem(num_temp_drivers[x]['name'])

        self.or_label = QtWidgets.QLabel(not_enough_drivers_popup)
        self.or_label.setGeometry(QtCore.QRect(262.5, 100, 150, 50))
        self.or_label.setObjectName("or_label")

        self.can_tl_label = QtWidgets.QLabel(not_enough_drivers_popup)
        self.can_tl_label.setGeometry(QtCore.QRect(25, 225, 150, 30))
        self.can_tl_label.setObjectName("can_tl_label")
        self.can_driver_label = QtWidgets.QLabel(not_enough_drivers_popup)
        self.can_driver_label.setGeometry(QtCore.QRect(225, 225, 121, 23))
        self.can_driver_label.setObjectName("can_driver_label")
        self.can_safety_label = QtWidgets.QLabel(not_enough_drivers_popup)
        self.can_safety_label.setGeometry(QtCore.QRect(400, 225, 150, 30))
        self.can_safety_label.setObjectName("can_safety_label")
        self.submit = QtWidgets.QPushButton(not_enough_drivers_popup)
        self.submit.setGeometry(QtCore.QRect(400, 500, 93, 28))
        self.submit.setStyleSheet("  border: none;\n"
                                "  padding: 0.5%;\n"
                                "  cursor: pointer;\n"
                                "  font-family: special_font;\n"
                                "  font-size: 130%;\n"
                                "  border-radius: 3%;\n"
                                "  opacity: 0.9;\n"
                                "  background-color: #006898;\n"
                                "  color: #ee7838;")
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.choose_temporary_driver)
        self.submit.show()
        self.verticalWidget = QtWidgets.QWidget(not_enough_drivers_popup)
        self.verticalWidget.setGeometry(QtCore.QRect(250, 300, 111, 131))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.can_drive_four_hour = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_drive_four_hour.setStyleSheet("")
        self.can_drive_four_hour.setObjectName("can_drive_four_hour")
        self.verticalLayout.addWidget(self.can_drive_four_hour)
        self.can_drive_full_day = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_drive_full_day.setStyleSheet("")
        self.can_drive_full_day.setObjectName("can_drive_full_day")
        self.verticalLayout.addWidget(self.can_drive_full_day)
        self.can_drive_c_wave = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_drive_c_wave.setStyleSheet("")
        self.can_drive_c_wave.setObjectName("can_drive_c_wave")
        self.verticalLayout.addWidget(self.can_drive_c_wave)
        self.can_drive_float = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_drive_float.setStyleSheet("")
        self.can_drive_float.setObjectName("can_drive_float")
        self.verticalLayout.addWidget(self.can_drive_float)
        self.can_drive_overnight = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_drive_overnight.setStyleSheet("")
        self.can_drive_overnight.setObjectName("can_drive_overnight")
        self.verticalLayout.addWidget(self.can_drive_overnight)

        self.driver_name = QtWidgets.QPlainTextEdit(not_enough_drivers_popup)
        self.driver_name.setGeometry(QtCore.QRect(125, 162.5, 161, 20))
        self.driver_name.setStyleSheet("background-color: #FFFFFF")
        self.driver_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.driver_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.driver_name.setObjectName("driver_name")
        self.class_label = QtWidgets.QLabel(not_enough_drivers_popup)
        self.class_label.setGeometry(QtCore.QRect(350, 150, 90, 41))
        self.class_label.setStyleSheet("")
        self.class_label.setObjectName("name_label")

        self.name_label = QtWidgets.QLabel(not_enough_drivers_popup)
        self.name_label.setGeometry(QtCore.QRect(25, 150, 81, 41))
        self.name_label.setStyleSheet("")
        self.name_label.setObjectName("name_label")

        self.classIVOptionWidget = QtWidgets.QWidget(not_enough_drivers_popup)
        self.classIVOptionWidget.setGeometry(QtCore.QRect(450, 162.5, 161, 21))
        self.classIVOptionWidget.setObjectName("classIVOptionWidget")
        self.classIVOptionLayout = QtWidgets.QVBoxLayout(self.classIVOptionWidget)
        self.classIVOptionLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.classIVOptionLayout.setContentsMargins(0, 0, 0, 0)
        self.classIVOptionLayout.setObjectName("classIVOptionLayout")
        self.class_IV = QtWidgets.QCheckBox(self.classIVOptionWidget)
        self.class_IV.setStyleSheet("")
        self.class_IV.setObjectName("class_IV")
        self.classIVOptionLayout.addWidget(self.class_IV)

        self.retranslateUi(not_enough_drivers_popup)
        QtCore.QMetaObject.connectSlotsByName(not_enough_drivers_popup)

    def retranslateUi(self, not_enough_drivers_popup):
        """Translates the string properties of the form

        Parameters
        ----------
        not_enough_drivers_popup : QDialog
            A QDialog object created in create_schedule_day() that allows the
            dialog to be created by the method when needed
        """

        not_enough_drivers_popup.setWindowTitle(QtWidgets.QApplication.translate(
            "not_enough_drivers_popup",
            "Create a New Temporary driver",
            None,
            0)
        )

        self.can_driver_label.setText(QtWidgets.QApplication.translate(
            "not_enough_drivers_popup",
            "<html><body><p><span style=\" font-size:14pt;\">Can drive:</span></p></body></html>",
            None,
            0)
        )


        self.submit.setText(QtWidgets.QApplication.translate(
            "not_enough_drivers_popup",
            "Submit",
            None,
            0)
        )

        self.can_drive_four_hour.setText(QtWidgets.QApplication.translate(
            "not_enough_drivers_popup",
            "Four Hour",
            None,
            0)
        )

        self.can_drive_full_day.setText(QtWidgets.QApplication.translate(
            "not_enough_drives_popup",
            "Full Day",
            None,
            0)
        )

        self.can_drive_c_wave.setText(QtWidgets.QApplication.translate(
            "not_enough_drives_popup",
            "C Wave",
            None,
            0)
        )

        self.can_drive_float.setText(QtWidgets.QApplication.translate(
            "not_enough_drives_popup",
            "Float",
            None,
            0)
        )

        self.can_drive_overnight.setText(QtWidgets.QApplication.translate(
            "not_enough_drives_popup",
            "Overnight",
            None,
            0)
        )

        self.name_label.setText(QtWidgets.QApplication.translate(
            "not_enough_drivers_popup",
            "<html><body><p><span style=\" font-size:14pt;\">Name: </span></p></body></html>",
            None,
            0)
        )

        self.class_label.setText(QtWidgets.QApplication.translate(
            "Form",
            "<html><body><p><span style=\" font-size:14pt;\">Class IV: </span></p></body></html>",
            None,
            0)
        )

        self.choose_saved.setText(QtWidgets.QApplication.translate(
            "Form", "<html><body><p><span style=\" font-size:14pt;\">Choose From: </span></p></body></html>",
            None,
            0)
        )

        self.or_label.setText(QtWidgets.QApplication.translate(
            "Form", "<html><body><p><span style=\" font-size:20pt;\"> - Or - </span></p></body></html>",
            None,
            0)
        )

    def choose_temporary_driver(self):
        """Choose a temporary driver from a list or create a new one using the
        fields provided

        If a new temporary driver is to be created, data is gathered from the
        fields and a new driver object is created and submitted to the driver
        table in staff.db

        """

        name = self.driver_name.toPlainText()

        if name != "" and self.comboBox.currentText() == "Choose driver...":

            has_class_IV = self.class_IV.isChecked()
            four_hour_driver = self.can_drive_four_hour.isChecked()
            full_day_driver = self.can_drive_full_day.isChecked()
            c_wave_driver = self.can_drive_c_wave.isChecked()
            float_driver = self.can_drive_float.isChecked()
            overnight_driver = self.can_drive_overnight.isChecked()


            new_driver = manage_staff.driver.driver(   name = name, in_stream = 'false',
                                                    has_class_IV = has_class_IV,
                                                    four_hour = four_hour_driver,
                                                    c_wave = c_wave_driver,
                                                    full_day = full_day_driver,
                                                    scenic_float = float_driver,
                                                    overnight = overnight_driver,
                                                    four_hour_seniority = 1,
                                                    c_wave_seniority = 1,
                                                    full_day_seniority = 1,
                                                    scenic_float_seniority = 1,
                                                    overnight_seniority = 1,
                                                    driven_this_summer_four_hour = 1,
                                                    driven_this_summer_c_wave = 1,
                                                    driven_this_summer_full_day = 1,
                                                    driven_this_summer_scenic_float = 1,
                                                    driven_this_summer_overnight = 1,
                                                    driven_this_period_four_hour = 1,
                                                    driven_this_period_c_wave = 1,
                                                    driven_this_period_full_day = 1,
                                                    driven_this_period_scenic_float = 1,
                                                    driven_this_period_overnight = 1,
                                                    days_since_last_day_off = 1
                                                )

            session_driver.add(new_driver)
            session_driver.commit()
            self.temp_driver = name
            self.DialogBox.accept()

        elif self.comboBox.currentText() != "Choose driver...":

            self.temp_driver = self.comboBox.currentText()
            self.DialogBox.accept()

    def return_temp_driver(self):
        """Return the selected driver to the main window

        Returns
        -------
        str
            The string representation of the name of the temporary driver chosen
        """

        return self.temp_driver
