message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😞",
    ":/": "😕",
    ":D": "😃",
    "O_o": "🤨",
    "XP": "😜",
    "O_O": "😳",
    "Howdy": "🤠"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)