import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sorting_visualizer",
    version="1.0",
    author="Debdut Goswami",
    author_email="debdutgoswami@gmail.com",
    description="A package to visualize various sorting algorithms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debdutgoswami/sorting-visualizer",
    download_url = 'https://github.com/debdutgoswami/sorting-visualizer/archive/v1.0.tar.gz',
    keywords = ['SORT', 'ALGORITHM', 'VISUALIZE'],
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)