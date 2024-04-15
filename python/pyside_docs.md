# Some things about pyside



PySide2  Section
Installing pyside app with pyinstaller
https://www.learnpyqt.com/courses/packaging-and-distribution/packaging-pyqt5-pyside2-applications-windows-pyinstaller/

Setting stylesheets to Pyside
https://stackoverflow.com/questions/48256772/dark-theme-for-qt-widgets

Sample tutorial PySide2
https://codeloop.org/python-tutorial-create-messagebox-with-pyside2/

''' label con imagen en PySide2
https://www.learnpyqt.com/blog/adding-images-to-pyqt5-applications/
https://stackoverflow.com/questions/50209879/how-to-load-an-image-with-qlabel-in-pyside2
'''
Events and Signals in PySide
http://zetcode.com/gui/pysidetutorial/eventsandsignals/
https://www.pythoncentral.io/pysidepyqt-tutorial-creating-your-own-signals-and-slots/


Drawing in PySide
http://zetcode.com/gui/pysidetutorial/drawing/
https://gist.github.com/Alquimista/1274149/ca37e497b3f2a16c9d3ec4889ed63c80986e9dba berzier curves.
https://github.com/eyllanesc/stackoverflow/tree/master/questions/46142167 conected nodes
https://doc.qt.io/qtforpython/overviews/graphicsview.html graphicsview framework

Sintaxis path SVG
https://css-tricks.com/svg-path-syntax-illustrated-guide/


### Trabajar con ventanas en wsl y ejecutar pyside

Es necesario instalar VcXsrv server. https://sourceforge.net/projects/vcxsrv/ para servir xwindows.
Tutorial para ejecutar gui apps en wsl  https://techcommunity.microsoft.com/t5/modern-work-app-consult-blog/running-wsl-gui-apps-on-windows-10/ba-p/1493242
Tutorial para trabajar con Pyside desde wsl https://www.appsloveworld.com/python/1235/wsl2-and-pyside6


1. X Server https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242

    1. Install https://sourceforge.net/projects/vcxsrv/

    2. ```export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0" ``` 
    3. Run `xev` to test image

    4. Include the command ii at the end of the `/etc/bash.bashrc` file:

2. ```sudo apt install pyside2-tools libopengl-dev```

3. Run python3 xxx.py it worked but still has some problem. output:

```bash
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-dev'
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
```



