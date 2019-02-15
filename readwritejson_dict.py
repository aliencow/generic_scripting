import json
import os




def readJSONfile(filename):
    """
    Devuelve una variable dictionary (content)
    cargada con el contenido del JSON referenciado en filename
    """
    content = {}
    with open(filename) as json_file:
        content = json.load(json_file)
        json_file.close()
    return content


def writeJSONfile(filename, content):
    """
    Escribe el contenido de una variable dictionary (content)
    en el fichero JSON referenciado en filename
    """
    with open(filename, 'w') as json_file:
        json.dump(content , json_file, indent=4)
        json_file.close()


config = readJSONfile('config_file.json')

for clave, valor in sorted(config.items()):
    valor['VERSION'] = 'VVVV'
"""
    ep109 = config['EP109']
    ep109['VERSION'] = 'b001'
    config['EP109'] = ep109
"""

writeJSONfile('config_fileb.json', config)
