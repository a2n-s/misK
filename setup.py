from setuptools import setup

setup(
    name="misK",
    version="1.0.0",
    description='"A custom miscellaneous tools library."',
    url="https://github.com/AntoineStevan/misK",
    author="Antoine Stevan",
    author_email='"stevan.antoine@gmail.com"',
    packages=["misK",
              "misK.distributions",
              "misK.misc",
              "misK.params",
              "misK.parse",
              "misK.plots",
              "misK.printing",
              "misK.rl",
              "misK.rl.procgen",
              "misK.rl.procgen.wrappers"],
    install_requires=[
        # 'cycler>=0.10.0',
        # 'kiwisolver>=1.0.1',
        # 'matplotlib>=3.0.3',
        # 'numpy>=1.16.2',
        # 'pandas>=0.24.2',
        # 'pyparsing>=2.3.1',
        # 'python-dateutil>=2.8.0',
        # 'pytz>=2018.9',
        # 'scipy>=1.2.1',
        # 'seaborn>=0.9.0',
        # 'six>=1.12.0',
        # 'torch>=1.0.0',
    ])
