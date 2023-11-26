from setuptools import find_packages, setup
from typing import List

H_E_ = "-e ."
def get_requirements(file_path:str) -> List[str]:
    # this function will returns the list of requirements

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace('\n',' ')  for r in requirements]

        if H_E_ in requirements:
            requirements.remove(H_E_)


setup(
    name = "ML-Project",
    version = "0.0.1",
    author = "Roshil Verma",
    author_email = "roshil.verma.3@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)