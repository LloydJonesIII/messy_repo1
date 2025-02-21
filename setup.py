from setuptools import setup, find_packages
from os import path
work_dir = path.abspath(path.dirname(__file__))

# turns the README.md file into a long description 
with open (path.join(work_dir, 'README.md'), encoding='utf-8') as f: long_desc = f.read

setup(
    name = 'messy_tools1',
    version = '0.0.1',
    # URL if applicable
    author = 'Lloyd W Jones III',
    author_email = 'lloydjonesx3@gmail.com',
    description = 'Simple data manipulation and visualization package',
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'matplotlib.pyplot', 'pathlib']
)
"""
Checking dist/messy_tools1-0.0.1.macosx-10.9-universal2.tar.gz: ERROR    
InvalidDistribution: Too many top-level members in sdist archive:      
         {self.filename} 
"""