import json

with open('graph base.graph') as f:
    data = json.load(f)

    vertices = data['vertices']

    print(data['vertices'])
    print(data['edges'])

    print('---')

    for edge in data['edges']:
        # print(edge['vertex1'], vertices[edge['vertex1']]['name'], edge['vertex2'], vertices[edge['vertex2']]['name'], edge)
        print(vertices[edge['vertex1']]['name'], vertices[edge['vertex2']]['name'])
