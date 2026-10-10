from machine import Pin
import time

BTN_PIN = 4

btn = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)
prev_state = btn.value()

while True:
    state = btn.value()
    if state != prev_state:
        prev_state = state
        print(f"кнопка поменяла состояние: {state}")
    time.sleep_ms(100)
