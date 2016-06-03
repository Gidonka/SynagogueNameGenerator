import random

list1=["Agudath", "Temple", "Beth", "Sha'arei", "Congregation", "Kehilath"]
item1=(random.choice(list1))

list2=["Or", "Bnei", "Knesseth", "Etz", "Darkhei", "She'erith", "Tikkun", "Ramat", "Adath", "Tifereth"]
item2=(random.choice(list2))

list3=["Chayim", "Tzion", "Israel", "Jeshurun", "Tzedek", "Shalom", "Achim", "Chessed"]
item3=(random.choice(list3))

print "{0} {1} {2}".format(item1, item2, item3)
