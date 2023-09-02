import time
import asyncio
from threading import Thread


# Синхронность
def red():
    time.sleep(3)
    print('Красный')


def yellow():
    time.sleep(5)
    print('Желтый')


def green():
    time.sleep(8)
    print('Зеленый')


red()
yellow()
green()
print('Старт!!!')
