message = input(">")
words = message.split(' ')
# to see emojies => control + command + space
emojis = {
":)": "😀",
":(": "😔",
}
output = ""
for word in words:
output += emojis.get(word, word) + " "
print(output)