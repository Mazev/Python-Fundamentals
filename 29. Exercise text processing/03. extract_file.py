file_path = input().split(chr(92))

file_name, extansion = file_path[-1].split('.')

print(f'File name: {file_name}')
print(f'File extension: {extansion}')