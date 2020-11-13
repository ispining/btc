from telebot import types
import text
buy = types.InlineKeyboardButton('מעוניין לקנות', callback_data="buy")
sell = types.InlineKeyboardButton('מעוניין למכור', callback_data="sell")
back1 = types.InlineKeyboardButton(text="חזרה לתפריט הראשי", callback_data="home")
confirm1 = types.InlineKeyboardButton(text="מאשר ומעוניין לשלם באשראי", callback_data="confirm")
confirm2 = types.InlineKeyboardButton(text="מאשר ומעוניין להמיר מביטקוין", callback_data="confirm2")
confirm3 = types.InlineKeyboardButton(text="מאשר ומעוניין להמיר מאטריום", callback_data="confirm3")

btc_select = types.InlineKeyboardButton("ביטקוין (BTC)", callback_data="btc_select")
eth_select = types.InlineKeyboardButton("אטריום (ETH)", callback_data="eth_select")
btc_select1 = types.InlineKeyboardButton("ביטקוין (BTC)", callback_data="btc_select")
eth_select1 = types.InlineKeyboardButton("אטריום (ETH)", callback_data="eth_select")


cost1 = types.InlineKeyboardButton(text=str("500₪"), callback_data="a500")
cost2 = types.InlineKeyboardButton(text=str("1,000₪"), callback_data="a1000")
cost3 = types.InlineKeyboardButton(text=str("2,000₪"), callback_data="a2000")
cost4 = types.InlineKeyboardButton(text=str("4,000₪"), callback_data="a4000")
cost5 = types.InlineKeyboardButton(text=str("8,000₪"), callback_data="a8000")
cost6 = types.InlineKeyboardButton(text=str("15,000₪"), callback_data="a15000")
cost7 = types.InlineKeyboardButton(text=str('20,000₪'), callback_data="a20000")
cost8 = types.InlineKeyboardButton(text=str('30,000₪'), callback_data="a30000")
