from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(800, 800)


#створюємо всі елементи
text = QTextEdit()
talklbl = QLabel("Список заміток")
talk2lbl = QLabel("Список тегів")

menuBth = QPushButton("Створити закладку")
restBth = QPushButton("Видалити закладку")
rektorBth = QPushButton("Зберегти зміни")
tagsBth = QPushButton("Додати до замітки")
tags2Bth = QPushButton("Відкріпити від замітки")
tags3Bth = QPushButton("Шукати запис по тегу")

fara = QListWidget()



#лінії



mainLine = QHBoxLayout()

qLine = QHBoxLayout()

mainLine.addLayout(qLine)

#добавляємо лінії

v1 = QVBoxLayout()
v1.addWidget(text)
mainLine.addLayout(v1)


firstLine = QVBoxLayout()
firstLine.addWidget(talklbl)
firstLine.addWidget(fara)
firstLine.addWidget(menuBth)
firstLine.addWidget(rektorBth)
firstLine.addWidget(restBth)


mainLine.addLayout(firstLine)
v2 = QVBoxLayout()
v2.addWidget(talklbl)
v2.addWidget(talk2lbl)




window.setLayout(mainLine)
window.show()
app.exec()
