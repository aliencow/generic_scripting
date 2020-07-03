@echo off
rem check de use of % symbol in vars
set kk=%%.0001
echo kk:
echo kk: %kk%
set kk2=prueba.%kk%
echo kk2: %kk2%
endlocal

rem test padding numerical
set "paddingFilename=C:\Users\testing\AppData\Local\Test\abc123\643456\VSALBT81_COM.0123"
rem set paddingFilename=%paddingFilename:~0,-4%
echo paddingfrom: %paddingFilename%

set withoutpadding=%paddingFilename:~0,-4%
set padding=%paddingFilename:~-4%

SET "numeric="&for /f "delims=0123456789" %%i in ("%padding%") do set numeric=%%i
echo var: %numeric%
if defined numeric (set result=%paddingFilename%) else (set result=%withoutpadding%%%04d)
echo result: %result%
