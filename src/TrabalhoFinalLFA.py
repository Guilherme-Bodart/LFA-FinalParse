# This example implements a LOGO-like toy language for Python's turtle, with interpreter.


import turtle

from lark import Lark

VariaveisGlobal = {}
FuncoesGlobal = {}


turtle_grammar = """
    ?start: sttmt

    ?sttmt : (expr) ";"

    ?expr : (assign) 
            | (ifexpr) 
            | (defun)
            | (atom)
            | (instruction)+ -> instruction
            | (conj)

    ?instruction: MOVEMENT valor               -> movement
               | "c" COLOR [COLOR]              -> change_color
               | "fill" (code_block)            -> fill
               | "repeat" valor (code_block)   -> repeat
               | "reset"                        -> reset

    paramlist : ((IDENT)? ("," (IDENT))*)

    ?defun : "def" (IDENT) "(" (paramlist) ")" (expr)      
    
    ?ifexpr : "if" (conj) "then" (conj) ("else" (conj))?       
    
    ?code_block: "{" instruction+ "}"

    ?conj : (variable|NUMBER) (OPERATOR (variable|NUMBER))*

    ?rel : OPERATOR

    MOVEMENT: "f"
                |"b"
                |"l"
                |"r"

    OPERATOR : "==" 
                | "!=" 
                | ">" 
                | "=>" 
                | "<" 
                | "=<"
    
    ?assign : "var"? (variable) "=" (expr)
    
    ?atom : "-" (atom)
                | "not" (atom)
                | "(" (expr) ")"
                | NUMBER
                | (functioncall)
                | (variable) 
    
    ?functioncall : (IDENT)  (arglist) 
    
    arglist : "(" ((expr) ("," (expr))*)? ")"
    
    ?valor: NUMBER|variable

    ?variable: (IDENT)

    IDENT : LETTER+

    COLOR: LETTER+
    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(turtle_grammar)

#Esta função define o que vai ser feito com o comando, apenas 1 por comando;
def leListaExp(lista,pos):
    global VariaveisGlobal
    if lista[0][0]=='NUMBER':
        print(lista[1][0])
    elif lista[0][0]=='IDENT':
        try:
            print(VariaveisGlobal[lista[1][0]])
        except:
            print('Nome de variavel não existe')
    
    else:

        for pos in range(len(lista[0])):
            
            if lista[0][pos]=='assign':
                valor = leAssign(lista,pos)
                break

            elif lista[0][pos]=='defun':
                leDefun(lista,pos)
                break

            elif lista[0][pos]=='functioncall':
                leFunctionCall(lista,pos)
                break

            elif lista[0][pos]=='ifexpr':
                valor = leIfExpr(lista,pos)
                print(valor)
                break

            elif lista[0][pos]=='instruction':
                leInstruction(lista,pos)
                turtle.end_fill()
                break
    return

#Esta função le o Assign na lista feita pela árvore;
def leAssign(lista,pos):
    listaNova = [lista[pos][pos+1:]]
    listaNova.extend(lista[pos+2:])
    try:
        VariaveisGlobal[lista[pos+1][0]] = lista[pos+1][1]
    except:
        VariaveisGlobal[lista[pos+1][0]] = listaNova

    return VariaveisGlobal[lista[pos+1][0]]

#Esta função le o Defun na lista feita pela árvore;
def leDefun(lista,pos):
    global FuncoesGlobal
    if lista[pos+1][0] in FuncoesGlobal:
        print("Função já existe")
        return
    else:
        listaNova = [lista[pos][pos+1:]]
        listaNova.extend(lista[pos+2:])
        FuncoesGlobal[lista[pos+1][0]] = listaNova
        return

#Esta função le a FunctionCall na lista feita pela árvore;
def leFunctionCall(lista,pos):
    
    for i in range(len(FuncoesGlobal[lista[pos+1][0]][1])):
        try:
            VariaveisGlobal[FuncoesGlobal[lista[pos+1][0]][1][i]] = lista[pos+2][i]
        except:
            break

    leListaExp(FuncoesGlobal[lista[pos+1][0]],pos+1)
    return

#Esta função le o If na lista feita pela árvore;
def leIfExpr(lista,pos):
    
    try:
        varConj = lista[0][pos+1]
        varEsq = lista[pos+2][0]
        varOper = lista[pos+2][1]
        varDir = lista[pos+2][2]
        varThen = lista[pos+2][3]

        try:
            varElse = lista[pos+2][4]
            valor = fazIfOper(varEsq,varOper,varDir,varThen,varElse)
        except:
            varElse = ''
            valor = fazIfOper(varEsq,varOper,varDir,varThen,varElse)        

    except:
        varIf = lista[pos+1][0]
        varThen = lista[pos+1][1]
        
        try:
            varElse = lista[pos+1][2]
            valor = fazIf(varIf,varThen,varElse)
        except:
            varElse = ''
            valor = fazIf(varIf,varThen,varElse)

    return valor

#Esta função serve para fazer o If quando não tem Operador;
def fazIf(varIf,varThen,varElse):
    if varIf:
        valor = varThen
    else:
        valor = varElse      

    return valor

#Esta função serve para fazer o If quando se tem Operador;
def fazIfOper(varEsq,varOper,varDir,varThen,varElse):
    try:
        varEsq = VariaveisGlobal[varEsq]
    except:
        varEsq = varEsq
    try:
        varDir = VariaveisGlobal[varDir]
    except:
        varDir = varDir
    try:
        varThen = VariaveisGlobal[varThen]
    except:
        varThen = varThen   
    try:
        varElse = VariaveisGlobal[varElse]
    except:
        varElse = varElse
    if varOper=='>':
        if varEsq > varDir:
            valor = varThen
        else:
            valor = varElse 

    elif varOper=='=>':
        if varEsq >= varDir:
            valor = varThen
        else:
            valor = varElse 

    elif varOper=='<':
        if varEsq < varDir:
            valor = varThen
        else:
            valor = varElse 

    elif varOper=='=<':
        if varEsq <= varDir:
            valor = varThen
        else:
            valor = varElse 

    elif varOper=='!=':
        if varEsq != varDir:
            valor = varThen
        else:
            valor = varElse 

    elif varOper=='==':
        if varEsq == varDir:
            valor = varThen
        else:
            valor = varElse
    return valor

#Esta função verifica qual a instrução que foi mandada pro Turtle;
def leInstruction(lista,pos):
    i=pos
    for i in range(len(lista[0])):
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


#Esta função começa o programa do Turtle com o .fill;
def leFill():
    turtle.begin_fill()
    
    return 

#Esta função é a função de repetição, para desenhar no Turtle, ela apenas será usada dentro do Turtle, Instruction, já que o objetivo da DSL é o Turtle;
def leRepeat(lista,pos):
    try:
        valor = VariaveisGlobal[lista[pos][0]]
    except:
        valor = valor
    
    count = int(valor)
    leBloco(lista,pos+1,count)
    return 

#Esta função roda o bloco, é mais usada para o turtle;
def leBloco(lista,pos,count):
    instr = pos
    i = 0
    while i < count:
        valor = instr+1
        try:
            if lista[0][instr]=='movement':
                leMovement(lista,valor)
                instr +=1;
            i = i + 1;
        except:
            
            instr = instr - 2;
            i = i - 1;
    return

#Esta função roda o .color do Turtle;
def leCores(lista,pos):
    cor1 = lista[pos][0]
    try:
        cor2 = lista[pos][1]

    except:
        cor2 = lista[pos][0] 

    turtle.color(cor1,cor2)
    return

#Esta função roda o .move do Turtle;
def leMovement(lista,pos):
    try:
        valor = VariaveisGlobal[lista[pos][1]]
    except:
        valor = valor

    if lista[pos][0]=='f':
        turtle.fd(int(valor))

    elif lista[pos][0]=='b':
        turtle.bk(int(valor))

    elif lista[pos][0]=='l':
        turtle.lt(int(valor))

    elif lista[pos][0]=='r':
        turtle.rt(int(valor))
    
    return
    
##Esta função roda .reset do turtle;
def leReset():
    turtle.reset()
    return
       


def run_instruction_tree(t):#Esta função foi usada como base para fazer a função que roda o Turtle;
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


#Esta função le a expressão e retorna uma lista equivalente;
def leExpressao(expression,lista):
    data=''
    try:
        expression.type
        lista[0].append(expression.type)
        lista.append([])
        lista[1].append(expression.value)
        return lista
    except:
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
    

#Esta função verifica se é Folha;
def verificaFolha(folha):
    try:
        folha.value
        return True
    except:
        return False

#Esta função roda a árvore;
def run_turtle(program):
    parse_tree = parser.parse(program)
    lista = [[]]
    lista = leExpressao(parse_tree,lista)
    print(lista)
    leListaExp(lista,0)
    # for inst in parse_tree.children:
    #     run_instruction_tree(inst)

def main():
    while True:
        code = input('> ')
        try:
            run_turtle(code)
            
        except Exception as e:
            print(e)


#Teste do programa, usado pelo site que eu usei como base para fazer;
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