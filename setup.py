from setuptools import setup

setup(
    name='ali8bits_auth',
    version='0.1.0',
    description='An auth Python package that can be use in your django projects for authentication.',
    url='https://github.com/shuds13/pyexample',
    author='Ali8Bits',
    author_email='the.ali8bits@gmail.com',
    license='MIT License',
    packages=['ali8bits_auth'],
    install_requires=['mpi4py>=4.0.3',
                      'numpy',
                      ],

    classifiers=[
        'Programming Language :: Python :: 3.9.6'
    ],
)


