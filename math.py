#%%
from graphviz import Digraph
from IPython.display import Image

machine = '''
digraph {
    rankdir=LR;
    0 [shape=rect, label="Start", color="red", fontcolor="red", fontsize=12, width=0.5, height=0.25];
    node [shape=circle]; A;
    node [shape=circle, fontsize=8, margin=0]; REJECT;
    node [shape=doublecircle, margin=0, fontsize=8]; ACCEPT;
    0->A [color=red];
    A->A [label=0];
    A->ACCEPT [label=1];
    ACCEPT->REJECT [label="0,1"];
    REJECT->REJECT [label="0,1"];
}
'''

graph = Digraph()
graph.format = 'png'
graph.engine = 'dot'
graph.body.append(machine)
display(Image(graph.pipe())) 

# %%
