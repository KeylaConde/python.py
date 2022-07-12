user_word = str(input("Ingresa una palabra: "))
word_without_vowels = ""# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

for letter in user_word.upper():
    if letter in "AEO":
        continue
    elif letter in "IU":
        continue
    else:
        word_without_vowels = letter
        print(word_without_vowels)
        

# Imprimir la palabra asignada a word_without_vowels.
