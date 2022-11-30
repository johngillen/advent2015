f = open('input/day21.txt')
lines = [line.rstrip() for line in f.readlines()]

from itertools import product

lines = [int(line.split(': ')[-1]) for line in lines]

class boss:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor
    
    def attack(self, other):
        other.tick(self)
        other.hp -= max(1, self.damage - other.armor)

    def alive(self):
        return self.hp > 0

class spell:
    def __init__(self, name, cost, damage = 0, armor = 0, heal = 0, mana = 0, duration = 0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.heal = heal
        self.mana = mana
        self.duration = duration

class player:
    def __init__(self, hp, armor, damage, mana = None):
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.mana = mana
        self.effects = []
        self.spent = 0

    def cast(self, spell, other):
        self.tick(other)
        self.spent += spell.cost
        if spell.duration != 0:
            self.effects.append(spell)
        else:
            other.hp -= spell.damage
            self.hp += spell.heal
            self.armor = spell.armor
            self.mana += spell.mana
    
    def tick(self, other):
        self.armor = 0
        for effect in self.effects:
            other.hp -= effect.damage
            self.hp += effect.heal
            self.armor = effect.armor
            self.mana += effect.mana
            effect.duration -= 1
        self.effects = [e for e in self.effects if effect.duration > 0]

    def alive(self):
        return self.hp > 0 and self.mana >=53
    
    def sum(self):
        return self.spent

spellbook = [spell('Magic Missile', 53, damage = 4), \
             spell('Drain', 73, damage = 2, heal = 2), \
             spell('Shield', 113, armor = 7, duration = 6), \
             spell('Poison', 173, damage = 3, duration = 6), \
             spell('Recharge', 229, mana = 101, duration = 5)]

attempts = []
i = 1
while True:
    for combo in product(spellbook, repeat=i):
        me = player(50, 0, 0, 500)
        wumpus = boss(lines[0], lines[1], 0)
        for spell in combo:
            me.cast(spell, wumpus)
            if not me.alive():
                break
            if not wumpus.alive():
                attempts.append(me.sum())
                break
            wumpus.attack(me)
            if not me.alive():
                break
    if attempts:
        break
    i += 1

part1 = min(attempts)
part2 = 0

print(f'part 1: {part1}')
print(f'part 2: {part2}')
