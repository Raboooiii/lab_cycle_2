import json
with open("iris.json", "r") as file:
    txt_file = file.read()
list_of_dictionary = json.loads(txt_file)

def calculate_total_area(flower):
    sepal_area = flower.get("sepalLength", 0) * flower.get("sepalWidth", 0)
    petal_area = flower.get("petalLength", 0) * flower.get("petalWidth", 0)
    return sepal_area + petal_area
for i in list_of_dictionary:
    if i.get("species") == "setosa":
        print(i)
petal_lst = []
sepal_lst = []

for j in list_of_dictionary:
    sepal_length = j.get('sepalLength')
    sepal_width = j.get('sepalWidth')
    petal_length = j.get('petalLength')
    petal_width = j.get('petalWidth')

    if all(v is not None for v in [sepal_length, sepal_width, petal_length, petal_width]):
        petal_area = round(petal_length * petal_width, 2)
        petal_lst.append(petal_area)
        sepal_area = round(sepal_length * sepal_width, 2)
        sepal_lst.append(sepal_area)
    else:
        print("Missing values for some attributes in the data.")

print("MAXIMUM SEPAL AREA:", max(sepal_lst))
print("MINIMUM PETAL AREA:", min(petal_lst))

sorted_list = sorted(list_of_dictionary, key=calculate_total_area, reverse=True)
print("Sorted List based on Total Area:")
for item in sorted_list:
    print(item)