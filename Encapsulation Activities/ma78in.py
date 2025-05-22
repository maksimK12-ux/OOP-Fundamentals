from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
player_character1 = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)
player_character2 = Player('Ario', 'Sub-Saharan', 'Warrior', 15, 210)
player_character3 = Player('Erin', 'Asian', 'Mage', 12, 195)
player_character4 = Player('Jamie', 'Australian', 'Knight', 13, 225)

# TODO: Create an instance of Weapon with random damage between 12 and 15

d = random.randint(12, 15)
p = random.randint(8, 20)
m = random.randint(7, 16)
e = random.randint(5, 10)
player_weapon1 = Weapon('Blasphemous Blade', 'greatsword', d)
player_weapon2 = Weapon('Grim Scythe', 'scythe', p)
player_weapon3 = Weapon('Rivers of blood', 'katana', m)
player_weapon4 = Weapon('Staff of Death', 'staff', e)

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140

rd = random.randint(15, 18)
rh = random.randint(80, 140)
enemy = Enemy('Rykard, Lord of Blasphemy', 'Lunarian', rd, rh)

# Print the player character details
print("--------------------------------------")
print(f"Player Name: {player_character1.name}")
print(f"Player Race: {player_character1.race}")
print(f"Player Class: {player_character1.cls}")
print(f"Player Attack: {player_character1.atk}")
print(f"Player Health: {player_character1.health}")
print("--------------------------------------")

print(f"Player Name: {player_character2.name}")
print(f"Player Race: {player_character2.race}")
print(f"Player Class: {player_character2.cls}")
print(f"Player Attack: {player_character2.atk}")
print(f"Player Health: {player_character2.health}")
print("--------------------------------------")

print(f"Player Name: {player_character3.name}")
print(f"Player Race: {player_character3.race}")
print(f"Player Class: {player_character3.cls}")
print(f"Player Attack: {player_character3.atk}")
print(f"Player Health: {player_character3.health}")
print("--------------------------------------")

print(f"Player Name: {player_character4.name}")
print(f"Player Race: {player_character4.race}")
print(f"Player Class: {player_character4.cls}")
print(f"Player Attack: {player_character4.atk}")
print(f"Player Health: {player_character4.health}")
print("--------------------------------------")

# TODO: Print the player weapon details
print(f"Weapon Damage: {player_weapon1.damage}")
print(f"Weapon Category: {player_weapon1.category}")
print(f"Weapon Name: {player_weapon1.name}")
print("--------------------------------------")

print(f"Weapon Damage: {player_weapon2.damage}")
print(f"Weapon Category: {player_weapon2.category}")
print(f"Weapon Name: {player_weapon2.name}")
print("--------------------------------------")

print(f"Weapon Damage: {player_weapon3.damage}")
print(f"Weapon Category: {player_weapon3.category}")
print(f"Weapon Name: {player_weapon3.name}")
print("--------------------------------------")

print(f"Weapon Damage: {player_weapon4.damage}")
print(f"Weapon Category: {player_weapon4.category}")
print(f"Weapon Name: {player_weapon4.name}")
print("--------------------------------------")

# TODO: Print the enemy character details
print(f"Enemy Name: {enemy.name}")
print(f"Enemy Race: {enemy.race}")
print(f"Enemy Damage: {enemy.damage}")
print(f"Enemy Health: {enemy.health}")