from setuptools import setup, find_packages

setup(
    name="mouse_jiggler_advanced",
    version="1.0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "jiggler=mouse_jiggler.jiggler:main",
        ],
    },
    install_requires=[
        "pytz",
        "pyautogui",
    ],
    author="Ali Hamza",
    author_email="alihamza19999@gmail.com",
    description="A script to move the cursor randomly to prevent idle detection.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hurryingauto3/mouse_jiggler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
