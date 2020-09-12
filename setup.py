import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="internalmonologue", # Replace with your own username
    version="0.0.11",
    author="Devashish Mulye",
    author_email="devashish.mulye@gmail.com",
    description="Internal Monologue will help you journal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devashishmulye/internal-monologue",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'logue = logue.logue:main'
        ]
    },
    install_requires=["requests>=2.18.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)






