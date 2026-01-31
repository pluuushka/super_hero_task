import requests

class Superhero:
    
    def __init__(self, height: float, name: str):
        self.height = height
        self.name = name

def find_the_best(gender: str, have_work: bool) -> tuple:
    "берет на себя пол и наличие работы и возвращает имя"
    
    heroes = {} # подходящие герои

    response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
    
    data = response.json()
    
    for json_number in range(0, len(data)):
        
        if data[json_number]['appearance']['gender'] == gender:
            if data[json_number]['work']['base'] == "-" or (data[json_number]['work']['base'] != "-" and have_work):
                curr_hero = Superhero(data[json_number]['appearance']['height'][1], data[json_number]['name'])

                if "meters" in curr_hero.height:
                    heroes[curr_hero.name] = float(curr_hero.height[:-6].strip()) * 100 # все приводим к сантиметрам
                else:
                    heroes[curr_hero.name] = float(curr_hero.height[:-2].strip())


    heroes_names = list(heroes.keys())
    heroes_height = list(heroes.values())
    
    name = heroes_names[0] # конечное имя
    max = heroes_height[0] # самый большой рост

    for i in range(len(heroes_height)):
        if heroes_height[i] > max:
            max = heroes_height[i]
            name = heroes_names[i]

    return name, max
    
if __name__ == "__main__":
    gender = input("Enter the gender: ").strip()
    if gender != 'Male' and gender != 'Female':
        raise ValueError("invalid gender. choose Male of Female.")
    have_work: bool
    print("Enter the have work of not: " \
    "1. Have work " \
    "2. Don't have work ")

    choose = int(input())

    if choose != 1 and choose != 2:
        raise ValueError("invalid choose")
    if choose == 1: 
        have_work = True 
    else: 
        have_work = False

    result = find_the_best(gender, have_work)
    print(result)

            






