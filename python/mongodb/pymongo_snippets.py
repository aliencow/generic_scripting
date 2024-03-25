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


""" How to connect to your remote MongoDB server:  https://ianlondon.github.io/blog/mongodb-auth/
"""

"""
______                                                                                                      _
| ___ \                                                                                                    (_)
| |_/ /   _ _ __ ___   ___  _ __   __ _  ___    ______   _ __ ___   ___  _ __   __ _  ___   ___ _ __   __ _ _ _ __   ___
|  __/ | | | '_ ` _ \ / _ \| '_ \ / _` |/ _ \  |______| | '_ ` _ \ / _ \| '_ \ / _` |/ _ \ / _ \ '_ \ / _` | | '_ \ / _ \
| |  | |_| | | | | | | (_) | | | | (_| | (_) |          | | | | | | (_) | | | | (_| | (_) |  __/ | | | (_| | | | | |  __/
\_|   \__, |_| |_| |_|\___/|_| |_|\__, |\___/           |_| |_| |_|\___/|_| |_|\__, |\___/ \___|_| |_|\__, |_|_| |_|\___|
       __/ |                       __/ |                                        __/ |                  __/ |
      |___/                       |___/                                        |___/                  |___/

"""

""" Definiendo base de datos en mongoengine: http://docs.mongoengine.org/guide/defining-documents.html#defining-a-document-s-schema
"""

""" References may be stored to other documents in the database using the ReferenceField.
    Pass in another document class as the first argument to the constructor, then simply
    assign document objects to the field:
"""

class User(Document):
    name = StringField()

class Page(Document):
    content = StringField()
    author = ReferenceField(User)

john = User(name="John Smith")
john.save()

post = Page(content="Test Page")
post.author = john
post.save()

""" The User object is automatically turned into a reference behind the scenes,
    and dereferenced when the Page object is retrieved.

    To add a ReferenceField that references the document being defined, use the string 'self'
    in place of the document class as the argument to ReferenceField‘s constructor.
    To reference a document that has not yet been defined, use the name of the undefined document
    as the constructor’s argument:
"""

class Employee(Document):
    name = StringField()
    boss = ReferenceField('self')
    profile_page = ReferenceField('ProfilePage')

class ProfilePage(Document):
    content = StringField()


