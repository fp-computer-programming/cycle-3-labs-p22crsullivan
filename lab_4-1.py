# Author: CRS 9/30/21
magic_charge = int(input("Please input your magic charge value."))
shield_charge = int(input("Please input your shield charge value."))
if ((magic_charge >= 90 and shield_charge >= 75)):
    print("You defeated the dragon! But the princess is in another castle.")
else:
    print("The dragon burns you to a crisp.")
