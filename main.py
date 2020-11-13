import telebot
from telebot import types
import config
import keyboard
import buttons
import text
import he
import info
from config import ddd


bot = telebot.TeleBot(config.token, parse_mode='Markdown')

@bot.message_handler(content_types=['photo'])
def photo(message):
    print(message.photo[1].file_id)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        if message.text == '/start':
            config.stage = 1
            if config.stage:
                start = types.InlineKeyboardMarkup()
                site = types.InlineKeyboardButton(text="✅ האתר של Bits Of Gold ✅", url="https://bitsofgold.co.il")
                news = types.InlineKeyboardButton(text="📰 ערוץ החדשות של BitsOfGold 📰", url="https://t.me/BitsOfGoldNews")
                exchange = types.InlineKeyboardButton(text="💱 המרה בטוחה 💱", callback_data="exchange")
                view_curr = types.InlineKeyboardButton(text="שערים", callback_data="view_curr")
                start.row(site)
                start.row(news)
                start.row(view_curr, exchange)
                f = open('welcome.jpg', 'rb')
                bot.send_photo(chat_id=message.chat.id, photo=config.welcome_photo, caption=he.welcome, reply_markup=start,
                               parse_mode='Markdown', timeout=1000)
    except:
        pass

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, message.photto[1].file_id)


@bot.callback_query_handler(func=lambda message: True)
def callbacks(call):
    if call.data == "exchange":
        config.stage = 1
        if config.stage:
            exchange = types.InlineKeyboardMarkup()
            buy = types.InlineKeyboardButton("מעוניין לקנות", callback_data="buy")
            sell = types.InlineKeyboardButton("מעוניין למכור", callback_data="sell")
            exchange.row(buy, sell)
            exchange.row(buttons.back1)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.send_photo(chat_id=call.message.chat.id, photo=config.welcome_photo, caption=text.ex_text,
                           reply_markup=keyboard.exchange, timeout=1000, parse_mode='Markdown')
    elif call.data == "sell":
        config.stage = 11
        if config.stage:
            buy = types.InlineKeyboardMarkup()
            buy.row(buttons.btc_select1, buttons.eth_select1)
            buy.row(buttons.back1)
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text.buy,
                                     reply_markup=buy, parse_mode='Markdown')



    elif call.data == "view_curr":
        config.stage = 1
        if config.stage:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.send_photo(chat_id=call.message.chat.id, photo=config.welcome_photo, caption=text.view_curr,
                           reply_markup=keyboard.back, timeout=1000, parse_mode='Markdown')

    elif call.data == "home":
        start1 = types.InlineKeyboardMarkup()
        site = types.InlineKeyboardButton(text="✅ האתר של Bits Of Gold ✅", url="https://bitsofgold.co.il")
        exchange = types.InlineKeyboardButton(text="💱 המרה בטוחה 💱", callback_data="exchange")
        view_curr = types.InlineKeyboardButton(text="שערים", callback_data="view_curr")
        news = types.InlineKeyboardButton(text="📰 ערוץ החדשות של BitsOfGold 📰", url="https://t.me/BitsOfGoldNews")
        start1.row(site)
        start1.row(news)
        start1.row(view_curr, exchange)
        f = open('welcome.jpg', 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=config.welcome_photo, caption=he.welcome, reply_markup=start1,
                       parse_mode='Markdown', timeout=1000)

    elif call.data == "buy":
        config.stage = 2
        if config.stage:
            buy = types.InlineKeyboardMarkup()
            buy.row(buttons.btc_select, buttons.eth_select)
            buy.row(buttons.back1)
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text.buy,
                                     reply_markup=buy, parse_mode='Markdown')

    elif call.data == "btc_select":
        config.crypto = "btc"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text.after_fee, parse_mode='Markdown')

    elif call.data == "eth_select":
        config.crypto = "eth"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption=text.after_fee, parse_mode='Markdown')

    elif call.data == "confirm2":
        config.stage = 21
        bot.send_message(chat_id=call.message.chat.id, text=text.after_confirm1, reply_markup=keyboard.back)

    elif call.data == "confirm3":
        config.stage = 12
        bot.send_message(chat_id=call.message.chat.id, text=text.after_confirm1, reply_markup=keyboard.back)


    elif call.data == "confirm":
        config.stage = 4
        bot.send_message(chat_id=call.message.chat.id, text=text.after_confirm, reply_markup=keyboard.back)



