import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="接口测试用例生成",
    version="0.0.1",
    author="Caiyizhang",
    author_email="1031282751@qq.com",
    description="提供接口测试用例生成方法",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caiyizhang/interface_testcases",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=['allpairspy'],
)
