import os  # import os, zorgt ervoor dat je functies van de computer kan besturen!
import random  # hiermee kan ik willekeurige cijfers genereren
import pyautogui  # pyautogui zorgt ervoor dat ik muis en toetsenbord kan besturen!
import time  # zorgt ervoor dat ik een pauze in het scriptje kan bouwen

os.startfile(
    r"C:\Xampp\Htdocs\School\Periode-5\Module 12 Python\Opdracht 2\example_file.txt"  # opent de file waarin geschreven moet worden
)
time.sleep(1)  # slaap 1 seconde

i = 1  # iterator
end = 5  # hoe vaak moet de while loop loopen?
while i < end:  # als de while loop end (5) bereikt heeft stop dan
    pyautogui.write(
        str(random.randint(1, 99) * (end ** (end * i))), interval=0.1
    )  # pygui typt een getal tussen 1 en 99 in het bestand 'example_file.txt' dit getal wordt omgezet naar een string en vermenigvuldigd met 5 tot de macht 5 maal de iterator met een interval van 100ms.
    i += 1
    with pyautogui.hold("ctrl"): 
        pyautogui.press("a") #selecteer alles met ctrl+a en typ voer daarna nogmaals de loop uit
    if i == end:
        pyautogui.press("enter") # buttenpress enter
        pyautogui.hotkey("alt", "f4") # sluit de file af met alt+f4
        pyautogui.press("enter") # en klik daarna op enter
