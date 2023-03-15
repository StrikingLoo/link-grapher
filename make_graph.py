import json
import networkx as nx
from bokeh.palettes import Category20
from bokeh.plotting import figure, from_networkx, show, output_file

output_file('wiki_graph.html')

# Load the JSON file
with open('output.json', 'r') as f:
    node_data = json.load(f)

with open('../../dev/strikingloo.github.io/_site/graph_data.json') as f:
    names_data = json.load(f)

url_to_metadata = {item.get('url','')[6:] : {'title': item['title'], 'url': item.get('url','')} for item in names_data['data']}

print(url_to_metadata)
def get_title(name):
    return url_to_metadata[name]['title']

def get_url(name):
    return url_to_metadata[name]['url']
    
seen = {}
node_to_id = {}
node_id = 0
# Create a NetworkX graph from the JSON data
G = nx.Graph()
for node, _ in node_data.items():
    node_to_id[node] = node_id
    node_id+=1
    G.add_node(node_to_id[node], name = get_title(node), url = get_url(node))

for node, edges in node_data.items():
    for dest in edges:
        G.add_edge(node_to_id[node], node_to_id[dest])

print(G)

p = figure(tools="hover,pan,wheel_zoom,box_zoom,reset", tooltips="@name", width=720, height=720, x_axis_location=None, y_axis_location=None)
p.grid.grid_line_color = None

graph = from_networkx(G, nx.spring_layout, scale=30, center=(0,0))

# Add some new columns to the node renderer data source
graph.node_renderer.data_source.data['index'] = list(range(len(G)))
graph.node_renderer.data_source.data['colors'] = (Category20[20]*5)[:len(G)]
graph.node_renderer.glyph.update(size = 20, fill_color="colors")

p.renderers.append(graph)

show(p)
