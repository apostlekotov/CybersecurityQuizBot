import string
from aiogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  KeyboardButton,
  Message,
  InlineKeyboardMarkup
)
from aiogram.types.message import ParseMode
from data import msgs, tests


def create_btn(text, data):
  return InlineKeyboardButton(text, callback_data=data)


def create_key(text):
  return KeyboardButton(text)


def get_test_list_markup():
  test_list_markup = InlineKeyboardMarkup()

  for test in tests:
    test_list_markup.add(create_btn(test['name'], f"create_test_{test['name']}"))

  return test_list_markup


def get_test_questions(test_name: str):
  return next(item for item in tests if item["name"] == test_name)['questions']


def get_initial_state(test_name: str):
  initial_state = {
    'current_question': 0,
    'score': 0,
    'test_name': test_name
  }

  return initial_state


async def ask_question(msg: Message, state):
  question = get_test_questions(state['test_name'])[
    state['current_question']]

  alphabet = list(string.ascii_uppercase)

  question_msg = f"*№{state['current_question'] + 1} {question['content']}*\n\n"

  options_markup = InlineKeyboardMarkup()

  btn_list = []

  for i, option in enumerate(question['options']):
    question_msg += f"*{alphabet[i]}:* {option['content']}\n"
    btn_list.append(
      create_btn(alphabet[i], f"{i+1}_{alphabet[i]}_{'right' if option['is_right'] else 'wrong'}")
    )

  options_markup.row(*btn_list)

  await msg.answer(question_msg, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=options_markup)


async def print_result(msg: Message, state):
  await msg.answer(f"{msgs['finish']} {state['score']}/{len(get_test_questions(state['test_name']))} 🎉")
