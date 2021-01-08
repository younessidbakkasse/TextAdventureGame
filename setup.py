import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textipy", 
    version="1.0.1",
    author="Youness ID BAKKASSE",
    author_email="std.youness@gmail.com",
    description="A textual simple game engine powered by Python and Pygame.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/younessidbakkasse/TextGameEngine",
    packages=setuptools.find_packages(),
    install_requires=[
        'pygame',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',

)