from typing import NamedTuple, Dict, Union

ERRO = 0
IDENTIFICADOR = 1
NUM_INT = 2
NUM_REAL = 3
EOS = 4

class token(NamedTuple):
    tipo: str
    lexema: str
    valor: Union[int, float, None]
    linha: int

RESERVADAS: Dict[str, str] = {
    #colocar os tokens depois que serem escolhidos
}

class Analisador_Lexico:
    def __init__(self, codigo):
        self.codigo = codigo + '\0'
        self.linha = 1
        self.i = 0
        self.char_atual = self.codigo[self.i]

    def prox_char(self):
        self.i += 1
        self.char_atual = self.codigo[self.i]
        return self.char_atual
    
    def voltar(self):
        self.i -= 1
        self.char_atual = self.codigo[self.i]

    def pula_branco_e_coments(self):
        while self.char_atual != '\0':
            if self.char_atual in (' ', '\t', '\r'):
                self.prox_char()
            elif self.char_atual == '\n':
                self.linha += 1
                self.prox_char()
            # TODO: Adicionar lógica para pular comentários (ex: //)
            # elif self.char_atual == '/' and self.fonte[self.pos_atual + 1] == '/':
            #     while self.char_atual != '\n' and self.char_atual != '\0':
            #         self.prox_char()
            else:
                break

    def identificador(self) -> token:
        """Trata identificadores e verifica se são palavras reservadas."""
        lexema = ''
        # TODO: Adicionar a regra completa para identificadores (ex: pode começar com _)
        while self.char_atual.isalnum() or self.char_atual == '_':
            lexema += self.char_atual
            self.prox_char()
        
        # Verifica se o lexema é uma palavra reservada ou um identificador comum
        tipo_token = RESERVADAS.get(lexema, 'IDENTIFICADOR')
        return token(tipo_token, lexema, None, self.linha)

    def numero(self) -> token:
        """Trata números inteiros."""
        lexema = ''
        while self.char_atual.isdigit():
            lexema += self.char_atual
            self.prox_char()
        return token('NUM_INT', lexema, int(lexema), self.linha)

    def proximo_token(self) -> token:
        """Retorna o próximo token do código fonte."""
        while self.char_atual != '\0':
            self.pula_branco_e_coments()

            if self.char_atual.isalpha() or self.char_atual == '_':
                return self.identificador()

            if self.char_atual.isdigit():
                return self.numero()

            # TODO: Adicionar reconhecimento para todos os operadores e delimitadores
            # Exemplo para operadores de um caractere:
            token_tipo = None
            if self.char_atual == '+':
                token_tipo = 'OP_SOMA'
            elif self.char_atual == '-':
                token_tipo = 'OP_SUB'
            elif self.char_atual == '*':
                token_tipo = 'OP_MULT'
            elif self.char_atual == '/':
                token_tipo = 'OP_DIV'
            elif self.char_atual == '(':
                token_tipo = 'ABRE_PAR'
            elif self.char_atual == ')':
                token_tipo = 'FECHA_PAR'
            # ... e assim por diante para {, }, :, etc.

            # Exemplo para operadores de dois caracteres:
            # if self.char_atual == '=' and self.fonte[self.pos_atual + 1] == '=':
            #     self.prox_char() # avança o primeiro '='
            #     self.prox_char() # avança o segundo '='
            #     return Token('OP_IGUAL', '==', self.linha)
            
            if token_tipo:
                lexema = self.char_atual
                self.prox_char()
                return token(token_tipo, lexema, None, self.linha)

            if self.char_atual == '\0':
                break
                
            # Se chegou aqui, é um caractere inválido
            raise Exception(f"Erro Léxico: Caractere inesperado '{self.char_atual}' na linha {self.linha}")

        return token('EOS', 'EOS', None, self.linha) # EOS = End of Source