from setuptools import setup

na = "gsea"

setup(
    name=na,
    version="0.1.0",
    python_requires=">=3.6",
    install_requires=["julia", "pandas"],
    packages=[na],
)
