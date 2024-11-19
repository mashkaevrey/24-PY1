# TODO решите задачи
import json
def task() -> float:
    result = 0
    json_file = json.load(open('input.json', "r"))
    for i in json_file:
        result+=i["score"]*i["weight"]

    return round(result, 3)



print(task())
