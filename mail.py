from re import T
import pyautogui
import time 
import keyboard
 
def cautare_google():
    time.sleep(5)
    if pyautogui.locateAllOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\123.png',confidence=0.7) !=None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\123.png',confidence=0.7) 
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://www.youtube.com')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")
            
cautare_google()
 
def cautare_yt():
    time.sleep(5)
    if pyautogui.locateAllOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\12.png',confidence=0.7) !=None:
        camp_yt = pyautogui.locateOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\12.png',confidence=0.7) 
        pyautogui.click(camp_yt)
        time.sleep(1)
        pyautogui.write('Valydex')
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")
            
cautare_yt()
 
def click_canal():
    time.sleep(3)
    if pyautogui.locateAllOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\valydex.png',confidence=0.7) !=None:
        camp_canal = pyautogui.locateOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\valydex.png',confidence=0.7) 
        pyautogui.click(camp_canal)


    else:


        print("Imaginea nu este pe ecran")
 

    click_canal()
 
def abonare_canal():
    time.sleep(3)
    if pyautogui.locateAllOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\aboneazate.jpg',confidence=0.7) !=None:
        camp_abonare = pyautogui.locateOnScreen(r'C:\Users\Dragos\Desktop\metode avansate de programare\aboneazate.jpg',confidence=0.7) 
        pyautogui.click(camp_abonare)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")
        
abonare_canal()

