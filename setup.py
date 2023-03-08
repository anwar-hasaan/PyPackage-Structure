from setuptools import find_packages, setup

with open("app/readme.txt", "r") as f:
    long_description = f.read()

setup(
    name="top_lavel_name",
    version="0.0.12",
    description="This package retrive sys info with encryption functinality",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anwar-hasaan/",
    author="Anwar Hasan",
    author_email="anwarhasan202@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent (Windows[10, 11] Tested)",
    ],
    install_requires=[
        'example>=39.0.1'
        ],
    python_requires=">=3.8",
    
    # extras_require={
    #     "dev": ["pytest>=7.0", "twine>=4.0.2"],
    # },
)