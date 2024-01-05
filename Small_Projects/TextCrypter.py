# Esta función genera una llave aleatoria entre 1 y 25
def generar_llave():
    import random
    return random.randint(1, 25)

# Esta función toma un texto y una llave como entrada, y devuelve el texto encriptado
def encriptar_texto(texto, llave):
    texto_encriptado = ""
    for char in texto:
        # Solo encriptamos los caracteres alfabéticos
        if char.isalpha():
            # Determinamos si el carácter es mayúscula o minúscula para mantener la capitalización después de la encriptación
            ascii_offset = 65 if char.isupper() else 97
            # Encriptamos el carácter desplazándolo 'llave' posiciones en el alfabeto
            texto_encriptado += chr((ord(char) - ascii_offset + llave) % 26 + ascii_offset)
        else:
            # Si el carácter no es alfabético, lo dejamos sin cambios
            texto_encriptado += char
    return texto_encriptado

# Generamos una llave
llave = generar_llave()
# Definimos el texto que queremos encriptar
texto = str(input("Escribe el texto: "))
# Encriptamos el texto
texto_encriptado = encriptar_texto(texto, llave)

# Imprimimos el texto original, el texto encriptado y el texto desencriptado
print("Texto original:", texto)
print("Texto encriptado:", texto_encriptado)
print(llave)