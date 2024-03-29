import json
import threading
import time

def traverse_graph(graph, current_vertex):
    print(current_vertex)
    edges = graph[current_vertex]['edges']
    
    threads = []
    for vertex, wait_time in edges.items():
        t = threading.Thread(target=travel_to_vertex, args=(graph,vertex, wait_time))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def travel_to_vertex(graph, vertex, wait_time):
    time.sleep(wait_time)
    traverse_graph(graph, vertex)

def start_vertex(graph_json):
    graph = json.loads(graph_json)
    
    start_vertex = None
    for vertex, attrs in graph.items():
        if attrs.get('start', False):
            start_vertex = vertex
            break
    
    if start_vertex is None:
        print("Error: No start vertex found in the graph.")
    else:
        traverse_graph(graph, start_vertex)

if __name__ == "__main__":
    graph_json = '''
    {
        "A": {"start": true, "edges": {"B": 5, "C": 2}},
        "B": {"edges": {"D": 5}},
        "C": {"edges": {"E": 8}},
        "D": {"edges": {}},
        "E": {"edges": {}}
    }
    '''
    #this is meant to return an error
    example_1='''
    {
        "A": {"edges": {"B": 5, "C": 2}},
        "B": {"edges": {"D": 5}},
        "C": {"edges": {"E": 8}},
        "D": {"edges": {}},
        "E": {"edges": {}}
    }
    '''
    #this is meant to return an error
    example_2='''
    {}
    '''
    start_vertex(graph_json)
    start_vertex(example_1)
    start_vertex(example_2)

    

