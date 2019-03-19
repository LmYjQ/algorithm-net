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
    cmd = "rm -r {}".format(os.path.join(conf.path.neo4j_path,'data','databases','*.db'))
    cmd_proc(cmd)

def start_neo4j():
    cmd = "{}  start".format(os.path.join(conf.path.neo4j_path,'bin','neo4j'))
    cmd_proc(cmd)
    

def format_raw_file():
    print(conf.node.sheet_names,conf.edge.sheet_names)
    for conf_obj in [conf.node,conf.edge]: # conf = global conf; conf_obj = conf for node OR edge 
        for _type in conf_obj.sheet_names.split(','): 
            cypher = build_cypher(conf_obj,_type)
            print(cypher)

def split_save(conf_obj,sheet_name):
    in_path = os.path.join(conf.path.inpath,conf_obj.file_name)
    #print(in_path)
    df = pd.read_excel(in_path,sheet_name=sheet_name)
    out_path = os.path.join(conf.path.neo4j_path,'import',sheet_name)
    #print(out_path)
    df.to_csv(out_path,index=False,sep='\t')
    return df
  
def build_cypher(conf_obj,_type):
    sheet_name = _type.split(':')[0]
    df = split_save(conf_obj,sheet_name)
    cols = list(df.columns)
    if conf_obj.obj_type=='node':
        path = 'file:///{}'.format(sheet_name)
        nodes_def = ','.join(['{}:row.{}'.format(e,e) for e in cols])
        create = 'CREATE (:%s { %s })'%(sheet_name,nodes_def)
        return '''
               USING PERIODIC COMMIT
               LOAD CSV WITH HEADERS FROM '{}' AS row
               FIELDTERMINATOR '\\t'
               {}; '''.format(path, create)
    else:
        path = 'file:///{}'.format(sheet_name)
        #_type = extend:Model#model-EXTEND_TO-ModelExtend#model
        [n1,r,n2] = _type.split(':')[1].split('-')
        # type read by people, name read by neo4j        
        [node1_name,node2_name] = [e.split('#')[0] for e in [n1,n2]]
        [node1_type,node2_type] = [e.split('#')[1] for e in [n1,n2]]
        #[node_df1,node_df2] = [pd.read_csv(e,sep='\t') for e in [node1_name,node2_name]]
        match = '(a:%s {name: row.from_id}),(b:%s {name: row.to_id})' % (node1_type,node2_type)
        create = '(a)-[:%s {how: row.property} ]->(b)' % (r)
       # node1 = '(%s:%s {%s: row.from_id})' % (node1_name,node1_type,'name')
       # node2 = '(%s:%s {%s: row.to_id})' % (node2_name,node2_type,'name')
       # link = '(%s)-[r:%s]->(%s) ON CREATE SET r.how=row.property;' % (node1_name,r,node2_name)
        return '''
               USING PERIODIC COMMIT
               LOAD CSV WITH HEADERS FROM '{}' AS row
               FIELDTERMINATOR '\\t'
               MATCH {}
               CREATE {} ;'''.format(path,match,create)
 
def main():
    parser = argparse.ArgumentParser(description="bravo!")
    parser.add_argument('--conf_file','-c')
    parser.add_argument('--restart','-r')
    args = parser.parse_args() 
    conf_file = args.conf_file
    restart = args.restart 
    global conf
    conf = parse_config(conf_file)
    if restart:
        stop_neo4j()
        start_neo4j()
    format_raw_file()
    


if __name__=='__main__':
    main()

