"""
______                                             ___  ___                            _ _
| ___ \                                            |  \/  |                           | | |
| |_/ /   _ _ __ ___   ___  _ __   __ _  ___       | .  . | ___  _ __   __ _  ___   __| | |__
|  __/ | | | '_ ` _ \ / _ \| '_ \ / _` |/ _ \      | |\/| |/ _ \| '_ \ / _` |/ _ \ / _` | '_ \
| |  | |_| | | | | | | (_) | | | | (_| | (_) |  _  | |  | | (_) | | | | (_| | (_) | (_| | |_) |
\_|   \__, |_| |_| |_|\___/|_| |_|\__, |\___/  (_) \_|  |_/\___/|_| |_|\__, |\___/ \__,_|_.__/
       __/ |                       __/ |                                __/ |
      |___/                       |___/                                |___/

los fonts estan aquí:	http://patorjk.com/software/taag/#p=display&f=Doom&t=Ejemplo%20tipografia%20ASCII

"""

""" Insertar un registro con referencia a otro registro..
"""
oid = ObjectId()
db.country.insert({ _id: oid, code : 1, name: 'Brasil' });
db.state.insert({ code : 1, state: 'SC', country: oid });
