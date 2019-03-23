#FFFFFF# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kayle\Desktop\Gui\Gui_Python_Files\stack_gui.ui'
#
# Created: Sat Aug 25 21:52:46 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import datetime
import sqlite3
import excel_scraper
import create_schedule
import manage_staff


from create_schedule import create_new_schedule

session_guide = manage_staff.guide.guide_session()
session_driver = manage_staff.driver.driver_session()


class hover_button(QtWidgets.QPushButton):

    def enterEvent(self,event):
        self.setStyleSheet("  border: none;\n"
                            "  padding: 5px;\n"
                            "  cursor: pointer;\n"
                            "  font-family: special_font;\n"
                            "  font-size: 20px;\n"
                            "  border-radius: 3%;\n"
                            "  opacity: 1;\n"
                            "  background-color: rgba(0,104,152,200);\n"
                            "  color: #ee7838;")

    def leaveEvent(self,event):
        self.setStyleSheet("  border: none;\n"
                            "  padding: 5px;\n"
                            "  cursor: pointer;\n"
                            "  font-family: special_font;\n"
                            "  font-size: 20px;\n"
                            "  border-radius: 3%;\n"
                            "  opacity: 0.5;\n"
                            "  background-color: rgba(255, 255, 255, 200);\n"
                            "  color: #ee7838;")



class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 764)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -30, 1200, 795))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet("background-color:#FFFFFF")
        self.stackedWidget.setAutoFillBackground(True)


