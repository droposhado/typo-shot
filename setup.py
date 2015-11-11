from setuptools import setup
import typoshot
import os


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="Typo Shot!",
    version=typoshot.__version__,
    author="Flaverton Rodrigues Rosa",
    author_email="contato@flaverton.com",
    description=("Typo is a script to take screenshot on your website/blog."
                 " A simpler way to check printing, viewing the page in complete."),
    license="MIT",
    keywords="splinter screenshot typo typography",
    url="https://github.com/flavertonrr/typo-shot",
    scripts=["typo"],
    packages=["typoshot"],
    long_description=read('README.md'),
    install_requires=[
        "splinter>=0.7.3",
        "requests>=2.4.3"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7"
    ]
)
