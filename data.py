msgs = {
  "welcome": "welcome",
  "start": "start",
  "begin": "begin",
  "finish": "finish",
  "wrong": "wrong",
  "right": "right",
  "is_ready": "is_ready?",
  "error": "error"
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
