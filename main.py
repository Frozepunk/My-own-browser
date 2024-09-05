# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, 
#                              QWidget, QHBoxLayout, QTabWidget, QToolBar, QAction)
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtCore import QUrl

# class Browser(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Advanced Browser')

#         # Create a Tabbed Browser
#         self.tabs = QTabWidget()
#         self.tabs.setDocumentMode(True)
#         self.tabs.tabCloseRequested.connect(self.close_current_tab)
#         self.tabs.currentChanged.connect(self.update_url)
#         self.setCentralWidget(self.tabs)

#         # Create a toolbar
#         self.toolbar = QToolBar()
#         self.addToolBar(self.toolbar)

#         # Add navigation buttons to the toolbar
#         back_btn = QAction('<', self)
#         back_btn.triggered.connect(lambda: self.current_browser().back())
#         self.toolbar.addAction(back_btn)

#         forward_btn = QAction('>', self)
#         forward_btn.triggered.connect(lambda: self.current_browser().forward())
#         self.toolbar.addAction(forward_btn)

#         reload_btn = QAction('⟳', self)
#         reload_btn.triggered.connect(lambda: self.current_browser().reload())
#         self.toolbar.addAction(reload_btn)

#         # Add Home Button
#         home_btn = QAction('Home', self)
#         home_btn.triggered.connect(self.navigate_home)
#         self.toolbar.addAction(home_btn)

#         # URL input field
#         self.url_input = QLineEdit()
#         self.url_input.returnPressed.connect(self.load_url)
#         self.toolbar.addWidget(self.url_input)

#         # Add new tab button
#         new_tab_btn = QAction('New Tab', self)
#         new_tab_btn.triggered.connect(self.add_new_tab)
#         self.toolbar.addAction(new_tab_btn)

#         # Initialize a browser history stack
#         self.history_stack = []

#         # Add the first tab (Google as homepage)
#         self.add_new_tab(QUrl('https://www.duckduckgo.com'), 'Home')

#     def add_new_tab(self, url=None, label='New Tab'):
#         if url is None:
#             url = QUrl('https://www.duckduckgo.com')

#         # Create a new browser instance for the tab
#         browser = QWebEngineView()
#         browser.setUrl(url)
#         browser.urlChanged.connect(self.update_url)
#         browser.loadFinished.connect(lambda: self.tabs.setTabText(self.tabs.currentIndex(), browser.page().title()))

#         # Add the new tab to the tab widget
#         self.tabs.addTab(browser, label)
#         self.tabs.setCurrentWidget(browser)

#     def close_current_tab(self, index):
#         if self.tabs.count() > 1:
#             self.tabs.removeTab(index)

#     def current_browser(self):
#         return self.tabs.currentWidget()

#     def navigate_home(self):
#         # Load the homepage (Google) in the current tab
#         self.current_browser().setUrl(QUrl('https://www.duckduckgo.com'))

#     def load_url(self):
#         url = self.url_input.text()
#         if not url.startswith('http'):
#             url = 'http://' + url
#         self.current_browser().setUrl(QUrl(url))

#     def update_url(self, url):
#         # Update the URL input field with the current URL
#         if self.current_browser():
#             self.url_input.setText(self.current_browser().url().toString())

#             # Add the current URL to the history stack
#             self.history_stack.append(self.current_browser().url().toString())

#     def go_back_in_history(self):
#         # Navigate back in history if there are URLs to visit
#         if len(self.history_stack) > 1:
#             self.history_stack.pop()  # Remove the current URL
#             last_url = self.history_stack[-1]  # Get the last URL
#             self.current_browser().setUrl(QUrl(last_url))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Browser()
#     window.show()
#     sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, 
                             QWidget, QHBoxLayout, QTabWidget, QToolBar, QAction)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Advanced Browser')

        # Create a Tabbed Browser
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.update_url)
        self.setCentralWidget(self.tabs)

        # Create a toolbar
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # Add navigation buttons to the toolbar
        back_btn = QAction('<', self)
        back_btn.triggered.connect(lambda: self.current_browser().back())
        self.toolbar.addAction(back_btn)

        forward_btn = QAction('>', self)
        forward_btn.triggered.connect(lambda: self.current_browser().forward())
        self.toolbar.addAction(forward_btn)

        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        self.toolbar.addAction(reload_btn)

        # Add Home Button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        self.toolbar.addAction(home_btn)

        # URL input field
        self.url_input = QLineEdit()
        self.url_input.returnPressed.connect(self.load_url)
        self.toolbar.addWidget(self.url_input)

        # Add new tab button
        new_tab_btn = QAction('New Tab', self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        self.toolbar.addAction(new_tab_btn)

        # Initialize a browser history stack
        self.history_stack = []

        # Add the first tab (Google as homepage)
        self.add_new_tab(QUrl('http://www.google.com'), 'Home')

    def add_new_tab(self, url=None, label='New Tab'):
        # Check if url is provided, otherwise use a default URL
        if url is None:
            url = QUrl('http://www.google.com')
        elif isinstance(url, str):  # If url is a string, convert it to QUrl
            url = QUrl(url)

        # Create a new browser instance for the tab
        browser = QWebEngineView()
        browser.setUrl(url)
        # Set the URL for the new browser tab
        browser.urlChanged.connect(self.update_url)
        browser.loadFinished.connect(lambda: self.tabs.setTabText(self.tabs.currentIndex(), browser.page().title()))

        # Add the new tab to the tab widget
        self.tabs.addTab(browser, label)
        self.tabs.setCurrentWidget(browser)

    def close_current_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def current_browser(self):
        return self.tabs.currentWidget()

    def navigate_home(self):
        # Load the homepage (Google) in the current tab
        self.current_browser().setUrl(QUrl('http://www.google.com'))

    def load_url(self):
        url = self.url_input.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.current_browser().setUrl(QUrl(url))

    def update_url(self, url):
        # Update the URL input field with the current URL
        if self.current_browser():
            self.url_input.setText(self.current_browser().url().toString())

            # Add the current URL to the history stack
            self.history_stack.append(self.current_browser().url().toString())

    def go_back_in_history(self):
        # Navigate back in history if there are URLs to visit
        if len(self.history_stack) > 1:
            self.history_stack.pop()  # Remove the current URL
            last_url = self.history_stack[-1]  # Get the last URL
            self.current_browser().setUrl(QUrl(last_url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())

