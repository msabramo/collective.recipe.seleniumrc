*******************************
Download recipe for Selenium RC
*******************************

This package downloads and installs Selenium RC using zc.buildout. It is based
on hexagonit.recipe.download.

buildout.cfg example::

  [buildout]
  parts = seleniumrc

  [seleniumrc]
  recipe = collective.recipe.seleniumrc

A control script will be created based on the part name. In this case a
control script will be created in bin/seleniumrc

You may also be interested in the selenium module for Python which allows you
to control Selenium RC.

  http://pypi.python.org/pypi/selenium

You can also choose the exact version of Selenium RC to be used::

  [buildout]
  parts = seleniumrc

  [seleniumrc]
  recipe = collective.recipe.seleniumrc
  url = http://selenium.googlecode.com/files/selenium-remote-control-1.0.3.zip
  md5sum = 8935cc7fe4dde2fd2a95ddd818e7493b

Sometimes you may want to use another Java executable::

  [buildout]
  parts = seleniumrc

  [seleniumrc]
  recipe = collective.recipe.seleniumrc
  java-cmd = /home/www/java/bin/java

To suppress all default values (e.g., to install without verifying the MD5
checksum), use the 'no-defaults' option::

  [buildout]
  parts = seleniumrc

  [seleniumrc]
  recipe = collective.recipe.seleniumrc
  url = http://selenium.googlecode.com/files/selenium-remote-control-1.0.3.zip
  java-cmd = /home/www/java/bin/java

License
-------

Open Source License - Zope Public License v2.1
