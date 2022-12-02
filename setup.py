from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.1.5',
      description='Sorting files by extensions in a given directory',
      author='Maksym Yurkevych',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:main']})