@bot.message_handler(content_types=['text'])
def text_to_str(message):
    if config.stage == 1:
        bot.send_message(chat_id=message.chat.id,
                         text="בשלב זה יש השימוש בבוט מתבצע ע\"י הכפתורים בלבד. \nהודעות לא מתקבלות!",
                         parse_mode='Markdown')  # if text not in text



    elif config.stage == 2:
        if config.crypto == "btc":
            try:
                w = int(message.text)
                if w < 500:
                    config.stage = 2
                    if config.stage:
                        bot.send_message(chat_id=message.chat.id, text="הסכום המינימלי להמרה הינו 500 ש\"ח",
                                         parse_mode='Markdown')
                else:
                    if config.stage == 2:
                        config.stage = 3
                        amla_nis = w / int(100) * int(3.45)
                        aaa = "\n---------------------------------------------------------------------------\n"
                        amla_nis_text = aaa + "עמלה בשקלים:       " + str(amla_nis) + " ש\"ח"
                        qqwq = 1 / text.BTC_ILS * w
                        qqwq_text = "\nכמות המטבע :        " + str(round(qqwq, 5)) + "000 BTC"
                        pay_info = "\nסה\"כ לתשלום:        " + str(w + amla_nis) + " ש\"ח"
                        end2 = "\n*בעבור:*        "+ str(w+amla_nis) + " ש\"ח"
                        end3 = "\n*תקבל:*         "+ str(round(qqwq, 5)) + "000 BTC"
                        config.selected_btc = amla_nis+ text.BTC_ILS
                        config.selected_btc1 = int(config.selected_btc)/int(text.BTC_ILS)
                        end1 = "נתונים סופיים:           \n"+end2+end3
                        bot.send_message(chat_id=message.chat.id,
                                         text=text.exchange_text0 + "הסכום שנבחר:        " + str(w) + " ש\"ח " + str(
                                             amla_nis_text) + qqwq_text +
                                              pay_info + "\n---------------------------------------------------------------------------\n"+end1,
                                         reply_markup=keyboard.confirm, parse_mode='Markdown')


            except:
                bot.send_message(chat_id=message.chat.id, text="\n\nשגיעה בנתונים. " + "הקלד ספרות בלבד!",
                                reply_markup=keyboard.back, parse_mode='Markdown')

        elif config.crypto == "eth":
            try:
                w = int(message.text)
                if w < 500:
                    config.stage = 2
                    if config.stage:
                        bot.send_message(chat_id=message.chat.id, text="הסכום המינימלי להמרה הינו 500 ש\"ח",
                                         parse_mode='Markdown')
                else:
                    if config.stage == 2:
                        config.stage = 3
                        amla_nis = w / int(100) * int(3.45)
                        aaa = "\n---------------------------------------------------------------------------\n"
                        amla_nis_text = aaa + "עמלה בשקלים:       " + str(amla_nis) + " ש\"ח"
                        qqwq = 1 / text.ETH_ILS * w
                        qqwq_text = "\nכמות המטבע :        " + str(round(qqwq, 5)) + "000 ETH"
                        pay_info = "\nסה\"כ לתשלום:        " + str(w + amla_nis) + " ש\"ח"
                        end2 = "\n*בעבור:*        " + str(w+amla_nis) + " ש\"ח"
                        end3 = "\n*תקבל:*         " + str(round(qqwq, 5)) + "000 ETH"
                        config.selected_btc = amla_nis + text.ETH_ILS
                        config.selected_btc1 = int(config.selected_btc) / int(text.ETH_ILS)
                        end1 = "נתונים סופיים:           \n" + end2 + end3
                        bot.send_message(chat_id=message.chat.id,
                                         text=text.exchange_text2 + "הסכום שנבחר:        " + str(w) + " ש\"ח " + str(
                                             amla_nis_text) + qqwq_text +
                                              pay_info + "\n---------------------------------------------------------------------------\n" + end1,
                                         reply_markup=keyboard.confirm, parse_mode='Markdown')


            except:
                bot.send_message(chat_id=message.chat.id, text="\n\nשגיעה בנתונים. " + "הקלד ספרות בלבד!",
                                 reply_markup=keyboard.back, parse_mode='Markdown')


    elif config.stage == 4:
        config.stage = 5
        info.card_name = message.text
        bot.send_message(message.chat.id, text.tz)

    elif config.stage == 5:
        config.stage = 6
        info.tz = message.text
        bot.send_message(message.chat.id, text.card_num)

    elif config.stage == 6:
        config.stage = 7
        info.card_num = message.text
        bot.send_message(message.chat.id, text.card_date)

    elif config.stage == 7:
        config.stage = 8
        info.card_date = message.text
        bot.send_message(message.chat.id, text.card_code)

    elif config.stage == 8:
        config.stage = 9
        info.card_back = message.text
        bot.send_message(message.chat.id, text.all_info, reply_markup=keyboard.back)



    elif config.stage == 11:
            if config.crypto == "btc":
                try:
                    w = int(message.text)
                    if w < 500:
                        config.stage = 2
                        if config.stage:
                            bot.send_message(chat_id=message.chat.id, text="הסכום המינימלי להמרה הינו 500 ש\"ח",
                                             parse_mode='Markdown')
                    else:
                        if config.stage == 11:
                            config.stage = 12
                            amla_nis = w / int(100) * int(3.45)
                            amla_nis_all = amla_nis / text.BTC_ILS
                            aaa = "\n---------------------------------------------------------------------------\n"
                            amla_nis_text = aaa + "עמלה בשקלים:       " + str(round(amla_nis, 0)) + " ש\"ח"
                            qqwq = 1 / text.BTC_ILS * w
                            qqwq_procent= qqwq/100*3.45
                            qqwq_text = "\nכמות המטבע :        " + str(round(qqwq, 5)) + "000 BTC"
                            pay_info = "\nסה\"כ לתשלום:        " + str(round(qqwq + qqwq_procent,5)) + "000 BTC"
                            end2 = "\n*בעבור:*        "+ str(round(qqwq+qqwq_procent,2)) + "000 BTC"
                            end3 = "\n*תקבל:*         "+ str(round(w, 5)) + " ש\"ח"
                            config.selected_btc = amla_nis+ text.BTC_ILS
                            config.selected_btc1 = int(config.selected_btc)/int(text.BTC_ILS)
                            end1 = "נתונים סופיים:           \n"+end2+end3
                            bot.send_message(chat_id=message.chat.id,
                                             text=text.exchange_text + "הסכום שנבחר:        " + str(w) + " ש\"ח " + str(
                                                 amla_nis_text) + qqwq_text +
                                                  pay_info + "\n---------------------------------------------------------------------------\n"+end1,
                                             reply_markup=keyboard.confirm1, parse_mode='Markdown')


                except:
                    bot.send_message(chat_id=message.chat.id, text="\n\nשגיעה בנתונים. " + "הקלד ספרות בלבד!",
                                    reply_markup=keyboard.back, parse_mode='Markdown')

            elif config.crypto == "eth":
                try:
                    w = int(message.text)
                    if w < 500:
                        config.stage = 2
                        if config.stage:
                            bot.send_message(chat_id=message.chat.id, text="הסכום המינימלי להמרה הינו 500 ש\"ח",
                                             parse_mode='Markdown')
                    else:
                        if config.stage == 11:
                            config.stage = 13
                            amla_nis = w / int(100) * int(3.45)
                            amla_nis_all = amla_nis / text.BTC_ILS
                            aaa = "\n---------------------------------------------------------------------------\n"
                            amla_nis_text = aaa + "עמלה בשקלים:       " + str(round(amla_nis, 0)) + " ש\"ח"
                            qqwq = 1 / text.ETH_ILS * w
                            qqwq_procent = qqwq / 100 * 3.45
                            qqwq_text = "\nכמות המטבע :        " + str(round(qqwq, 5)) + "000 ETH"
                            pay_info = "\nסה\"כ לתשלום:        " + str(round(qqwq + qqwq_procent, 5)) + "000 ETH"
                            end2 = "\n*בעבור:*        " + str(round(qqwq + qqwq_procent, 3)) + "00 ETH"
                            end3 = "\n*תקבל:*         " + str(round(w, 5)) + " ש\"ח"
                            config.selected_btc = amla_nis + text.ETH_ILS
                            config.selected_btc1 = int(config.selected_btc) / int(text.ETH_ILS)
                            end1 = "נתונים סופיים:           \n" + end2 + end3

                            bot.send_message(chat_id=message.chat.id,
                                             text=text.exchange_text2 + "הסכום שנבחר:        " + str(w) + " ש\"ח " + str(
                                                 amla_nis_text) + qqwq_text +
                                                  pay_info + "\n---------------------------------------------------------------------------\n" + end1,
                                             reply_markup=keyboard.confirm2, parse_mode='Markdown')


                except:
                    bot.send_message(chat_id=message.chat.id, text="\n\nשגיעה בנתונים. " + "הקלד ספרות בלבד!",
                                     reply_markup=keyboard.back, parse_mode='Markdown')

    elif config.stage ==12:
        config.stage = 14
        bot.send_message(message.chat.id, text.after_confirm_num)



    elif config.stage==14:
        config.stage = 15
        bot.send_message(message.chat.id, text.after_confirm1_date)

    elif config.stage==15:
        bot.send_message(message.chat.id, text.send_crypto, reply_markup=keyboard.back)

    elif config.stage ==21:
        config.stage = 22
        bot.send_message(message.chat.id, text.after_confirm_num)
    elif config.stage ==22:
        config.stage = 23
        bot.send_message(message.chat.id, text.after_confirm1_date)
    elif config.stage ==23:
        bot.send_message(message.chat.id, text.send_crypto1, reply_markup=keyboard.back)



bot.polling(none_stop=True, timeout=1000)





