# PipenvLib: A library for manipulating Pipenv projects.

This library exists to make it easy to programmatically interact with / introspect / manipulate [Pipenv](https://docs.pipenv.org) projects.

It allows you examine dependencies and requirements of a project, as well as install/uninstall packages from Python directly.


## Example Usage

```python
import pipenvlib

# Establish where the Pipenv project lives.
project = pipenvlib.PipenvProject('.')

```

```pycon
>>> project.packages
[<Dependency 'toml' constraint='*'>, <Dependency 'delegator.py' constraint='*'>]

>>> project.locked_packages
[<LockedDependency 'delegator.py==0.0.14'>, <LockedDependency 'pexpect==4.3.1'>, <LockedDependency 'ptyprocess==0.5.2'>, <LockedDependency 'toml==0.9.4'>]

>>> project.install('requests', dev=True)
True

>>> project.dev_packages
[<Dependency 'requests' constraint='*'>]

>>> project.virtualenv_location
/Volumes/KR/.local/share/virtualenvs/pipenvlib-kjpeBSWf

```

------------

This project (which is a work in progress) was built to facilitate the development of a Sublime Text 3 plugin (which in the works).
