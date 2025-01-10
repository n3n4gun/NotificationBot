from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

botMenu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = '/Add_notification'), KeyboardButton(text = '/Remove_notification')],
        [KeyboardButton(text = '/Show_all_notifications')]
    ], resize_keyboard = True, input_field_placeholder = 'Выберите пункт из меню'
)
