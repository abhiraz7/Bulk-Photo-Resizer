from importlib.metadata import entry_points
from setuptools import setup ,find_packages

setup(
    name = "Bulk Image Resizer For Annotation",
    version="1.1",
    author="abhinav",
    author_email="abhiraz308@gmail.com",
    packages=find_packages,
    entry_points={"console_scripts":["Resizer=resizer.resizer:main"],},
    keywords=["python","Bulk Image Resizer","CLI","Bulk"],
    install_requires=["Pollow==8.2.0","tqdm==4.43.0"],

)