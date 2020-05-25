menu = []
menu.append(["Egg", "Spam", "Bacon"])
menu.append(["Egg", "Sausage", "Bacon"])
menu.append(["Egg", "Spam"])
menu.append(["Egg", "Bacon", "Spam"])
menu.append(["Egg", "Bacon", "Sausage", "Spam"])
menu.append(["Spam", "Bacon", "Sausage", "Spam"])
menu.append(["Spam", "Egg", "Spam", "Spam", "Bacon", "Spam"])
menu.append(["Spam", "Egg", "Sausage", "Spam"])



for meal in menu:
    if not "Spam" in meal:
        for item in meal:
            print(item)