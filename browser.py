import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Setting up the navbar of the browser
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Setting up the Back Button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        # Setting up the Forward Button
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Setting up the Refresh button
        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        # Setting up the Home button
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('My Fantastic Browser')
window = MainWindow()
app.exec_()