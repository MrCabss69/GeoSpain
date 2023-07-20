import setuptools

setuptools.setup(
    name="geospain",
    version="0.1",
    description="Obtención y visualización de datos territoriales de España.",
    packages=setuptools.find_packages(include=['geospain*']),
    python_requires='>=3.7',
)
