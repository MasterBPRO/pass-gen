import sys
from PySide import QtCore, QtGui
from ui import Ui_MainWindow
from faker import Faker

app = QtGui.QApplication(sys.argv)
fake = Faker()

MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def gen_pass():
    """
    Функция для вывода сгененированного пароля пользователю
    :return: Empty
    """
    password = get_pass()
    ui.lineEdit.setText(password)
    set_clipboard(password)


def set_clipboard(password):
    """
    Фунция для установки текств в Буфер Обмена
    :param password: Пароль для установки в Буфер Обмена
    :return: Empty
    """
    cb = QtGui.QApplication.clipboard()
    cb.clear(mode=cb.Clipboard)
    cb.setText(password, mode=cb.Clipboard)


def get_chars():
    """
    Функция для получения статуска отиметки опции "Символы"
    :return: True если опция отмечена, в противном случае False
    """
    return ui.checkBox.isChecked()


def get_digits():
    """
    Функция для получения статуска отиметки опции "Цифры"
    :return: True если опция отмечена, в противном случае False
    """
    return ui.checkBox_2.isChecked()


def get_upper():
    """
    Функция для получения статуска отиметки опции "Верхний регистр"
    :return: True если опция отмечена, в противном случае False
    """
    return ui.checkBox_3.isChecked()


def get_lower():
    """
    Функция для получения статуска отиметки опции "Нижний регистр"
    :return: True если опция отмечена, в противном случае False
    """
    return ui.checkBox_4.isChecked()


def get_length():
    """
    Функция для получения выбранного количества длины пароля
    :return: Возвращает число от 4 до 99
    """
    return ui.spinBox.value()


def get_pass():
    """
    Функция генерирует пароль, исходя из параметров выбрынных пользователем
    :return: Сгененированный пароль
    """
    return fake.password(length=get_length(), special_chars=get_chars(), digits=get_digits(), upper_case=get_upper(), lower_case=get_lower())


ui.pushButton.clicked.connect(gen_pass)  # Если кнопка была нажата зарускаем функцию gen_pass()
sys.exit(app.exec_())
