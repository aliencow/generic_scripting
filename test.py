import base64
print "icon='''\\\n" + base64.encodestring(open("./resources/flecha_close.gif", "rb").read(  )) + "'''"
