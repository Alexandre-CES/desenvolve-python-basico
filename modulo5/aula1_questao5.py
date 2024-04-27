import emoji

print("Emojis disponíveis: ")
print("😺 - :grinning_cat:")
print("🥶 - :cold_face:")
print("👾 - :alien_monster:")
print("🐈 - :cat:")

print("Digite uma palavra e ela será emojizada: ")

frase = input()
print(emoji.emojize(frase))
