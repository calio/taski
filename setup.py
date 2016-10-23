from distutils.core import setup

setup(
    name="taski",
    version="0.1.1",
    author="Jiale Zhi",
    author_email="vipcalio@gmail.com",
    packages=["app"],
    include_package_data=True,
    url="http://pypi.python.org/pypi/taski_v011/",
    license='MIT',
    description="Taski is a tool to help manage your GTD tasks",
    long_description=open("README.txt").read(),
    scripts=['taski'],
    install_requires=[
        "pytodoist",
        "pytz",
        "tzlocal",
    ],
)
