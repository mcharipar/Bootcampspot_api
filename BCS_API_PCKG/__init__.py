import BCS_API_PCKG.bcs_api as bcs

# module level doc-string
__doc__ = """
bcs_api - a Python library that simplifies connecting and working with the 
bootcampspot.com api.
=====================================================================

**bcs_api** is a Python package that was created to simplify connecting with
and working with the bootcampspot.com api and that provides methods to
collect metrics from the api simply.

Main Features
-------------
Here are just a few of the things that bcs_api does well:

  - Easily retrieve a users **authToken**.
  - Provides a PDF report of students metrics.
"""

# Tell user if they're missing hard dependencies
hard_dependencies = ("pandas", "requests", "matplotlib")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies