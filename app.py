# coding=utf-8
from flask import Flask, jsonify, render_template
from py2neo import Graph

app = Flask(__name__)
graph = Graph(
     host = "localhost", # neo4j 搭载服务器的ip地址，ifconfig可获取到
    http_port = 7474, # neo4j 服务器监听的端口号  
    user = "neo4j", # 数据库user name，如果没有更改过，应该是neo4j
    password = "qiyu" # 自己设定的密码
)

# def buildNodes(nodeRecord):
#     data = {"id": str(nodeRecord.n._id), "label": next(iter(nodeRecord.n.labels))}
#     data.update(nodeRecord.n.properties)

#     return {"data": data}

# def buildEdges(relationRecord):
#     data = {"source": str(relationRecord.r.start_node._id), 
#             "target": str(relationRecord.r.end_node._id),
#             "relationship": relationRecord.r.rel.type}
#     return {"data": data}

def build_node(index,n):
    d = dict(zip(n['n'].keys(),n['n'].values()))
    d.update({"id":str(n['n'].identity)})
    d.update({"label":str(n['n'].labels)[1:]})
    return {"data": d}

def build_edge(r):
    d={
    "source": r['r'].start_node.identity,
    "target": r['r'].end_node.identity,
    "relationship":list(r['r'].relationships[0].types())[0]}
    return {"data":d}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def get_graph():
    nodes = graph.run('MATCH (n) RETURN n').data()
    edges = graph.run('MATCH ()-[r]->() RETURN r').data() 

    return jsonify(elements = {"nodes": [build_node(index,n) for index, n in enumerate(nodes)],
                                 "edges": [build_edge(r) for r in edges]})    

if __name__ == '__main__':
    app.run(debug = True)