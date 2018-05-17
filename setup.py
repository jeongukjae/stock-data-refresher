from setuptools import setup, find_packages

setup(
    name='stock-data-refresher',
    version='0.0.1',
    url='https://github.com/JeongUkJae/stock-data-refresher',
    license='MIT',
    author='Jeong Ukjae',
    author_email='jeongukjae@gmail.com',
    description='stock data refresher',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'SQLAlchemy==1.2.7',
        'requests==2.18.4',
        'PyMySQL==0.8.1'
    ],
    entry_points={
        'console_scripts': [
            'stock_data_refresher = stock_data_refresher.__main__:main'
        ]
    },
)
