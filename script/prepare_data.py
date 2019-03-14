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

def format_raw_file():
    print(conf.node.sheet_names,conf.edge.sheet_names)
    nodes = [(conf.node.file_name,i) for i in conf.node.sheet_names.split(',')]
    edges = [(conf.edge.file_name,i) for i in conf.edge.sheet_names.split(',')]
    print(nodes,edges)
    #df = pd.read_excel(conf.path.inpath)


def main():
    conf_file = sys.argv[1]
    global conf
    conf = parse_config(conf_file)
    print(conf)
    format_raw_file()
    


if __name__=='__main__':
    main()

