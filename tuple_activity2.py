data = (
    [10, 20, 30],
    {
        "name": "Daniel",
        "age": 13
    }
)

print(data)

data[0].append(40)
data[1]["city"] = "London"
print(data)

data[0][1] = 85
data[1]["age"] = 14
print(data)

data[0].extend([50,60])
data[1].update({"city": "liverpool", "gender": "male"})
print(data)

data[0].remove(85)
data[1].pop("age")
print(data)