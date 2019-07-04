# LFA-Parser
Implementação de um parser descendente recursivo para uma Linguagem Livre de Contexto usando a biblioteca Lark, chamada de MEL.

### Informações gerais
- **Autor**: Guilherme Bodart de Oliveira Castro
- **Linguagem de programação**: Python (versão 3.7.3)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.33.1)


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
O código fonte está estruturado em um único arquivo principal;

##### MELParser.py
É o arquivo onde contém a main e as funções utilizadas para resolver o exercício;

```python
def main():    
    expression = input("\nEscreve uma expressao: ")
    while True:
        print(parser.parse(expression))    
        expression = input("\nEscreve uma expressao ou aberte enter: ")
        if expression == "":
            break 
if __name__ == '__main__':
    main()
```

<p> O código acima mostra a main, uma main simples apenas para escrever a expressão e rodar o código principal até ser pressionado apenas o "Enter"</p>

<pre><code class="bash">?start:expr 
    ?expr: (term) (("+" | "-") (term))*
    ?term : (factor) (("*" | "/" | "//" | "%") (factor))*
    ?factor : (base) ("^" (factor))?
    ?base : ("+" | "-") (base) | NUMBER | "(" expr ")"</code></pre>

<p>     Nesta parte do código foi colocado "?" na frente das gramáticas para que fosse resumido o resultado, caso queira ver a árvore </p>
<p>mais completa, apenas retire todas as "?" da frente, que não interfira no código em si.

<h3>Gramática do Trabalho</h3>

  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/IDENT.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/MOVEMENT.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/OPERATOR.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/arglist.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/assign.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/code_block.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/conj.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/defun.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/expr.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/functioncall.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/ifexpr.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/instruction.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/paramlist.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/rel.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/sttmt.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/valor.png" title="hover text">
  <img src="https://github.com/Guilherme-Bodart/LFA-FinalParse/blob/master/imagens/variable.png" title="hover text">

</p>


### Como executar?
Para buildar/executar o app no ambiente Linux basta abrir o CLI no diretório do MELParser.py e digitar o comando:
    
    python3 LarkPythonParse.py 
    
O python é na versão 3.7.3, não tenho ciência se terá que baixar a nova versão antes, eu apenas testei o programa no ambiente Windowns.

### Informações sobre "erros"
Neste trabalho eu não tratei nenhum possível erro do usuário
    
### Informações adicionais
Todo o código fonte está hospedado no meu [GitHub](https://github.com/Guilherme-Bodart/LFA-Parser).
