Documentación sphinx
====================

`Markdown to rst converter <https://github.com/miyakogi/m2r>`__

`Otra alternativa en web <https://cloudconvert.com/md-to-html>`__

Installing
----------

Create a virtualenv sphinxdocs (optional name) In this case we use the
structure of makevirtualenv wrapper.

.. code:: shell

    C:\myfolder> mkvirtualenv sphinxdocs
    C:\myfolder> workon sphinxdocs
    (sphinxdocs)C:\myfolder>

Now we will install sphinx inside this virtualenv

.. code:: shell

    (sphinxdocs)C:\myfolder> pip instal -U sphinx

Setting up a project documentation
----------------------------------

Go to the root folder of your project, if you had not active the
environment activate it now.

.. code:: shell

    C:\myrootProject> workon sphinxdocs
    (sphinxdocs)C:\myrootProject>

Then create a folder named docs or whatever you want. Go to this new
folder and run sphinx-quickstart:

.. code:: shell

    (sphinxdocs)C:\myrootProject> mkdir docs
    (sphinxdocs)C:\myrootProject> cd docs
    (sphinxdocs)C:\myrootProject\docs> sphinx-quickstart

Next we are going to customize sphinx. The sphinx quickstart will ask us
a series of questionsk, and based in our answers it will do the setup of
documentation. You have a good reference in `this
tutorial <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`__:

In this other link you have `another starting
tutorial <https://medium.com/@eikonomega/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365>`__
`Another point of
view <https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/>`__

Is very important to separate build and source folders.

To check the rendering of .rst files check `this
link <http://socrates.io>`__

Info to document the chode for autodoc python files:
----------------------------------------------------

This is `A complete getting
started <https://medium.com/@eikonomega/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365>`__.
Here is `rst syntax for
documentation <https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>`__.
And here `napoleon Support for NumPy and Google style
docstrings <http://www.sphinx-doc.org/es/stable/ext/napoleon.html>`__.

How to separate de output folder
--------------------------------

You can check in
`here <https://stackoverflow.com/questions/16617347/separate-sphinx-build-and-source-directories-for-version-control>`__.

Path para la web sphinx
-----------------------

https://pipelinebuilder.antaruxa.com/
