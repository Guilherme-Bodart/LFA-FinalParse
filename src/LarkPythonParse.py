from lark import Lark
grammar = """
    ?start:sttmt+

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
    
    ?assign : "var"? (ident) "=" (expr)
    
    ?lexpr : (disj) ("or" (disj))*
    
    ?disj : (conj) ("and" (conj))*

    ?conj : (aexpr) ((rel) (aexpr))?
    
    ?rel : "==" | "!=" | ">" | ">=" | "<" | "<="
    
    ?aexpr : (factor) (("+"|"-") (factor))*
    
    ?factor : (term) (("*"|"/") (term))*
    
    ?term : (atom) ("^" (atom))?
    
    ?atom : "-" (atom)
                | "not" (atom)
                | "(" (expr) ")"
                | NUMBER
                | (functioncall)
                | (variable)
    
    ?functioncall : (ident) "(" (arglist)? ")"
    
    ?arglist : (expr) ("," (expr))*
    
    ?variable : (ident)
    
    ?ident : NUMBER+
    
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""
   

parser = Lark(grammar)


def main():    
    expression = input("\nEscreve uma expressao: ")
    while True:
        print(parser.parse(expression))    
        expression = input("\nEscreve uma expressao ou aberte enter: ")
        if expression == "":
            break 
if __name__ == '__main__':
    main()