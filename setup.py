from setuptools import setup

setup(
    name="chatmemoryc",
    version="0.1.4",
    url="https://github.com/uezo/chatmemory",
    author="uezo",
    author_email="uezo@uezo.net",
    maintainer="uezo",
    maintainer_email="uezo@uezo.net",
    description="Long-term and medium-term memories between you and chatbot💕",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["fastapi==0.100.0", "anthropic==0.20.0", "requests==2.31.0", "SQLAlchemy==2.0.20", "uvicorn==0.23.1", "pycryptodome==3.18.0"],
    license="Apache v2",
    packages=["chatmemoryc"],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)