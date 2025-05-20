import pandas as pd
import pyautogui
import time


produtos=pd.read_csv('produtos.csv')

pyautogui.PAUSE= 0.20
pyautogui.press('win')
pyautogui.write('gx')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=989, y=576)
pyautogui.write('mhitz@dbz.com')
pyautogui.press('tab')
pyautogui.write('winter')
pyautogui.click(x=957, y=824)
time.sleep(2)

for linha in produtos.index:
    pyautogui.click(x=1122, y=414)
    pyautogui.write(str(produtos.loc[linha , 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha , 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha , 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha , 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha , 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha , 'custo']))
    pyautogui.press('tab')
    if not pd.isna(produtos.loc[linha , 'obs']):
        pyautogui.write(str(produtos.loc[linha , 'obs']))
    pyautogui.click(x=828, y=806)
    time.sleep(1)
    pyautogui.scroll(+600)
    pyautogui.click(x=830, y=409)