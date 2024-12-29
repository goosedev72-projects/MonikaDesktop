import sys
import openai
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel

# Установите ваш API ключ OpenAI
openai.api_key = 'axjoerqghegihrpghwergwegpoh'

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat with OpenAI')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.user_input = QTextEdit(self)
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def send_message(self):
        user_message = self.user_input.toPlainText()
        if user_message:
            self.chat_display.append(f'You: {user_message}')
            self.user_input.clear()
            response = self.get_response(user_message)
            self.chat_display.append(f'OpenAI: {response}')

    def get_response(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
