

class Person:
    def __init__(self, first_name, last_name, nickname=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.contacts = []
        self.groups = {}
        self.social_media = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

    def edit_contact(self, old_contact, new_contact):
        if old_contact in self.contacts:
            index = self.contacts.index(old_contact)
            self.contacts[index] = new_contact

    def add_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []

    def add_contact_to_group(self, group_name, contact):
        if group_name in self.groups:
            self.groups[group_name].append(contact)

    def remove_contact_from_group(self, group_name, contact):
        if group_name in self.groups and contact in self.groups[group_name]:
            self.groups[group_name].remove(contact)

    def add_social_media(self, social_media):
        self.social_media.append(social_media)

    def remove_social_media(self, social_media):
        if social_media in self.social_media:
            self.social_media.remove(social_media)

class Contact:
    def __init__(self, phone_number, email=None, address=None):
        self.phone_number = phone_number
        self.email = email
        self.address = address

class SocialMedia:
    def __init__(self, platform, username):
        self.platform = platform
        self.username = username

class Address:
    def __init__(self, home_address=None, work_address=None):
        self.home_address = home_address
        self.work_address = work_address

# نمونه استفاده
person = Person("Hedieh", "sheikh", "Hedi")
contact1 = Contact("091234*****", "ali@example.com", Address("Tehran", "Company Address"))
social_media1 = SocialMedia("Instagram", "Hedieh_sheikh")

person.add_contact(contact1)
person.add_social_media(social_media1)

# اضافه کردن گروه‌ها و مخاطبین به گروه‌ها
person.add_group("Family")
person.add_group("Friends")
person.add_group("Work")
person.add_group("Emergency")
person.add_contact_to_group("Family", contact1)

print(" | ----  Full name  ----    |")
print(f"Name: {person.first_name} {person.last_name}")
print("              ")
print(" | ---- phone number ----   |")
print(f"Contacts: {[contact.phone_number for contact in person.contacts]}")
print("              ")
print(" |  ---- Information ----   |")
print(f"Social Media: {[sm.platform + ': ' + sm.username for sm in person.social_media]}")
print(f"Groups: {person.groups}")