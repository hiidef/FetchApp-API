from setuptools import setup, find_packages
# Also requires python-dev and python-openssl
setup(

    name = "FetchApp-Api",

    version = "0.0.1",

    packages = find_packages(),

    install_requires = [],
    include_package_data = True,

    # metadata for upload to PyPI
    author = "John Wehr",
    author_email = "johnwehr@hiidef.com",
    description = "http://fetchapp.com API Python Client",
    license = "MIT License",
    keywords = "fetchapp client",
    url = "http://github.com/rays/hiispider"

)
