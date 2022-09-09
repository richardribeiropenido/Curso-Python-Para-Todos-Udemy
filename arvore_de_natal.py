# estrela da árvore
print('☆'.center(20))  # center(int) para centralizar a estrela
# construindo a árvore
for i in range(1, 20, 2):
    print(('*' * i).center(20))
# tronco da árvore
for r in range(2):
    print('||'.center(19))
# base da árvore
print('\====/'.center(19))
print()
# mensagem final
print('Feliz Natal e, que Jesus ulumine a todos vocês!', end='\n\n')
