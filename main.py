# main.py
from Analisador_lexico import Lexer
from Analisador_sintatico import Parser

def main():
    # TODO: Mudar para ler o código de um arquivo .swiftlite
    codigo_exemplo = """
    // Coloque aqui um código de exemplo em SwiftLite para testar
    // var a: Int
    // a = 10 + 5
    // print(a)
    """

    print("--- INICIANDO ANÁLISE LÉXICA E SINTÁTICA ---")
    print(f"Código a ser analisado:\n{codigo_exemplo}\n")
    
    # Instancia o analisador léxico
    lexer = Lexer(codigo_exemplo)
    
    # Instancia o analisador sintático
    parser = Parser(lexer)
    
    try:
        # Inicia a análise a partir da regra inicial "programa"
        parser.programa()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()