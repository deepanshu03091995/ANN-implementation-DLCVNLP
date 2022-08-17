from setuptools import setup


with open('README.md',"r",encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name="src",
    version="0.0.1",
    author="deepanshu rajput",
    description="Python package for ANN implementation",
    url="https://github.com/deepanshu03091995/ANN-implementation-DLCVNLP.git",
    author_email="201812009@daiict.ac.in",
    packages=['src'],
    python_requires='>=3.6',
    install_requires=[
        "tensorflow",
        "matplotlib",
        "pandas ",
        "numpy"
        "seaborn"]

)    
