# avapi-python-cli

### Installation
#### OSX
Simple instructions to get you started, if you are experienced you may want to skip these instructions and do your own thing. To get up and running simply perform the following in a terminal entering your sudo password when requested (copy and paste friendly).

Install Python setup tools...

```curl -o setuptools.tar.gz https://pypi.python.org/packages/source/s/setuptools/setuptools-17.1.1.tar.gz#md5=7edec6cc30aca5518fa9bad42ff0179b;
tar -xvf setuptools.tar.gz;
cd setuptools-17.1.1;
sudo python setup.py install```

Install Python requests module...

```sudo easy_install requests```

Clone the AVAPI Python CLI repo...

```git clone https://github.com/AVAPI/avapi-python-cli.git; cd avapi-python-cli```

Edit file to contain your API key...

```sed -i 's\<changeme_apikey>\INSERT YOUR API KEY HERE\g' cli_tools/scanfile.osx.py```

Scan a file...

``````
