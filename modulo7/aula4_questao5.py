'''
*.Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
*.No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
*.Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
*.A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
*.Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.
'''

import os

with open('meus_livros.csv', 'w') as f:
    
    f.write('Título,Autor,Ano de publicação,Número de páginas\n')

    #tem muitos que posuem variações no número de páginas, provavelmente por ter várias versões de um mesmo livro, coloquei as que apareciam mais no topo

    informacoes = ['A arte da guerra,','Sun Tzu,','500 a.C.,','160\n',
    'O Pequeno Príncipe,','Antoine de Saint-Exupéry,','1943,','96\n',
    'Dom Quixote,','Miguel de Cervantes,','1605,','1033\n',
    'It - A Coisa,','Stephen King,','2014,','1103\n',
    'O Príncipe,','Nicolau Maquiavel,','1532,','176\n'
    ]

    for i in informacoes:
        f.write(i)

