import json

new_file = open('json.txt', 'r', encoding='utf-8')
new_json_file = json.load(new_file)
print(new_json_file, sep='*')
print(type(new_json_file))
new_file.close()
