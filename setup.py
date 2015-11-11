from setuptools import setup
import typoshot


setup(
    name="typo-shot",
    version=typoshot.__version__,
    author="Flaverton Rodrigues Rosa",
    author_email="contato@flaverton.com",
    description=("Check your website/blog typography simple, with screenshots!"),
    license="MIT",
    keywords="splinter screenshot typo typography",
    url="https://github.com/flavertonrr/typo-shot",
    scripts=["typo"],
    packages=["typoshot"],
    install_requires=[
        "splinter>=0.7.3",
        "requests>=2.4.3"
    ],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"
    ]
)
