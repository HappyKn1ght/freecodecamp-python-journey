full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if character_name == "":
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"

    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'


    str_bar = (full_dot * strength) + (empty_dot * (10 - strength))
    int_bar = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_bar = (full_dot * charisma) + (empty_dot * (10 - charisma))

    character_sheet = character_name + "\n"
    character_sheet += "STR " + str_bar + "\n"
    character_sheet += "INT " + int_bar + "\n"
    character_sheet += "CHA " + cha_bar

    return character_sheet
print(create_character('ren',4, 2, 1))