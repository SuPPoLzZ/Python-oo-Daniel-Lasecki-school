def smallest_average(person1, person2, person3):
    def calculate_average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3.0

    averages = {
        "person1": calculate_average(person1),
        "person2": calculate_average(person2),
        "person3": calculate_average(person3),
    }

    min_person = min(averages, key=averages.get)
    
    if min_person == "person1":
        return person1
    elif min_person == "person2":
        return person2
    else:
        return person3


person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

result = smallest_average(person1, person2, person3)
print(result)