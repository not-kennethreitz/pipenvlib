import os

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
        return self._get_section_of_pipfile('packages', Dependency)

    @property
    def dev_packages(self):
        return self._get_section_of_pipfile('dev-packages', Dependency)

    @property
    def requires(self):
        return self._get_section_of_pipfile('requires', Requirement)

    @property
    def locked_packages(self):
        pass

    @property
    def locked_dev_packages(self):
        pass

    def _assert_pipenv_is_installed(self):
        pass

    def _run(self, cmd):
        """Run a Pipenv command."""
        pass

    def install(package_name):
        pass

    def uninstall(package_name):
        pass

    @property
    def virtualenv_location(self):
        pass

    # @property
    # def site_packages_location(self):
    #     pass

    # @property
    # def python_home_location(self):
    #     pass




