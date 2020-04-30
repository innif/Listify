from setuptools import setup

setup(name='listify',
      description='a program to manage your playlists in Spotify',
      version=0.1,
      author='Finn Harms',
      packages=['listify'],
      install_requires=[
          'spotipy'
      ],
      entry_points = {
        'console_scripts': ['listify=listify.command_line:main'],
      },
      include_package_data=True,)