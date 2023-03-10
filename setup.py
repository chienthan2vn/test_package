import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "test_package",
    version = "0.0.1",
    description='Feature Selection using PSO_LR.',
    url='https://github.com/chienthan2vn/test_package',
    author='Thuan Luong',
    author_email='thuanluong19102001@gmail.com',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)