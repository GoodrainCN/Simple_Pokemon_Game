# Create your Classes here
import time
import sys
import random

characters = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock',  'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40, 'Speed': 90, 'Experience': 112},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78, 'Speed': 100, 'Experience': 240},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle',  'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65, 'Speed': 43, 'Experience': 63},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20, 'Speed': 20, 'Experience': 95},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60, 'Speed': 110, 'Experience':225},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],  'Attack': 35, 'Defense': 70, 'Speed': 45, 'Experience': 65},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49, 'Speed': 45, 'Experience': 64},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43, 'Speed': 65, 'Experience': 62},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40, 'Speed': 75, 'Experience': 178},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130, 'Speed': 45, 'Experience': 223},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet',  'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80, 'Speed': 70, 'Experience': 166},
    'Hypno': {'Type': ['Psychic'],'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70, 'Speed': 67, 'Experience': 169},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': [ 'Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28, 'Speed': 15, 'Experience': 44},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40, 'Speed': 84, 'Experience': 61}
}
#print(characters['Pikachu']['Type'])
moves_dict = {
    'Scratch': 
    {
        'name': 'Scratch',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    }, 
    'Tackle': 
    {
        'name': 'Tackle',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    }, 
    'Pound': 
    {
        'name': 'Pound', 'power': 40, 'type': 'Normal', 
        'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']
    }, 
    'Rage': 
    {
        'name': 'Rage', 'power': 20, 'type': 'Normal',
        'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']
    }, 
    'Fury Attack': {'name': 'Fury Attack', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Ember': {'name': 'Ember', 'power': 40, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Fire Spin': {'name': 'Fire Spin', 'power': 35, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Bubble': {'name': 'Bubble', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Aqua Jet': {'name': 'Aqua Jet', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Thunder Shock': {'name': 'Thunder Shock', 'power': 40, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Thunderbolt': {'name': 'Thunderbolt', 'power': 90, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Vine Whip': {'name': 'Vine Whip', 'power': 45, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Magical Leaf': {'name': 'Magical Leaf', 'power': 60, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Ice Shard': {'name': 'Ice Shard', 'power': 40, 'type': 'Ice', 'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']}, 
    'Double Kick': {'name': 'Double Kick', 'power': 30, 'type': 'Fighting', 'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']}, 
    'Earthquake': {'name': 'Earthquake', 'power': 100, 'type': 'Ground', 'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'not very effective against': ['Grass', 'Bug']}, 
    'Wing Attack': {'name': 'Wing Attack', 'power': 60, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Peck': {'name': 'Peck', 'power': 35, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Confusion': {'name': 'Confusion', 'power': 50, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Twineedle': {'name': 'Twineedle', 'power': 25, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Rock Throw': {'name': 'Rock Throw', 'power': 50, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Rock Slide': {'name': 'Rock Slide', 'power': 75, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Lick': {'name': 'Lick', 'power': 30, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}, 
    'Outrage': {'name': 'Outrage', 'power': 120, 'type': 'Dragon', 'super effective against': ['Dragon'], 'not very effective against': ['Steel']}, 
    'Crunch': {'name': 'Crunch', 'power': 80, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Bite': {'name': 'Bite', 'power': 60, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Flash Cannon': {'name': 'Flash Cannon', 'power': 80, 'type': 'Steel', 'super effective against': ['Ice', 'Rock', 'Fairy'], 'not very effective against': ['Fire', 'Water', 'Electric', 'Steel']}, 
    'Smog': {'name': 'Smog', 'power': 30, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'], 'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']}, 
    'Dream Eater': {'name': 'Dream Eater', 'power': 100, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Body Slam': {'name': 'Body Slam', 'power': 85, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Double Slap': {'name': 'Double Slap', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Razor Leaf': {'name': 'Razor Leaf', 'power': 55, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Headbutt': {'name': 'Headbutt', 'power': 70, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Absorb': {'name': 'Absorb', 'power': 20, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Fairy Wind': {'name': 'Fairy Wind', 'power': 40, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Struggle Bug': {'name': 'Struggle Bug', 'power': 50, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Draining Kiss': {'name': 'Draining Kiss', 'power': 50, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Shadow Ball': {'name': 'Shadow Ball', 'power': 80, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}
}

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

class Pokemon:
    def __init__(self, name, all_info, health='==================='):
        # save variables as attributes
        self.name = name
        self.all_info = all_info
        self.types = all_info['Type']
        self.moves = all_info['Moves']
        self.attack = all_info['Attack']
        self.defense = all_info['Defense']
        self.speed = all_info['Speed']
        self.experience = all_info['Experience']
        self.health = all_info['HP']
        self.level = 3
        self.bars = 20
    
    def battle(self, Pokemon2_name, Pokemon2):
        print("-----POKEMONE BATTLE-----")
        print(f"\n  ###{self.name}###")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("HP", self.health)
        print()
        print()
        
        #Put the second Pokemon
        Pokemon2 = Pokemon(Pokemon2_name, Pokemon2)
        print('Fight Against')
        print(f"\n  ###{Pokemon2_name}###")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print('HP', Pokemon2.health)
        print()
        print()
        
        #Pick Move
        delay_print(self.moves)
        print('Pick One Of The Move    ')
        check = False
        #Make Sure User's Selections would be interger
        while True:
            try:
                choice = int(input('Please Pick A Move  '))
            except ValueError:
                print("Sorry, a selection must be an integer!")
            else:
                if choice > len(self.moves):
                    print('Sorry, your selection cannot exceed {} '.format(len(self.moves)))
                else:
                    break 
        self.picked_move = self.moves[int(choice)-1]
        
        #Get Effectiveness(Super_effective)
        self.effective = moves_dict[self.picked_move]['super effective against']
        self.not_effective = moves_dict[self.picked_move]['not very effective against']
        print(self.effective)
        self.modifier_type = 1
        a = [x for x in self.effective if x in Pokemon2.types] #element exists on both lists
        if len(a) >= 1:
            self.modifier_type = 2
            delay_print('Your Attack is Really Effective!')
            print()
        #Get Effectiveness(Weak)
        b = [x for x in self.not_effective if x in Pokemon2.types]
        if len(b) >= 1:
            self.modifier_type = 0.5
            delay_print('Your Attack is Not Effective')
            print()
        #Get Effectiveness(Normal)
        #if len(b) == 0:
            #self.modifier_type = 1
            #print('Your Attack is Not Really Effective')
        

    def cal_damage(self):
        
        #Generating random_d
        random_d = random.uniform(0.85, 1)
        #Critical
        p = random.randint(0,511)
        if p > self.speed:
            critical = 2
            delay_print('Critical Hit!!!')
            print()
        else:
            critical = 1
        #####################
        
        modifier = critical * random_d * self.modifier_type
        
        power = moves_dict[self.picked_move]['power']
        self.damage = ((0.4 * self.level) + 2) * power * (self.attack / self.defense)
        self.damage = (self.damage / 50) * modifier
        return self.damage

Pikachu = Pokemon('Pikachu', characters['Pikachu'])
Jigglypuff = Pokemon('Jigglypuff', characters['Jigglypuff'])
Dewgong = Pokemon('Dewgong', characters['Dewgong'])
#Pikachu.battle('Jigglypuff', characters['Jigglypuff'])
#print(Pikachu.effective)
Pikachu.battle('Dewgong', characters['Dewgong'])
damage_caused = Pikachu.cal_damage()
delay_print(f'Your attack cause {damage_caused} damage!')
#print(type(damage_caused))

class Pokedex:
    
    def __init__(self):
        self.poke_deck = []
        
    def get_poke(self, name):
        self.poke_deck.append(name)
        
    def show_poke(self):
        count = 0
        for i in self.poke_deck:
            print(count, i)
    
    def use_poke(self, num):
        selection = self.poke_deck[num]
        return characters[selection]
    
test = Pokedex()
test.get_poke('Pikachu')
test.show_poke()
test.use_poke(0)