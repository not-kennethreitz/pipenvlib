# PipenvLib: A library for manipulating Pipenv projects.

This library exists to make it easy to programatically interact with / introspect / manipulate Pipenv projects.

It allows you examine depenencies and requirements of a project, as well as install/uninstall packages from Python directly.


## Example Usage

```python
import pipenvlib

# Establish where the Pipenv project lives.
project = pipenvlib.PipenvProject('.')

```

```pycon
>>> project.packages
[<Depedency 'toml' constraint='*'>, <Depedency 'delegator.py' constraint='*'>]

>>> project.locked_packages
[<LockedDepedency 'delegator.py==0.0.14'>, <LockedDepedency 'pexpect==4.3.1'>, <LockedDepedency 'ptyprocess==0.5.2'>, <LockedDepedency 'toml==0.9.4'>]

>>> project.install('requests', dev=True)
True

>>> project.dev_packages
[<Depedency 'requests' constraint='*'>]
```

------------

This project (which is a work in progress) was built to facilitate the development of a Sublime Text 3 plugin (which in the works).
