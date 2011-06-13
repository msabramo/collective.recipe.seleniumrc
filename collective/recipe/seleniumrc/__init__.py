import os, shutil, tempfile, urllib2, urlparse
import setuptools.archive_util
import pkg_resources
import ConfigParser
import hexagonit.recipe.download
import stat

def string2version(s):
    l = s.split('-')
    goodindex = -1
    for (index, part) in enumerate(l):
        if like_a_version(part):
            goodindex = index
            break
          
    assert goodindex >= 0, "Did not find a version string."
    return '-'.join(l[goodindex:])

def like_a_version(s):
    def _all(things): # for Python 2.4 compatibility
        return reduce(lambda thing1, thing2: thing1 and thing2, things)
    return _all([c in '0123456789.' for c in s])


class Recipe(hexagonit.recipe.download.Recipe):
    def __init__(self, buildout, name, options):
        if options.get('no-defaults') is None:
            # Copy configuration set in defaults.cfg to our options namespace,
            # but only if the user hasn't disabled it.
            config_file = pkg_resources.resource_stream(__name__,
                                                        "defaults.cfg")
            config = ConfigParser.ConfigParser()
            config.readfp(config_file)
            for key, value in config.items("seleniumrc"):
                options.setdefault(key, value)

        super(Recipe, self).__init__(buildout, name, options)

        options['location'] = os.path.join(
            buildout['buildout']['parts-directory'],
            self.name)
        self.url = options['url']

    def calculate_base(self, extract_dir):
        names = os.listdir(extract_dir)
        for selrcdir in names:
            if selrcdir.startswith('selenium-server'):
                return os.path.join(extract_dir, selrcdir)
                break
        else:
            version = string2version(names[0])
            return os.path.join(
                extract_dir, selrcdir, 'selenium-server-%s' % version)

    def install_wrapper(self):
        ctl_path = os.path.join(self.buildout["buildout"]["bin-directory"],
                                self.name)
        open(ctl_path, "w").write(pkg_resources.resource_string(__name__, "seleniumrc_ctl.in") % self.options)
        os.chmod(ctl_path, (os.stat(ctl_path).st_mode |
                            stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
                                        
    def install(self):
        parts = super(Recipe, self).install()
        self.install_wrapper()
        return parts
        
    def update(self):
        parts = super(Recipe, self).update()
        self.install_wrapper()
        return parts
