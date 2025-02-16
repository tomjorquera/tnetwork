from setuptools import setup, find_packages
from codecs import open
from os import path

__author__ = 'Remy Cazabet'
__license__ = "BSD-2-Clause"
__email__ = "remy.cazabet@gmail.com"


def get_requirements(remove_links=True):
    """
    lists the requirements to install.
    """

    try:
        with open('requirements.txt') as f:
            requirements = f.read().splitlines()
    except Exception as ex:
        with open('DecoraterBotUtils.egg-info\requires.txt') as f:
            requirements = f.read().splitlines()
    if remove_links:
        for requirement in requirements:
            # git repository url.
            if requirement.startswith("git+"):
                requirements.remove(requirement)
            # subversion repository url.
            if requirement.startswith("svn+"):
                requirements.remove(requirement)
            # mercurial repository url.
            if requirement.startswith("hg+"):
                requirements.remove(requirement)
    return requirements


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='tnetwork',
      version='0.1',
      license='BSD-Clause-2',
      description='tempoal network libary',
      url='https://github.com/Yquetzal/tnetwork',
      author='Remy Cazabet',
      author_email='remy.cazabet@gmail.com',
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: BSD License',

          "Operating System :: POSIX :: Other",
          "Operating System :: MacOS",

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python',
          'Programming Language :: Python :: 3'
      ],
      keywords='network-science temporal-networks community-detection',
      install_requires=get_requirements(),
      packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
      include_package_data=True
      )