from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="erpnext_custom_theme",
    version="0.0.1",
    author="Custom",
    author_email="custom@example.com",
    description="Custom theme for ERPNext based on ThemeRef styling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Engsawysaad/ERPNEXTTheme",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Frappe",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.10",
    install_requires=["frappe>=16.0.0"],
)
