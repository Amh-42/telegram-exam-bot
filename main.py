from typing import Pattern
from telegram import chat
from telegram.ext import *
from telegram import *
from Token import key
from mongodb import *


_estates = ["_exam_", "_answer_", "_support_", "_courses_"]
pro_states = "("+")|(".join(_estates)+")"

_estates2 = ["_addexam_", "_adduser_"]
pro_states2 = "("+")|(".join(_estates2)+")"


def start(update: Update, context: CallbackContext):

    # ... If the user is an administrator it takes him to administrator Interface
    if update.message.chat['id'] in _ADMIN:
        # ... This button allows admin to add new exams to the bot
        buttons = [[InlineKeyboardButton("Add Exam", callback_data="_addexam_")], [
            InlineKeyboardButton("Add Users", callback_data="_adduser_")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text="Choose an Option")

    # ... If the user is not an administrator it takes him to standard interface
    else:
        buttons = [[InlineKeyboardButton("Exam", callback_data="_exam_"), InlineKeyboardButton("Answer", callback_data="_answer_")],
                   [InlineKeyboardButton("Support Community",
                                         callback_data="_support_")],
                   [InlineKeyboardButton("Availble Courses", callback_data="_courses_")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text="Choose an Option")


def examHandler(update: Update, context: CallbackContext):
    context.user_data["current"] = ""
    query = update.callback_query
    text = query.data
    if "_exam_" == text:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Enter Course Code")
        context.user_data["current"] = text
    elif "_answer_" == text:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Enter Course Code")
        context.user_data["current"] = text
    elif "_support_" == text:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="You can go to @Anwar0misbah to get help")
        context.user_data["current"] = text
    elif "_courses_" == text:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='''CSE1101\nCSE2101''')
        context.user_data["current"] = text


def adminHandler(update: Update, context: CallbackContext):
    context.user_data["current"] = ""
    query = update.callback_query
    text = query.data
    if "_addexam_" == text:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="add Exam")
        context.user_data["current"] = text
    elif "_adduser_" == text:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="add User")
        context.user_data["current"] = text


def messageHandler(update: Update, context: CallbackContext):
    if context.user_data.get("current", "") == "_exam_":
        if update.message.text in db:
            buttons = [[InlineKeyboardButton("Mid", callback_data="mid"), InlineKeyboardButton(
                "Final", callback_data="final")]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
                buttons), text="Choose an Option")
    elif context.user_data.get("current", "") == "_answer_":
        if update.message.text in ans:
            buttons = [[InlineKeyboardButton("Mid Answer", callback_data="_mid_"), InlineKeyboardButton(
                "Final Answer", callback_data="_final_")]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
                buttons), text="Choose an Option")


def main():
    updater = Updater(key)
    dispatcher = updater.dispatcher
    updater.start_polling()
    dispatcher.add_handler(CommandHandler("start", start))
    # dispatcher.add_handler(CallbackQueryHandler(queryHandler))
    dispatcher.add_handler(CallbackQueryHandler(
        examHandler, pattern=pro_states))
    dispatcher.add_handler(CallbackQueryHandler(
        adminHandler, pattern=pro_states2))
    dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))


if __name__ == '__main__':
    main()
