import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nagahamavh",
    version="0.0.1",
    author="Victor Hugo Nagahama",
    author_email="victor.nagahama@sistemafiep.org.br",
    description="Exercícios resolvidos no curso de python (AI2)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Residencia-Fiep-Turma-2/distribuicao_nagahamavh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)