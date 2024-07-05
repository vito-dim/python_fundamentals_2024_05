# circle.py
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            return True
        return False

    def get_items(self):
        return self.items


import unittest


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_add_new_item(self):
        result = self.inventory.add_item('apple')
        self.assertTrue(result)
        self.assertIn('apple', self.inventory.get_items())


# comment.py
class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

z
comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)


# email.py
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    data = input().split()

    if data[0] == 'Stop':
        break

    sender, receiver, content = data
    current_email = Email(sender, receiver, content)
    emails.append(current_email)


indices = list(map(int, input().split(', ')))

for index in indices:
    emails[index].send()

for email in emails:
    print(email.get_info())


# example123.py
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

rect = Rectangle(4, 5)

area = rect.calculate_area()
print(area)

rect.resize(6, 7)
area = rect.calculate_area()
print(area)


# party.py
class Party:
    def __init__(self):
        self.people = []

    def add_peron(self, name_):
        self.people.append(name_)

    def print_party_info(self):
        return f'Going: {", ".join(self.people)}\nTotal: {len(party_object.people)}'


party_object = Party()

while True:
    name = input()

    if name == 'End':
        break

    party_object.add_peron(name)

result = party_object.print_party_info()
print(result)
