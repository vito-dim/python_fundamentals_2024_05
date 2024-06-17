# 80 / 100
# to_do_notes = list()
#
# current_note = input()
# while current_note != 'End':
#     to_do_notes.append(current_note)
#     current_note = input()
#
# to_do_notes.sort()
#
# to_do_notes_sorted_list_modified = []
# for note in to_do_notes:
#     current_note_attributes = note.split('-')
#     current_note = current_note_attributes[1]
#     to_do_notes_sorted_list_modified.append(current_note)
#
# print(to_do_notes_sorted_list_modified)

# 80 / 100
# to_do_notes = list()
#
# current_note = input()
# while current_note != 'End':
#     to_do_notes.append(current_note)
#     current_note = input()
#
# to_do_notes.sort()
#
# for note_index in range(len(to_do_notes)):
#     current_note_attributes = to_do_notes[note_index].split('-')
#     current_note = current_note_attributes[1]
#     to_do_notes.pop(note_index)
#     to_do_notes.insert(note_index, current_note)
#
# print(to_do_notes)

# 100 / 100
# notes = [0] * 10  # zero list, for the scale 1 - 10
#
# while True:
#     command = input()
#     if command == 'End':
#         break
#
#     note_attributes = command.split('-')
#     current_note_priority = int(note_attributes[0]) - 1
#     current_note = note_attributes[1]
#     notes.pop(current_note_priority)
#     notes.insert(current_note_priority, current_note)
#
# result = [element for element in notes if element != 0]
# print(result)

# 100 / 100
notes = [0] * 10  # zero list, for the scale 1 - 10
command = input()
while command != 'End':
    note_attributes = command.split('-')
    current_note_priority = int(note_attributes[0]) - 1
    current_note = note_attributes[1]
    notes.pop(current_note_priority)
    notes.insert(current_note_priority, current_note)
    command = input()

result = [element for element in notes if element != 0]
print(result)
