# Підрахуйте загальну кількість речень у тексті, кількість
# окличних речень, кількість питальних речень, кількість речень, що
# закінчуються трикрапкою.

text = 'Ssfsfd. Ssfsfd. Ssfsfd. Ssfsfd. Ssfsfd. Ssfsfd. Ddsfgsdgsdg? Ddsfgsdgsdg? Ddsfgsdgsdg? Ffdgd gfdg gfdgfdg! Ssfsfd. Ffsdgfsdsf...  Hgffr dfg fdsfd!? Hgffr dfg fdsfd!? Hgffr dfg fdsfd!?'

sentences_count = (len(text.split('. ')) - 1) - (len(text.split('... ')) - 1)


def get_sentences_count(text):
    return (len(text.split('.')) - 1) - (get_not_end_sentences(text) * 3)

def get_not_end_sentences(text):
    return (len(text.split('...')) - 1)

def get_question_sentences(text):
    return (len(text.split('?')) - 1)  - get_question_exclamatory_sentences(text)

def get_exclamatory_sentences(text):
    return (len(text.split('!')) - 1) - get_question_exclamatory_sentences(text)

def get_question_exclamatory_sentences(text):
    return (len(text.split('!?')) - 1)

print(f'. -  {get_sentences_count(text)}')
print(f'... - {get_not_end_sentences(text)}')
print(f'? - {get_question_sentences(text)}')
print(f'! - {get_exclamatory_sentences(text)}')
print(f'!? - {get_question_exclamatory_sentences(text)}')