from setuptools import setup, find_packages

setup(
    name="requestz",  # 模仿requests包名
    version="0.1.0",
    author="Example Author",
    author_email="author@example.com",
    description="HTTP library for humans, similar to requests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",  # 安装requests依赖
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
