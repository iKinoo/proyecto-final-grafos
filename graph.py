import json
import networkx as nx
import matplotlib.pyplot as plt

data = json.load(open("response.json", "r"))

graph = nx.Graph()


for issue in data["data"]["repository"]["issues"]["nodes"]:
    graph.add_node(issue["number"], title=issue["title"])
    print(issue["title"])
    print("\t\t Referenced by:")
    for referenced_issue in issue["timelineItems"]["nodes"]:
        try:
            graph.add_edge(issue["number"], referenced_issue["source"]["number"])
            print("\t\t\t", referenced_issue["source"]["number"])
            graph.add_edge(issue["number"], referenced_issue["source"]["number"])
        except: 
            pass
            
            
nx.draw(graph, with_labels=True)