import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QPoint

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Убираем рамку окна
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # Устанавливаем прозрачный фон
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Получаем размеры экрана
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Устанавливаем размер окна
        window_width = 800
        window_height = 400
        self.setGeometry(screen_width - window_width - 100, screen_height - window_height - 100, window_width, window_height)

        # Создаем метку для отображения GIF
        self.label = QLabel(self)
        self.label.setAttribute(Qt.WA_TranslucentBackground)

        # Загружаем GIF-файл
        gif_path = "ваш_файл.gif"
        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        self.movie.start()

        # Устанавливаем размер метки в соответствии с размером GIF
        self.label.setGeometry(0, 0, self.movie.currentImage().width(), self.movie.currentImage().height())

        # Обрабатываем нажатие на метку
        self.label.mousePressEvent = self.on_click

        # Переменные для перемещения окна
        self.dragging = False
        self.drag_start_position = QPoint()

    def on_click(self, event):
        # Здесь вы можете вызвать ваш Python-скрипт
        os.system('python ваш_скрипт.py')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Начинаем перетаскивание
            self.dragging = True
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.dragging:
            # Перемещаем окно
            self.move(event.globalPos() - self.drag_start_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Заканчиваем перетаскивание
            self.dragging = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec_())
