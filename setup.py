import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="oliverj-utils",
    version="0.0.1",
    author="Olliejohnson",
    author_email="contact@oliverj.io",
    packages=["oliverj-utils"],
    description="A utility package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/oliverj-utils",
    license="MIT",
    python_requires=">=3.8",
    install_requires=[]
)