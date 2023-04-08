PLACEHOLDER_NAME = '[name]'
PLACEHOLDER_AUTOR = '[autor]'

autor = input('What is your name?: ')

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()

    for name in names:
        name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER_NAME, name)
        new_letter = new_letter.replace(PLACEHOLDER_AUTOR, autor)

        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as complete_letter:
            complete_letter.write(f'{new_letter}')
