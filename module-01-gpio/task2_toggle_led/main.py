from machine import Pin
import time

BTN_PIN = 4
LED_PIN = 5
DEBOUNCE_MS = 20

btn = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)
led = Pin(LED_PIN, Pin.OUT)
prev_state = btn.value()
count = 1
last_time = time.ticks_ms()
while True:
    now = time.ticks_ms()
    state = btn.value()
    if time.ticks_diff(now, last_time) >= DEBOUNCE_MS:
        last_time = now

        if state == 0 and prev_state == 1:
            print(f'кнопку нажал кнопку {count} раз')
            led.toggle()
            count += 1
        prev_state = state

    time.sleep_ms(1)
