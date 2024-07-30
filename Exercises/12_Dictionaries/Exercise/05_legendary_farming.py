# legendary_materials = {}
# junk_materials = {}
# is_obtained = False
#
# for item in ("Shadowmourne", "Valanyr", "Dragonwrath"):
#     material = ''
#     if item == "Shadowmourne":
#         material = 'shards'
#     elif item == "Valanyr":
#         material = 'fragments'
#     else:
#         material = 'motes'
#     legendary_materials[material] = {'item': item, 'quantity': 0}
#
# current_items = input()
# while not is_obtained:
#     obtained_items = current_items.lower().split()
#     for index in range(0, len(obtained_items), 2):
#         current_quantity = int(obtained_items[index])
#         current_material = obtained_items[index + 1]
#         if current_material in legendary_materials:
#             legendary_materials[current_material]['quantity'] += current_quantity
#             if legendary_materials[current_material]['quantity'] >= 250:
#                 is_obtained = True
#                 legendary_materials[current_material]['quantity'] -= 250
#                 print(f"{legendary_materials[current_material]['item']} obtained!")
#         else:
#             if current_material not in junk_materials:
#                 junk_materials[current_material] = current_quantity
#             else:
#                 junk_materials[current_material] += current_quantity
#         if is_obtained:
#             break
#     if is_obtained:
#         break
#     current_items = input()
#
# for material in legendary_materials:
#     print(f"{material}: {legendary_materials[material]['quantity']}")
#
# for material, quantity in junk_materials.items():
#     print(f"{material}: {quantity}")


materials = {"shards": 0, "fragments": 0, "motes": 0}
won_legendary_item = False
while not won_legendary_item:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index+1].lower()
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials["shards"] >= 250:
            materials["shards"] -= 250
            print("Shadowmourne obtained!")
            won_legendary_item = True
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            print("Valanyr obtained!")
            won_legendary_item = True
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            print("Dragonwrath obtained!")
            won_legendary_item = True
        if won_legendary_item:
            break
for material, quantity in materials.items():
    print(f"{material}: {quantity}")