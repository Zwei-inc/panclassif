import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="panclassif", # Replace with your own username
    version="1.22.1",
    author="Md. Robiuddin, Kazi Ferdous Mahin",
    author_email="mrrobi040@gmail.com",
    description="A method to improve TCGA pancancer classifiers performance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zwei-inc/panclassif",
    project_urls={
        "Bug Tracker": "https://github.com/Zwei-inc/panclassif/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
       'seaborn',
       'scikit-learn',
       'numpy',
       'pandas',
       'matplotlib',
       'imbalanced-learn',
       'tensorflow',
       'gseapy'
    ]
)