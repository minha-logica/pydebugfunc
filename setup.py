from setuptools import setup

setup(
    name = 'PyDebugFunc',
    version = '1.0.0',
    author = 'Tiago Bandeira',
    author_email = 'tecnicotronfullstack@gmail.com',
    packages = ['PyDebugFunc'],
    description = 'A simple decorator to debug functions',
    long_description = 'PyDebugFunc catches the exception thrown by your function.  If there is an error, the type of error and the name of the function will be displayed.' + 'Therefore, we avoid repeating try / except blocks.',
    url = 'https://github.com/minha-logica/pydebugfunc',
    project_urls = {
        'Code': 'https://github.com/minha-logica/pydebugfunc',
        'Download': 'https://github.com/minha-logica/pydebugfunc/archive/refs/heads/main.zip'
    },
    license = 'MIT',
    keywords = 'python debug function',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Debuggers',
        
        'Programming Language :: Python :: 2.4',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    ]
)
