def convert_to_kilometers(distance, unit):
    #Convert distances to kilometers.#
    if unit == "meters" :
       return distance * 0.001
    elif unit == "miles": 
        return distance * 1.609364
    elif unit == "kilometers" :
        return distance 
    else:
        raise ValueError("Invalid distance unit")

def convert_to_kilograms(weight, unit):
    #Convert weight to kilograms.#
    if unit == "pounds" :
       return weight * 0.453592
    elif unit == "ounces": 
        return weight * 0.453592
    elif unit == "grams" :
        return weight * 0.001
    elif unit == "kilograms" :
        return weight
    else:
        raise ValueError("Invalid weight unit")

def assign_priority(distance, weight, fragility):
#Assign priority to a job based on distance, weight and fragility.#
    priority = distance + weight + fragility
    if priority >= 100 :
        return "High"
    elif priority >= 50:
        return "Medium"
    else:
        return "Low"



distance = 20
weight = 500
fragility  = 3

distance_km = convert_to_kilometers(distance, "meters")
weight_kg = convert_to_kilograms(weight, "grams")
priority = assign_priority(distance_km, weight_kg, fragility)
print(f"The priority of the job is : {priority}")






