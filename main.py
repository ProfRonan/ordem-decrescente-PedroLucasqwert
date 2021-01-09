"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    palavra_1=input("Digite a primeira palvra:\n")
    palavra_2=input("Digite a segunda palvra:\n")
    palavra_3=input("Digite a terceira palvra:\n")
    
    lista=[palavra_1,palavra_2,palavra_3]
    for i in range(len(lista)):
      for a in range(len(lista)-1):
        if lista [a] < lista [a+1]:
          lista[a],lista[a+1] = lista[a+1],lista[a]
    print(lista[0])
    print(lista[1])
    print(lista[2])



if __name__ == '__main__':
    main()
