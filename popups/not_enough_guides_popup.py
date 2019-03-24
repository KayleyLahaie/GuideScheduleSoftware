    # -*- coding: utf-8 -*-

    # Form implementation generated from reading ui file 'dialogwindow.ui'
    #
    # Created: Mon Feb 18 18:32:39 2019
    #      by: pyside-uic 0.2.15 running on PySide 1.2.4
    #
    # WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import manage_staff
from manage_staff import staff_util

from manage_staff import guide

session_guide = guide.guide_session()

class Ui_not_enough_guides_popup(object):

    def setupUi(self, not_enough_guides_popup, DialogBox):

        self.DialogBox = DialogBox
        self.temp_guide = ""

        not_enough_guides_popup.setObjectName("not_enough_guides_popup")
        not_enough_guides_popup.resize(600, 600)
        not_enough_guides_popup.setStyleSheet("background-color: white;")

        self.choose_saved = QtWidgets.QLabel(not_enough_guides_popup)
        self.choose_saved.setGeometry(QtCore.QRect(100, 50, 150, 30))
        self.choose_saved.setObjectName("choose_saved")

        self.comboBox = QtWidgets.QComboBox(not_enough_guides_popup)
        self.comboBox.setGeometry(QtCore.QRect(300, 50, 201, 22))
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItem("Choose Guide...")
        self.comboBox.addItem("Unknown")

        num_temp_guides = manage_staff.staff_util.get_total_temp_guides()
        print(num_temp_guides)
        for x in range(len(num_temp_guides)):
            self.comboBox.addItem(num_temp_guides[x]['name'])

        self.or_label = QtWidgets.QLabel(not_enough_guides_popup)
        self.or_label.setGeometry(QtCore.QRect(262.5, 100, 150, 50))
        self.or_label.setObjectName("or_label")

        self.can_tl_label = QtWidgets.QLabel(not_enough_guides_popup)
        self.can_tl_label.setGeometry(QtCore.QRect(25, 225, 150, 30))
        self.can_tl_label.setObjectName("can_tl_label")
        self.can_guide_label = QtWidgets.QLabel(not_enough_guides_popup)
        self.can_guide_label.setGeometry(QtCore.QRect(225, 225, 121, 23))
        self.can_guide_label.setObjectName("can_guide_label")
        self.can_safety_label = QtWidgets.QLabel(not_enough_guides_popup)
        self.can_safety_label.setGeometry(QtCore.QRect(400, 225, 150, 30))
        self.can_safety_label.setObjectName("can_safety_label")
        self.submit = QtWidgets.QPushButton(not_enough_guides_popup)
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
        self.submit.clicked.connect(self.choose_temporary_guide)
        self.submit.show()
        self.verticalWidget = QtWidgets.QWidget(not_enough_guides_popup)
        self.verticalWidget.setGeometry(QtCore.QRect(250, 300, 111, 131))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.can_guide_four_hour = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_guide_four_hour.setStyleSheet("")
        self.can_guide_four_hour.setObjectName("can_guide_four_hour")
        self.verticalLayout.addWidget(self.can_guide_four_hour)
        self.can_guide_full_day = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_guide_full_day.setStyleSheet("")
        self.can_guide_full_day.setObjectName("can_guide_full_day")
        self.verticalLayout.addWidget(self.can_guide_full_day)
        self.can_guide_c_wave = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_guide_c_wave.setStyleSheet("")
        self.can_guide_c_wave.setObjectName("can_guide_c_wave")
        self.verticalLayout.addWidget(self.can_guide_c_wave)
        self.can_guide_float = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_guide_float.setStyleSheet("")
        self.can_guide_float.setObjectName("can_guide_float")
        self.verticalLayout.addWidget(self.can_guide_float)
        self.can_guide_overnight = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_guide_overnight.setStyleSheet("")
        self.can_guide_overnight.setObjectName("can_guide_overnight")
        self.verticalLayout.addWidget(self.can_guide_overnight)
        self.canSafetyOptionWidget = QtWidgets.QWidget(not_enough_guides_popup)
        self.canSafetyOptionWidget.setGeometry(QtCore.QRect(425, 300, 111, 131))
        self.canSafetyOptionWidget.setObjectName("canSafetyOptionWidget")
        self.canSafetyOptionLayout = QtWidgets.QVBoxLayout(self.canSafetyOptionWidget)
        self.canSafetyOptionLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.canSafetyOptionLayout.setContentsMargins(0, 0, 0, 0)
        self.canSafetyOptionLayout.setObjectName("canSafetyOptionLayout")
        self.can_safety_four_hour = QtWidgets.QCheckBox(self.canSafetyOptionWidget)
        self.can_safety_four_hour.setStyleSheet("")
        self.can_safety_four_hour.setObjectName("can_safety_four_hour")
        self.canSafetyOptionLayout.addWidget(self.can_safety_four_hour)
        self.can_safety_full_day = QtWidgets.QCheckBox(self.canSafetyOptionWidget)
        self.can_safety_full_day.setStyleSheet("")
        self.can_safety_full_day.setObjectName("can_safety_full_day")
        self.canSafetyOptionLayout.addWidget(self.can_safety_full_day)
        self.can_safety_c_wave = QtWidgets.QCheckBox(self.canSafetyOptionWidget)
        self.can_safety_c_wave.setStyleSheet("")
        self.can_safety_c_wave.setObjectName("can_safety_c_wave")
        self.canSafetyOptionLayout.addWidget(self.can_safety_c_wave)
        self.can_safety_float = QtWidgets.QCheckBox(self.canSafetyOptionWidget)
        self.can_safety_float.setStyleSheet("")
        self.can_safety_float.setObjectName("can_safety_float")
        self.canSafetyOptionLayout.addWidget(self.can_safety_float)
        self.can_safety_overnight = QtWidgets.QCheckBox(self.canSafetyOptionWidget)
        self.can_safety_overnight.setStyleSheet("")
        self.can_safety_overnight.setObjectName("can_safety_overnight")
        self.canSafetyOptionLayout.addWidget(self.can_safety_overnight)
        self.canTlOptionWidget = QtWidgets.QWidget(not_enough_guides_popup)
        self.canTlOptionWidget.setGeometry(QtCore.QRect(50, 300, 111, 131))
        self.canTlOptionWidget.setObjectName("canTlOptionWidget")
        self.canTlOptionLayout = QtWidgets.QVBoxLayout(self.canTlOptionWidget)
        self.canTlOptionLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.canTlOptionLayout.setContentsMargins(0, 0, 0, 0)
        self.canTlOptionLayout.setObjectName("canTlOptionLayout")
        self.can_Tl_four_hour = QtWidgets.QCheckBox(self.canTlOptionWidget)
        self.can_Tl_four_hour.setStyleSheet("")
        self.can_Tl_four_hour.setObjectName("can_Tl_four_hour")
        self.canTlOptionLayout.addWidget(self.can_Tl_four_hour)
        self.can_Tl_full_day = QtWidgets.QCheckBox(self.canTlOptionWidget)
        self.can_Tl_full_day.setStyleSheet("")
        self.can_Tl_full_day.setObjectName("can_Tl_full_day")
        self.canTlOptionLayout.addWidget(self.can_Tl_full_day)
        self.can_Tl_c_wave = QtWidgets.QCheckBox(self.canTlOptionWidget)
        self.can_Tl_c_wave.setStyleSheet("")
        self.can_Tl_c_wave.setObjectName("can_Tl_c_wave")
        self.canTlOptionLayout.addWidget(self.can_Tl_c_wave)
        self.can_Tl_float = QtWidgets.QCheckBox(self.canTlOptionWidget)
        self.can_Tl_float.setStyleSheet("")
        self.can_Tl_float.setObjectName("can_Tl_float")
        self.canTlOptionLayout.addWidget(self.can_Tl_float)
        self.can_Tl_overnight = QtWidgets.QCheckBox(self.canTlOptionWidget)
        self.can_Tl_overnight.setStyleSheet("")
        self.can_Tl_overnight.setObjectName("can_Tl_overnight")
        self.canTlOptionLayout.addWidget(self.can_Tl_overnight)
        self.guide_name = QtWidgets.QPlainTextEdit(not_enough_guides_popup)
        self.guide_name.setGeometry(QtCore.QRect(125, 162.5, 161, 20))
        self.guide_name.setStyleSheet("background-color: #FFFFFF")
        self.guide_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.guide_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.guide_name.setObjectName("guide_name")
        self.class_label = QtWidgets.QLabel(not_enough_guides_popup)
        self.class_label.setGeometry(QtCore.QRect(350, 150, 90, 41))
        self.class_label.setStyleSheet("")
        self.class_label.setObjectName("name_label")

        self.name_label = QtWidgets.QLabel(not_enough_guides_popup)
        self.name_label.setGeometry(QtCore.QRect(25, 150, 81, 41))
        self.name_label.setStyleSheet("")
        self.name_label.setObjectName("name_label")

        self.classIVOptionWidget = QtWidgets.QWidget(not_enough_guides_popup)
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

        self.retranslateUi(not_enough_guides_popup)
        QtCore.QMetaObject.connectSlotsByName(not_enough_guides_popup)

