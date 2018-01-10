import pipenvlib

p = pipenvlib.PipenvProject('.')
print(p.lockfile_is_latest)