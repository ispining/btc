from telebot import types
import config
import buttons
exchange = types.InlineKeyboardMarkup()
exchange.row(buttons.buy, buttons.sell)
exchange.row(buttons.back1)

back = types.InlineKeyboardMarkup()
back.row(buttons.back1)

confirm = types.InlineKeyboardMarkup()
confirm.row(buttons.confirm1)
confirm.row(buttons.back1)

confirm1 = types.InlineKeyboardMarkup()
confirm1.row(buttons.confirm2)
confirm1.row(buttons.back1)

confirm2 = types.InlineKeyboardMarkup()
confirm2.row(buttons.confirm3)
confirm2.row(buttons.back1)

buy = types.InlineKeyboardMarkup()
buy.row(buttons.btc_select, buttons.eth_select)
buy.row(buttons.back1)

sell = types.InlineKeyboardMarkup()
sell.row(buttons.btc_select, buttons.eth_select)
sell.row(buttons.back1)

how_many = types.InlineKeyboardMarkup()
how_many.row(buttons.cost8, buttons.cost7)
how_many.row(buttons.cost6, buttons.cost5, buttons.cost4)
how_many.row(buttons.cost3, buttons.cost2, buttons.cost1)
how_many.row(buttons.back1)
