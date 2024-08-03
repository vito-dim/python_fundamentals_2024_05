# number_of_heroes = int(input())
# party = {}
#
# for _ in range(number_of_heroes):
#     hero_information = input().split()
#     hero_name, hero_hp, hero_mana = hero_information[0], int(hero_information[1]), int(hero_information[2])
#     if hero_hp > 100:
#         hero_hp = 100
#     if hero_mana > 200:
#         hero_mana = 200
#
#     if hero_name not in party:
#         party[hero_name] = {'hp': hero_hp, 'mana': hero_mana}
#
# command = input()
# while command != 'End':
#     current_command = command.split(' - ')
#
#     if current_command[0] == "CastSpell":
#         hero_name = current_command[1]
#         mana_needed = int(current_command[2])
#         spell_name = current_command[3]
#
#         if mana_needed <= party[hero_name]['mana']:
#             mana_left = party[hero_name]['mana'] - mana_needed
#             party[hero_name]['mana'] = mana_left
#             print(f'{hero_name} has successfully cast {spell_name} and now has {mana_left} MP!')
#         else:
#             print(f'{hero_name} does not have enough MP to cast {spell_name}!')
#
#     elif current_command[0] == "TakeDamage":
#         hero_name = current_command[1]
#         damage_taken = int(current_command[2])
#         attacker = current_command[3]
#
#         if damage_taken < party[hero_name]['hp']:
#             hp_left = party[hero_name]['hp'] - damage_taken
#             party[hero_name]['hp'] = hp_left
#             print(f'{hero_name} was hit for {damage_taken} HP by {attacker} and now has {hp_left} HP left!')
#         else:
#             party.pop(hero_name)
#             print(f'{hero_name} has been killed by {attacker}!')
#
#     elif current_command[0] == "Recharge":
#         hero_name = current_command[1]
#         mana_recharged = int(current_command[2])
#         mana_recovered = mana_recharged
#
#         mana_after_recharge = party[hero_name]['mana'] + mana_recharged
#         if mana_after_recharge > 200:
#             mana_above = mana_after_recharge - 200
#             mana_recovered = mana_recharged - mana_above
#
#         party[hero_name]['mana'] += mana_recovered
#
#         print(f'{hero_name} recharged for {mana_recovered} MP!')
#
#     elif current_command[0] == "Heal":
#         hero_name = current_command[1]
#         hp_gained = int(current_command[2])
#         hp_recovered = hp_gained
#
#         hp_after_heal = party[hero_name]['hp'] + hp_gained
#         if hp_after_heal > 100:
#             hp_above = hp_after_heal - 100
#             hp_recovered = hp_gained - hp_above
#
#         party[hero_name]['hp'] += hp_recovered
#
#         print(f'{hero_name} healed for {hp_recovered} HP!')
#
#     command = input()
#
# for hero, stats in party.items():
#     print(f'{hero}')
#     print(f'  HP: {stats["hp"]}')
#     print(f'  MP: {stats["mana"]}')

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
