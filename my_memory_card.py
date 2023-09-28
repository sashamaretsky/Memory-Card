#подключение модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle, randint
#создание класса Question(вопрос и ответы на него)

class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
        
# задать вопрос и дать на него 4 ответа
def ask(q: Question):
    question.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    result.setText(q.right)
    show_question()
#Верный ли ответ?
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.right_amount+=1
    else:
        show_correct('Неверно')
#показать верный ответ
def show_correct(res):
    group_answers.hide()
    group_result.show()
    title.setText(res)
    ans_button.setText('Следующий вопрос')
#показать следующий вопрос
def show_question():
    group_1.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    group_1.setExclusive(True)
    group_result.hide()
    group_answers.show()
    ans_button.setText('Ответить')

def next_question():
    cur_question = randint(0, (len(questions_list)-1))
    while cur_question in list_of_numbers:
        cur_question = randint(0, (len(questions_list)-1))
    list_of_numbers.append(cur_question)
    window.total+=1
    ask(questions_list[cur_question])
    

def click_ok():
    if ans_button.text() == 'Ответить':
        check_answer()
    elif len(list_of_numbers) == len(questions_list):
        show_result()
    else:
        next_question()
    

def show_result():
    group_answers.hide()
    group_result.hide()
    group_rating.show()
    all_questions.setText(f'Всего вопросов: {window.total}')
    right_answers.setText(f'Правильных ответов: {window.right_amount}')
    statistics = (window.right_amount/window.total)*100
    rating.setText(f'Рейтинг: {statistics} %')
    


#создание приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(800, 400)
window.total = 0
window.right_amount = 0

#создание виджетов
ans_button = QPushButton('Ответить')
group_answers = QGroupBox('Варианты ответов')
question = QLabel('')
ans1 = QRadioButton()
ans2 = QRadioButton()
ans3 = QRadioButton()
ans4 = QRadioButton()
answers = [ans1, ans2, ans3, ans4]
group_result = QGroupBox('Результат теста')
title = QLabel('Правильно/Неправильно')
result = QLabel('Правильный ответ')
all_questions = QLabel()
right_answers = QLabel()
rating = QLabel()
group_rating = QGroupBox('Конечный результат')

#расположение виджетов по лэйаутам
h_line5 = QHBoxLayout()
h_line6 = QHBoxLayout()
v_line3 = QVBoxLayout()
h_line5.addWidget(title, alignment=Qt.AlignLeft)
h_line6.addWidget(result, alignment=Qt.AlignCenter)
v_line3.addLayout(h_line5)
v_line3.addLayout(h_line6)
group_result.setLayout(v_line3)
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
v_line1 = QVBoxLayout()
h_line1.addWidget(ans1, alignment = Qt.AlignCenter)
h_line1.addWidget(ans2, alignment = Qt.AlignCenter)
h_line2.addWidget(ans3, alignment = Qt.AlignCenter)
h_line2.addWidget(ans4, alignment = Qt.AlignCenter)
v_line1.addLayout(h_line1)
v_line1.addLayout(h_line2)
group_answers.setLayout(v_line1)

h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()
v_line2 = QVBoxLayout()
h_line3.addWidget(question, alignment = Qt.AlignCenter)
h_line4.addWidget(ans_button, alignment = Qt.AlignCenter)
v_line2.addLayout(h_line3)
v_line2.addWidget(group_answers)
v_line2.addWidget(group_result)
group_result.hide()
v_line2.addLayout(h_line4)
window.setLayout(v_line2)

v_line4 = QVBoxLayout()
v_line4.addWidget(all_questions, alignment = Qt.AlignCenter)
v_line4.addWidget(right_answers, alignment = Qt.AlignCenter)
v_line4.addWidget(rating, alignment = Qt.AlignCenter)
group_rating.setLayout(v_line4)
group_rating.hide()


ans_button.clicked.connect(click_ok)
group_1 = QButtonGroup()
group_1.addButton(ans1)
group_1.addButton(ans2)
group_1.addButton(ans3)
group_1.addButton(ans4)

questions_list = list()
questions_list.append(Question('Государственный язык Бразилии', 'португальский', 'испанский', 'бразильский', 'итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'зелёный', 'белый', 'красный', 'синий'))
questions_list.append(Question('Какой национальности не существует?', 'смурфы', 'энцы', 'алеуты', 'буряты'))
questions_list.append(Question('Какого числа День Летнего Солнцестояния?', '21 июня', '1 июня', '1 сентября', '31 декабря'))
list_of_numbers = list()

next_question()


window.show()
app.exec_()