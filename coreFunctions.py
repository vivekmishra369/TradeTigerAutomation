#! python2

from __future__ import division
import pyautogui
import time
import pyperclip

pyautogui.Pause = 2
pyautogui.FailSafe = True


def start():
    "function to automatically start trade  tiger"
    pyautogui.moveTo(0,765) #move to start button
    pyautogui.click()
    pyautogui.moveTo(100,76)
    time.sleep(1)
    #pyautogui.scroll(-300)
    pyautogui.typewrite('trade')
    time.sleep(2)
    pyautogui.click(1155,267)
    #pyautogui.PAUSE
    time.sleep(15)
 

def login(loginId,membership_pass,trading_pass):
    "loginId, membership_pass and trading_pass are strings to be passed "
    pyautogui.hotkey('ctrl','l')   
    time.sleep(1)
    pyautogui.click(740,340) # click on login id field
    pyautogui.typewrite(loginId)
    pyautogui.typewrite('\t')
    time.sleep(0.25)
    pyautogui.typewrite('\t')
    pyautogui.typewrite(membership_pass)
    pyautogui.typewrite('\t')
    pyautogui.typewrite(trading_pass)
    pyautogui.press('enter')
    time.sleep(30)

def setup_marketwatch(script):
    "script is a string that is to be traded on the bse .the script is the security symbol, example 'AAPL'"
    pyautogui.press('f12')
    time.sleep(1)
    pyautogui.hotkey('ctrl','i')
    time.sleep(0.5)
    pyautogui.moveTo(881,300,duration = 0.5) #arrow to select the exchange - comment out if you want to trade NSE
    pyautogui.click() #coment out for trading NSE
    pyautogui.moveTo(870,344,duration = 0.5) #comment out if you want to trade NSE
    pyautogui.click()
    pyautogui.moveTo(787,333)  #to type the name of the script
    pyautogui.click()
    pyautogui.press('backspace')
    pyautogui.typewrite(script)
    pyautogui.moveTo(648,385,duration=0.5) # select the first script in the list
    #pyautogui.click(duration=0.5)
    pyautogui.moveTo(656,547,duration=0.5) #add button
    pyautogui.click()
    pyautogui.moveTo(898,240) #close button
    pyautogui.click()
  


""" fields in data 
Exchange,    -index = 68
Script_name,
pct_change,
Last_traded_qty,
Current,
Bid_qty,
Bid_price,
Offer_price,
Offer_qty,
Open,
High,
Low,
Close,
Last_updated_time,
Last_traded_time,
Last_traded_date,
Qty,
Total_buy_qty, 
Total_sell_qty,
OI_difference,
Company_name,

#now index from last 

Pivo_sup_3
Pivo_sup_2
Pivo_sup_1
Pivot
Pivot_res_1
Pivot_res_2
Pivot_res_3
P_quantity
P_close
P_low
P_High
P_open



"""  

def get_data(coordinate):
    pyautogui.moveTo(20,coordinate)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    raw = pyperclip.paste()
    raw = raw.split()
    data =[]
    for i in range(70,81):
        data.append(eval(raw[i]))
    for i in range(84,88):
        data.append(eval(raw[i]))
    for i in range(-12,-1):
        data.append(raw[i])
    fields = ['pct_change',
    'Last_traded_qty',
    'Current',
    'Bid_qty',
    'Bid_price',
    'Offer_price',
    'Offer_qty',
    'Open',
    'High',
    'Low',
    'Close',
    'Pivo_sup_3',
    'Pivo_sup_2',
    'Pivo_sup_1',
    'Pivot',
    'Pivot_res_1',
    'Pivot_res_2',
    'Pivot_res_3',
    'P_quantity',
    'P_close',
    'P_low',
    'P_High',
    'P_open']

     
    final_data_dict = dict(zip(fields,data))
    return final_data_dict






def buy(coordinate,current_price,quantity):
    "only maxtrade -still need editing"
    pyautogui.moveTo(20,coordinate)
    pyautogui.click()
    pyautogui.hotkey('shift','f1')
    time.sleep(0.5)
    pyautogui.moveTo(780,373) #quantity box
    pyautogui.click()
    pyautogui.press('delete')
    pyautogui.typewrite(quantity)
    pyautogui.moveTo(1060,406,duration=0.5) #order extension arrow
    pyautogui.click()
    pyautogui.moveTo(1060,493)  #select brkt +tsl
    pyautogui.click()
    time.sleep(0.5)
    """
    book_profit = 
    stop_loss = 
    limit_loss = 

    """
    pyautogui.moveTo(400,540,duration=0.5) #book profit area 
    pyautogui.clcik()
    pyautogui.press('delete')
    pyautogui.typewrite(book_profit)
    pyautogui.moveTo(500,540,duration = 0.5) #stop loss area
    pyautogui.click()
    pyautogui.press('delete')
    pyautogui.typewrite(stop_loss)
    pyautogui.moveTo(600,540,duration=0.5) #limit loss area
    pyautogui.clcik()
    pyautogui.press('delete')
    pyautogui.typewrite(limit_loss)
    pyautogui.moveTo(880,540,duration = 0.5) #place buton
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(530,470,duration = 0.5) #confirm button
    pyautogui.click()








