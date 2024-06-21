from setuptools import setup, find_packages

setup(
    name='manipulator_learning',
    version='0.2.0',
    description='Package with OpenAI Gym robotic manipulation environments and learning code.',
    author='Trevor Ablett',
    author_email='trevor.ablett@robotics.utias.utoronto.ca',
    license='MIT',
    packages=find_packages(),
    install_requires=['pybullet',
                      'numpy<2.0',
                      'liegroups @ git+ssh://git@github.com/utiasSTARS/liegroups@master#egg=liegroups',
                      'gym',
                      'transforms3d',
                      'Pillow'],
    include_package_data=True
)
