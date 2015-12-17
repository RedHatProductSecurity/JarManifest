from setuptools import setup
# To use a consistent encoding

setup(
    name='jarmanifest',

    packages = ['jarmanifest'],

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.14',

    description='Tool for parsing Java Manifest files',

    # The project's main homepage.
    url='https://github.com/RedHatProductSecurity/JarManifest',

    # Author details
    author='Red Hat',
    author_email='jshepher@redhat.com',

    # Choose your license
    license='GPLv3',

    data_files=[('etc', ['config/jarmanifest.cfg'])],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Java Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='java dependencies metadata',

)
