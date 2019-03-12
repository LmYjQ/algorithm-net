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

def get_data():


def main():
   # inpath = sys.argv[1]
   # out_folder = sys.argv[2]
    df = pd.read_excel(inpath)
    


if __name__=='__main__':
    main()

