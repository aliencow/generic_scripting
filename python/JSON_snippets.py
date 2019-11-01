# -*- coding: utf-8 -*-
# json validator https://codebeautify.org/jsonvalidator

import json
import os

"""
                    _    _                         _ _   _          ___ _____  _____ _   _               _                  _
                   | |  (_)                       (_) | | |        |_  /  ___||  _  | \ | |             (_)                | |
__      _____  _ __| | ___ _ __   __ _   __      ___| |_| |__        | \ `--. | | | |  \| |    ___ _ __  _ _ __  _ __   ___| |_ ___
\ \ /\ / / _ \| '__| |/ / | '_ \ / _` |  \ \ /\ / / | __| '_ \       | |`--. \| | | | . ` |   / __| '_ \| | '_ \| '_ \ / _ \ __/ __|
 \ V  V / (_) | |  |   <| | | | | (_| |   \ V  V /| | |_| | | |  /\__/ /\__/ /\ \_/ / |\  |   \__ \ | | | | |_) | |_) |  __/ |_\__ \
  \_/\_/ \___/|_|  |_|\_\_|_| |_|\__, |    \_/\_/ |_|\__|_| |_|  \____/\____/  \___/\_| \_/   |___/_| |_|_| .__/| .__/ \___|\__|___/
                                  __/ |                                                                   | |   | |
                                 |___/                                                                    |_|   |_|

los fonts estan aquí:	http://patorjk.com/software/taag/#p=display&f=Doom&t=Ejemplo%20tipografia%20ASCII

"""


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



## Funciones para escribir leer y tratar ficheros JSON
# la primera es pasar el path a un fichero JSON
# more about in https://stackoverflow.com/questions/25226208/represent-directory-tree-as-json
""" Represent directory tree as JSON
como en este ejemplo:

{
  "type": "directory",
  "name": "hello",
  "children": [
    {
      "type": "directory",
      "name": "world",
      "children": [
        {
          "type": "file",
          "name": "one.txt"
        },
        {
          "type": "file",
          "name": "two.txt"
        }
      ]
    },
    {
      "type": "file",
      "name": "README"
    }
  ]
}

"""
import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

print json.dumps(path_to_dict('.'))

decoded = json.loads(data_string)


""" Volcar una varible json a fichero

Writing JSON to a File
"""
#more about in https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


""" Ejemplo con JSON identado
"""
import json

d = {'one': 1, 'group': [4,9,7]}
print json.dumps(d, indent=4, sort_keys=True)

"""
will output:

   {
        "one": 1,
            "group": [
            4,
            9,
            7
        ]
    }
"""
