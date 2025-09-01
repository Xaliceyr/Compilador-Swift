# parser.py
from Analisador_lexico import Analisador_Lexico, token

class Parser:
    def __init__(self, lexer: Analisador_Lexico):
        self.lexer = lexer
        self.token_atual = self.lexer.proximo_token()

    def _consumir(self, tipo_token_esperado: str):
        """
        Consome o token atual se for do tipo esperado.
        Caso contrário, lança um erro sintático.
        """
        if self.token_atual.tipo == tipo_token_esperado:
            print(f"Consumido: {self.token_atual}") # Linha para depuração
            self.token_atual = self.lexer.proximo_token()
        else:
            raise Exception(
                f"Erro Sintático na linha {self.token_atual.linha}: "
                f"Esperado [{tipo_token_esperado}], encontrado [{self.token_atual.tipo}]"
            )

    # --- Métodos para cada regra da gramática ---
    # Estes são os métodos que os integrantes 3 e 4 irão implementar.

    def programa(self):
        """
        <programa> ::= { <comando> }
        """
        # TODO: Implementar a lógica para analisar o programa
        # Geralmente um laço que chama self.comando() até encontrar o token 'EOS'
        while self.token_atual.tipo != 'EOS':
            self.comando()
        print("Análise sintática concluída com sucesso!")

    def comando(self):
        """
        <comando> ::= <declaracao_variavel> | <atribuicao> | <comando_if> | ...
        """
        # TODO: Olhar para o token atual e decidir qual regra de comando seguir
        # if self.token_atual.tipo == 'VAR':
        #     self.declaracao_variavel()
        # elif self.token_atual.tipo == 'IF':
        #     self.comando_if()
        # ... e assim por diante
        pass # remover depois de implementar

    def declaracao_variavel(self):
        """
        <declaracao_variavel> ::= 'var' IDENTIFICADOR ':' <tipo>
        """
        # TODO: Implementar a sequência de chamadas self._consumir()
        # Exemplo:
        # self._consumir('VAR')
        # self._consumir('IDENTIFICADOR')
        # ...
        pass

    # TODO: Criar um método para cada regra da gramática
    # def comando_if(self): ...
    # def expressao(self): ...
    # def termo(self): ...
    # def fator(self): ...