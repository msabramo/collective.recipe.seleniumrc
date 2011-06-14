from setuptools import setup, find_packages
import os

name = "collective.recipe.seleniumrc"
version = '0.6dev'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description=(
        read('README.txt')
        + '\n' +
'''\
Contributors
============

''' +
        read('CONTRIBUTORS.txt').replace('\n', '\n\n') +
        '\n' +
        read('CHANGES.txt')
        )

file('doc.txt', 'w').write(long_description)

setup(
    name = name,
    version = version,
    author = "Jordan Baker",
    author_email = "jbb@scryent.com",
    description = "zc.buildout recipe for installing the Selenium RC distribution.",
    long_description = long_description,
    license = "ZPL 2.1",
    keywords = "buildout recipe",
    url = 'http://svn.plone.org/svn/collective/buildout/' + name,
    classifiers = [
      'Framework :: Buildout',
      'Topic :: Software Development :: Build Tools',
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data = True,
    namespace_packages = ['collective', 'collective.recipe'],
    install_requires = ['zc.buildout', 'setuptools', 'hexagonit.recipe.download'],
    dependency_links = ['http://download.zope.org/distribution/'],
    entry_points = {'zc.buildout': ['default = %s:Recipe' % name]},
)
