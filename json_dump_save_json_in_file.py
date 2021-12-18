import json

Data = {
   "firstName": "Иван",
   "lastName": "Иванов",
   "address": {
       "streetAddress": "Московское ш., 101, кв.101",
       "city": "Ленинград",
       "postalCode": "101101"
   },
   "phoneNumbers": [
       "812 123-1234",
       "916 123-4567"
   ]
}
with open('json.txt', 'w', encoding='utf-8') as new_file:
    json.dump(Data, new_file, ensure_ascii=False, indent=4)