import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QAction, qApp, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon
from controller import Controller


class App(QMainWindow):
    appTitle = "Face Detect VLC Controller"
    appMarginLeft = 100
    appMarginTop = 100
    appWidth = 640
    appHeight = 480
    controller = Controller()
    fileName = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.appTitle)
        self.setGeometry(self.appMarginLeft, self.appMarginTop, self.appWidth, self.appHeight)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Z')
        exitAct.setStatusTip('Exit Appliction')
        exitAct.triggered.connect(qApp.quit)

        loadVideo = QAction('&Open',self)
        loadVideo.setStatusTip('Load Video')
        loadVideo.triggered.connect(self.openFileDialog)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(loadVideo)
        fileMenu.addAction(exitAct)

        self.addWidgets()

    def addWidgets(self):
        self.statusBar().showMessage('Ready')
        self.centralWidget = QWidget(self)
        vBoxLayout = QHBoxLayout()
        self.centralWidget.setLayout(vBoxLayout)
        self.setCentralWidget(self.centralWidget)

        self.playBtn = QPushButton("Play Video")
        self.playBtn.clicked.connect(self.playVideo)
        vBoxLayout.addWidget(self.playBtn)

        self.closeBtn = QPushButton("Close Video")
        self.closeBtn.clicked.connect(self.closePlayer)
        vBoxLayout.addWidget(self.closeBtn)

    def openFileDialog(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileDialog.setViewMode(QFileDialog.List)
        filter = "Videos *.mp4; *.avi; *.mkv"
        fileDialogTitle = "Load Video"
        initialDir = "E:\\"
        self.fileName, _filter = fileDialog.getOpenFileNames(self.centralWidget, fileDialogTitle, initialDir, filter)
        if not self.fileName:
            print("No files")
        else:
            print(str(len(self.fileName)) + " files selected")
            print(self.fileName[0])
            self.controller.initiate_player(self.fileName[0])

    def playVideo(self):
        self.controller.player_start()

    def closePlayer(self):
        self.controller.player_close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())