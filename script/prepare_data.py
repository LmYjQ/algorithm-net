import pandas as pd
import argparse
import os,sys
from config import * 

def cmd_proc(cmd):
    print(cmd)
    os.system(cmd)

def stop_neo4j():
    cmd = "{}  stop".format(os.path.join(neo4j_path,'bin','neo4j'))
    cmd_proc(cmd)
    cmd = "rm {}".format(os.path.join(neo4j_path,'import','*'))
    cmd_proc(cmd)

def start_neo4j():
    pass

def format_raw_file():
    print(conf.node.sheet_names,conf.edge.sheet_names)
    nodes = [(conf.node.file_name,i) for i in conf.node.sheet_names.split(',')]
    edges = [(conf.edge.file_name,i) for i in conf.edge.sheet_names.split(',')]
    for tup in nodes+edges:
        in_path = os.path.join(conf.path.inpath,tup[0])
        print(in_path)
        df = pd.read_excel(in_path,sheet_name=tup[1])
        out_path = os.path.join(conf.path.neo4j_path,'import',tup[1])
        print(out_path)
        df.to_csv(out_path,index=False,sep='\t')



def main():
    conf_file = sys.argv[1]
    global conf
    conf = parse_config(conf_file)
    format_raw_file()
    


if __name__=='__main__':
    main()

