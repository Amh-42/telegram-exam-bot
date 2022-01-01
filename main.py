from telegram import chat
from telegram.ext import *
from telegram import *
from Token import key

_ADMIN = [712156622]


def start(update: Update, context: CallbackContext):

    # ... If the user is an administrator it takes him to administrator Interface
    if update.message.chat['id'] in _ADMIN:
        # ... This button allows admin to add new exams to the bot
        buttons = [[InlineKeyboardButton("Add Exam", callback_data="add")], [
            InlineKeyboardButton("Add Users", callback_data="users")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text="Choose an Option")

    # ... If the user is not an administrator it takes him to standard interface
    else:
        buttons = [[InlineKeyboardButton("Exam", callback_data="exam"), InlineKeyboardButton("Answer", callback_data="answer")],
                   [InlineKeyboardButton("Support Community",
                                         callback_data="support")],
                   [InlineKeyboardButton("Availble Courses", callback_data="courses")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text="Choose an Option")


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    if 'exam' in query:
        buttons = [[InlineKeyboardButton("Mid", callback_data="mid"), InlineKeyboardButton(
            "Final", callback_data="final")]]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons), text="Choose an Option")
    elif 'answer' in query:
        buttons = [[InlineKeyboardButton("Mid", callback_data="mid"), InlineKeyboardButton(
            "Final", callback_data="final")]]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons), text="Choose an Option")
        context.user_data["current"] = "mid"
    elif 'support' in query:
        update.callback_query.edit_message_text(
            text='You can go to @Anwar0Misbah')
    elif 'courses' in query:
        update.callback_query.edit_message_text(text='''
            CSE -> compouter science Engineering
            ECE -> Electornics and communications Engineereing
            EPCE -> Electrical and power Engineering
            CE -> Civil Engineering
        ''')
    elif 'mid' in query:
        if context.user_data.get("current", "") == 'add':
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Enter the Course code")
            context.user_data["current"] = "addmid"
        elif context.user_data.get("current", "") == 'mid':
            pass
    elif 'final' in query:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Enter the Course code")
    elif 'add' in query:
        # ... This Allows admin to add mid or final to the database
        buttons = [[InlineKeyboardButton("Add Mid", callback_data="addmid"), InlineKeyboardButton(
            "Add Final", callback_data="addfinal")]]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons), text="Choose an Option")
    elif 'addmid' in query:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Enter the Course codfhee")


def main():
    updater = Updater(key)
    dispatcher = updater.dispatcher
    updater.start_polling()
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(queryHandler))


if __name__ == '__main__':
    main()
