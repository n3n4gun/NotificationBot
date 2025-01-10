import botFunctions.botMenu as keyboard

from aiogram import html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from uuid import uuid4

BOT_ROUTER = Router()

# user state
class UserNotification(StatesGroup):
    notification_text = State() # user state, when user writes notification text
    notification_date = State() # user state, when user points date of notification

# processing /start command
@BOT_ROUTER.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f'Приветствую, {message.from_user.first_name}!', reply_markup = keyboard.botMenu)

# processing /Add_notification command
@BOT_ROUTER.message(Command('Add_notification'))
async def add_notification(message : Message, state : FSMContext):
    await state.set_state(UserNotification.notification_text)
    await message.answer(f'{message.from_user.first_name}, о чем вам напомнить?')

@BOT_ROUTER.message(UserNotification.notification_text)
async def get_notification_text(message : Message, state : FSMContext):
    await state.update_data(notification_text = message.text)
    await state.set_state(UserNotification.notification_date)
    await message.answer(f'{message.from_user.first_name}, когда вам напомнить об этом?')

@BOT_ROUTER.message(UserNotification.notification_date)
async def get_notification_date(message : Message, state : FSMContext):
    await state.update_data(notification_date = message.text)
    notification_data = await state.get_data()
    notification_id = uuid4()
    await message.answer(f'{message.from_user.first_name}, ваше напоминание создано!\nID уведомления: {notification_id}\nНапоминание: {notification_data["notification_text"]}\nКогда напомнить: {notification_data["notification_date"]}')
    await state.clear()

