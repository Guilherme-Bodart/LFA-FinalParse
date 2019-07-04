from lark import Lark
grammar = """
    ?start:sttmt

    ?sttmt : (expr) ";"
    
    ?expr : (assign) 
            | (ifexpr) 
            | (whileexpr) 
            | (blockexpr) 
            | (lexpr) 
            | (defun)
  
    ?defun : "def" (ident) "(" paramlist? ")" (expr)
  
    ?paramlist : (ident) ("," (ident))*
    
    ?ifexpr : "if" (expr) "then" (expr) ("else" (expr))?
    
    ?whileexpr : "while" (expr) "do" (expr)
    
    ?blockexpr : "{" (sttmt) "}"
    
    ?assign : "var"? (ident) "=" (expr) -> assign_var
    
    ?lexpr : (disj) ("or" (disj))?
    
    ?disj : (conj) ("and" (conj))?

    ?conj : (aexpr) ((rel) (aexpr))?
    
    ?rel : operator
    
    ?aexpr : (factor) ((EXPONENTIAL) (factor))?
    
    ?factor : (term) ((DIVISION|TIMES) (term))?
    
    ?term : (atom) ((PLUS|MINUS) (atom))?
    
    ?atom : "-" (atom)
                | "not" (atom)
                | "(" (expr) ")"
                | NUMBER
                | (functioncall)
                | (variable)

    ?operator: EQUAL| DIFFERENT| EQUALBIG| BIGGER| EQUALSMALL| SMALLER
    
    ?functioncall : (ident) "(" (arglist)? ")"
    
    ?arglist : (expr) ("," (expr))*
    
    ?variable : (ident)
    
    ?ident : (CHAR)(CHAR|NUMBER)*



    PLUS:"+"
    MINUS:"-"
    DIVISION:"/"
    TIMES:"*"
    EXPONENTIAL:"^"
    EQUAL:"=="
    DIFFERENT:"!="
    EQUALBIG:"=>"
    BIGGER:">"
    EQUALSMALL:"=<"
    SMALLER:"<"    

    CHAR: LETTER+
    %import common.NUMBER
    %import common.LETTER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""
   

parser = Lark(grammar)

def leExpressao(expression,lista):
    data=''
    try:
        data = expression.data
        lista[0].append(data)
        leExpressao(expression.children,lista)
    except:
        try:
            filho = expression.children
            leExpressao(filho,lista)
        except:
            lista.append([])
            for i in range(len(expression)):
                verif = verificaFolha(expression[i])
                count = i
                if(verif):
                    lista[-1].append(expression[i].value)

                else:
                    leExpressao(expression[i],lista)
            return  
        return
    return lista

def verificaFolha(folha):
    try:
        folha.value
        return True
    except:
        return False
class Variaveis():
    def __init__(self):
            self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        print(value)
        return value

    def var(self, name):
        return self.vars[name]


def main():    
    expression = input("\nEscreve uma expressao: ")
    
    
    while True:
        try:
            lista=[[]]
            expressao = parser.parse(expression)
            lista = leExpressao(expressao,lista)
            print(lista)
        except:
            print('Expressao incorreta, escreva outra')
        finally:  
            expression = input("\nEscreve uma expressao ou aberte enter: ")
        if expression == "":
            break 
if __name__ == '__main__':
    main()