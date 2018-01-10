import os

import toml
import delegator


class Dependency(object):
    """A Dependency."""
    def __init__(self, name, constraint, locked=False):
        self.name = name
        self.constraint = constraint
        self.locked = locked


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

    @property
    def packages(self):
        pass

    @property
    def dev_packages(self):
        pass

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




