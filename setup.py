from setuptools import setup

setup(
    name = "craption",
    packages = ['craption'],
    description='Screenshot uploader for OS X',
    url='https://github.com/spillevink/CRAPtion',
    package_dir = {'craption':'craption'},
    package_data = {
        'cod': ['glass.mp3'],
    },
    entry_points = {
        'console_scripts': [
            'craption = craption.cli:dispatch',
        ],
    },
    install_requires = [
        'dropbox',
        'pyperclip',
        'requests',
        'opster',
        'configobj',
    ],
)