def sell(coordinate,current_price,quantity):
     "only maxtrade -still need editing"
    pyautogui.moveTo(20,coordinate)
    pyautogui.click()
    pyautogui.hotkey('shift','f2')
    time.sleep(0.5)
    pyautogui.moveTo(780,373) #quantity box
    pyautogui.click()
    pyautogui.press('delete')
    pyautogui.typewrite(quantity)
    pyautogui.moveTo(1060,406,duration=0.5) #order extension arrow
    pyautogui.click()
    pyautogui.moveTo(1060,493)  #select brkt +tsl
    pyautogui.click()
    time.sleep(0.5)
    """
    book_profit = 
    stop_loss = 
    limit_loss = 

    """
    pyautogui.moveTo(400,540,duration=0.5) #book profit area 
    pyautogui.clcik()
    pyautogui.press('delete')
    pyautogui.typewrite(book_profit)
    pyautogui.moveTo(500,540,duration = 0.5) #stop loss area
    pyautogui.click()
    pyautogui.press('delete')
    pyautogui.typewrite(stop_loss)
    pyautogui.moveTo(600,540,duration=0.5) #limit loss area
    pyautogui.clcik()
    pyautogui.press('delete')
    pyautogui.typewrite(limit_loss)
    pyautogui.moveTo(880,540,duration = 0.5) #place buton
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(530,470,duration = 0.5) #confirm button
    pyautogui.click()






def short(coordinate,current_price,quantity):
      "only maxtrade -still need editing"
    pyautogui.moveTo(20,coordinate)
    pyautogui.click()
    pyautogui.hotkey('ctrl','e')
    time.sleep(0.5)
    pyautogui.moveTo(780,373) #quantity box
    pyautogui.click()
    pyautogui.press('delete')
    pyautogui.typewrite(quantity)
    pyautogui.moveTo(570,433,duration = 0.5) #product type arrow
    pyautogui.click()
    pyautogui.moveTo(567,481,duration = 0.5) #bigtrade selctor
    pyautogui.click()
    pyautogui.moveTo(1060,406,duration=0.5) #order extension arrow
    pyautogui.click()
    pyautogui.moveTo(1060,493)  #select brkt +tsl
    pyautogui.click()
    time.sleep(0.5)
    """
    book_profit = 
    stop_loss = 
    limit_loss = 

    """
    pyautogui.moveTo(400,540,duration=0.5) #book profit area 
    pyautogui.clcik()
    pyautogui.press('delete')
    pyautogui.typewrite(book_profit)
    pyautogui.moveTo(500,540,duration = 0.5) #stop loss area
    pyautogui.click()
    pyautogui.press('delete')
    pyautogui.typewrite(stop_loss)
    pyautogui.moveTo(600,540,duration=0.5) #limit loss area
    pyautogui.clcik()
    pyautogui.press('delete')
    pyautogui.typewrite(limit_loss)
    pyautogui.moveTo(880,540,duration = 0.5) #place buton
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(530,470,duration = 0.5) #confirm button
    pyautogui.click()

clear_positions():
    """Settle all longs and shorts"""


confirm_order():
    """check after six seconds if the order went throgh and return status and cancel if order not filled"""
    time.sleep(6)
    pyautogui.moveTo(226,34,duration = 0.5) #reports button
    pyautogui.click()
    pyautogui.moveTo(40,,65,duration = 0.5) #orders button
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(290,280,duration = 0.5) #latest order
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    raw_str = pyperclip.paste()
    raw_arr  = raw_str.split()
    status = raw_arr[14]  #need to check
    if status == 'Fully Executed':
        return 1
    else:
        pyautogui.moveTo(790,215,duration = 0.5) #cancel button
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(530,470,duration = 0.5) #confirm button
        pyautogui.click()
        "need to chck additional procedures"
        return 0




#start()
#time.sleep(5)
#setup_marketwatch('ICICIBANK')

#time.sleep(5)
#x = get_data(238)
#print x
