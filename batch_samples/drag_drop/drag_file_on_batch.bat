@echo off

rem Ejemplo de las nomenclaturas cuando se hade drag drop sobre un batch

cls

echo fully qualified name %~f1

echo drive %~d1

echo path %~p1

echo filename %~n1

echo file extension %~x1

echo short filename %~sn1

echo short file extension %~sx1

echo drive and directory %~dp1

echo filename and extension %~nx1

pause
