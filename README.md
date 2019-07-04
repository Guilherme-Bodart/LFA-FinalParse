# LFA-Parser
Implementação de um parser descendente recursivo para uma Linguagem Livre de Contexto usando a biblioteca Lark, chamada de MEL.

### Informações gerais
- **Autor**: Guilherme Bodart de Oliveira Castro e Ana Carolina Cebin
- **Linguagem de programação**: Python (versão 3.7.3)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.33.1) -  Windows
- **Biblioteca de Parse**: Lark



### Lark - Texto copiado de "https://lark-parser.readthedocs.io/en/latest/"

<p>Lark pode analisar qualquer gramática livre de contexto.</p>

<p>Lark fornece:</p>

<p>Linguagem de gramática avançada, baseada em EBNF</p>
<p>Três algoritmos de análise para escolher: Earley, LALR (1) e CYK</p>
<p>Construção automática de árvore, inferida da sua gramática</p>
<p>"Fast unicode lexer" com suporte a regexp e contagem automática de linhas</p>
<p>O código de Lark está hospedado no Github: https://github.com/lark-parser/lark</p>

<pre><code class="bash">$ pip install lark-parser</code></pre>

### Descrição geral do código fonte
LFA-FINALPARSE
|_ .vscode
  |_ launch.json
|_imagens
|_ src
  |_ __pycache__
    |_turtle.cpython-37.pyc
|_ biblioLark.txt
|_ TrabalhoFinalLFA.py
|_ TrabalhoFinalLFADSL.py
|_ grammar.ebnf
|_ lfa-trab-final-2019-1.pdf
|_ README.md


##### TrabalhoFinalLFA.py
É o arquivo onde contém a main, as funções e as expressões do Lark;

##### TrabalhoFinalLFADSL.py
É o arquivo onde contém a main, e as funções;

##### biblioLark.txt
É o arquivo onde fica as expressões do Lark usadas no arquivo TrabalhoFinalLFADSL.psy;

#### Instalação
<h2>Turtle</h2>
<pre><code class="bash">
sudo apt install python3-tk
</code></pre>
<h2>Python 3.7</h2>
<pre><code class="bash">
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
</code></pre>
<h2>Extrair</h2>
<pre><code class="bash">
sudo tar xzf Python-3.7.3.tgz
</code></pre>
<h2>Compile</h2>
<pre><code class="bash">
cd Python-3.7.3
sudo ./configure --enable-optimizations
sudo make altinstall
</code></pre>
<h2>Lark</h2>
<pre><code class="bash">
pip install lark-parser
</code></pre>


```python
def main():
    while True:
        code = input('> ')
        try:
            run_turtle(code)
            
        except Exception as e:
            print(e)
```

<p> O código acima mostra a main, uma main simples apenas para escrever a expressão e rodar o código principal, o código foi feito pelo autor do Lark no exemplo da DSL Turtle que utilizei</p>

<p>Eu usei este código em vez de um arquivo com várias linhas para serem lidas, porque como é o Turtle ele ficaria desenhando vários desenhos, então preferi fazer vários "testes" pré prontos para serem usados</p>

<pre><code class="bash">?start: sttmt

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
</code></pre>
<p>     Nesta parte do código foi colocado "?" na frente das gramáticas para que fosse resumido o resultado, caso queira ver a árvore mais completa, retirando o ? da frente irá interferir diretamente no Código;

<h3>Gramática do Trabalho</h3>
  <h2>IDENT<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/IDENT.png" title="hover text">
  <h2>MOVEMENT<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/MOVEMENT.png" title="hover text">
  <h2>OPERATOR<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/OPERATOR.png" title="hover text">
  <h2>arglist<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/arglist.png" title="hover text">
  <h2>assign<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/assign.png" title="hover text">
  <h2>code_block<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/code_block.png" title="hover text">
  <h2>conj<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/conj.png" title="hover text">
  <h2>defun<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/defun.png" title="hover text">
  <h2>expr<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/expr.png" title="hover text">
  <h2>functioncall<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/functioncall.png" title="hover text">
  <h2>ifexpr<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/ifexpr.png" title="hover text">
  <h2>instruction<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/instruction.png" title="hover text">
  <h2>paramlist<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/paramlist.png" title="hover text">
  <h2>rel<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/rel.png" title="hover text">
  <h2>sttmt<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/sttmt.png" title="hover text">
  <h2>valor<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/valor.png" title="hover text">
  <h2>variable<h2>
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/variable.png" title="hover text">

</p>


### Como executar?
Para buildar/executar o app no ambiente Linux basta abrir o CLI no diretório do MELParser.py e digitar o comando:
    
    python3 LarkPythonParse.py 
    
O python é na versão 3.7.3, não tenho ciência se terá que baixar a nova versão antes, eu apenas testei o programa no ambiente Windowns.

### Informações sobre "erros"
Neste trabalho ainda há vários bugs, porém não consigo dizer exatamente o que, e irei dizer exatamente como que funciona o trabalho, e que tem algumas decisões de projeto, como o if so aceitar números e comparações com ">","<" etc;   Apenas uma expressão por linha, não é permitido escrever mais de um sttmt, irá recusar. Outras decisões que explicarei sobre quando falar de cada uma das expressões;

### Informações adicionais
Todo o código fonte está hospedado no meu [GitHub](https://github.com/Guilherme-Bodart/LFA-Parser).
