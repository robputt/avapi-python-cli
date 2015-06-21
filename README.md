# avapi-python-cli

### Installation
#### Linux

Install Python setup tools...

```
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-17.1.1.tar.gz
tar -xvf setuptools-17.1.1.tar.gz
cd setuptools-17.1.1
python setup.py install
```

Install Python requests module...

```easy_install requests```

Clone the AVAPI Python CLI repo...

```git clone https://github.com/AVAPI/avapi-python-cli.git; cd avapi-python-cli```

Edit file to contain your API key, replace INSERT YOUR API KEY HERE with your API Key, if you require an API key visit https://www.avapi.co...

```sed -i 's/<apikey>/INSERT YOUR API KEY HERE/g' cli_tools/scanfile.linux.py```

#### OSX
Simple instructions to get you started, if you are experienced you may want to skip these instructions and do your own thing. To get up and running simply perform the following in a terminal entering your sudo password when requested (copy and paste friendly).

Install Python setup tools...

```
curl -o setuptools.tar.gz https://pypi.python.org/packages/source/s/setuptools/setuptools-17.1.1.tar.gz
tar -xvf setuptools.tar.gz
cd setuptools-17.1.1
sudo python setup.py install
```

Install Python requests module...

```sudo easy_install requests```

Clone the AVAPI Python CLI repo...

```git clone https://github.com/AVAPI/avapi-python-cli.git; cd avapi-python-cli```

Edit file to contain your API key, replace INSERT YOUR API KEY HERE with your API Key, if you require an API key visit https://www.avapi.co...

```sed -i '' 's/<apikey>/INSERT YOUR API KEY HERE/g' cli_tools/scanfile.osx.py```

Scan a file...

```python cli_tools/scanfile.osx.py <path_to_file>```

### Usage
#### OSX

Scan an individual file...

```
python cli_tools/scanfile.osx.py /var/log/wifi.log
 - Fetching Token
 - Checking Hash
 - No intelligence about file, submitting for analysis
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  234k    0    20  100  234k      4  55387  0:00:04  0:00:04 --:--:--     0
 -  Waiting for scan result
 + /var/log/wifi.log is safe
 ```

Recursively scan a whole directory (in this case ~/Downloads)...

```
find ~/Downloads -type f -size -100M -not -path '*/\.*' -exec python cli_tools/scanfile.osx.py {} \;
```
