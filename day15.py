f = open('input/day15.txt')
lines = [line.rstrip() for line in f.readlines()]

class cookie:
    ingredients = []
    candidates = []

    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients
        self.recipes = self.cookbook()
        
        pass

    def cookbook(self):
        from itertools import product
        l = []
        for recipe in product(range(100), repeat=len(self.ingredients)):
            if sum(recipe) == 100:
                l += [list(recipe)]
        return l
    
    def scores(self):
        scores = []
        for recipe in self.recipes:
            score = 1
            for i in range(1, len(self.ingredients[0]) - 1):
                propertyscore = 0
                calories = 0
                for ingredient, amount in zip(self.ingredients, recipe):
                    propertyscore += ingredient[i] * amount
                    calories += ingredient[-1] * amount
                score *= max(0, propertyscore)
            scores.append((score, calories))
        return scores
    

ingredients = []
for line in lines:
    capacity, durability, flavor, texture, calories = line.split(',')
    name = line.split(':')[0]
    capacity = int(capacity[-2:])
    durability = int(durability[-2:])
    flavor = int(flavor[-2:])
    texture = int(texture[-2:])
    calories = int(calories[-2:])
    ingredients.append([name, capacity, durability, flavor, texture, calories])

kitchen = cookie(ingredients)

part1 = max(i[0] for i in kitchen.scores())
part2 = max([i[0] for i in kitchen.scores() if i[1] == 500])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
