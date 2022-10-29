from setuptools import setup

package_name = 'robot_q'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='biznizo',
    maintainer_email='biznizo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
entry_points={
        'console_scripts': [
                'pembicara = robot_q.pembicara:main',
                'pendengar = robot_q.pendengar:main',
        ],
},
)
