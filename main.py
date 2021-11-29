atbilde = [[],[],[],[],[]]
jaut = ['Kads? ', 'Kas? ', 'Kur? ', 'Ko darija? ', 'Kas sanaca?']
output = ''
print('Speles noteikumi:')
print('Speletaji pec kartas ievada atbildes')
print('')
for n in range(5):
    for n1 in range(5):
        atbilde[n1].append(input(jaut[n]))
for n in atbilde:
    for n1 in n:
        output += n1 + ' '
    print(output)
    output = ''


