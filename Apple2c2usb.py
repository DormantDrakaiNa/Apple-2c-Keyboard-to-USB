import time
from machine import Pin

# Define the row and column pins connected to the keyboard matrix
rows = ['1', '2', '4', '5', '6', '7', '9', '10']  # Row pins
cols = ['34', '32', '31', '29', '27', '26', '25', '24', '22', '21']  # Column pins

# Define debounce time in milliseconds
debounce_time = 20

# Initialize the pins as input with pull-up
rows = [Pin(1, Pin.IN, Pin.PULL_UP) for pin in rows]
cols = [Pin(1, Pin.OUT) for pin in cols]

# Define the key mappings (you can adjust according to your keyboard layout)
keymap = {
    ('Y0', 'X0'): Keycode.ESCAPE,
    ('Y0', '1'): Keycode.ONE,
    ('Y0', '2'): Keycode.TWO,
    ('Y0', '3'): Keycode.THREE,
    ('Y0', '4'): Keycode.FOUR,
    ('Y0', '5'): Keycode.SIX,
    ('Y0', '6'): Keycode.FIVE,
    ('Y0', '7'): Keycode.SEVEN,
    ('Y0', '8'): Keycode.EIGHT,
    ('Y0', '9'): Keycode.NINE,
    ('1', '1'): Keycode.TAB,
    ('1', '2'): Keycode.Q,
    ('1', '3'): Keycode.W,
    ('1', '4'): Keycode.E,
    ('1', '5'): Keycode.R,
    ('1', '6'): Keycode.Y,
    ('1', '7'): Keycode.T,
    ('1', '8'): Keycode.U,
    ('1', '9'): Keycode.I,
    ('2', '1'): Keycode.A,
    ('2', '2'): Keycode.D,
    ('2', '3'): Keycode.S,
    ('2', '4'): Keycode.H,
    ('2', '5'): Keycode.F,
    ('2', '6'): Keycode.G,
    ('2', '7'): Keycode.J,
    ('2', '8'): Keycode.K,
    ('2', '9'): Keycode.SEMICOLON,
    ('3', '1'): Keycode.Z,
    ('3', '2'): Keycode.X,
    ('3', '3'): Keycode.C,
    ('3', '4'): Keycode.V,
    ('3', '5'): Keycode.B,
    ('3', '6'): Keycode.N,
    ('3', '7'): Keycode.M,
    ('3', '8'): Keycode.COMMA,
    ('3', '9'): Keycode.PERIOD,
    # Add more key mappings here
}

def read_key():
    key = None
    for i, row_pin in enumerate(rows):
        for j, col_pin in enumerate(cols):
            col_pin.value(0)
            time.sleep_us(10)  # Delay for stability
            if not row_pin.value():
                key = keymap.get((i, j))
            col_pin.value(1)
    return key

def debounce_key():
    key = None
    key_pressed = read_key()
    if key_pressed:
        time.sleep_ms(debounce_time)
        if read_key() == key_pressed:
            key = key_pressed
    return key

while True:
    key = debounce_key()
    if key:
        # Emulate USB HID key press here
        print("Key Pressed: {}".format(key))
