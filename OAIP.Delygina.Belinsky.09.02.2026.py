import json
table_games = [
    {"name": "Oxygen Not Included", "date_of_publishing": 2019, "developer": "Klei Entertainment", "price": 449},
    {"name": "Minecraft", "date_of_publishing": 2011, "developer": "Mojang Studios", "price": 2100},
    {"name": "Detroit: Become Human", "date_of_publishing": 2019, "developer": "Quantic Dream", "price": 2999}
]

with open("games.json", "w", encoding="utf-8") as f:
    json.dump(table_games, f, ensure_ascii=False, indent=2)


#json_string = json.dumps(table_games)


for table_game in table_games:
    print(table_game)  #вывод таблицы
