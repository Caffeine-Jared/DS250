#%%
import graphviz
dot = graphviz.Digraph()
dot.node('A', 'Hello')
dot.node('B', 'World')
dot.edge('A', 'B')
dot.render('test-output/graphviz-output', view=True)
#%%