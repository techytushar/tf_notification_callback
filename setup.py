import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(name='tf_notification_callback',
      description='Receive notifications about your model training anywhere you want!',
      long_description=long_description,
      long_description_content_type="text/markdown",
      version='0.2',
      url='https://github.com/techytushar/tf_notification_callback',
      author='Tushar Mittal',
      author_email='chiragmittal.mittal@gmail.com',
      license='GNU General Public License v3 (GPLv3)',
      classifiers=[
          'Development Status :: Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python 3'
      ],
      keywords='api python keras training callback tensorflow machine learning deep learning nlp',
      install_requires=[
        'python-telegram-bot>=12',
        'matplotlib>=3',
        'keras>=2.3',
        'tensorflow>=2'
        'requests>=2'
      ],
      packages=setuptools.find_packages(),
      python_requires='>=3.6'
)
