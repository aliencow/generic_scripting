# Documentación sphinx

[Markdown to rst converter](https://github.com/miyakogi/m2r)

[Otra alternativa en web](https://cloudconvert.com/md-to-html)

## Installing

Create a virtualenv sphinxdocs (optional name)
In this case we use the structure of makevirtualenv wrapper.
```shell
C:\myfolder> mkvirtualenv sphinxdocs
C:\myfolder> workon sphinxdocs
(sphinxdocs)C:\myfolder>
```
Now we will install sphinx inside this virtualenv

```shell
(sphinxdocs)C:\myfolder> pip instal -U sphinx
```

## Setting up a project documentation

Go to the root folder of your project, if you had not active the environment activate it now.
```shell
C:\myrootProject> workon sphinxdocs
(sphinxdocs)C:\myrootProject>
```
Then create a folder named docs or whatever you want. Go to this new folder and run sphinx-quickstart:

```shell
(sphinxdocs)C:\myrootProject> mkdir docs
(sphinxdocs)C:\myrootProject> cd docs
(sphinxdocs)C:\myrootProject\docs> sphinx-quickstart
```

Next we are going to customize sphinx. The sphinx quickstart will ask us a series of questionsk, and based in our answers it will do the setup of documentation. You have a good reference in [this tutorial](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html):

In this other link you have [another starting tutorial](https://medium.com/@eikonomega/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365)
[Another point of view](https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/)


Is very important to separate build and source folders.

To check the rendering of .rst files check [this link](http://socrates.io)

## Info to document the chode for autodoc python files:

This is [A complete getting started](https://medium.com/@eikonomega/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365).
Here is [rst syntax for documentation](https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html).
And here [napoleon Support for NumPy and Google style docstrings](http://www.sphinx-doc.org/es/stable/ext/napoleon.html).

## How to separate de output folder

You can check in [here](https://stackoverflow.com/questions/16617347/separate-sphinx-build-and-source-directories-for-version-control).

## Path para la web sphinx

https://pipelinebuilder.antaruxa.com/
