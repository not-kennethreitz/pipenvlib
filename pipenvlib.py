import os
import json

import toml
import delegator


class Dependency(object):
    """A Dependency."""

    def __init__(self, name, constraint, locked=False):
        self.name = name
        self.constraint = constraint
        self.locked = locked

    def __repr__(self):
        return "<Depedency '{0}' constraint='{1}'>".format(
            self.name, self.constraint
        )


class LockedDependency(object):
    """A Locked Dependency"""
    def __init__(self, name, constraint, hashes):
        self.name = name
        self.constraint = constraint
        self.hashes = hashes

    def __repr__(self):
        return "<LockedDepedency '{0}{1}'>".format(
            self.name, self.constraint
        )

class Requirement(object):
    """A Requirement."""

    def __init__(self, name, constraint):
        self.name = name
        self.constraint = constraint

    def __repr__(self):
        return "<Requirement '{0}' constraint='{1}'>".format(
            self.name, self.constraint
        )


class PipenvProject(object):
    """A Pipenv project."""

    def __init__(self, home, pipfile='Pipfile'):
        self.home = home
        self.pipfile = pipfile

        # Assert that the Pipfile exists.
        self.assert_has_pipfile()

    @property
    def _pipfile_path(self):
        return os.path.sep.join([self.home, self.pipfile])

    @property
    def _lockfile_path(self):
        return os.path.sep.join([self.home, '{0}.lock'.format(self.pipfile)])

    def assert_has_pipfile(self):
        """Asserts that the Pipfile exists."""
        assert os.path.isfile(self._pipfile_path)

    def assert_has_lockfile(self):
        """Asserts that the Pipfile.lock exists."""
        assert os.path.isfile(self._pipfile_path)

    @property
    def lockfile_is_latest(self):
        pass

    def _get_section_of_pipfile(self, section, target):
        def gen():
            pipfile = toml.load(self._pipfile_path)
            for package in pipfile[section]:
                name = package
                constraint = pipfile[section][package]
                yield target(name, constraint)

        return [p for p in gen()]

    @property
    def packages(self):
        """Returns a list of Dependency objects (for [packages]) for
        the Pipenv project.
        """
        return self._get_section_of_pipfile('packages', Dependency)

    @property
    def dev_packages(self):
        """Returns a list of Dependency objects (for [dev-packages]) for
        the Pipenv project.
        """
        return self._get_section_of_pipfile('dev-packages', Dependency)

    @property
    def requires(self):
        """Returns a list of Requirement objects for the Pipenv project.
        """
        return self._get_section_of_pipfile('requires', Requirement)

    @property
    def locked_packages(self):
        """Returns a list of LockedDependency objects for the Pipenv
        project.
        """
        self.assert_has_lockfile()

        def gen():
            with open(self._lockfile_path) as f:
                lockfile = json.load(f)

            for package in lockfile['default']:
                name = package
                constraint = lockfile['default'][package]['version']
                hashes = lockfile['default'][package]['hashes']

                yield LockedDependency(name, constraint, hashes)

        return [l for l in gen()]

    @property
    def locked_dev_packages(self):
        """Returns a list of LockedDependency objects for the Pipenv
        project.
        """
        self.assert_has_lockfile()

        def gen():
            with open(self._lockfile_path) as f:
                lockfile = json.load(f)

            for package in lockfile['develop']:
                name = package
                constraint = lockfile['develop'][package]['version']
                hashes = lockfile['develop'][package]['hashes']

                yield LockedDependency(name, constraint, hashes)

        return [l for l in gen()]

    @property
    def locked_requirements(self):
        """Returns a list of Requirement objects for the Pipenv
        project, from the Pipfile.lock.
        """
        self.assert_has_lockfile()

        def gen():
            with open(self._lockfile_path) as f:
                lockfile = json.load(f)

            for require in lockfile['_meta']['requires']:
                name = require
                constraint = lockfile['_meta']['requires'][require]

                yield Requirement(name, constraint)

        return [l for l in gen()]

    def _assert_pipenv_is_installed(self):
        pass

    def _run(self, cmd):
        """Run a Pipenv command for the Pipenv project.."""
        return delegator.run('pipenv {0}'.format(cmd), cwd=self.home)

    def install(self, package_name, constraint=None, dev=False):
        """Installs a given package to the Pipenv project."""
        # If no constraint was

        if constraint is not None:
            # Append the constraint to the package name.
            package_name = 'package_name{0}'.format(constraint)

        dev = '' if not dev else '--dev'

        return self._run('install {0} {1}'.format(package_name)).return_code == 0

    def uninstall(self, package_name):
        """Uninstalls a given package from the pipenv project."""

        return self._run('uninstall {0}'.format(package_name)).return_code == 0

    @property
    def virtualenv_location(self):
        # return self._
        pass

    # @property
    # def site_packages_location(self):
    #     pass

    # @property
    # def python_home_location(self):
    #     pass




