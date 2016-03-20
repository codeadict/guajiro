from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'guajiro/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
        name='Guajiro',
        version=version,
        url='https://github.com/codeadict/guajiro',
        description='Insanely fast high-productivity web services framework built with python 3 asyncio features.',
        long_description=open('README.md').read(),
        author='Dairon Medina',
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
            'Framework :: Guajiro',
            'Environment :: Console',
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
            "aiohttp==0.15.0",
            "aiohttp_jinja2==0.3.0",
        ],
)
