#1
def contains(raw_key: str, cmd_details: list):
    substring = cmd_details[1]
    if substring in raw_key:
        return f"{raw_key} contains {substring}"
    return "Substring not found!"


def flip(raw_key: str, cmd_details: list):
    upper_lower = cmd_details[1]
    start_index = int(cmd_details[2])
    end_index = int(cmd_details[3])
    left_part = raw_key[:start_index]
    right_part = raw_key[end_index:]
    string_to_manipulate = raw_key[start_index:end_index]
    if upper_lower.lower() == "upper":
        string_to_manipulate = raw_key[start_index:end_index].upper()
        raw_key = left_part + string_to_manipulate + right_part

    elif upper_lower.lower() == "lower":
        string_to_manipulate = raw_key[start_index:end_index].lower()
        raw_key = left_part + string_to_manipulate + right_part

    return raw_key


def slice_cmd(raw_key: str, cmd_details: list):
    start_index = int(cmd_details[1])
    end_index = int(cmd_details[2])
    raw_key = raw_key[:start_index] + raw_key[end_index:]
    return raw_key


raw_activation_key = input()

command = input()
while command != 'Generate':
    command_details = command.split('>>>')
    current_command = command_details[0]

    if "Contains" == current_command:
        print(contains(raw_activation_key, command_details))

    elif "Flip" == current_command:
        raw_activation_key = flip(raw_activation_key, command_details)
        print(raw_activation_key)

    elif "Slice" == current_command:
        raw_activation_key = slice_cmd(raw_activation_key, command_details)
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")

#2
import re

text = input()
pattern = r"([@#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"
matches = re.findall(pattern, text)
mirror_pairs = []

for match in matches:
    first_word = match[1]
    second_word = match[2]

    if first_word == second_word[::-1]:
        mirror_pair_found = f"{first_word} <=> {second_word}"
        mirror_pairs.append(mirror_pair_found)

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_pairs:
    print(f"The mirror words are:\n{', '.join(mirror_pairs)}")
else:
    print("No mirror words!")

# 3
def cast_spell(hero_dict: dict, cmd_details: list):
    current_hero = cmd_details[1]
    mana_needed = int(cmd_details[2])
    spell_name = cmd_details[3]

    if mana_needed <= hero_dict[current_hero]['mana']:
        mana_left = hero_dict[current_hero]['mana'] - mana_needed
        hero_dict[current_hero]['mana'] = mana_left
        print(f'{current_hero} has successfully cast {spell_name} and now has {mana_left} MP!')
        return hero_dict
    else:
        print(f'{current_hero} does not have enough MP to cast {spell_name}!')
        return hero_dict


def take_damage(hero_dict: dict, cmd_details: list):
    current_hero = current_command[1]
    damage_taken = int(current_command[2])
    attacker = current_command[3]

    if damage_taken < hero_dict[current_hero]['hp']:
        hp_left = hero_dict[current_hero]['hp'] - damage_taken
        hero_dict[current_hero]['hp'] = hp_left
        print(f'{current_hero} was hit for {damage_taken} HP by {attacker} and now has {hp_left} HP left!')
        return hero_dict

    else:
        hero_dict.pop(current_hero)
        print(f'{current_hero} has been killed by {attacker}!')
        return hero_dict


def recharge(hero_dict: dict, cmd_details: list):
    current_hero = current_command[1]
    mana_recharged = int(current_command[2])
    mana_recovered = mana_recharged

    mana_after_recharge = hero_dict[current_hero]['mana'] + mana_recharged
    if mana_after_recharge > 200:
        mana_above = mana_after_recharge - 200
        mana_recovered = mana_recharged - mana_above

    hero_dict[current_hero]['mana'] += mana_recovered
    print(f'{current_hero} recharged for {mana_recovered} MP!')
    return hero_dict


def heal(hero_dict: dict, cmd_details: list):
    current_name = current_command[1]
    hp_gained = int(current_command[2])
    hp_recovered = hp_gained

    hp_after_heal = hero_dict[current_name]['hp'] + hp_gained
    if hp_after_heal > 100:
        hp_above = hp_after_heal - 100
        hp_recovered = hp_gained - hp_above

    hero_dict[current_name]['hp'] += hp_recovered
    print(f'{current_name} healed for {hp_recovered} HP!')
    return hero_dict


number_of_heroes = int(input())
party = {}

for _ in range(number_of_heroes):
    hero_information = input().split()
    hero_name, hero_hp, hero_mana = hero_information[0], int(hero_information[1]), int(hero_information[2])
    if hero_name not in party:
        party[hero_name] = {'hp': hero_hp, 'mana': hero_mana}

command = input()
while command != 'End':
    current_command = command.split(' - ')

    if current_command[0] == "CastSpell":
        party = cast_spell(party, current_command)

    elif current_command[0] == "TakeDamage":
        party = take_damage(party, current_command)

    elif current_command[0] == "Recharge":
        party = recharge(party, current_command)

    elif current_command[0] == "Heal":
        party = heal(party, current_command)

    command = input()

for hero, stats in party.items():
    print(f'{hero}')
    print(f'  HP: {stats["hp"]}')
    print(f'  MP: {stats["mana"]}')
