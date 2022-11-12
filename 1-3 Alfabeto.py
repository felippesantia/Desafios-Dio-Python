# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
NUM = 31
  
# Função para calcular a posição dos caracteres
def positions(str):
    for i in str:
          
        # Operação de cálculo dentro das 31 letras do alfabeto
        print((ord(i) & NUM))
  
# Código de chamada
str = input()
positions(str)

# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;
