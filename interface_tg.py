from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from main import Board

"5622032812:AAErQJys-QqlVXWGOYHnWekTIELGOgoWbH0"

updater = Updater("5622032812:AAErQJys-QqlVXWGOYHnWekTIELGOgoWbH0", use_context=True)
bot = Bot("5622032812:AAErQJys-QqlVXWGOYHnWekTIELGOgoWbH0")
dp = updater.dispatcher
sp = {}


def start(up, co):
    sp[up.message.from_user.id] = [Board(5, 5, 5), False]
    a = sp[up.message.from_user.id][0].create_board()
    kb = []
    for i in range(len(a)):
        kb.append([InlineKeyboardButton("⬜", callback_data=f"place;{i};{j}") for j in range(len(a[i]))])
    kb.append([InlineKeyboardButton("Пометить бомбу", callback_data="check_bomb;true")])
    inline_kb = InlineKeyboardMarkup(kb)
    message = bot.send_message(chat_id=up.message.from_user.id, text="На поле 5 бомб, найди все",
                               reply_markup=inline_kb)
    sp[up.message.from_user.id].append(message.message_id)


def process_callback(up, co):
    query = up.callback_query
    variant = query.data.split(';')
    if variant[0] == "place":
        kb = []
        if not sp[query.from_user.id][1]:
            a = sp[query.from_user.id][0].open_place(int(variant[2]), int(variant[1]))
            if a[1]:
                kb = []
                for i in range(len(a[0])):
                    x = []
                    for j in range(len(a[0][i])):
                        if a[0][i][j] == "b":
                            x.append(InlineKeyboardButton("🔴", callback_data=f"end;{i};{j}"))
                        elif a[0][i][j] == 0:
                            x.append(InlineKeyboardButton("➖", callback_data=f"end;{i};{j}"))
                        else:
                            x.append(InlineKeyboardButton(str(a[0][i][j]), callback_data=f"end;{i};{j}"))
                    kb.append(x)
                inline_kb = InlineKeyboardMarkup(kb)
                bot.edit_message_text(chat_id=query.from_user.id, text="Проигрыш",
                                      reply_markup=inline_kb, message_id=sp[query.from_user.id][2])
            else:
                kb = []
                for i in range(len(a[0])):
                    x = []
                    for j in range(len(a[0][i])):
                        if a[0][i][j] == "F":
                            x.append(InlineKeyboardButton("🔹", callback_data=f"place;{i};{j}"))
                        elif a[0][i][j] == 0:
                            x.append(InlineKeyboardButton("➖", callback_data=f"place;{i};{j}"))
                        elif a[0][i][j] == '*':
                            x.append(InlineKeyboardButton("⬜", callback_data=f"place;{i};{j}"))
                        else:
                            x.append(InlineKeyboardButton(str(a[0][i][j]), callback_data=f"place;{i};{j}"))
                    kb.append(x)
                kb.append([InlineKeyboardButton("Пометить бомбу", callback_data="check_bomb;true")])
                inline_kb = InlineKeyboardMarkup(kb)
                bot.edit_message_text(chat_id=query.from_user.id, text="На поле 5 бомб, найди все",
                                      reply_markup=inline_kb, message_id=sp[query.from_user.id][2])
        else:
            a = sp[query.from_user.id][0].check_bomb(int(variant[2]), int(variant[1]))
            if a[1]:
                kb = []
                for i in range(len(a[0])):
                    x = []
                    for j in range(len(a[0][i])):
                        if a[0][i][j] == "F":
                            x.append(InlineKeyboardButton("🟢", callback_data=f"end;{i};{j}"))
                        elif a[0][i][j] == 0:
                            x.append(InlineKeyboardButton("➖", callback_data=f"end;{i};{j}"))
                        else:
                            x.append(InlineKeyboardButton(str(a[0][i][j]), callback_data=f"end;{i};{j}"))
                    kb.append(x)
                inline_kb = InlineKeyboardMarkup(kb)
                bot.edit_message_text(chat_id=query.from_user.id, text="Победа",
                                      reply_markup=inline_kb, message_id=sp[query.from_user.id][2])
            else:
                kb = []
                for i in range(len(a[0])):
                    x = []
                    for j in range(len(a[0][i])):
                        if a[0][i][j] == "F":
                            x.append(InlineKeyboardButton("🔹", callback_data=f"place;{i};{j}"))
                        elif a[0][i][j] == 0:
                            x.append(InlineKeyboardButton("➖", callback_data=f"place;{i};{j}"))
                        elif a[0][i][j] == '*':
                            x.append(InlineKeyboardButton("⬜", callback_data=f"place;{i};{j}"))
                        else:
                            x.append(InlineKeyboardButton(str(a[0][i][j]), callback_data=f"place;{i};{j}"))
                    kb.append(x)
                kb.append([InlineKeyboardButton("Пометить бомбу", callback_data="check_bomb;true")])
                inline_kb = InlineKeyboardMarkup(kb)
                bot.edit_message_text(chat_id=query.from_user.id, text="На поле 5 бомб, найди все",
                                      reply_markup=inline_kb, message_id=sp[query.from_user.id][2])
    elif variant[0] == "check_bomb":
        sp[query.from_user.id][1] = not sp[query.from_user.id][1]
    bot.answer_callback_query(callback_query_id=query.id)


dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(process_callback))

updater.start_polling()
