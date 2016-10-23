from distutils.core import setup

setup(
    name="tasky",
    version="0.1.0",
    author="Jiale Zhi",
    author_email="vipcalio@gmail.com",
    packages=["app"],
    include_package_data=True,
    url="http://pypi.python.org/pypi/tasky_v010/",
    license='MIT',
    description="Tasky is a tool to help manage your GTD tasks",
    long_description=open("README.txt").read(),
    scripts=['tasky'],
    install_requires=[
        "pytodoist",
        "pytz",
        "tzlocal",
    ],
)