################################################################################

        self.main_menu = QtWidgets.QWidget()
        self.main_menu.setObjectName("main_menu")

        self.white = QtGui.QColor.fromRgb(255,255,255,0.5)

        self.background = QtWidgets.QLabel(self.main_menu)
        self.background.setPixmap(QtGui.QPixmap('background4.png'))
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 795))

        self.pushButton_5 = hover_button(self.main_menu)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 480, 225, 40))
        self.pushButton_5.setStyleSheet("  border: none;\n"
                                        "  padding: 5px;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 20px;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.8;\n"
                                        "  background-color: rgba(255, 255, 255, 200);\n"
                                        "  color: #ee7838;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.on_clicked_create_guide)
        #background-color: #006898
        self.pushButton_5.show()
        self.pushButton_7 = hover_button(self.main_menu)
        self.pushButton_7.setGeometry(QtCore.QRect(425, 635, 350, 40))
        self.pushButton_7.setStyleSheet("  border: none;\n"
                                        "  padding: 5px;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 20px;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: rgba(255, 255, 255, 200);\n"
                                        "  color: #ee7838;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.on_clicked_create_new_schedule)
        self.pushButton_7.show()
        self.pushButton = hover_button(self.main_menu)
        self.pushButton.setGeometry(QtCore.QRect(350, 400, 500, 75))
        self.pushButton.setStyleSheet(
                                        "  padding: 5px;\n"
                                        "     border: none;\n"
                                        "    cursor: pointer;\n"
                                        "    margin-bottom: 1%;\n"
                                        "    font-family: special_font;\n"
                                        "    font-size: 20px;\n"
                                        "    color: #ee7838;\n"
                                        "  background-color: rgba(255, 255, 255, 200);\n"
                                        " opacity: 0.8;\n")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_clicked_view_staff)
        self.pushButton.show()
        self.pushButton_4 = hover_button(self.main_menu)
        self.pushButton_4.setGeometry(QtCore.QRect(625, 480, 225, 40))
        self.pushButton_4.setStyleSheet("  border: none;\n"
                                        "  padding: 5px;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 20px;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: rgba(255, 255, 255, 200);\n"
                                        "  color: #ee7838;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.on_clicked_create_driver)
        self.pushButton_4.show()
        self.pushButton_3 =hover_button(self.main_menu)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 555, 500, 75))
        font = QtGui.QFont()
        font.setFamily("special_font")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("  padding: 5px;\n"
                                        "     border: none;\n"
                                        "    cursor: pointer;\n"
                                        "    margin-bottom: 1%;\n"
                                        "    font-family: special_font;\n"
                                        "    font-size: 20px;\n"
                                        "    opacity: 0.8;\n"
                                        "    color: #ee7838;\n"
                                        "  background-color: rgba(255, 255, 255, 200);\n")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_clicked_view_schedule)
        self.pushButton_3.show()
        self.stackedWidget.addWidget(self.main_menu)
        ########################################################################
        self.view_staff = QtWidgets.QWidget()
        self.view_staff.setObjectName("view_staff")
        self.view_staff.setStyleSheet("background-color:#FFFFFF")

        self.background = QtWidgets.QLabel(self.view_staff)
        self.background.setPixmap(QtGui.QPixmap('background.jpg'))
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 795))


        self.tableWidget = QtWidgets.QTableWidget(self.view_staff)
        self.tableWidget.setGeometry(QtCore.QRect(135, 175, 900, 250))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(50)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setStyleSheet("Background-color: rgba(255,255,255,200);\n"
                                        "  border-radius: 5%;\n")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.submit_changes = QtWidgets.QPushButton(self.view_staff)
        self.submit_changes.setGeometry(QtCore.QRect(914, 115, 121, 28))
        self.submit_changes.setStyleSheet(  "  border: none;\n"
                                            "  padding: 0.5%;\n"
                                            "  cursor: pointer;\n"
                                            "  font-family: special_font;\n"
                                            "  font-size: 130%;\n"
                                            "  border-radius: 3%;\n"
                                            "  opacity: 0.9;\n"
                                            "  background-color: #006898;\n"
                                            "  color: #ee7838;")
        self.submit_changes.setObjectName("submit_changes")
        self.back_1 = QtWidgets.QPushButton(self.view_staff)
        self.back_1.setGeometry(QtCore.QRect(942, 75, 93, 28))
        self.back_1.clicked.connect(self.back_page)
        self.back_1.show()
        self.back_1.setStyleSheet("  border: none;\n"
                                        "  padding: 0.5%;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 130%;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: #006898;\n"
                                        "  color: #ee7838;")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.view_staff)
        self.tableWidget_5.setGeometry(QtCore.QRect(135, 575, 900, 175))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(24)
        self.tableWidget_5.setRowCount(10)
        self.tableWidget_5.setStyleSheet("Background-color: rgba(255,255,255,200);\n"
                                        "  border-radius: 5%;\n")
        item_2 = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item_2)

        self.main_label_3 = QtWidgets.QLabel(self.view_staff)
        self.main_label_3.setGeometry(QtCore.QRect(135, 75, 355, 81))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        self.main_label_3.setFont(font)
        self.main_label_3.setStyleSheet( " background-color: #006898;\n"
                                            " border-radius: 5%;\n"
                                            "padding-left: 57px;\n"
                                            "  color: #ee7838;")
        self.main_label_3.setObjectName("main_label_3")

        self.main_label_4 = QtWidgets.QLabel(self.view_staff)
        self.main_label_4.setGeometry(QtCore.QRect(135, 475, 355, 81))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        self.main_label_4.setFont(font)
        self.main_label_4.setStyleSheet( " background-color: #006898;\n"
                                            " border-radius: 5%;\n"
                                            "padding-left: 57px;\n"
                                            "  color: #ee7838;")
        self.main_label_4.setObjectName("main_label_4")
        self.stackedWidget.addWidget(self.view_staff)
        self.load_staff_data()
        ########################################################################
        self.create_guide = QtWidgets.QWidget()
        self.create_guide.setStyleSheet("color: #ee7838;\n"
                                        "background-color:#FFFFFF")
        self.create_guide.setObjectName("create_guide")


        self.background = QtWidgets.QLabel(self.create_guide)
        self.background.setPixmap(QtGui.QPixmap('background.jpg'))
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 795))

        self.container= QtWidgets.QLabel(self.create_guide)
        self.container.setStyleSheet("Background-color: rgba(255,255,255,200);\n"
                                        "  border-radius: 5%;\n")
        self.container.setGeometry(QtCore.QRect(135, 262.5, 900, 350))


        self.back_2 = QtWidgets.QPushButton(self.create_guide)
        self.back_2.setGeometry(QtCore.QRect(942, 75, 93, 28))
        self.back_2.clicked.connect(self.back_page)
        self.back_2.show()
        self.back_2.setStyleSheet("  border: none;\n"
                                        "  padding: 0.5%;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 130%;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: #006898;\n"
                                        "  color: #ee7838;")
        self.can_tl_label = QtWidgets.QLabel(self.create_guide)
        self.can_tl_label.setGeometry(QtCore.QRect(175, 400, 150, 30))
        self.can_tl_label.setObjectName("can_tl_label")
        self.can_guide_label = QtWidgets.QLabel(self.create_guide)
        self.can_guide_label.setGeometry(QtCore.QRect(350, 400, 121, 23))
        self.can_guide_label.setObjectName("can_guide_label")
        self.can_safety_label = QtWidgets.QLabel(self.create_guide)
        self.can_safety_label.setGeometry(QtCore.QRect(525, 400, 150, 30))
        self.can_safety_label.setObjectName("can_safety_label")
        self.submit = QtWidgets.QPushButton(self.create_guide)
        self.submit.setGeometry(QtCore.QRect(942, 700, 93, 28))
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
        self.submit.clicked.connect(self.create_new_guide)
        self.submit.show()
        self.verticalWidget = QtWidgets.QWidget(self.create_guide)
        self.verticalWidget.setGeometry(QtCore.QRect(375, 440, 111, 131))
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
        self.canSafetyOptionWidget = QtWidgets.QWidget(self.create_guide)
        self.canSafetyOptionWidget.setGeometry(QtCore.QRect(550, 440, 111, 131))
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
        self.canTlOptionWidget = QtWidgets.QWidget(self.create_guide)
        self.canTlOptionWidget.setGeometry(QtCore.QRect(225, 440, 111, 131))
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
        self.guide_name = QtWidgets.QPlainTextEdit(self.create_guide)
        self.guide_name.setGeometry(QtCore.QRect(275, 325, 161, 21))
        self.guide_name.setStyleSheet("background-color: #FFFFFF")
        self.guide_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.guide_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.guide_name.setObjectName("guide_name")


        self.classIVOptionWidget = QtWidgets.QWidget(self.create_guide)
        self.classIVOptionWidget.setGeometry(QtCore.QRect(640, 327.5, 161, 21))
        self.classIVOptionWidget.setObjectName("classIVOptionWidget")
        self.classIVOptionLayout = QtWidgets.QVBoxLayout(self.classIVOptionWidget)
        self.classIVOptionLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.classIVOptionLayout.setContentsMargins(0, 0, 0, 0)
        self.classIVOptionLayout.setObjectName("classIVOptionLayout")
        self.class_IV = QtWidgets.QCheckBox(self.classIVOptionWidget)
        self.class_IV.setStyleSheet("")
        self.class_IV.setObjectName("class_IV")
        self.classIVOptionLayout.addWidget(self.class_IV)

        self.verticalWidget_4 = QtWidgets.QWidget(self.create_guide)
        self.verticalWidget_4.setGeometry(QtCore.QRect(900, 440, 89, 126))
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.priority_value_four_hour = QtWidgets.QTextEdit(self.verticalWidget_4)
        self.priority_value_four_hour.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_four_hour.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_four_hour.setObjectName("priority_value_four_hour")
        self.verticalLayout_4.addWidget(self.priority_value_four_hour)
        self.priority_value_full_day = QtWidgets.QTextEdit(self.verticalWidget_4)
        self.priority_value_full_day.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_full_day.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_full_day.setObjectName("priority_value_full_day")
        self.verticalLayout_4.addWidget(self.priority_value_full_day)
        self.priority_value_c_wave = QtWidgets.QTextEdit(self.verticalWidget_4)
        self.priority_value_c_wave.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_c_wave.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_c_wave.setObjectName("priority_value_c_wave")
        self.verticalLayout_4.addWidget(self.priority_value_c_wave)
        self.priority_value_float = QtWidgets.QTextEdit(self.verticalWidget_4)
        self.priority_value_float.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_float.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_float.setObjectName("priority_value_float")
        self.verticalLayout_4.addWidget(self.priority_value_float)
        self.priority_value__overnight = QtWidgets.QTextEdit(self.verticalWidget_4)
        self.priority_value__overnight.setStyleSheet("background-color: #FFFFFF")
        self.priority_value__overnight.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value__overnight.setObjectName("priority_value__overnight")
        self.verticalLayout_4.addWidget(self.priority_value__overnight)
        self.priority_label = QtWidgets.QLabel(self.create_guide)
        self.priority_label.setGeometry(QtCore.QRect(700, 399, 101, 31))
        self.priority_label.setObjectName("priority_label")
        self.name_label = QtWidgets.QLabel(self.create_guide)
        self.name_label.setGeometry(QtCore.QRect(175, 315, 81, 41))
        self.name_label.setStyleSheet("")
        self.name_label.setObjectName("name_label")
        self.class_label = QtWidgets.QLabel(self.create_guide)
        self.class_label.setGeometry(QtCore.QRect(525, 315, 90, 41))
        self.class_label.setStyleSheet("")
        self.class_label.setObjectName("name_label")
        self.main_label = QtWidgets.QLabel(self.create_guide)
        self.main_label.setGeometry(QtCore.QRect(135, 75, 355, 81))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        self.main_label.setFont(font)
        self.main_label.setStyleSheet( " background-color: #006898;\n"
                                            " border-radius: 5%;\n"
                                            "padding-left: 57px;")
        self.main_label.setObjectName("main_label")
        self.verticalWidget_2 = QtWidgets.QWidget(self.create_guide)
        self.verticalWidget_2.setGeometry(QtCore.QRect(730, 430, 161, 181))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setContentsMargins(0, 10, 10, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.four_hr_group = QtWidgets.QButtonGroup(self.create_guide)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.four_hr_group.addButton(self.radioButton)
        self.four_hr_group.addButton(self.radioButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.full_day_group = QtWidgets.QButtonGroup(self.create_guide)
        self.radioButton_31 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_31.setObjectName("radioButton_31")
        self.horizontalLayout_16.addWidget(self.radioButton_31)
        self.radioButton_32 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_32.setObjectName("radioButton_32")
        self.horizontalLayout_16.addWidget(self.radioButton_32)
        self.full_day_group.addButton(self.radioButton_31)
        self.full_day_group.addButton(self.radioButton_32)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.c_wave_group = QtWidgets.QButtonGroup(self.create_guide)
        self.radioButton_33 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_33.setObjectName("radioButton_33")
        self.horizontalLayout_17.addWidget(self.radioButton_33)
        self.radioButton_34 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_34.setObjectName("radioButton_34")
        self.horizontalLayout_17.addWidget(self.radioButton_34)
        self.c_wave_group.addButton(self.radioButton_33)
        self.c_wave_group.addButton(self.radioButton_34)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.float_group = QtWidgets.QButtonGroup(self.create_guide)
        self.radioButton_35 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_35.setObjectName("radioButton_35")
        self.horizontalLayout_18.addWidget(self.radioButton_35)
        self.radioButton_36 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_36.setObjectName("radioButton_36")
        self.horizontalLayout_18.addWidget(self.radioButton_36)
        self.float_group.addButton(self.radioButton_35)
        self.float_group.addButton(self.radioButton_36)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.overnight_group = QtWidgets.QButtonGroup(self.create_guide)
        self.radioButton_37 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_37.setObjectName("radioButton_37")
        self.horizontalLayout_19.addWidget(self.radioButton_37)
        self.radioButton_38 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.radioButton_38.setObjectName("radioButton_38")
        self.horizontalLayout_19.addWidget(self.radioButton_38)
        self.overnight_group.addButton(self.radioButton_35)
        self.overnight_group.addButton(self.radioButton_36)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.stackedWidget.addWidget(self.create_guide)
        ########################################################################
        self.create_driver = QtWidgets.QWidget()
        self.create_driver.setStyleSheet("color: #ee7838;\n"
                                         "background-color:#FFFFFF")
        self.create_driver.setObjectName("create_driver")

        self.background = QtWidgets.QLabel(self.create_driver)
        self.background.setPixmap(QtGui.QPixmap('background.jpg'))
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 795))

        self.container= QtWidgets.QLabel(self.create_driver)
        self.container.setStyleSheet("Background-color: rgba(255,255,255,200);\n"
                                        "  border-radius: 5%;\n")
        self.container.setGeometry(QtCore.QRect(135, 262.5, 900, 350))

        self.back_3 = QtWidgets.QPushButton(self.create_driver)
        self.back_3.setGeometry(QtCore.QRect(960, 75, 93, 28))
        self.back_3.clicked.connect(self.back_page)
        self.back_3.show()
        self.back_3.setStyleSheet("  border: none;\n"
                                        "  padding: 0.5%;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 130%;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: #006898;\n"
                                        "  color: #ee7838;")
        self.can_drive_label = QtWidgets.QLabel(self.create_driver)
        self.can_drive_label.setGeometry(QtCore.QRect(300, 400, 121, 23))
        self.can_drive_label.setObjectName("can_drive_label")
        self.can_drive_label.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.submit_2 = QtWidgets.QPushButton(self.create_driver)
        self.submit_2.clicked.connect(self.create_new_driver)
        self.submit_2.setGeometry(QtCore.QRect(942, 700, 93, 28))
        self.submit_2.setStyleSheet("  border: none;\n"
                                    "  padding: 0.5%;\n"
                                    "  cursor: pointer;\n"
                                    "  font-family: special_font;\n"
                                    "  font-size: 130%;\n"
                                    "  border-radius: 3%;\n"
                                    "  opacity: 0.9;\n"
                                    "  background-color: #006898;\n"
                                    "  color: #ee7838;")
        self.submit_2.setObjectName("submit")
        #self.submit_2.clicked.connect(self.create_new_driver)
        #self.submit_2.show()
        self.verticalWidget_7 = QtWidgets.QWidget(self.create_driver)
        self.verticalWidget_7.setGeometry(QtCore.QRect(325, 440, 111, 131))
        self.verticalWidget_7.setObjectName("verticalWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.can_drive_four_hour = QtWidgets.QCheckBox(self.verticalWidget_7)
        self.can_drive_four_hour.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.can_drive_four_hour.setObjectName("can_drive_four_hour")
        self.verticalLayout_7.addWidget(self.can_drive_four_hour)
        self.can_drive_full_day = QtWidgets.QCheckBox(self.verticalWidget_7)
        self.can_drive_full_day.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.can_drive_full_day.setObjectName("can_drive_full_day")
        self.verticalLayout_7.addWidget(self.can_drive_full_day)
        self.can_drive_c_wave = QtWidgets.QCheckBox(self.verticalWidget)
        self.can_drive_c_wave.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.can_drive_c_wave.setObjectName("can_drive_c_wave")
        self.verticalLayout_7.addWidget(self.can_drive_c_wave)
        self.can_drive_float = QtWidgets.QCheckBox(self.verticalWidget_7)
        self.can_drive_float.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.can_drive_float.setObjectName("can_drive_float")
        self.verticalLayout_7.addWidget(self.can_drive_float)
        self.can_drive_overnight = QtWidgets.QCheckBox(self.verticalWidget_7)
        self.can_drive_overnight.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.can_drive_overnight.setObjectName("can_drive_overnight")
        self.verticalLayout_7.addWidget(self.can_drive_overnight)
        self.driver_name = QtWidgets.QPlainTextEdit(self.create_driver)
        self.driver_name.setGeometry(QtCore.QRect(390, 325, 161, 21))
        self.driver_name.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.driver_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.driver_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.driver_name.setObjectName("driver_name")
        self.verticalWidget_8 = QtWidgets.QWidget(self.create_driver)
        self.verticalWidget_8.setGeometry(QtCore.QRect(760, 440, 89, 126))
        self.verticalWidget_8.setObjectName("verticalWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.priority_value_four_hour_2 = QtWidgets.QTextEdit(self.verticalWidget_8)
        self.priority_value_four_hour_2.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_four_hour_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_four_hour_2.setObjectName("priority_value_four_hour_2")
        self.verticalLayout_8.addWidget(self.priority_value_four_hour_2)
        self.priority_value_full_day_2 = QtWidgets.QTextEdit(self.verticalWidget_8)
        self.priority_value_full_day_2.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_full_day_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_full_day_2.setObjectName("priority_value_full_day_2")
        self.verticalLayout_8.addWidget(self.priority_value_full_day_2)
        self.priority_value_c_wave_2 = QtWidgets.QTextEdit(self.verticalWidget_8)
        self.priority_value_c_wave_2.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_c_wave_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_c_wave_2.setObjectName("priority_value_c_wave_2")
        self.verticalLayout_8.addWidget(self.priority_value_c_wave_2)
        self.priority_value_float_2 = QtWidgets.QTextEdit(self.verticalWidget_8)
        self.priority_value_float_2.setStyleSheet("background-color: #FFFFFF")
        self.priority_value_float_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value_float_2.setObjectName("priority_value_float_2")
        self.verticalLayout_8.addWidget(self.priority_value_float_2)
        self.priority_value__overnight_2 = QtWidgets.QTextEdit(self.verticalWidget_8)
        self.priority_value__overnight_2.setStyleSheet("background-color: #FFFFFF")
        self.priority_value__overnight_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.priority_value__overnight_2.setObjectName("priority_value__overnight")
        self.verticalLayout_8.addWidget(self.priority_value__overnight_2)

        self.priority_label_2 = QtWidgets.QLabel(self.create_driver)
        self.priority_label_2.setGeometry(QtCore.QRect(560, 399, 101, 31))
        self.priority_label_2.setObjectName("priority_label_2")
        self.priority_label_2.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.name_label_2 = QtWidgets.QLabel(self.create_driver)
        self.name_label_2.setGeometry(QtCore.QRect(300, 315, 81, 41))
        self.name_label_2.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.name_label_2.setObjectName("name_label_2")
        self.main_label_2 = QtWidgets.QLabel(self.create_driver)
        self.main_label_2.setGeometry(QtCore.QRect(135, 75, 355, 81))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        self.main_label_2.setFont(font)
        self.main_label_2.setStyleSheet( " background-color: #006898;\n"
                                            " border-radius: 5%;\n"
                                            "padding-left: 57px;")
        self.main_label_2.setObjectName("main_label_2")

        self.class_label_2 = QtWidgets.QLabel(self.create_driver)
        self.class_label_2.setGeometry(QtCore.QRect(590, 315, 90, 41))
        self.class_label_2.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.class_label_2.setObjectName("class_label_2")

        self.classIVOptionWidgetDriver = QtWidgets.QWidget(self.create_driver)
        self.classIVOptionWidgetDriver.setGeometry(QtCore.QRect(690, 327.5, 161, 21))
        self.classIVOptionWidgetDriver.setObjectName("classIVOptionWidgetDriver")
        self.classIVOptionLayoutDriver = QtWidgets.QVBoxLayout(self.classIVOptionWidgetDriver)
        self.classIVOptionLayoutDriver.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.classIVOptionLayoutDriver.setContentsMargins(0, 0, 0, 0)
        self.classIVOptionLayoutDriver.setObjectName("classIVOptionLayoutDriver")
        self.class_IVDriver = QtWidgets.QCheckBox(self.classIVOptionWidgetDriver)
        self.class_IVDriver.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.class_IVDriver.setObjectName("class_IVDriver")
        self.classIVOptionLayoutDriver.addWidget(self.class_IVDriver)


        self.verticalWidget_9 = QtWidgets.QWidget(self.create_driver)
        self.verticalWidget_9.setGeometry(QtCore.QRect(590, 430, 161, 181))
        self.verticalWidget_9.setObjectName("verticalWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget_9)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_9.setContentsMargins(0, 10, 10, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")

        self.four_hr_group_2 = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_22 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_22.setObjectName("radioButton_212")
        self.radioButton_22.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_22.addWidget(self.radioButton_22)
        self.radioButton_21 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_21.setObjectName("radioButton_21")
        self.radioButton_21.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_22.addWidget(self.radioButton_21)
        self.four_hr_group_2.addButton(self.radioButton_22)
        self.four_hr_group_2.addButton(self.radioButton_21)
        self.verticalLayout_9.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.full_day_group_2 = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_23 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_23.setObjectName("radioButton_23")
        self.radioButton_23.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_23.addWidget(self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_24.setObjectName("radioButton_24")
        self.radioButton_24.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_23.addWidget(self.radioButton_24)
        self.full_day_group_2.addButton(self.radioButton_23)
        self.full_day_group_2.addButton(self.radioButton_24)
        self.verticalLayout_9.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.c_wave_group_2 = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_25 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_25.setObjectName("radioButton_25")
        self.radioButton_25.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_24.addWidget(self.radioButton_25)
        self.radioButton_26 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_26.setObjectName("radioButton_26")
        self.radioButton_26.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_24.addWidget(self.radioButton_26)
        self.c_wave_group_2.addButton(self.radioButton_25)
        self.c_wave_group_2.addButton(self.radioButton_26)
        self.verticalLayout_9.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.float_group_2 = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_27 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_27.setObjectName("radioButton_27")
        self.radioButton_27.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_25.addWidget(self.radioButton_27)
        self.radioButton_28 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_28.setObjectName("radioButton_28")
        self.radioButton_28.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_25.addWidget(self.radioButton_28)
        self.float_group_2.addButton(self.radioButton_28)
        self.float_group_2.addButton(self.radioButton_27)
        self.verticalLayout_9.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.overnight_group_2 = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_29 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_29.setObjectName("radioButton_29")
        self.radioButton_29.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_26.addWidget(self.radioButton_29)
        self.radioButton_77 = QtWidgets.QRadioButton(self.verticalWidget_9)
        self.radioButton_77.setObjectName("radioButton_77")
        self.radioButton_77.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_26.addWidget(self.radioButton_77)
        self.overnight_group_2.addButton(self.radioButton_29)
        self.overnight_group_2.addButton(self.radioButton_77)
        self.verticalLayout_9.addLayout(self.horizontalLayout_26)

        self.verticalWidget_Seniority = QtWidgets.QWidget(self.create_driver)
        self.verticalWidget_Seniority.setGeometry(QtCore.QRect(440, 430, 161, 181))
        self.verticalWidget_Seniority.setObjectName("verticalWidget_Seniority")
        self.verticalLayout_Seniority = QtWidgets.QVBoxLayout(self.verticalWidget_Seniority)
        self.verticalLayout_Seniority.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_Seniority.setContentsMargins(0, 10, 10, 0)
        self.verticalLayout_Seniority.setObjectName("verticalLayout_Seniority")

        self.horizontalLayout_Seniority = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Seniority.setObjectName("horizontalLayout_Seniority")

        self.four_hr_group_Seniority = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_100 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_100.setObjectName("radioButton_100")
        self.radioButton_100.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority.addWidget(self.radioButton_100)
        self.radioButton_101 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_101.setObjectName("radioButton_101")
        self.radioButton_101.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority.addWidget(self.radioButton_101)
        self.four_hr_group_Seniority.addButton(self.radioButton_100)
        self.four_hr_group_Seniority.addButton(self.radioButton_101)
        self.verticalLayout_Seniority.addLayout(self.horizontalLayout_Seniority)
        self.horizontalLayout_Seniority_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Seniority_2.setObjectName("horizontalLayout_Seniority_2")
        self.full_day_group_Seniority = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_104 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_104.setObjectName("radioButton_104")
        self.radioButton_104.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_2.addWidget(self.radioButton_104)
        self.radioButton_105 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_105.setObjectName("radioButton_105")
        self.radioButton_105.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_2.addWidget(self.radioButton_105)
        self.full_day_group_Seniority.addButton(self.radioButton_104)
        self.full_day_group_Seniority.addButton(self.radioButton_105)
        self.verticalLayout_Seniority.addLayout(self.horizontalLayout_Seniority_2)
        self.horizontalLayout_Seniority_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Seniority_3.setObjectName("horizontalLayout_Seniority_3")
        self.c_wave_group_Seniority = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_106 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_106.setObjectName("radioButton_106")
        self.radioButton_106.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_3.addWidget(self.radioButton_106)
        self.radioButton_107 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_107.setObjectName("radioButton_107")
        self.radioButton_107.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_3.addWidget(self.radioButton_107)
        self.c_wave_group_Seniority.addButton(self.radioButton_106)
        self.c_wave_group_Seniority.addButton(self.radioButton_107)
        self.verticalLayout_Seniority.addLayout(self.horizontalLayout_Seniority_3)
        self.horizontalLayout_Seniority_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Seniority_4.setObjectName("horizontalLayout_Seniority_4")
        self.float_group_Seniority = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_108 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_108.setObjectName("radioButton_108")
        self.radioButton_108.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_4.addWidget(self.radioButton_108)
        self.radioButton_109 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_109.setObjectName("radioButton_109")
        self.radioButton_109.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_4.addWidget(self.radioButton_109)
        self.float_group_Seniority.addButton(self.radioButton_108)
        self.float_group_Seniority.addButton(self.radioButton_109)
        self.verticalLayout_Seniority.addLayout(self.horizontalLayout_Seniority_4)
        self.horizontalLayout_Seniority_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Seniority_5.setObjectName("horizontalLayout_Seniority_5")
        self.overnight_group_Seniority = QtWidgets.QButtonGroup(self.create_driver)
        self.radioButton_110 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_110.setObjectName("radioButton_110")
        self.radioButton_110.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_5.addWidget(self.radioButton_110)
        self.radioButton_111 = QtWidgets.QRadioButton(self.verticalWidget_Seniority)
        self.radioButton_111.setObjectName("radioButton_111")
        self.radioButton_111.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.horizontalLayout_Seniority_5.addWidget(self.radioButton_111)
        self.overnight_group_Seniority.addButton(self.radioButton_110)
        self.overnight_group_Seniority.addButton(self.radioButton_111)
        self.verticalLayout_Seniority.addLayout(self.horizontalLayout_Seniority_5)

        self.stackedWidget.addWidget(self.create_driver)
        ########################################################################
        self.view_schedule = QtWidgets.QWidget()
        self.view_schedule.setObjectName("view_schedule")
        self.view_schedule.setStyleSheet("background-color:#FFFFFF")

        self.background = QtWidgets.QLabel(self.view_schedule)
        self.background.setPixmap(QtGui.QPixmap('background.jpg'))
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 795))

        self.tableWidget_2 = QtWidgets.QTableWidget(self.view_schedule)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 50, 884, 700))
        self.tableWidget_2.setRowCount(56)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setStyleSheet("Background-color: rgba(255,255,255,200);\n"
                                        "  border-radius: 5%;\n")
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.back_4 = QtWidgets.QPushButton(self.view_schedule)
        self.back_4.setGeometry(QtCore.QRect(1015, 50, 93, 28))
        self.back_4.clicked.connect(self.back_page)
        self.back_4.show()
        self.back_4.setStyleSheet("  border: none;\n"
                                        "  padding: 0.5%;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 130%;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: #006898;\n"
                                        "  color: #ee7838;")

        self.start_date = QtWidgets.QDateEdit(self.view_schedule)
        self.start_date.setGeometry(QtCore.QRect(955, 170, 100, 22))
        self.start_date.setStyleSheet("background-color: #FFFFFF")
        self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 18), QtCore.QTime(0, 0, 0)))
        self.start_date.setObjectName("start_date")
        self.end_date = QtWidgets.QDateEdit(self.view_schedule)
        self.end_date.setGeometry(QtCore.QRect(1065, 170, 100, 22))
        self.end_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 25), QtCore.QTime(0, 0, 0)))
        self.end_date.setStyleSheet("background-color: #FFFFFF")
        self.end_date.setObjectName("start_date")


        self.submit_date_range = QtWidgets.QPushButton(self.view_schedule)
        self.submit_date_range.setGeometry(QtCore.QRect(1015, 225, 93, 28))
        self.submit_date_range.setStyleSheet("  border: none;\n"
                                        "  padding: 0.5%;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 130%;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: #006898;\n"
                                        "  color: #ee7838;")
        self.submit_date_range.setObjectName("submit_date_range")
        self.submit_date_range.clicked.connect(self.submit_dates)
        self.stackedWidget.addWidget(self.view_schedule)

        ########################################################################
        self.create_new_schedule = QtWidgets.QWidget()
        self.create_new_schedule.setStyleSheet("color: #ee7838;\n"
                                               "background-color:#FFFFFF")
        self.create_new_schedule.setObjectName("create_new_schedule")

        self.background = QtWidgets.QLabel(self.create_new_schedule)
        self.background.setPixmap(QtGui.QPixmap('background.jpg'))
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 795))

        self.container= QtWidgets.QLabel(self.create_new_schedule)
        self.container.setStyleSheet("Background-color: rgba(255,255,255,200);\n"
                                        "  border-radius: 5%;\n")
        self.container.setGeometry(QtCore.QRect(235, 262.5, 700, 250))

        self.file_path = QtWidgets.QTextEdit(self.create_new_schedule)
        self.file_path.setGeometry(QtCore.QRect(450, 350, 356, 31))
        self.file_path.setStyleSheet("background-color: #FFFFFF")
        self.file_path.setObjectName("file_path")
        self.label = QtWidgets.QLabel(self.create_new_schedule)
        self.label.setGeometry(QtCore.QRect(350, 350, 91, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.submit_3 = QtWidgets.QPushButton(self.create_new_schedule)
        self.submit_3.setGeometry(QtCore.QRect(710, 410, 93, 28))
        self.submit_3.setStyleSheet("  border: none;\n"
                                    "  padding: 0.5%;\n"
                                    "  cursor: pointer;\n"
                                    "  font-family: special_font;\n"
                                    "  font-size: 130%;\n"
                                    "  border-radius: 3%;\n"
                                    "  opacity: 0.9;\n"
                                    "  background-color: #006898;\n"
                                    "  color: #ee7838;")
        self.submit_3.setObjectName("submit_3")
        self.submit_3.clicked.connect(self.scrape_excel_sheet)
        self.submit_3.show()
        self.back_5 = QtWidgets.QPushButton(self.create_new_schedule)
        self.back_5.setGeometry(QtCore.QRect(942, 75, 93, 28))
        self.back_5.clicked.connect(self.back_page)
        self.back_5.show()
        self.back_5.setStyleSheet("  border: none;\n"
                                        "  padding: 0.5%;\n"
                                        "  cursor: pointer;\n"
                                        "  font-family: special_font;\n"
                                        "  font-size: 130%;\n"
                                        "  border-radius: 3%;\n"
                                        "  opacity: 0.9;\n"
                                        "  background-color: #006898;\n"
                                        "  color: #ee7838;")

        self.stackedWidget.addWidget(self.create_new_schedule)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, 0))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("Form", "Create Guide", None, 0))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("Form", "Create New Schedule", None, 0))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "View Staff", None, 0))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "Create Driver", None, 0))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "View Schedule", None, 0))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.submit_changes.setText(QtWidgets.QApplication.translate("Form", "Submit Changes", None, 0))
        self.can_guide_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Can Guide:</span></p></body></html>", None, 0))
        self.can_tl_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Can Trip Lead:</span></p></body></html>", None, 0))
        self.can_safety_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Can Safety:</span></p></body></html>", None, 0))
        self.submit.setText(QtWidgets.QApplication.translate("Form", "Submit", None, 0))
        self.can_guide_four_hour.setText(QtWidgets.QApplication.translate("Form", "Four Hour", None, 0))
        self.can_guide_full_day.setText(QtWidgets.QApplication.translate("Form", "Full Day", None, 0))
        self.can_guide_c_wave.setText(QtWidgets.QApplication.translate("Form", "C Wave", None, 0))
        self.can_guide_float.setText(QtWidgets.QApplication.translate("Form", "Float", None, 0))
        self.can_guide_overnight.setText(QtWidgets.QApplication.translate("Form", "Overnight", None, 0))
        self.can_safety_four_hour.setText(QtWidgets.QApplication.translate("Form", "Four Hour", None, 0))
        self.can_safety_full_day.setText(QtWidgets.QApplication.translate("Form", "Full Day", None, 0))
        self.can_safety_c_wave.setText(QtWidgets.QApplication.translate("Form", "C Wave", None, 0))
        self.can_safety_float.setText(QtWidgets.QApplication.translate("Form", "Float", None, 0))
        self.can_safety_overnight.setText(QtWidgets.QApplication.translate("Form", "Overnight", None, 0))
        self.can_Tl_four_hour.setText(QtWidgets.QApplication.translate("Form", "Four Hour", None, 0))
        self.can_Tl_full_day.setText(QtWidgets.QApplication.translate("Form", "Full Day", None, 0))
        self.can_Tl_c_wave.setText(QtWidgets.QApplication.translate("Form", "C Wave", None, 0))
        self.can_Tl_float.setText(QtWidgets.QApplication.translate("Form", "Float", None, 0))
        self.can_Tl_overnight.setText(QtWidgets.QApplication.translate("Form", "Overnight", None, 0))
        self.priority_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Priority:</span></p></body></html>", None, 0))
        self.name_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Name: </span></p></body></html>", None, 0))
        self.class_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Class IV: </span></p></body></html>", None, 0))
        self.main_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:24pt;\">Create Guide</span></p></body></html>", None, 0))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_31.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_32.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_33.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_34.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_35.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_36.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_37.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_38.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))


        self.can_drive_label.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Can Drive:</span></p></body></html>", None, 0))
        self.submit_2.setText(QtWidgets.QApplication.translate("Form", "Submit", None, 0))
        self.can_drive_four_hour.setText(QtWidgets.QApplication.translate("Form", "Four Hour", None, 0))
        self.can_drive_full_day.setText(QtWidgets.QApplication.translate("Form", "Full Day", None, 0))
        self.can_drive_c_wave.setText(QtWidgets.QApplication.translate("Form", "C Wave", None, 0))
        self.can_drive_float.setText(QtWidgets.QApplication.translate("Form", "Float", None, 0))
        self.can_drive_overnight.setText(QtWidgets.QApplication.translate("Form", "Overnight", None, 0))
        self.priority_label_2.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Priority:</span></p></body></html>", None, 0))
        self.name_label_2.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Name: </span></p></body></html>", None, 0))
        self.main_label_2.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:24pt;\">Create Driver</span></p></body></html>", None, 0))
        self.class_label_2.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:14pt;\">Class IV: </span></p></body></html>", None, 0))
        self.radioButton_22.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_21.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_23.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_24.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_25.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_26.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_27.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_28.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))
        self.radioButton_29.setText(QtWidgets.QApplication.translate("Form", "Default", None, 0))
        self.radioButton_77.setText(QtWidgets.QApplication.translate("Form", "other", None, 0))

        self.radioButton_100.setText(QtWidgets.QApplication.translate("Form", "High", None, 0))
        self.radioButton_101.setText(QtWidgets.QApplication.translate("Form", "Low", None, 0))
        self.radioButton_104.setText(QtWidgets.QApplication.translate("Form", "High", None, 0))
        self.radioButton_105.setText(QtWidgets.QApplication.translate("Form", "Low", None, 0))
        self.radioButton_106.setText(QtWidgets.QApplication.translate("Form", "High", None, 0))
        self.radioButton_107.setText(QtWidgets.QApplication.translate("Form", "Low", None, 0))
        self.radioButton_108.setText(QtWidgets.QApplication.translate("Form", "High", None, 0))
        self.radioButton_109.setText(QtWidgets.QApplication.translate("Form", "Low", None, 0))
        self.radioButton_110.setText(QtWidgets.QApplication.translate("Form", "High", None, 0))
        self.radioButton_111.setText(QtWidgets.QApplication.translate("Form", "Low", None, 0))

        self.main_label_3.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:24pt;\">Guides</span></p></body></html>", None, 0))
        self.main_label_4.setText(QtWidgets.QApplication.translate("Form", "<html><body><p><span style=\" font-size:24pt;\">Drivers</span></p></body></html>", None, 0))
        self.back_1.setText(QtWidgets.QApplication.translate("Form", "Back", None, 0))
        self.back_2.setText(QtWidgets.QApplication.translate("Form", "Back", None, 0))
        self.back_3.setText(QtWidgets.QApplication.translate("Form", "Back", None, 0))
        self.back_4.setText(QtWidgets.QApplication.translate("Form", "Back", None, 0))
        self.back_5.setText(QtWidgets.QApplication.translate("Form", "Back", None, 0))
        self.submit_date_range.setText(QtWidgets.QApplication.translate("Form", "Submit", None, 0))
        self.file_path.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, 0))
        self.label.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">File Path</span></p></body></html>", None, 0))
        self.submit_3.setText(QtWidgets.QApplication.translate("Form", "Submit", None, 0))
    def on_clicked_view_staff(self):
        self.load_staff_data()
        self.stackedWidget.setCurrentIndex(1)
    def on_clicked_create_guide(self):
        self.stackedWidget.setCurrentIndex(2)
    def on_clicked_create_driver(self):
        self.stackedWidget.setCurrentIndex(3)
    def on_clicked_view_schedule(self):

        row_number = 0

        for row in range(0, 56, 8):

            self.tableWidget_2.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem(create_schedule.schedule_dictionaries.view_staff_headers[row/8]))

            for index in range(1, 8):
                item = QtWidgets.QTableWidgetItem(create_schedule.schedule_dictionaries.role_switch[index-1])
                self.tableWidget_2.setVerticalHeaderItem(index+row, item)

            row+=1

        self.stackedWidget.setCurrentIndex(4)
    def on_clicked_create_new_schedule(self):
        self.stackedWidget.setCurrentIndex(5)
    def back_page(self):
        self.stackedWidget.setCurrentIndex(0)


    def create_new_guide(self):
        name = self.guide_name.toPlainText()
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
        if(self.radioButton_2.isChecked()):
            priority_four_hour = 1
        else:
            priority_four_hour = int(self.priority_value_four_hour.toPlainText())
        if(self.radioButton_31.isChecked()):
            priority_full_day = 1
        else:
            priority_full_day = int(self.priority_value_full_day.toPlainText())
        if(self.radioButton_33.isChecked()):
            priority_c_wave = 1
        else:
            priority_c_wave = int(self.priority_value_c_wave.toPlainText())
        if(self.radioButton_35.isChecked()):
            priority_float = 1
        else:
            priority_float = int(self.priority_value_float.toPlainText())
        if(self.radioButton_37.isChecked()):
            priority_overnight = 1
        else:
            priority_overnight = int(self.priority_value__overnight.toPlainText())


        new_guide = manage_staff.guide.guide(   name = name, in_stream = 'true', has_class_IV = has_class_IV,
                                                tl_four_hour = four_hour, tl_c_wave = c_wave, tl_full_day = full_day,
                                                tl_scenic_float = float, tl_overnight = overnight, guide_four_hour = four_hour_guide, guide_c_wave = c_wave_guide,
                                                guide_full_day = full_day_guide, guide_scenic_float = float_guide, guide_overnight = overnight_guide, safety_four_hour= four_hour_safety,
                                                safety_c_wave = c_wave_safety, safety_full_day= full_day_safety, safety_scenic_float = float_safety, safety_overnight = overnight_safety,
                                                tl_this_summer_four_hour = priority_four_hour,
                                                tl_this_summer_c_wave = priority_c_wave,
                                                tl_this_summer_full_day = priority_full_day,
                                                tl_this_summer_scenic_float = priority_float,
                                                tl_this_summer_overnight = priority_overnight,
                                                tl_this_period_four_hour = 1,
                                                tl_this_period_c_wave = 1,
                                                tl_this_period_full_day = 1,
                                                tl_this_period_scenic_float = 1,
                                                tl_this_period_overnight = 1,
                                                guided_this_summer_four_hour = priority_four_hour, guided_this_summer_c_wave = priority_c_wave,
                                                guided_this_summer_full_day = priority_full_day, guided_this_summer_scenic_float = priority_float,
                                                guided_this_summer_overnight = priority_overnight, guided_this_period_four_hour = 1,
                                                guided_this_period_c_wave = 1, guided_this_period_full_day = 1,
                                                guided_this_period_scenic_float = 1, guided_this_period_overnight = 1,
                                                safety_this_summer_four_hour = 1, safety_this_summer_c_wave = 1,
                                                safety_this_summer_full_day = 1, safety_this_summer_scenic_float=1,
                                                safety_this_summer_overnight = 1,
                                                safety_this_period_four_hour = 1, safety_this_period_c_wave = 1,
                                                safety_this_period_full_day = 1, safety_this_period_scenic_float = 1,
                                                safety_this_period_overnight = 1,
                                                days_since_last_day_off = 1
                                            )

        session_guide.add(new_guide)
        session_guide.commit()

        self.on_clicked_view_staff()

    def create_new_driver(self):
          name = self.driver_name.toPlainText()
          has_class_IV = self.class_IVDriver.isChecked()
          four_hour_drive = self.can_drive_four_hour.isChecked()
          full_day_drive = self.can_drive_full_day.isChecked()
          c_wave_drive = self.can_drive_c_wave.isChecked()
          float_drive = self.can_drive_float.isChecked()
          overnight_drive = self.can_drive_overnight.isChecked()

          if(self.radioButton_22.isChecked()):
              priority_four_hour = 0
          else:
              priority_four_hour = int(self.priority_value_four_hour_2.toPlainText())
          if(self.radioButton_23.isChecked()):
              priority_full_day = 0
          else:
              priority_full_day = int(self.priority_value_full_day_2.toPlainText())
          if(self.radioButton_25.isChecked()):
              priority_c_wave = 0
          else:
              priority_c_wave = int(self.priority_value_c_wave_2.toPlainText())
          if(self.radioButton_27.isChecked()):
              priority_float = 0
          else:
              priority_float = int(self.priority_value_float_2.toPlainText())
          if(self.radioButton_29.isChecked()):
              priority_overnight = 0
          else:
              priority_overnight = int(self.priority_value__overnight_2.toPlainText())

          if(self.radioButton_100.isChecked()):
              seniority_four_hour = 1
          else:
             seniority_four_hour = 0
          if(self.radioButton_104.isChecked()):
              seniority_full_day = 1
          else:
             seniority_full_day = 0
          if(self.radioButton_106.isChecked()):
              seniority_c_wave = 1
          else:
              seniority_c_wave = 0
          if(self.radioButton_108.isChecked()):
              seniority_float = 1
          else:
              seniority_float = 0
          if(self.radioButton_110.isChecked()):
              seniority_overnight = 1
          else:
             seniority_overnight = 0



          new_driver = manage_staff.driver.driver(    name = name, in_stream = 'true',
                                                    has_class_IV = has_class_IV, four_hour = four_hour_drive,
                                                    c_wave = c_wave_drive, full_day = full_day_drive,
                                                    scenic_float = float_drive, overnight = overnight_drive,
                                                    four_hour_seniority = seniority_four_hour,
                                                    c_wave_seniority = seniority_c_wave, full_day_seniority = seniority_full_day,
                                                    scenic_float_seniority = seniority_float, overnight_seniority = seniority_overnight,
                                                    driven_this_summer_four_hour = priority_four_hour,
                                                    driven_this_summer_c_wave = priority_c_wave,
                                                    driven_this_summer_full_day = priority_full_day,
                                                    driven_this_summer_scenic_float = priority_float,
                                                    driven_this_summer_overnight = priority_overnight,
                                                    driven_this_period_four_hour = 0,
                                                    driven_this_period_c_wave = 0,
                                                    driven_this_period_full_day = 0,
                                                    driven_this_period_scenic_float = 0,
                                                    driven_this_period_overnight = 0,
                                                    days_since_last_day_off = 0,
                                            )

          session_driver.add(new_driver)
          session_driver.commit()

          self.on_clicked_view_staff()




    def submit_dates(self):

        temp_date = self.start_date.dateTime()
        start = self.start_date.textFromDateTime(temp_date)
        temp_date = self.end_date.dateTime()
        end = self.end_date.textFromDateTime(temp_date)
        self.load_schedule_data(start, end)

    def load_staff_data(self):

        guide_header = [   "name",
                      "in_stream",
                      "has_class_IV",
                      "tl_four_hour",
                      "tl_c_wave",
                      "tl_full_day",
                      "tl_scenic_float",
                      "tl_overnight",
                      "guide_four_hour",
                      "guide_c_wave",
                      "guide_full_day",
                      "guide_scenic_float",
                      "guide_overnight",
                      "safety_four_hour",
                      "safety_c_wave",
                      "safety_full_day",
                      "safety_scenic_float",
                      "safety_overnight",
                      "tl_this_summer_four_hour",
                      "tl_this_summer_c_wave",
                      "tl_this_summer_full_day",
                      "tl_this_summer_scenic_float",
                      "tl_this_summer_overnight",
                      "tl_this_period_four_hour",
                      "tl_this_period_c_wave",
                      "tl_this_period_full_day",
                      "tl_this_period_scenic_float",
                      "tl_this_period_overnight",
                      "guided_this_summer_four_hour",
                      "guided_this_summer_c_wave",
                      "guided_this_summer_full_day",
                      "guided_this_summer_scenic_float",
                      "guided_this_summer_overnight",
                      "guided_this_period_four_hour",
                      "guided_this_period_c_wave",
                      "guided_this_period_full_day",
                      "guided_this_period_scenic_float",
                      "guided_this_period_overnight",
                      "safety_this_summer_four_hour",
                      "safety_this_summer_c_wave",
                      "safety_this_summer_full_day",
                      "safety_this_summer_overnight",
                      "safety_this_period_four_hour",
                      "safety_this_period_c_wave",
                      "safety_this_period_full_day",
                      "safety_this_period_overnight",
                      "days_since_last_day_off"]

        driver_header = [   'name',
                            'in_stream',
                            'has_class_IV',
                            'four_hour',
                            'c_wave',
                            'full_day',
                            'scenic_float',
                            'overnight',
                            'four_hour_seniority',
                            'c_wave_seniority',
                            'full_day_seniority',
                            'scenic_float_seniority',
                            'overnight_seniority',
                            'driven_this_summer_four_hour',
                            'driven_this_summer_c_wave',
                            'driven_this_summer_full_day',
                            'driven_this_summer_scenic_float',
                            'driven_this_summer_overnight',
                            'driven_this_period_four_hour',
                            'driven_this_period_c_wave',
                            'driven_this_period_full_day',
                            'driven_this_period_scenic_float',
                            'driven_this_period_overnight',
                            'days_since_last_day_off']

        self.tableWidget.setHorizontalHeaderLabels(guide_header)
        self.tableWidget_5.setHorizontalHeaderLabels(driver_header)

        self.tableWidget.setRowCount(0)
        self.tableWidget_5.setRowCount(0)

        guide_object = session_guide.query(manage_staff.guide.guide)
        guide_list = [u.__dict__ for u in guide_object.all()]
        print("\n\n",guide_list)




