import pandas as pd
import argparse
import os,sys
from config import * 

def cmd_proc(cmd):
    print(cmd)
    os.system(cmd)

def stop_neo4j():
    cmd = "{}  stop".format(os.path.join(conf.path.neo4j_path,'bin','neo4j'))
    cmd_proc(cmd)
    cmd = "rm -r {}".format(os.path.join(conf.path.neo4j_path,'data','databases','graph.db'))
    cmd_proc(cmd)

def start_neo4j():
    cmd = "{}  start".format(os.path.join(conf.path.neo4j_path,'bin','neo4j'))
    cmd_proc(cmd)
    

def format_raw_file():
    print(conf.node.sheet_names,conf.edge.sheet_names)
    nodes = [(conf.node.file_name,i,'node') for i in conf.node.sheet_names.split(',')]
    edges = [(conf.edge.file_name,i,'edge') for i in conf.edge.sheet_names.split(',')]
    for tup in nodes+edges:
        in_path = os.path.join(conf.path.inpath,tup[0])
        #print(in_path)
        df = pd.read_excel(in_path,sheet_name=tup[1])
        out_path = os.path.join(conf.path.neo4j_path,'import',tup[1])
        print(out_path)
        df.to_csv(out_path,index=False,sep='\t')
        cypher = build_cypher(out_path,tup[2])        
        print(cypher)

def build_cypher(out_path, obj_type):
    name = out_path.split('/')[-1]
    df = pd.read_csv(out_path,sep='\t')
    cols = list(df.columns)
    if obj_type=='node':
        path = 'file:///{}'.format(name)
        nodes_def = ','.join(['{}:row.{}'.format(e,e) for e in cols])
        create = 'CREATE (:%s { %s });'%(name,nodes_def)
        return '''
               USING PERIODIC COMMIT
               LOAD CSV WITH HEADERS FROM '{}' AS row
               {} '''.format(path, create)
    else:
        path = 'file:///{}'.format(name)
        node1 = ''
        node2 = ''
        link = ''
        return '''
               USING PERIODIC COMMIT
               LOAD CSV WITH HEADERS FROM '{}' AS row
               MATCH {}
               MATCH {}
               MERGE {} '''.format(path,node1,node2,link)
 



def main():
    conf_file = sys.argv[1]
    global conf
    conf = parse_config(conf_file)
#    stop_neo4j()
    format_raw_file()
#    start_neo4j()
    


if __name__=='__main__':
    main()

