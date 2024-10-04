phrase = input('Digite uma frase: ').strip().lower()

words = phrase.split()
wordsTogether = ''.join(words)
reverse = ''

for letter in range(len(wordsTogether) -1, -1, -1):
    reverse += wordsTogether[letter]

print(f'O inverso de {phrase} é {reverse}')

if phrase == reverse:
    print(f'A frase {phrase} é um palíndromo!')
else:
    print(f'A frase {phrase} não é um palíndromo!')
    