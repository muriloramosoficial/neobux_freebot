import pyautogui as py
import time

# next = py.locateOnScreen('')


# define a cor a ser procurada
cor_procurada = (255, 0, 0)  # vermelho

print('Bot Iniciado!')
print('Obedecendo Ordens...')

while True:
    star = py.locateOnScreen('./prints/star.PNG', confidence=0.7)
    if star:
        x, y = py.center(star)
        py.leftClick(x, y)

        time.sleep(2)

        # procura a cor desejada na tela
        redcircle = py.locateOnScreen(
            './prints/circle.png', grayscale=False, confidence=0.7)
        if redcircle:
            x, y = py.center(redcircle)
            py.leftClick(x, y)

            time.sleep(2)

            close = py.locateOnScreen(
                './prints/close.PNG', grayscale=False, confidence=0.7)
            if close:
                x, y = py.center(close)
                py.leftClick(x, y)
    else:
        nex = py.locateOnScreen('./prints/nex.png')
        if nex:
            x, y = py.center(nex)
            py.leftClick(x, y)
        else:
            close = py.locateOnScreen(
                './prints/close.PNG', grayscale=False, confidence=0.7)
            if close:
                x, y = py.center(close)
                py.leftClick(x, y)
    ad = py.locateOnScreen('./prints/ad.PNG', grayscale=False, confidence=0.7)
    if ad:
        py.click(1379, 741)

    # if ad:
    #     x, y = py.center(ad)
    #     py.leftClick(x, y)
    # if next:
    #     x, y = py.center(next)
    #     py.leftClick(x, y)
