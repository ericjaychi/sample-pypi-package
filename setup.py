# Import our newly installed setuptools package.
import setuptools

# Opens our README.md and assigns it to long_description.
with open("README.md", "r") as fh:
	long_description = fh.read()

# Defines requests as a requirement in order for this package to operate. The dependencies of the project.
# requirements = ["requests<=2.21.0"]

# Function that takes several arguments. It assigns these values to our package.
setuptools.setup(
	# Distribution name the package. Name must be unique so adding your username at the end is common.
	name="hello_world_ericjaychi",
	# Version number of your package. Semantic versioning is commonly used.
	version="0.0.1",
	# Author name.
	author="Eric Chi",
	# Author's email address.
	author_email="ericjaychi@gmail.com",
	# Short description that will show on the PyPi page.
	description="A Hello World package",
	# Long description that will display on the PyPi page. Uses the repo's README.md to populate this.
	long_description=long_description,
	# Defines the content type that the long_description is using.
	long_description_content_type="text/markdown",
	# The URL that represents the homepage of the project. Most projects link to the repo.
	url="https://github.com/ericjaychi/sample-pypi-package",
	# Finds all packages within in the project and combines them into the distribution together.
	packages=setuptools.find_packages(),
	# requirements or dependencies that will be installed alongside your package when the user installs it via pip.
	# install_requires=requirements,
	# Gives pip some metadata about the package. Also displays on the PyPi page.
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	# The version of Python that is required.
	python_requires='>=3.6',
)