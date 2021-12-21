msgs = {
  "welcome": "Друже! Вітаємо тебе в нашому боті.\nНижче розміщене посилання на матеріали, які допоможуть покращити твої знання з кібербезпеки. Але чи добре ти засвоїш ці правила? Чи завжди їх дотримуєшься?\nЩоб відповісти на це запитання, ми пропонуємо тобі виконати наші тести. Перший перевірить твої знання, другий — визначить твій рівень кіберзахисту.\nБажаємо успіхів та приємного користування!\n\nhttps://buklib.net/books/28625/\n\nhttps://niss.gov.ua/doslidzhennya/nacionalna-bezpeka/bezpekova-politika-ukraini-v-konteksti-formuvannya-sistemi\n\nhttps://buduysvoe.com/publications/ryzyk-menedzhment-i-ocinka-ryzykiv-na-storozhi-zahystu-vashogo-biznesu\n\nhttps://wiki.hostpro.ua/ua/knowledgebase/shifruvannja-tipi-i-algoritmi/\n\nhttps://10guards.com/ua/articles/the-most-common-types-of-cyber-attacks-in-2021/",
  "start": "Ну що ж, почнімо. Успіхів!",
  "begin": "Починаємо тест",
  "finish": "Вітаємо! Твій результат:",
  "wrong": "✖️",
  "right": "✔️",
  "is_ready": "Готовий?",
  "error": "На жаль, сталась помилка, спробуйте ще раз"
}

name1_questions = [
  {
    'content': 'Question 1',
    'options': [
      {'content': 'Option 1 \(wrong\)', 'is_right': False},
      {'content': 'Option 2 \(right\)', 'is_right': True},
      {'content': 'Option 3 \(wrong\)', 'is_right': False},
      {'content': 'Option 4 \(wrong\)', 'is_right': False},
    ]
  },
  {
    'content': 'Question 2',
    'options': [
      {'content': 'Option 1 \(wrong\)', 'is_right': False},
      {'content': 'Option 2 \(wrong\)', 'is_right': False},
      {'content': 'Option 3 \(right\)', 'is_right': True},
      {'content': 'Option 4 \(wrong\)', 'is_right': False},
      {'content': 'Option 5 \(wrong\)', 'is_right': False},
    ]
  },
  {
    'content': 'Question 3',
    'options': [
      {'content': 'Option 1 \(right\)', 'is_right': True},
      {'content': 'Option 2 \(wrong\)', 'is_right': False},
      {'content': 'Option 3 \(wrong\)', 'is_right': False},
    ]
  }
]

name2_questions = [
  {
    'content': 'Lol Question 1',
    'options': [
      {'content': 'Option 1 \(wrong\)', 'is_right': False},
      {'content': 'Option 2 \(right\)', 'is_right': True},
      {'content': 'Option 3 \(wrong\)', 'is_right': False},
      {'content': 'Option 4 \(wrong\)', 'is_right': False},
    ]
  },
  {
    'content': 'Lol Question 2',
    'options': [
      {'content': 'Option 1 \(wrong\)', 'is_right': False},
      {'content': 'Option 3 \(right\)', 'is_right': True},
      {'content': 'Option 5 \(wrong\)', 'is_right': False},
    ]
  },
]

tests = [
  {
    'name': 'name1',
    'questions': name1_questions
  },
  {
    'name': 'name2',
    'questions': name2_questions
  }
]
