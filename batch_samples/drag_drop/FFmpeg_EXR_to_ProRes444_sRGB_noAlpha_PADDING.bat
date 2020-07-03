rem PMP_converter.bat
rem
rem Version 1.0
rem This allows drag-and-drop conversion of video files into an PMP official format videos
rem
rem USAGE
rem Simply drag one or more AVI/MOV/FLV/MP4 files onto this batch file
rem
rem If you want you can make a shortcut to this batch file
rem and drag to that shortcut if you prefer.
rem
rem Tested in Windows 7 and 10
rem Tested with ffmpeg version N-91141


@cls
@echo off

:processFile
if "%~f1"=="" goto :endProcessingFiles

set inputFileName=%~nx1
REM set inputFileName=%~n1%~x1

set isValidVideoFile=0
if %~x1==.exr set isValidVideoFile=1
if %~x1==.EXR set isValidVideoFile=1

set paddingFilename=%~n1
set withoutpadding=%paddingFilename:~0,-4%
set padding=%paddingFilename:~-4%

SET "numeric="&for /f "delims=0123456789" %%i in ("%padding%") do set numeric=%%i
if defined numeric (set result=%paddingFilename%) else (set result=%withoutpadding%%%04d)
set inputFileName=%result%.exr
echo inputFilename: %inputFileName%

echo PMP Video Converter

cd /D "%~dp1"

echo Input File: %inputFileName%
if %isValidVideoFile%==1 (
    set outputFileName="%~n1_converted.mov"
    if not exist !outputFileName! (
        echo Cropping...
REM        \\argonte\pipeline\config\bin\ffmpeg\bin\ffmpeg.exe -i "%inputFileName%"  -vf "crop=in_w:in_w*9/16,scale=1920x1080:flags=lanczos" -sws_flags bilinear -vcodec h264 "%~n1_converted.mov"
		\\argonte\pipeline\config\bin\ffmpeg\bin\ffmpeg.exe -apply_trc iec61966_2_1 -framerate 24 -f image2 -start_number 0001 -i "%inputFileName%" -r 24 -y -vf "zscale=matrix=709:transferin=709:transfer=709:primariesin=709:primaries=709" -f mov -vcodec prores_ks -pix_fmt yuva444p10le -profile:v 4444 -vendor ap10 -vtag ap4h -strict -2 "%~n1_converted.mov"
echo		\\argonte\pipeline\config\bin\ffmpeg\bin\ffmpeg.exe -apply_trc iec61966_2_1 -framerate 24 -f image2 -start_number 0001 -i "%inputFileName%" -r 24 -y -vf "zscale=matrix=709:transferin=709:transfer=709:primariesin=709:primaries=709" -f mov -vcodec prores_ks -pix_fmt yuva444p10le -profile:v 4444 -vendor ap10 -vtag ap4h -strict -2 "%~n1_converted.mov"
		pause
    ) else (
        echo SKIPPING FILE - %inputFileName%
        echo !outputFileName! already exists.
    )
) else (
    echo Not valid video for convert, are you sure that is a video file?,  [mov mp4 avi flv]
    set outputFileName=%inputFileName%
)

shift
goto :processFile


shift
echo EXITING - All files processed.
echo.

pause

goto:eof
