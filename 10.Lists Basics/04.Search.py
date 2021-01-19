n = int(input())
text = input()
string = []
match_words = []

for i in range(n):
    current_text = input()
    string.append(current_text)
    if text in current_text:
        match_words.append(current_text)

print(string)
print(match_words)