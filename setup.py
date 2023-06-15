from setuptools import setup, find_packages
setup(
    name='Face Recognition Based Attendance Monitoring System',
    extras_required=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"}

)