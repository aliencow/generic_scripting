@cls
@echo off

rem check if a file is dropped over batch
:processFile
if "%~f1"=="" goto :endProcessingFiles

set inputFileName=%~nx1
REM set inputFileName=%~n1%~x1

set isValidVideoFile=0
if %~x1==.exr set isValidVideoFile=1
if %~x1==.EXR set isValidVideoFile=1

rem get de filename without extension
set paddingFilename=%~n1

rem cut last four characters (change for differente padding)
set withoutpadding=%paddingFilename:~0,-4%
rem get only last four characters (change for differente padding)
set padding=%paddingFilename:~-4%

rem check if padding is numeric
SET "numeric="&for /f "delims=0123456789" %%i in ("%padding%") do set numeric=%%i
rem if yes replace it with %04d else get the same filename
 if defined numeric (set result=%paddingFilename%) else (set result=%withoutpadding%%%04d)
rem append extension to name
set inputFileName=%result%.exr
echo inputFilename: %inputFileName%

pause

:endProcessingFiles
