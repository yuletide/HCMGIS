# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_prefix_suffix_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hcmgis_prefix_suffix_form(object):
    def setupUi(self, hcmgis_prefix_suffix_form):
        hcmgis_prefix_suffix_form.setObjectName("hcmgis_prefix_suffix_form")
        hcmgis_prefix_suffix_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_prefix_suffix_form.setEnabled(True)
        hcmgis_prefix_suffix_form.resize(343, 265)
        hcmgis_prefix_suffix_form.setMouseTracking(False)
        self.LblChar = QtWidgets.QLabel(hcmgis_prefix_suffix_form)
        self.LblChar.setGeometry(QtCore.QRect(10, 109, 151, 16))
        self.LblChar.setObjectName("LblChar")
        self.BtnOKCancel = QtWidgets.QDialogButtonBox(hcmgis_prefix_suffix_form)
        self.BtnOKCancel.setGeometry(QtCore.QRect(180, 220, 156, 51))
        self.BtnOKCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.BtnOKCancel.setObjectName("BtnOKCancel")
        self.LblInput = QtWidgets.QLabel(hcmgis_prefix_suffix_form)
        self.LblInput.setGeometry(QtCore.QRect(10, 11, 321, 16))
        self.LblInput.setObjectName("LblInput")
        self.CboInput = QgsMapLayerComboBox(hcmgis_prefix_suffix_form)
        self.CboInput.setGeometry(QtCore.QRect(10, 27, 321, 21))
        self.CboInput.setObjectName("CboInput")
        self.LblOutput_2 = QtWidgets.QLabel(hcmgis_prefix_suffix_form)
        self.LblOutput_2.setGeometry(QtCore.QRect(10, 60, 321, 16))
        self.LblOutput_2.setObjectName("LblOutput_2")
        self.CboField = QgsFieldComboBox(hcmgis_prefix_suffix_form)
        self.CboField.setGeometry(QtCore.QRect(10, 77, 321, 21))
        self.CboField.setObjectName("CboField")
        self.LinPrefix = QtWidgets.QLineEdit(hcmgis_prefix_suffix_form)
        self.LinPrefix.setGeometry(QtCore.QRect(10, 125, 151, 20))
        self.LinPrefix.setObjectName("LinPrefix")
        self.LblChar_2 = QtWidgets.QLabel(hcmgis_prefix_suffix_form)
        self.LblChar_2.setGeometry(QtCore.QRect(10, 155, 41, 20))
        self.LblChar_2.setObjectName("LblChar_2")
        self.LinSuffix = QtWidgets.QLineEdit(hcmgis_prefix_suffix_form)
        self.LinSuffix.setGeometry(QtCore.QRect(10, 173, 151, 20))
        self.LinSuffix.setObjectName("LinSuffix")
        self.CboCharPrefix = QtWidgets.QComboBox(hcmgis_prefix_suffix_form)
        self.CboCharPrefix.setGeometry(QtCore.QRect(180, 125, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CboCharPrefix.setFont(font)
        self.CboCharPrefix.setEditable(True)
        self.CboCharPrefix.setObjectName("CboCharPrefix")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.CboCharPrefix.addItem("")
        self.LblChar_3 = QtWidgets.QLabel(hcmgis_prefix_suffix_form)
        self.LblChar_3.setGeometry(QtCore.QRect(180, 109, 151, 16))
        self.LblChar_3.setObjectName("LblChar_3")
        self.LblChar_4 = QtWidgets.QLabel(hcmgis_prefix_suffix_form)
        self.LblChar_4.setGeometry(QtCore.QRect(180, 155, 151, 16))
        self.LblChar_4.setObjectName("LblChar_4")
        self.CboCharSuffix = QtWidgets.QComboBox(hcmgis_prefix_suffix_form)
        self.CboCharSuffix.setGeometry(QtCore.QRect(180, 173, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CboCharSuffix.setFont(font)
        self.CboCharSuffix.setEditable(True)
        self.CboCharSuffix.setObjectName("CboCharSuffix")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.CboCharSuffix.addItem("")
        self.ChkSelectedFeaturesOnly = QtWidgets.QCheckBox(hcmgis_prefix_suffix_form)
        self.ChkSelectedFeaturesOnly.setGeometry(QtCore.QRect(10, 207, 321, 17))
        self.ChkSelectedFeaturesOnly.setObjectName("ChkSelectedFeaturesOnly")

        self.retranslateUi(hcmgis_prefix_suffix_form)
        self.BtnOKCancel.accepted.connect(hcmgis_prefix_suffix_form.accept)
        self.BtnOKCancel.rejected.connect(hcmgis_prefix_suffix_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_prefix_suffix_form)

    def retranslateUi(self, hcmgis_prefix_suffix_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_prefix_suffix_form.setWindowTitle(_translate("hcmgis_prefix_suffix_form", "Add Prefix/ Suffix"))
        self.LblChar.setText(_translate("hcmgis_prefix_suffix_form", "Prefix"))
        self.LblInput.setText(_translate("hcmgis_prefix_suffix_form", "Imput Layer"))
        self.LblOutput_2.setText(_translate("hcmgis_prefix_suffix_form", "Field"))
        self.LblChar_2.setText(_translate("hcmgis_prefix_suffix_form", "Suffix"))
        self.CboCharPrefix.setItemText(0, _translate("hcmgis_prefix_suffix_form", "Space"))
        self.CboCharPrefix.setItemText(1, _translate("hcmgis_prefix_suffix_form", "Tab"))
        self.CboCharPrefix.setItemText(2, _translate("hcmgis_prefix_suffix_form", ","))
        self.CboCharPrefix.setItemText(3, _translate("hcmgis_prefix_suffix_form", "_"))
        self.CboCharPrefix.setItemText(4, _translate("hcmgis_prefix_suffix_form", "-"))
        self.CboCharPrefix.setItemText(5, _translate("hcmgis_prefix_suffix_form", "/"))
        self.CboCharPrefix.setItemText(6, _translate("hcmgis_prefix_suffix_form", "|"))
        self.CboCharPrefix.setItemText(7, _translate("hcmgis_prefix_suffix_form", "\\"))
        self.CboCharPrefix.setItemText(8, _translate("hcmgis_prefix_suffix_form", "."))
        self.CboCharPrefix.setItemText(9, _translate("hcmgis_prefix_suffix_form", ":"))
        self.CboCharPrefix.setItemText(10, _translate("hcmgis_prefix_suffix_form", ";"))
        self.CboCharPrefix.setItemText(11, _translate("hcmgis_prefix_suffix_form", "~"))
        self.CboCharPrefix.setItemText(12, _translate("hcmgis_prefix_suffix_form", "`"))
        self.CboCharPrefix.setItemText(13, _translate("hcmgis_prefix_suffix_form", "!"))
        self.CboCharPrefix.setItemText(14, _translate("hcmgis_prefix_suffix_form", "@"))
        self.CboCharPrefix.setItemText(15, _translate("hcmgis_prefix_suffix_form", "#"))
        self.CboCharPrefix.setItemText(16, _translate("hcmgis_prefix_suffix_form", "$"))
        self.CboCharPrefix.setItemText(17, _translate("hcmgis_prefix_suffix_form", "%"))
        self.CboCharPrefix.setItemText(18, _translate("hcmgis_prefix_suffix_form", "&"))
        self.CboCharPrefix.setItemText(19, _translate("hcmgis_prefix_suffix_form", "*"))
        self.CboCharPrefix.setItemText(20, _translate("hcmgis_prefix_suffix_form", "("))
        self.CboCharPrefix.setItemText(21, _translate("hcmgis_prefix_suffix_form", ")"))
        self.CboCharPrefix.setItemText(22, _translate("hcmgis_prefix_suffix_form", "{"))
        self.CboCharPrefix.setItemText(23, _translate("hcmgis_prefix_suffix_form", "}"))
        self.CboCharPrefix.setItemText(24, _translate("hcmgis_prefix_suffix_form", "["))
        self.CboCharPrefix.setItemText(25, _translate("hcmgis_prefix_suffix_form", "]"))
        self.CboCharPrefix.setItemText(26, _translate("hcmgis_prefix_suffix_form", "\'"))
        self.CboCharPrefix.setItemText(27, _translate("hcmgis_prefix_suffix_form", "\""))
        self.CboCharPrefix.setItemText(28, _translate("hcmgis_prefix_suffix_form", "<"))
        self.CboCharPrefix.setItemText(29, _translate("hcmgis_prefix_suffix_form", ">"))
        self.LblChar_3.setText(_translate("hcmgis_prefix_suffix_form", "Linking Characters"))
        self.LblChar_4.setText(_translate("hcmgis_prefix_suffix_form", "Linking Characters"))
        self.CboCharSuffix.setItemText(0, _translate("hcmgis_prefix_suffix_form", "Space"))
        self.CboCharSuffix.setItemText(1, _translate("hcmgis_prefix_suffix_form", "Tab"))
        self.CboCharSuffix.setItemText(2, _translate("hcmgis_prefix_suffix_form", ","))
        self.CboCharSuffix.setItemText(3, _translate("hcmgis_prefix_suffix_form", "_"))
        self.CboCharSuffix.setItemText(4, _translate("hcmgis_prefix_suffix_form", "-"))
        self.CboCharSuffix.setItemText(5, _translate("hcmgis_prefix_suffix_form", "/"))
        self.CboCharSuffix.setItemText(6, _translate("hcmgis_prefix_suffix_form", "|"))
        self.CboCharSuffix.setItemText(7, _translate("hcmgis_prefix_suffix_form", "\\"))
        self.CboCharSuffix.setItemText(8, _translate("hcmgis_prefix_suffix_form", "."))
        self.CboCharSuffix.setItemText(9, _translate("hcmgis_prefix_suffix_form", ":"))
        self.CboCharSuffix.setItemText(10, _translate("hcmgis_prefix_suffix_form", ";"))
        self.CboCharSuffix.setItemText(11, _translate("hcmgis_prefix_suffix_form", "~"))
        self.CboCharSuffix.setItemText(12, _translate("hcmgis_prefix_suffix_form", "`"))
        self.CboCharSuffix.setItemText(13, _translate("hcmgis_prefix_suffix_form", "!"))
        self.CboCharSuffix.setItemText(14, _translate("hcmgis_prefix_suffix_form", "@"))
        self.CboCharSuffix.setItemText(15, _translate("hcmgis_prefix_suffix_form", "#"))
        self.CboCharSuffix.setItemText(16, _translate("hcmgis_prefix_suffix_form", "$"))
        self.CboCharSuffix.setItemText(17, _translate("hcmgis_prefix_suffix_form", "%"))
        self.CboCharSuffix.setItemText(18, _translate("hcmgis_prefix_suffix_form", "&"))
        self.CboCharSuffix.setItemText(19, _translate("hcmgis_prefix_suffix_form", "*"))
        self.CboCharSuffix.setItemText(20, _translate("hcmgis_prefix_suffix_form", "("))
        self.CboCharSuffix.setItemText(21, _translate("hcmgis_prefix_suffix_form", ")"))
        self.CboCharSuffix.setItemText(22, _translate("hcmgis_prefix_suffix_form", "{"))
        self.CboCharSuffix.setItemText(23, _translate("hcmgis_prefix_suffix_form", "}"))
        self.CboCharSuffix.setItemText(24, _translate("hcmgis_prefix_suffix_form", "["))
        self.CboCharSuffix.setItemText(25, _translate("hcmgis_prefix_suffix_form", "]"))
        self.CboCharSuffix.setItemText(26, _translate("hcmgis_prefix_suffix_form", "\'"))
        self.CboCharSuffix.setItemText(27, _translate("hcmgis_prefix_suffix_form", "\""))
        self.CboCharSuffix.setItemText(28, _translate("hcmgis_prefix_suffix_form", "<"))
        self.CboCharSuffix.setItemText(29, _translate("hcmgis_prefix_suffix_form", ">"))
        self.ChkSelectedFeaturesOnly.setText(_translate("hcmgis_prefix_suffix_form", "Selected features only"))

from qgis.gui import QgsFieldComboBox, QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_prefix_suffix_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_prefix_suffix_form()
    ui.setupUi(hcmgis_prefix_suffix_form)
    hcmgis_prefix_suffix_form.show()
    sys.exit(app.exec_())
