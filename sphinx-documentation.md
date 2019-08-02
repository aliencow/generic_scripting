# Documentación sphinx

## Installing

Create a virtualenv sphinxdocs (optional name)
In this case we use the structure of makevirtualenv wrapper.
```shell
$ mkviertualenv sphinxdocs
$ workon sphinxdocs
(sphinxdocs) $
```
Now we will install sphinx inside this virtualenv

```shell
(sphinxdocs) $ pip instal -U sphinx
```

## Setting up a project documentation

Go to the root folder of your project, if you had not active the environment activate it now.
```shell
C:\myrootProject> workon sphinxdocs
(sphinxdocs)C:\myrootProject>
```
Then create a folder named docs or whatever you want.
then from your project folder run sphinx-quickstart

```shell
(sphinxdocs)C:\myrootProject> mkdir docs
(sphinxdocs)C:\myrootProject> sphinx-quickstart
```
