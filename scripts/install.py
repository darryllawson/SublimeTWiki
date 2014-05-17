#!/usr/bin/env python

# Installs the TWiki package into your local Sublime Text packages path.

from os import pardir, environ
from os.path import abspath, join, dirname, isdir
from shutil import rmtree, copytree

package_name = "TWiki"
packages_path = join(environ["HOME"],
                     "Library/Application Support/Sublime Text 3/Packages")
src_path = abspath(join(dirname(__file__), pardir))
dest_path = join(packages_path, package_name)

print("Installing {0} to {1}...".format(src_path, packages_path))

if isdir(dest_path):
    rmtree(dest_path)

copytree(src_path, dest_path)

print("Done")
