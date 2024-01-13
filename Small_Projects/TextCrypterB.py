def desencriptar_texto(texto_encriptado, llave):
    texto_desencriptado = ""
    for char in texto_encriptado:
        # Solo desencriptamos los caracteres alfabéticos
        if char.isalpha():
            # Determinamos si el carácter es mayúscula o minúscula para mantener la capitalización después de la desencriptación
            ascii_offset = 65 if char.isupper() else 97
            # Desencriptamos el carácter desplazándolo 'llave' posiciones en el alfabeto en sentido contrario
            texto_desencriptado += chr((ord(char) - ascii_offset - llave) % 26 + ascii_offset)
        else:
            # Si el carácter no es alfabético, lo dejamos sin cambios
            texto_desencriptado += char
    return texto_desencriptado

texto_encriptado=str(input("Ingresa el mensaje codificado: "))
llave=int(input("Ingresa la llave de encriptado: "))
texto_desencriptado = desencriptar_texto(texto_encriptado, llave)
print(texto_desencriptado)