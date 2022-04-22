from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ['allure-python-commons', 'jsonschema']

setup(
    name="pytest_assertions",
    version="0.4.1",
    author="Nikita Filonov",
    author_email="filonov.nikitkaa@gmail.com",
    description="Pytest Assertions",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Nikita-Filonov/assertions",
    packages=find_packages(),
    install_requires=requirements,
)
