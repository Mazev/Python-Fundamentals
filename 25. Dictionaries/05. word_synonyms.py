n = int(input())

synonyms = {}

for _ in range(n):
    key = input()
    synonym = input()
    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(synonym)
for key, synonym in synonyms.items():
    print(f"{key} - {', '.join(synonym)}")