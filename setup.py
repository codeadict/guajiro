"""
=======
Guajiro
=======

.. image:: https://raw.githubusercontent.com/codeadict/guajiro/master/artwork/logo.png

**Guajiro** is a word used to designate people from countryside in Cuba.
They are usually very hardworking people with lot of culture and traditions.
What you're more likely to see when you search "guajiro" are Cuban cowboys wearing
hand made hat, riding horses and smoking tobaccos.

The aim of this project is to make a insanely fast high-productivity web services
framework built with python 3 honouring this hardworking people that every day work hard
in the land, but this time in the land of coding.

Guajiro is pretty easy, check the docs on `Github <https://github.com/codeadict/guajiro>`_
"""
from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'guajiro/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
        name='Guajiro',
        version=version,
        url='https://github.com/codeadict/guajiro',
        description='Insanely fast high-productivity web services framework built with'
                    'Python3 asyncio features.',
        long_description=__doc__,
        author='Dairon Medina',
        author_email='dairon.medina@gmail.com',
        maintainer='Dairon Medina',
        maintainer_email='dairon.medina@gmail.com',
        license='BSD',
        packages=find_packages(exclude=["docs", "tests*"]),
        include_package_data=True,
        zip_safe=False,
        entry_points={
            'console_scripts': ['guajiro = guajiro.cmdline:execute']
        },
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        install_requires=[
            "aiohttp==0.21.4",
            "aiohttp_jinja2==0.7.0",
        ],
)
