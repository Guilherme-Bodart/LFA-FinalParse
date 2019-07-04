# This example implements a LOGO-like toy language for Python's turtle, with interpreter.

VariaveisGlobal = {}


import turtle

from lark import Lark

turtle_grammar = """
    ?start: sttmt

    ?sttmt : (expr) ";"

    ?expr : (assign) 
            | (ifexpr) 
            | (whileexpr)
            | (defun)
            | (atom)
            | (instruction)+ -> instruction

    ?instruction: MOVEMENT NUMBER           -> movement
               | "c" COLOR [COLOR]          -> change_color
               | "fill" (code_block)          -> fill
               | "repeat" NUMBER (code_block) -> repeat
               | "reset"                    -> reset

    ?paramlist : (ident) ("," (ident))*

    ?defun : "def" (ident) "(" paramlist? ")" (expr)          
    
    ?ifexpr : "if" (expr) "then" (expr) ("else" (expr))?
    
    ?whileexpr : "while" (expr) "do" (expr)          
    
    ?code_block: "{" instruction+ "}"
    
    MOVEMENT: "f"|"b"|"l"|"r"
    
    ?assign : "var"? (ident) "=" (expr)
    
    ?atom : "-" (atom)
                | "not" (atom)
                | "(" (expr) ")"
                | NUMBER
                | (functioncall)
                | (variable)
    
    ?functioncall : (ident) "(" (arglist)? ")"
    
    ?arglist : (expr) ("," (expr))*
    
    ?variable: (ident)

    ?ident : (COLOR)

    COLOR: LETTER+
    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(turtle_grammar)


def leListaExp(lista):
    for i in range(len(lista[0])):
        
        if lista[0][i]=='assign':
            leAssign(lista,i+1)

        elif lista[0][i]=='defun':
            leDefun(lista,i+1)

        elif lista[0][i]=='paramList':
            leParamList(lista,i+1)

        elif lista[0][i]=='ifexpr':
            leIfExpr(lista,i+1)

        elif lista[0][i]=='instruction':
            leInstruction(lista,i+1)
    return

def leAssign(lista,pos):
    
    return

def leDefun(lista,pos):

    return

def leParamList(lista,pos):

    return

def leIfExpr(lista,pos):
    
    return


def leInstruction(lista,pos):
    i=pos
    if lista[0][i]=='change_color':
        leCores(lista,i+1)

    elif lista[0][i]=='fill':
        leFill()
    
    elif lista[0][i]=='repeat':
        count = leRepeat(lista,i+1)
    
    elif lista[0][i]=='movement':
        leMovement(lista,i+1)
    
    elif lista[0][i]=='reset':
        leReset()
    return


def leFill():
    turtle.begin_fill()
    turtle.end_fill()
    return 

def leRepeat(lista,pos):
    count = lista[pos][0]
    leBloco(lista,pos+1,count)
    return

def leBloco(lista,pos,count):
    instr = pos
    
    for i in range(count):
        valor = instr+1
        try:
            if lista[0][instr]=='movement':
                leMovement(lista,valor)
                instr +=1;
        except:
            instr = instr - 2;
            i = i - 1;
    return

def leCores(lista,pos):
    cor1 = lista[pos][0]
    try:
        cor2 = lista[pos][1]

    except:
        cor2 = lista[pos][0] 

    turtle.color(cor1,cor2)
    return

def leMovement(lista,pos):
    if lista[pos][0]=='f':
        turtle.fd(lista[pos][1])

    elif lista[pos][0]=='b':
        turtle.bk(lista[pos][1])

    elif lista[pos][0]=='l':
        turtle.lt(lista[pos][1])

    elif lista[pos][0]=='r':
        turtle.rt(lista[pos][1])
    
    return
    
def leReset():
    turtle.reset()
    return
     
        


def run_instruction_tree(t):
    if t.data == 'change_color':
        turtle.color(*t.children)   # We just pass the color names as-is

    elif t.data == 'movement':
        name, number = t.children
        { 'f': turtle.fd,
          'b': turtle.bk,
          'l': turtle.lt,
          'r': turtle.rt, }[name](int(number))

    elif t.data == 'repeat':
        count, block = t.children
        for i in range(int(count)):
            run_instruction_tree(block)

    elif t.data == 'fill':
        turtle.begin_fill()
        run_instruction_tree(t.children[0])
        turtle.end_fill()

    elif t.data == 'code_block':
        for cmd in t.children:
            run_instruction_tree(cmd)

    elif t.data == 'reset':
        turtle.reset()
        return
    
    else:
        raise SyntaxError('Unknown instruction: %s' % t.data)


# def run_instruction(instruction):
#     turtle.color(instruction[color])        
#     name = instruction[movement][0]
#     number = instruction[movement][1]
#     { 'f': turtle.fd,
#         'b': turtle.bk,
#         'l': turtle.lt,
#         'r': turtle.rt, }[name](int(number))

#     count = 
#         count, block = t.children
#         for i in range(int(count)):
#             run_instruction_tree(block)

#     elif t.data == 'fill':
#         turtle.begin_fill()
#         run_instruction_tree(t.children[0])
#         turtle.end_fill()

#     elif t.data == 'code_block':
#         for cmd in t.children:
#             run_instruction_tree(cmd)
#     else:
#         raise SyntaxError('Unknown instruction: %s' % t.data)

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



def run_turtle(program):
    parse_tree = parser.parse(program)
    lista = [[]]
    lista = leExpressao(parse_tree,lista)
    print(parse_tree,'\n')
    print(lista)
    for inst in parse_tree.children:
        run_instruction_tree(inst)

        

def main():
    while True:
        code = input('> ')
        try:
            run_turtle(code)
            
        except Exception as e:
            print(e)

def test():
    text = """
        c red yellow
        fill { repeat 36 {
            f200 l170
        }}
    """
    run_turtle(text)

if __name__ == '__main__':
    # test()
    main()