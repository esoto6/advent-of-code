
import os
from collections import defaultdict

def makelist(values: list):
    numbers = values.split(":")[1]
    myList = numbers.lstrip().split("\n")
    for i in range(0, len(myList)):
        myList[i] = [int(x) for x in myList[i].split()]
    print(myList)

    return myList

def main(file: str):

    location_low = None
    with open(file, "r") as f:
        # Split content based on empty row
        sections = f.read().split("\n\n")
        # print(sections)


        tables = []
        seeds = []
        for section in sections:
            if section.startswith("seeds"):
                numbers = section.split(":")[1]
                numbers = [int(x) for x in numbers.split()]

                for i in range(0, len(numbers), 2):
                    seeds.append((numbers[i], numbers[i] + numbers[i + 1]))
                print(seeds)

            
                
            if section.startswith("seed-to-soil"):
                seedToSoil = makelist(section)
                tables.append(seedToSoil)
                # print(seedToSoil)
            
            if section.startswith("soil-to-fertilizer"):
                soilToFertilizer = makelist(section)
                tables.append(soilToFertilizer)

                # print(soilToFertilizer)

            if section.startswith("fertilizer-to-water"):
                fertilizerToWater = makelist(section)
                tables.append(fertilizerToWater)
                # print(fertilizerToWater)
            
            if section.startswith("water-to-light"):
                waterToLight = makelist(section)
                tables.append(waterToLight)
                # print(waterToLight)

            if section.startswith("light-to-temperature"):
                lightToTemperature = makelist(section)
                tables.append(lightToTemperature)
                # print(lightToTemperature)

            if section.startswith("temperature-to-humidity"):
                termperatureToHumidity = makelist(section)
                tables.append(termperatureToHumidity)
                # print(termperatureToHumidity)

            if section.startswith("humidity-to-location"):
                humidityToLocation = makelist(section)
                tables.append(humidityToLocation)
                # print(humidityToLocation)
        
        for table in tables:
            # https://www.youtube.com/watch?v=NmxHw_bHhGM time: 11:38
            new = []
            while len(seeds) > 0:
                #Pop off last element of list
                start, end = seeds.pop()
                for a, b, c in table:
                    overlapStart = max(start, b)
                    overlapEnd = min(end, b + c)
                    if overlapStart < overlapEnd:
                        # shift range
                        new.append((overlapStart - b + a, overlapEnd - b + a))
                        if overlapStart > start:
                            seeds.append((start, overlapStart))
                        if end > overlapEnd:
                            seeds.append((overlapEnd, end))
                        break
                else:
                    new.append((start, end))
            seeds = new
    # print(min(seeds)[0])
    return min(seeds)[0]

if __name__ == "__main__":
    isTest = False
    expected = 46

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