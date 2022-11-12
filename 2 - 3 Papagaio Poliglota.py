# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado



while True: 
    try: 
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio
           pernaLevantada = input()
           pernaLevantada = pernaLevantada.lower()
           if pernaLevantada =="esquerda":
                print('ingles')
           elif pernaLevantada =="direita":
                print('frances')
           elif pernaLevantada =="nenhuma":
                print('portugues')
           elif pernaLevantada =="ambas":
                print('caiu')
           else:
                break
    except EOFError: 
        break
