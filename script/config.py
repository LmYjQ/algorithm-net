import sys,os
import yaml

class DottableDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self

    def allowDotting(self, state=True):
        if state:
            self.__dict__ = self
        else:
            self.__dict__ = dict()

def parse_config(yaml_file):
    """
    parse yaml config
        :param yaml_file:
    """
    if not os.path.exists(yaml_file):
        raise FileNotFoundError()

    with open(yaml_file, 'r') as data:
        _config = yaml.load(data)
        for k, v in _config.items():
            if isinstance(v, dict):
                _config[k] = DottableDict(v)
        config = DottableDict(_config)
        #parse_data_conf_part(config.data)
        #parse_feature_conf_part(config.feature)
        
        return config

if __name__=='__main__':
    path = sys.argv[1]
    conf = parse_config(path)
    print(conf)
