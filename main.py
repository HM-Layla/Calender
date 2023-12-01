import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()

        # Configure the window
        self.setWindowTitle("My Calendar App")
        self.resize(800, 600)

        # Create our widgets
        self.calendar = QtWidgets.QCalendarWidget()
        self.event_list = QtWidgets.QListWidget()
        self.event_title = QtWidgets.QLineEdit()
        self.event_category = QtWidgets.QComboBox()
        self.event_time = QtWidgets.QTimeEdit(QtCore.QTime(8, 0))
        self.allday_check = QtWidgets.QCheckBox('All Day')
        self.event_detail = QtWidgets.QTextEdit()
        self.add_button = QtWidgets.QPushButton('Add/Update')
        self.del_button = QtWidgets.QPushButton('Delete')

        # Configure some widgets

        # Add event categories
        self.event_category.addItems(
            ['Select category…', 'New…', 'Work',
             'Meeting', 'Doctor', 'Family']
            )
        # disable the first category item
        self.event_category.model().item(0).setEnabled(False)

        # Arrange the widgets
        main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)
        # Calendar expands to fill the window
        self.calendar.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        right_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(right_layout)
        right_layout.addWidget(QtWidgets.QLabel('Events on Date'))
        right_layout.addWidget(self.event_list)
        # Event list expands to fill the right area
        self.event_list.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )

        # Create a sub-layout for the event view/add form
        event_form = QtWidgets.QGroupBox('Event')
        right_layout.addWidget(event_form)
        event_form_layout = QtWidgets.QGridLayout()
        event_form.setLayout(event_form_layout)

        event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
        event_form_layout.addWidget(self.event_category, 2, 1)
        event_form_layout.addWidget(self.event_time, 2, 2,)
        event_form_layout.addWidget(self.allday_check, 2, 3)
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
        event_form_layout.addWidget(self.add_button, 4, 2)
        event_form_layout.addWidget(self.del_button, 4, 3)

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())