################################################################################


    def retranslateUi(self, not_enough_guides_popup):

        not_enough_guides_popup.setWindowTitle(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Create a New Temporary Guide",
            None,
            0)
        )

        self.can_guide_label.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "<html><body><p><span style=\" font-size:14pt;\">Can Guide:</span></p></body></html>",
            None,
            0)
        )

        self.can_tl_label.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "<html><body><p><span style=\" font-size:14pt;\">Can Trip Lead:</span></p></body></html>",
            None,
            0)
        )

        self.can_safety_label.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "<html><body><p><span style=\" font-size:14pt;\">Can Safety:</span></p></body></html>",
             None,
             0)
        )

        self.submit.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Submit",
            None,
            0)
        )

        self.can_guide_four_hour.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Four Hour",
            None,
            0)
        )

        self.can_guide_full_day.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Full Day",
            None,
            0)
        )

        self.can_guide_c_wave.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "C Wave",
            None,
            0)
        )

        self.can_guide_float.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Float",
            None,
            0)
        )

        self.can_guide_overnight.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Overnight",
            None,
            0)
        )

        self.can_safety_four_hour.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Four Hour",
            None,
            0)
        )

        self.can_safety_full_day.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Full Day",
            None,
            0)
        )

        self.can_safety_c_wave.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "C Wave",
            None,
            0)
        )

        self.can_safety_float.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Float",
            None,
            0)
        )

        self.can_safety_overnight.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Overnight",
            None,
            0)
        )

        self.can_Tl_four_hour.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Four Hour",
            None,
            0)
        )

        self.can_Tl_full_day.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Full Day",
            None,
            0)
        )

        self.can_Tl_c_wave.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "C Wave",
            None,
            0)
        )

        self.can_Tl_float.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Float",
            None,
            0)
        )

        self.can_Tl_overnight.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
            "Overnight",
            None,
            0)
        )

        self.name_label.setText(QtWidgets.QApplication.translate(
            "not_enough_guides_popup",
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

################################################################################


    def choose_temporary_guide(self):

        name = self.guide_name.toPlainText()

        if name != "":

            has_class_IV = self.class_IV.isChecked()
            four_hour_guide = self.can_guide_four_hour.isChecked()
            full_day_guide = self.can_guide_full_day.isChecked()
            c_wave_guide = self.can_guide_c_wave.isChecked()
            float_guide = self.can_guide_float.isChecked()
            overnight_guide = self.can_guide_overnight.isChecked()
            four_hour = self.can_Tl_four_hour.isChecked()
            full_day  = self.can_Tl_full_day.isChecked()
            c_wave  = self.can_Tl_c_wave.isChecked()
            float  = self.can_Tl_float.isChecked()
            overnight  = self.can_Tl_overnight.isChecked()
            four_hour_safety = self.can_safety_four_hour.isChecked()
            full_day_safety = self.can_safety_full_day.isChecked()
            c_wave_safety = self.can_safety_c_wave.isChecked()
            float_safety = self.can_safety_float.isChecked()
            overnight_safety = self.can_safety_overnight.isChecked()

            new_guide = manage_staff.guide.guide(   name = name, in_stream = 'false',
                                                    has_class_IV = has_class_IV,
                                                    tl_four_hour = four_hour,
                                                    tl_c_wave = c_wave,
                                                    tl_full_day = full_day,
                                                    tl_scenic_float = float,
                                                    tl_overnight = overnight,
                                                    guide_four_hour = four_hour_guide,
                                                    guide_c_wave = c_wave_guide,
                                                    guide_full_day = full_day_guide,
                                                    guide_scenic_float = float_guide,
                                                    guide_overnight = overnight_guide,
                                                    safety_four_hour= four_hour_safety,
                                                    safety_c_wave = c_wave_safety,
                                                    safety_full_day= full_day_safety,
                                                    safety_scenic_float = float_safety,
                                                    safety_overnight = overnight_safety,
                                                    tl_this_summer_four_hour = 1,
                                                    tl_this_summer_c_wave = 1,
                                                    tl_this_summer_full_day = 1,
                                                    tl_this_summer_scenic_float = 1,
                                                    tl_this_summer_overnight = 1,
                                                    tl_this_period_four_hour = 1,
                                                    tl_this_period_c_wave = 1,
                                                    tl_this_period_full_day = 1,
                                                    tl_this_period_scenic_float = 1,
                                                    tl_this_period_overnight = 1,
                                                    guided_this_summer_four_hour = 1,
                                                    guided_this_summer_c_wave = 1,
                                                    guided_this_summer_full_day = 1,
                                                    guided_this_summer_scenic_float = 1,
                                                    guided_this_summer_overnight = 1,
                                                    guided_this_period_four_hour = 1,
                                                    guided_this_period_c_wave = 1,
                                                    guided_this_period_full_day = 1,
                                                    guided_this_period_scenic_float = 1,
                                                    guided_this_period_overnight = 1,
                                                    safety_this_summer_four_hour = 1,
                                                    safety_this_summer_c_wave = 1,
                                                    safety_this_summer_full_day = 1,
                                                    safety_this_summer_scenic_float=1,
                                                    safety_this_summer_overnight = 1,
                                                    safety_this_period_four_hour = 1,
                                                    safety_this_period_c_wave = 1,
                                                    safety_this_period_full_day = 1,
                                                    safety_this_period_scenic_float = 1,
                                                    safety_this_period_overnight = 1,
                                                    days_since_last_day_off = 1
                                                )

            session_guide.add(new_guide)
            session_guide.commit()
            self.temp_guide = name
            self.DialogBox.accept()

        elif self.comboBox.currentText() != "Choose Guide...":

            self.temp_guide = self.comboBox.currentText()

            print("Chose ", self.temp_guide)

            self.DialogBox.accept()

################################################################################


    def return_temp_guide(self):

        return self.temp_guide
