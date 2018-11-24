from meta import githubUrl
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_chalk",
    version="0.1.0",
    author="phil",
    author_email="philip.olson@pm.me",
    description="A terminal string styling library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://{githubUrl}",
    packages=setuptools.find_packages(),
    license="WTFNMFPL-1.0",
    python_requires=">=3.6",
)
