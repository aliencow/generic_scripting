@echo off

REM Para el setup de las librerias y startup en vbs  solo para el estudio
F:
cd F:\pipeline\config\lib\vbs\tools\vbsjson
git pull
cd F:\pipeline\config\setup\startup
git pull
cd F:\pipeline\config\lib\vbs\studio
git pull

rem custom plugins
F:
cd F:\pipeline\config\tools\studio\maya\QAntaruxa
git pull
cd F:\pipeline\config\tools\studio\maya\skin_bones
git pull

rem valentina
F:
cd F:\pipeline\config\tools\projects\ved\maya
git pull
rem concatenator update versions etc
cd F:\pipeline\config\tools\projects\ved\out_of_maya
git pull

rem grisu
F:
cd F:\pipeline\config\tools\projects\grs\maya\grs_tools
git pull


rem pipeline
F:
cd F:\pipeline\config\lib\python\studio\nomen
git pull
cd F:\pipeline\config\lib\python\studio\pipeline
git pull
cd F:\pipeline\config\lib\python\studio\treelib
git pull

rem common libs
F:
cd F:\pipeline\config\lib\python\studio\maya
git pull
cd F:\pipeline\config\lib\python\studio\shotgun
git pull
cd F:\pipeline\config\lib\python\studio\logger
git pull
cd F:\pipeline\config\lib\python\studio\deadline
git pull
cd F:\pipeline\config\lib\python\studio\sysutils
git pull
