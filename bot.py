import os
import logging
import string
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.types.message import ParseMode

from data import msgs
from utils import get_initial_state, ask_question, get_test_questions, get_test_list_markup, print_result

logging.basicConfig(level=logging.INFO)

# Config
load_dotenv()

TOKEN = os.getenv('TOKEN')

# Bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

global_state = {}

# Actions


@dp.message_handler(commands=['start'])
async def start(msg: Message):
  await msg.answer(msgs['welcome'])
  await msg.answer(msgs['start'], reply_markup=get_test_list_markup())


@dp.message_handler(content_types=ContentType.ANY)
async def default_reply(msg: Message):
  await msg.delete()


async def question_player(msg: Message, state):
  cid = msg.chat.id
  global_state[cid] = state

  await ask_question(msg, global_state[cid])


async def answer_question(msg: Message, option):
  cid = msg.chat.id
  state = global_state[cid]

  is_right = option[2] in 'right'

  # hilight the right answer
  question = get_test_questions(state['test_name'])[
    state['current_question']]

  alphabet = list(string.ascii_uppercase)

  question_msg = f"*№{state['current_question'] + 1} {question['content']}*\n"

  for i, question_option in enumerate(question['options']):
    if alphabet[i] == option[1]:
      question_msg += f"*{alphabet[i]}: {question_option['content']}* {'✅' if is_right else '❌'}\n"
    else:
      question_msg += f"*{alphabet[i]}:* {question_option['content']} {'✅' if question_option['is_right'] else ''}\n"

  await msg.edit_text(question_msg, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=None)

  # manage state
  state['current_question'] += 1
  if is_right:
    state['score'] += 1

  if state['current_question'] == len(get_test_questions(state['test_name'])):
    del global_state[cid]
    await print_result(msg, state)
    await msg.answer(msgs['start'], reply_markup=get_test_list_markup())
    return

  global_state[cid] = state

  # continue test
  await question_player(msg, global_state[cid])

# Handlers


@dp.callback_query_handler()
async def btn_handler(query: CallbackQuery):
  cid = query.message.chat.id

  if 'create_test' in query.data:
    await query.message.edit_reply_markup()  # clear btn
    await question_player(query.message, get_initial_state(query.data.split('_')[2]))
    await query.answer(msgs['begin'])

  elif 'wrong' in query.data or 'right' in query.data:
    # [№, char, 'wrong' | 'right']
    await answer_question(query.message, query.data.split('_'))
    await query.answer(msgs[query.data.split('_')[2]])

  else:
    await bot.send_message(cid, msgs['error'])

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
