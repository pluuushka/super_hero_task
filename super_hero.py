import requests

#def parse(json_number):
#    return requests.get(f"https://akabab.github.io/superhero-api/api/id/{json_number}.json")

class Superhero:
    
    def __init__(self, height, name):
        self.height = height
        self.name = name

def find_the_best(sex: str, have_work: bool) -> str:
    "берет на себя пол и наличие работы и возвращает имя"

    heroes = {} # подходящие герои

    response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
    data = response.json()
    
    
    for json_number in range(0,  len(data)):
        print(f"json_number = {json_number}")
        
        if data[json_number]['appearance']['gender'] == sex:
            if data[json_number]['work']['base'] == "-" or (data[json_number]['work']['base'] != "-" and have_work):
                curr_hero = Superhero(data[json_number]['appearance']['height'][1], data[json_number]['name'])

                print(f"curr_hero = {curr_hero.name} and his height is {curr_hero.height}")
                
                if "meters" in curr_hero.height:
                    heroes[curr_hero.name] = float(curr_hero.height[:-6].strip()) * 100 # все приводим к сантиметрам
                else:
                    heroes[curr_hero.name] = float(curr_hero.height[:-2].strip())

        json_number += 1

    heroes_names = list(heroes.keys())
    heroes_height = list(heroes.values())
    
    name = heroes_names[0] # конечное имя
    max = heroes_height[0] # самый большой рост

    for i in range(len(heroes_height)):
        if heroes_height[i] > max:
            max = heroes_height[i]
            name = heroes_names[i]

    return name, max
    
print(find_the_best('Male', True))

            






