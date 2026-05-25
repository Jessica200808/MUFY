import random
name = input("What is your name?\n")
adjectives = ['Cunning', 'Majestic','Sluggish','Fearless','Secret','Sneaky']
animals = ['Cheetah','Sloth','Eagle','Fox','Dragon','Otter']
adj = random.choice(adjectives)
animal = random.choice(animals)
codename = adj + " " + animal
lucky_number = random.randint(1,99)
print(name + ", your codename is: " + codename)
random_num = random.randint(1,99)
print("Your lucky number is: " + str(lucky_number))