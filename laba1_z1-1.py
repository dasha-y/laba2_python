sequence = input("Введите произвольную последовательность: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
new_sequence = ""
for char in sequence:
    if char in vowels or not char.isalpha():
        new_sequence += char
print("Новая последовательность: ", new_sequence)