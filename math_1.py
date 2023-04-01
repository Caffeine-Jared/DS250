#%%
tree2 = '''
digraph tree {
    layout=dot
    node [shape=circle]
    A -> B
    A -> C
    B -> D
    B -> E
    C -> F
    C -> G
}
'''

from graphviz import Source
from IPython.display import Image, display
display(Image(Source(tree2, format='png').render()))
#%%
from graphviz import Graph

# Define the six non-isomorphic unrooted trees with 6 vertices
trees = [    [('1', '2'), ('1', '3'), ('2', '4'), ('2', '5'), ('3', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('4', '5'), ('4', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('4', '5'), ('5', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('5', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('2', '5'), ('3', '6')],
    [('1', '2'), ('1', '3'), ('2', '4'), ('3', '5'), ('3', '6')]
]

# Generate visualizations of each tree using Graphviz
for i, edges in enumerate(trees):
    dot = Graph(comment='Tree %d' % (i+1), format='png')
    for edge in edges:
        dot.edge(edge[0], edge[1])
    dot.render('tree%d' % (i+1), view=True)
#%%
from graphviz import Graph
from IPython.display import Image, display

# Define the six non-isomorphic unrooted trees with 6 vertices
trees = [
    [('1', '2'), ('1', '3'), ('2', '4'), ('2', '5'), ('3', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('4', '5'), ('4', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('4', '5'), ('5', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('5', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('2', '5'), ('3', '6')],
    [('1', '2'), ('1', '3'), ('2', '4'), ('3', '5'), ('3', '6')]
]

# Create a subgraph to contain the individual graphs
sub = Subgraph('cluster', comment='Unrooted Trees with 6 Vertices', engine='dot')
sub.attr(label='Unrooted Trees with 6 Vertices')
sub.attr(fontsize='16')

# Generate each graph and add it to the subgraph
for i, edges in enumerate(trees):
    dot = Graph(name='tree%d' % (i+1), format='png', engine='dot')
    dot.attr('node', shape='circle', style='open', height='0.1', width='0.1')
    for edge in edges:
        dot.edge(edge[0], edge[1])
    dot.attr(label='Tree %d' % (i+1))
    sub.subgraph(dot)

# Render the subgraph and display it
sub.render('unrooted_trees', format='png')
display(Image(filename='unrooted_trees.png'))

#%%
from graphviz import Digraph
from IPython.display import Image, display

# Expression 1: a(b+c)
expression1 = Digraph(comment="Expression 1: a(b+c)")
expression1.node("*", "*")
expression1.node("a", "a")
expression1.node("+", "+")
expression1.node("b", "b")
expression1.node("c", "c")
expression1.edge("*", "a")
expression1.edge("*", "+")
expression1.edge("+", "b")
expression1.edge("+", "c")

# Expression 2: ab + c
expression2 = Digraph(comment="Expression 2: ab + c")
expression2.node("+", "+")
expression2.node("*", "*")
expression2.node("a", "a")
expression2.node("b", "b")
expression2.node("c", "c")
expression2.edge("+", "*")
expression2.edge("+", "c")
expression2.edge("*", "a")
expression2.edge("*", "b")


# Expression 3: ab + ac
expression3 = Digraph(comment="Expression 3: ab + ac")
expression3.node("+", "+")
expression3.node("*1", "*")
expression3.node("*2", "*")
expression3.node("a1", "a")
expression3.node("a2", "a")
expression3.node("b", "b")
expression3.node("c", "c")
expression3.edge("+", "*1")
expression3.edge("+", "*2")
expression3.edge("*1", "a1")
expression3.edge("*1", "b")
expression3.edge("*2", "a2")
expression3.edge("*2", "c")



# Expression 4: bb-4ac
expression4 = Digraph(comment="Expression 4: bb-4ac")
expression4.node("-", "-")
expression4.node("*1", "*")
expression4.node("*2", "*")
expression4.node("b1", "b")
expression4.node("b2", "b")
expression4.node("*3", "*")
expression4.node("4", "4")
expression4.node("a", "a")
expression4.node("c", "c")
expression4.edge("-", "*1")
expression4.edge("-", "*2")
expression4.edge("*1", "b1")
expression4.edge("*2", "c")
expression4.edge("*2", "*3")
expression4.edge("*3", "4")
expression4.edge("*3", "a")
expression4.edge("*1", "b2")



# Expression 5: a^2 + b^2
expression5 = Digraph(comment="Expression 5: a^2 + b^2")
expression5.node("+", "+")
expression5.node("^", "^")
expression5.node("a", "a")
expression5.node("2", "2")
expression5.node("^1", "^")
expression5.node("b", "b")
expression5.node("2_1", "2")
expression5.edge("+", "^")
expression5.edge("^", "a")
expression5.edge("^", "2")
expression5.edge("+", "^1")
expression5.edge("^1", "b")
expression5.edge("^1", "2_1")

# Render the graphs and display them
trees = [(expression1, "Expression 1: a(b+c)"),
         (expression2, "Expression 2: ab + c"),
         (expression3, "Expression 3: ab + ac"),
         (expression4, "Expression 4: bb-4ac"),
         (expression5, "Expression 5: a^2 + b^2")]
for i, (graph, title) in enumerate(trees):
    graph.render("expression%d" % (i+1), format="png")
    display(Image(filename="expression%d.png" % (i+1)))

        #%%
from graphviz import Graph
from IPython.display import Image, display

# Define the six non-isomorphic unrooted trees with 6 vertices
trees = [
    [('1', '2'), ('1', '3'), ('2', '4'), ('2', '5'), ('3', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('4', '5'), ('4', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('4', '5'), ('5', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('5', '6')],
    [('1', '2'), ('1', '3'), ('1', '4'), ('2', '5'), ('3', '6')],
    [('1', '2'), ('1', '3'), ('2', '4'), ('3', '5'), ('3', '6')]
]

# Create a graph to contain the individual graphs
dot = Graph(comment='Unrooted Trees with 6 Vertices', format='png', engine='dot')
dot.attr(label='Unrooted Trees with 6 Vertices')
dot.attr(fontsize='16')

# Generate each graph and add it to the main graph
for i, edges in enumerate(trees):
    sub = Graph(name='cluster_tree%d' % (i+1), format='png', engine='dot')
    sub.attr(label='Tree %d' % (i+1))
    sub.attr(fontsize='12')
    sub.attr('node', shape='circle', style='open', height='0.1', width='0.1')
    for edge in edges:
        sub.edge(edge[0], edge[1])
    dot.subgraph(sub)

# Render the graph and display it
dot.render('unrooted_trees', format='png')
display(Image(filename='unrooted_trees.png'))
#%%
from graphviz import Graph, Source
from IPython.display import Image, display

# Define the expressions
expressions = [
    "a(b+c)",
    "ab+c",
    "ab+ac",
    "bb-4ac",
    "a^2 + b^2"
]

# Define the corresponding Graphviz code for each expression
graph_codes = [
    '''
    graph tree {
        layout=dot;
        node [shape=circle];
        "*"--a;
        "*"--"+";
        "+"--b;
        "+"--c;
    }
    ''',
    '''
    graph tree {
        layout=dot;
        node [shape=circle];
        "+"--"*";
        "*"--a;
        "*"--b;
        "+"--c;
    }
    ''',
    '''
    graph tree {
        layout=dot;
        node [shape=circle];
        "+"--"* ";
        "+"--"*";
        "* "--a;
        "* "--b;
        "*"--"a ";
        "*"--c;
    }
    ''',
    '''
    graph tree {
        layout=dot;
        node [shape=circle];
        "-"--"*";
        "-"--"* ";
        "*"--"b";
        "*"--"b ";
        "* "--" *";
        "* "--c;
        " *"--4;
        " *"--a;
    }
    ''',
    '''
    graph tree {
        layout=dot;
        node [shape=circle];
        "+"--"*";
        "*"--a;
        "*"--"a ";
        "+"--"* ";
        "* "--b;
        "* "--"b ";
    }
    '''
]

# Generate the expression trees and display them
for i in range(len(expressions)):
    dot = Source(graph_codes[i], format='png')
    dot.format = 'png'
    dot.attr('graph', label='Expression %d: %s' % (i+1, expressions[i]))
    dot.attr('graph', fontsize='16')
    display(Image(dot.render()))
#%%
from graphviz import Digraph

expression_tree = Digraph(comment="Expression Tree")
expression_tree.attr(rankdir="TB")
expression_tree.node("-", "-")
expression_tree.node("*1", "*")
expression_tree.node("13", "13")
expression_tree.node("+", "+")
expression_tree.node("/", "/")
expression_tree.node("32", "32")
expression_tree.node("-4", "-4")
expression_tree.node("12", "12")
expression_tree.node("*2", "*")
expression_tree.node("+1", "+")
expression_tree.node("-", "-")
expression_tree.node("10", "10")
expression_tree.node("1", "1")
expression_tree.node("+2", "+")
expression_tree.node("3", "3")
expression_tree.node("4", "4")
expression_tree.edge("-", "*1")
expression_tree.edge("*1", "13")
expression_tree.edge("*1", "+")
expression_tree.edge("+", "/")
expression_tree.edge("/", "32")
expression_tree.edge("/", "-4")
expression_tree.edge("+", "12")
expression_tree.edge("*1", "*2")
expression_tree.edge("*2", "+1")
expression_tree.edge("+1", "-", "-10")
expression_tree.edge("-", "1")
expression_tree.edge("+1", "+2")
expression_tree.edge("+2", "3")
expression_tree.edge("*2", "4")

expression_tree


#%%

graph expression_tree {
    node [shape=circle];
    "-" -- "*" -- "13";
    "*" -- "+" -- "12";
    "+" -- "/" -- "32" -- "-4";
    "+" -- "*" -- "4" -- "+" -- "-" -- "10" -- "1" -- "3";
}
#%%
def evaluate_expression_tree(et):
    if isinstance(et, int): # Base case: et is a leaf node
        return et
    elif et[0] == '-': # et is a subtraction
        return evaluate_expression_tree(et[1]) - evaluate_expression_tree(et[2])
    elif et[0] == '+': # et is an addition
        return evaluate_expression_tree(et[1]) + evaluate_expression_tree(et[2])
    elif et[0] == '*': # et is a multiplication
        return evaluate_expression_tree(et[1]) * evaluate_expression_tree(et[2])
    elif et[0] == '/': # et is a division
        return evaluate_expression_tree(et[1]) // evaluate_expression_tree(et[2])
    else:
        raise ValueError("Invalid expression tree")

et = ['-', ['*', 13, ['+', ['/', 32, -4], 12]], ['*', ['+', ['-', 10, 1], 3], 4]]
result = evaluate_expression_tree(et)
print(result)


# %%
prefix_codes = {' ': '110',
                'a': '0111',
                'b': '1011100',
                'c': '10110',
                'd': '0000',
                'e': '1111',
                'f': '1011101',
                'g': '0110110',
                'h': '01101011',
                'i': '001',
                'j': '011010100',
                'k': '011010101',
                'l': '0001',
                'm': '11100',
                'n': '0101',
                'o': '1000',
                'p': '01100',
                'q': '1011111',
                'r': '0100',
                's': '11101',
                't': '1010',
                'u': '1001',
                'v': '0110111',
                'w': '011010010',
                'x': '1011110',
                'y': '011010011',
                'z': '01101000'}
message = "discrete math is fun"
encoded_message = ''.join(map(lambda x: prefix_codes[x.lower()], list(message)))
print(encoded_message)

# %%
prefix_codes = {' ': '110',
                'a': '0111',
                'b': '1011100',
                'c': '10110',
                'd': '0000',
                'e': '1111',
                'f': '1011101',
                'g': '0110110',
                'h': '01101011',
                'i': '001',
                'j': '011010100',
                'k': '011010101',
                'l': '0001',
                'm': '11100',
                'n': '0101',
                'o': '1000',
                'p': '01100',
                'q': '1011111',
                'r': '0100',
                's': '11101',
                't': '1010',
                'u': '1001',
                'v': '0110111',
                'w': '011010010',
                'x': '1011110',
                'y': '011010011',
                'z': '01101000'}

reverse_codes = {v: k for k, v in prefix_codes.items()}

message = "0110001001111101110100110111101101011010000000111111101110011101001111110101110110010101"
decoded_message = ''
prefix = ''

for bit in message:
    prefix += bit
    if prefix in reverse_codes:
        decoded_message += reverse_codes[prefix]
        prefix = ''

print(decoded_message)

# %%
def preorder(T):
    if not T:
        return
    print(T[0], end=' ')
    preorder(T[1])
    preorder(T[2])

tree = ['a', ['b', ['c', ['d'], ['e']], ['f', ['g'], ['h']]], ['i', ['j'], ['k', ['l'], ['m', ['n'], ['o']]]]]
preorder(tree) # output: a b c d e f g h i j k l m n o 

# %%
tree = ['a', ['b', ['c', ['d'], ['e']], ['f', ['g'], ['h']]], ['i', ['j'], ['k', ['l'], ['m', ['n'], ['o']]]]]

# Print a single node
def process(v):
    print(v, end=" ")

def preorder(T):
    process(T[0])
    for child in T[1:]:
        preorder(child)

preorder(tree) # should result in: a b c d e f g h i j k l m n o 
# %%
