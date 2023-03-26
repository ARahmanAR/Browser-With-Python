from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLineEdit, QTabWidget, QPushButton

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AR Browser")
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.back)
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.forward)
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.toolbar = QToolBar()
        self.toolbar.addWidget(self.back_button)
        self.toolbar.addWidget(self.forward_button)
        self.toolbar.addWidget(self.refresh_button)
        self.toolbar.addWidget(self.url_bar)
        self.addToolBar(self.toolbar)
        new_tab_action = QAction("New Tab", self)
        new_tab_action.triggered.connect(self.new_tab)
        self.toolbar.addAction(new_tab_action)
        self.new_tab()

    def new_tab(self):
        web_view = QWebEngineView()
        web_view.load(QUrl("https://www.google.com"))
        self.tabs.addTab(web_view, "New Tab")
        self.tabs.setCurrentWidget(web_view)
        web_view.urlChanged.connect(self.update_url)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.tabs.currentWidget().load(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def back(self):
        self.tabs.currentWidget().back()

    def forward(self):
        self.tabs.currentWidget().forward()

    def refresh(self):
        self.tabs.currentWidget().reload()

if __name__ == "__main__":
    app = QApplication([])
    window = BrowserWindow()
    window.show()
    app.exec_()