# print(QtGui.QStyleFactory.keys())

        for row in range(len(guide_list)):

            self.tableWidget.insertRow(row)

            for column in range(len(guide_header)):

                item = QtWidgets.QTableWidgetItem(str(guide_list[row][guide_header[column]]))
                self.tableWidget.setItem(row, column, item)

        self.tableWidget.verticalHeader().setStyle(QtWidgets.QStyleFactory.create('CleanLooks'))

        driver_object = session_driver.query(manage_staff.driver.driver)
        driver_list = [u.__dict__ for u in driver_object.all()]


        for row in range(len(driver_list)):
            self.tableWidget_5.insertRow(row)
            for column in range(len(driver_list[row])-1):

                self.tableWidget_5.setItem(row, column, QtWidgets.QTableWidgetItem(str(driver_list[row][driver_header[column]])))


    def load_schedule_data(self, start_date, end_date):

        connection_trips = sqlite3.connect('trips.db')
        c_trips = connection_trips.cursor()

        print(start_date, end_date)

        date = start_date
        day_of_week = int(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%w'))
        end_date = create_schedule.schedule_util.calculate_next_date(end_date)

        row_label = []

        column_label = [0,0,0,0,0,0,0]

        column_number = day_of_week

        column_label.insert(column_number, date)
        del column_label[column_number+1]

        current_date = date
        for day in range (day_of_week+1,7):
            column_label.insert(day, create_schedule.schedule_util.calculate_next_date(current_date))
            del column_label[day+1]
            current_date  = create_schedule.schedule_util.calculate_next_date(current_date)

        current_date = date
        for day in range (0, day_of_week):
            column_label.insert(day, create_schedule.schedule_util.calculate_previous_date(current_date))
            del column_label[day+1]
            current_date = create_schedule.schedule_util.calculate_previous_date(current_date)

        for row in range(0, 56, 8):

            self.tableWidget_2.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem(create_schedule.schedule_dictionaries.view_staff_headers[row/8]))

            for index in range(1, 8):

                self.tableWidget_2.setVerticalHeaderItem(index+row, QtWidgets.QTableWidgetItem(create_schedule.schedule_dictionaries.role_switch[index-1]))

            row+=1

        for column in range(0,7):
            self.tableWidget_2.setHorizontalHeaderItem(column, QtWidgets.QTableWidgetItem(column_label[column]))

        while date != end_date:
            print(date)


            for row in range(0, 56, 8):

                self.tableWidget_2.setItem(row, column_number, QtWidgets.QTableWidgetItem(""))
                print(row)
                for trip_num in range(1,8):
                    c_trips.execute("SELECT "+create_schedule.schedule_dictionaries.role_switch[trip_num-1]+create_schedule.schedule_dictionaries.trip_switch_numerical[row/8]+" FROM schedule WHERE date =  ?",(date,))
                    result = c_trips.fetchone()
                    print(row+trip_num)


                    if result[0] is not None:
                        self.tableWidget_2.setItem(row+trip_num, column_number, QtWidgets.QTableWidgetItem(str(result[0])))


            column_number+=1


            date = create_schedule.schedule_util.calculate_next_date(date)
        c_trips.close()


    def scrape_excel_sheet(self):
        path = self.file_path.toPlainText()

        excel_data = excel_scraper.scraper.excel_scraper(path)
        date = excel_data.get_first_date()
        num_days = excel_data.get_num_days()

        for x in range(0, num_days):
            create_schedule.create_new_schedule.create_schedule_day(self, excel_data, date)
            date = create_schedule.schedule_util.calculate_next_date(date)

        self.load_schedule_data(excel_data.get_first_date(), create_schedule.schedule_util.calculate_previous_date(date))

        self.on_clicked_view_schedule()
