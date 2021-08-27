from setuptools import find_packages, setup

na = "gsea"

setup(
    name=na,
    version="0.5.0",
    url="https://github.com/KwatME/gsea",
    python_requires=">=3.6.0",
    install_requires=["julia", "pandas"],
    packages=find_packages(),
)
