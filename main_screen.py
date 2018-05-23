from PyQt5 import QtWidgets
from autoMainScreen import Ui_MainWindow

import queries

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.ui = Ui_MainWindow() # Load ui file for main window
        self.ui.setupUi(self)
        self.anotherwindow = None
        self.bypass = False

        # Connect buttons
        self.ui.button_search_events.clicked.connect(self.handle_search_events)

    # Handles
    def handle_search_events(self):
        event_type = str(self.ui.combo_box_choose_event_type.currentText())
        date_start = self.ui.date_edit_start.date().toPyDate()
        date_end = self.ui.date_edit_end.date().toPyDate()
        organizer_cpf = self.ui.line_edit_cpf.text()

        # Deals with empty cpf or invalid amount of digits
        if organizer_cpf == "...":
            organizer_cpf = None
        elif len(organizer_cpf) != 14:
            self.warning("CPF inválido!")
            return

        organizer_name = self.ui.line_edit_name.text()
        data = queries.search_events(event_type, date_start, date_end,
                                     organizer_cpf, organizer_name)
        for line in data:
            self.ui.list_event_search.addItem(line)

    def warning(self, message):
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle("Aviso")
        box.setText(message)
        box.setStandardButtons(QtWidgets.QMessageBox.Yes)
        button_yes = box.button(QtWidgets.QMessageBox.Yes)
        button_yes.setText('Ok')
        box.exec_()

        if box.clickedButton() == button_yes:  # Yes pressed
            box.close()

    # Overloading classes
    # TODO: def closeEvent(self, event):
    def temp(self, event):
        if self.bypass:
            event.accept()
            return

        # Verifies if the user wants to exit the window
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle('Saindo!')
        box.setText('Tem certeza que quer sair?')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        button_yes = box.button(QtWidgets.QMessageBox.Yes)
        button_yes.setText('Sim')
        button_no = box.button(QtWidgets.QMessageBox.No)
        button_no.setText('Não')
        box.exec_()

        if box.clickedButton() == button_yes:  # Yes pressed
            event.accept()
        elif box.clickedButton() == button_no:
            event.ignore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = MainScreen()
    gui.show()
    sys.exit(app.exec_())
