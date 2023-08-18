import json

# json 파일 읽어오기
file_path = "assignment/ex.json"
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(type(data))

# 읽기
print(data)
print(data["users"][0]["name"])

# 수정
data["users"][1]["password"] = "1010"
print(data["users"][1])

# 추가
data["users"].append({"id": "4321", "password": "4321", "name": "손흥민", "phone": "010-4321-4321"})
print(data)

# json 파일 저장/수정
file_path = "assignment/ex_change.json"
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent='\t')