import pandas as pd
import argparse
import os,sys

sheet_names = []
inpath =  '/Users/maerkesu/Downloads/'
neo4j_path = '/Users/maerkesu/Downloads/neo4j-community-3.5.1' 

inpath = '/Users/a123/Downloads/'
neo4j_path = '/Users/a123/Downloads/neo4j-community-3.4.1'

def cmd_proc():
    print(cmd)
    os.system(cmd)

def stop_neo4j():
    cmd = "{}  stop".format(os.path.join(neo4j_path,'bin','neo4j'))
    cmd_proc(cmd)
    cmd = "rm {}".format(os.path.join(neo4j_path,'import','*')
    cmd_proc(cmd)

def format_raw_file(conf):
    df = pd.read_excel(path)


def main():
   # inpath = sys.argv[1]
   # out_folder = sys.argv[2]
    conf_file = sys.argv[1]
    
    


if __name__=='__main__':
    main()

