
import os
from collections import defaultdict

def makelist(values: list):
    numbers = values.split(":")[1]
    myList = numbers.lstrip().split("\n")
    for i in range(0, len(myList)):
        myList[i] = [int(x) for x in myList[i].split()]
    print(myList)

    return myList

def find_value(list, val):
    returnValue = 0
    for each in list:
        print(f"Val: {val}, {each[1]}, {each[1] + each[2]}")
        if val > each[1] and val < each[1] + each[2]:
            # print("This is true")
            returnValue = (val - each[1]) + each[0]
            # print(returnValue)
        else:
            pass
    if returnValue == 0:
        return val
    else: 
        return returnValue

def main(file: str):

    locations = []
    with open(file, "r") as f:
        # Split content based on empty row
        sections = f.read().split("\n\n")
        # print(sections)

        # list_of_string_matches = ["seed-to-soil","soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location"]
        
        # split content based on empty lines
    
        for section in sections:
            if section.startswith("seeds"):
                numbers = section.split(":")[1]
                seeds = [int(x) for x in numbers.split()]
                print(seeds)

            if section.startswith("seed-to-soil"):
                seedToSoil = makelist(section)
                print(seedToSoil)
            
            if section.startswith("soil-to-fertilizer"):
                soilToFertilizer = makelist(section)
                print(soilToFertilizer)

            if section.startswith("fertilizer-to-water"):
                fertilizerToWater = makelist(section)
                print(fertilizerToWater)
            
            if section.startswith("water-to-light"):
                waterToLight = makelist(section)
                print(waterToLight)

            if section.startswith("light-to-temperature"):
                lightToTemperature = makelist(section)
                print(lightToTemperature)

            if section.startswith("temperature-to-humidity"):
                termperatureToHumidity = makelist(section)
                print(termperatureToHumidity)

            if section.startswith("humidity-to-location"):
                humidityToLocation = makelist(section)
                print(humidityToLocation)

        for ea in seeds:
            print(f"Seed: {ea}")

            soil = find_value(seedToSoil, ea)
            # print(f"Soil: {soil}")

            fertilizer = find_value(soilToFertilizer, soil)
            # print(f"Fertilizer: {fertilizer}")

            water = find_value(fertilizerToWater, fertilizer)
            # print(f"Water: {water}")

            light = find_value(waterToLight, water)
            # print(f"Light: {light}")

            temperature = find_value(lightToTemperature, light)
            # print(f"Temperature: {temperature}")

            humidity = find_value(termperatureToHumidity, temperature)
            # print(f"Humidity: {humidity}")

            location = find_value(humidityToLocation, humidity)
            # print(f"Location: {location}")

            locations.append(location)
    
    print(f"all Locations: {locations}")

    return min(locations)
if __name__ == "__main__":

    isTest = False
    expected = 35

    if isTest:
        data_file = "data_day5_test.txt"
    else:
        data_file = "data_day5.txt"

    file = os.path.join(os.path.dirname(__file__), data_file)
    val = main(file)
    
    if isTest:
        if val == expected:
            print("Passed: True")
        else:
            print("Passed: False")
    else:
        print(f"Result: {val}")