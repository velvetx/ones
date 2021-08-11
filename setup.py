import tempfile
import shutil
import os
import setuptools
from distutils.core import setup


current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, "README.md"), encoding='utf-8') as file:
    read_me_description = file.read()

env_dir = tempfile.mkdtemp(prefix="ones-install-")
shutil.copytree(os.path.abspath(os.getcwd()),
                os.path.join(env_dir, "ones"))

os.chdir(env_dir)

setup(
    name='ones',
    version='0.0.1',
    author='velvetx',
    platforms='GNU/Linux',
    url='https://github.com/velvetxq',
    license='GPL',
    description='A simple program that collects Russian names and surnames.',
    long_description=read_me_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3.9"],
    entry_points={
        'console_scripts': ['ones = ones.ones:Program']
    },
    package_data={
        "ones": ["*", "src/*", "logs/*"]
    },
)