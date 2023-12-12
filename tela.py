# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setMinimumSize(QtCore.QSize(400, 650))
        MainWindow.setMaximumSize(QtCore.QSize(400, 650))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(215, 215, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputLabel = QtWidgets.QLabel(self.frame)
        self.outputLabel.setStyleSheet("\n"
"font: 35pt \"Arial Rounded MT Bold\";\n"
"\n"
"background-color: #fff;\n"
"color: #000;\n"
"")
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout.addWidget(self.outputLabel)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clearButton = QtWidgets.QPushButton(self.frame_6)
        self.clearButton.setMinimumSize(QtCore.QSize(0, 0))
        self.clearButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.clearButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(200, 196, 255);\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_6.addWidget(self.clearButton)
        self.percentagemButton = QtWidgets.QPushButton(self.frame_6)
        self.percentagemButton.setMinimumSize(QtCore.QSize(0, 0))
        self.percentagemButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.percentagemButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(200, 196, 255);\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.percentagemButton.setObjectName("percentagemButton")
        self.horizontalLayout_6.addWidget(self.percentagemButton)
        self.backsplaceButton = QtWidgets.QPushButton(self.frame_6)
        self.backsplaceButton.setMinimumSize(QtCore.QSize(0, 0))
        self.backsplaceButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.backsplaceButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(200, 196, 255);\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.backsplaceButton.setObjectName("backsplaceButton")
        self.horizontalLayout_6.addWidget(self.backsplaceButton)
        self.divisaoButton = QtWidgets.QPushButton(self.frame_6)
        self.divisaoButton.setMinimumSize(QtCore.QSize(0, 0))
        self.divisaoButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.divisaoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(200, 196, 255);\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.divisaoButton.setObjectName("divisaoButton")
        self.horizontalLayout_6.addWidget(self.divisaoButton)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.seteButton = QtWidgets.QPushButton(self.frame_2)
        self.seteButton.setMinimumSize(QtCore.QSize(0, 0))
        self.seteButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.seteButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.seteButton.setObjectName("seteButton")
        self.horizontalLayout_2.addWidget(self.seteButton)
        self.oitoButton = QtWidgets.QPushButton(self.frame_2)
        self.oitoButton.setMinimumSize(QtCore.QSize(0, 0))
        self.oitoButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.oitoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.oitoButton.setObjectName("oitoButton")
        self.horizontalLayout_2.addWidget(self.oitoButton)
        self.noveButton = QtWidgets.QPushButton(self.frame_2)
        self.noveButton.setMinimumSize(QtCore.QSize(0, 0))
        self.noveButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.noveButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.noveButton.setObjectName("noveButton")
        self.horizontalLayout_2.addWidget(self.noveButton)
        self.multiplicacaoButton = QtWidgets.QPushButton(self.frame_2)
        self.multiplicacaoButton.setMinimumSize(QtCore.QSize(0, 0))
        self.multiplicacaoButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.multiplicacaoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.multiplicacaoButton.setObjectName("multiplicacaoButton")
        self.horizontalLayout_2.addWidget(self.multiplicacaoButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quatroButton = QtWidgets.QPushButton(self.frame_3)
        self.quatroButton.setMinimumSize(QtCore.QSize(0, 0))
        self.quatroButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.quatroButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.quatroButton.setObjectName("quatroButton")
        self.horizontalLayout_3.addWidget(self.quatroButton)
        self.cincoButton = QtWidgets.QPushButton(self.frame_3)
        self.cincoButton.setMinimumSize(QtCore.QSize(0, 0))
        self.cincoButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.cincoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.cincoButton.setObjectName("cincoButton")
        self.horizontalLayout_3.addWidget(self.cincoButton)
        self.seisButton = QtWidgets.QPushButton(self.frame_3)
        self.seisButton.setMinimumSize(QtCore.QSize(0, 0))
        self.seisButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.seisButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.seisButton.setObjectName("seisButton")
        self.horizontalLayout_3.addWidget(self.seisButton)
        self.menosButton = QtWidgets.QPushButton(self.frame_3)
        self.menosButton.setMinimumSize(QtCore.QSize(0, 0))
        self.menosButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.menosButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.menosButton.setObjectName("menosButton")
        self.horizontalLayout_3.addWidget(self.menosButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.umButton = QtWidgets.QPushButton(self.frame_4)
        self.umButton.setMinimumSize(QtCore.QSize(0, 0))
        self.umButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.umButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.umButton.setObjectName("umButton")
        self.horizontalLayout_4.addWidget(self.umButton)
        self.doisButton = QtWidgets.QPushButton(self.frame_4)
        self.doisButton.setMinimumSize(QtCore.QSize(0, 0))
        self.doisButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.doisButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.doisButton.setObjectName("doisButton")
        self.horizontalLayout_4.addWidget(self.doisButton)
        self.tresButton = QtWidgets.QPushButton(self.frame_4)
        self.tresButton.setMinimumSize(QtCore.QSize(0, 0))
        self.tresButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.tresButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.tresButton.setObjectName("tresButton")
        self.horizontalLayout_4.addWidget(self.tresButton)
        self.somaButton = QtWidgets.QPushButton(self.frame_4)
        self.somaButton.setMinimumSize(QtCore.QSize(0, 0))
        self.somaButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.somaButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.somaButton.setObjectName("somaButton")
        self.horizontalLayout_4.addWidget(self.somaButton)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.zeroButton = QtWidgets.QPushButton(self.frame_5)
        self.zeroButton.setMinimumSize(QtCore.QSize(0, 0))
        self.zeroButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.zeroButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.zeroButton.setObjectName("zeroButton")
        self.horizontalLayout_5.addWidget(self.zeroButton)
        self.maisMenosButton = QtWidgets.QPushButton(self.frame_5)
        self.maisMenosButton.setMinimumSize(QtCore.QSize(0, 0))
        self.maisMenosButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.maisMenosButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.maisMenosButton.setObjectName("maisMenosButton")
        self.horizontalLayout_5.addWidget(self.maisMenosButton)
        self.pontoButton = QtWidgets.QPushButton(self.frame_5)
        self.pontoButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pontoButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.pontoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.pontoButton.setObjectName("pontoButton")
        self.horizontalLayout_5.addWidget(self.pontoButton)
        self.igualButton = QtWidgets.QPushButton(self.frame_5)
        self.igualButton.setMinimumSize(QtCore.QSize(0, 0))
        self.igualButton.setMaximumSize(QtCore.QSize(16777215, 130))
        self.igualButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"font: 28pt \"Arial Rounded MT Bold\";")
        self.igualButton.setObjectName("igualButton")
        self.horizontalLayout_5.addWidget(self.igualButton)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CalculadoraPython"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.clearButton.setText(_translate("MainWindow", "A/C"))
        self.percentagemButton.setText(_translate("MainWindow", "%"))
        self.backsplaceButton.setText(_translate("MainWindow", "<<"))
        self.divisaoButton.setText(_translate("MainWindow", "/"))
        self.seteButton.setText(_translate("MainWindow", "7"))
        self.oitoButton.setText(_translate("MainWindow", "8"))
        self.noveButton.setText(_translate("MainWindow", "9"))
        self.multiplicacaoButton.setText(_translate("MainWindow", "*"))
        self.quatroButton.setText(_translate("MainWindow", "4"))
        self.cincoButton.setText(_translate("MainWindow", "5"))
        self.seisButton.setText(_translate("MainWindow", "6"))
        self.menosButton.setText(_translate("MainWindow", "-"))
        self.umButton.setText(_translate("MainWindow", "1"))
        self.doisButton.setText(_translate("MainWindow", "2"))
        self.tresButton.setText(_translate("MainWindow", "3"))
        self.somaButton.setText(_translate("MainWindow", "+"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.maisMenosButton.setText(_translate("MainWindow", "+/-"))
        self.pontoButton.setText(_translate("MainWindow", "."))
        self.igualButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
