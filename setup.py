from setuptools import setup, find_packages

setup(
    name="Prefocus",
    version="0.0",
    description="An app that lets you focus.",
    author="Stephen Ka-Wah Ma",
    author_email="980907mjh@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "flask",
        "flask-cors",
        "mysql-connector-python",
    ],
    extras_require={"dev": []},
)
