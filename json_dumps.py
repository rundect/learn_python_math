import json

inData = {
    "one": ["http", "yandex.ru"],
    "two": ["https", "google.com"]
}
outData = json.dumps(inData, ensure_ascii=False, indent=4)
print(f'outData: ', type(outData), outData, sep='\n')