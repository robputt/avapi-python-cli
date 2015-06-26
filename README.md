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

Copy to folder within path and make executable...

```cp cli_tools/scanfile.linux.py /usr/bin/avapiscan; chmod 755 /usr/bin/avapiscan```

Scan a file...

```avapiscan /var/log/messages```

#### OSX

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

Copy to folder within path and make executable...

```sudo cp cli_tools/scanfile.osx.py /usr/bin/avapiscan; sudo chmod 755 /usr/bin/avapiscan```

Scan a file...

```avapiscan /var/log/wifi.log```

### Usage
#### Linux

Scan an individual file...

```
avapiscan /home/samples/eicar/eicar.txt
 - Fetching Token
 - Checking Hash
 + eicar.com is infected: EICAR_Test
```

Recursively scan a whole directory...

```
find /var/log/ -type f -size -100M -not -path '*/\.*' -exec avapiscan {} \;
```

#### OSX

Scan an individual file...

```
avapiscan /var/log/wifi.log
 - Fetching Token
 - Checking Hash
 - No intelligence about file, submitting for analysis
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  234k    0    20  100  234k      4  55387  0:00:04  0:00:04 --:--:--     0
 -  Waiting for scan result
 + /var/log/wifi.log is safe
 ```

Recursively scan a whole directory...

```
find ~/Downloads -type f -size -100M -not -path '*/\.*' -exec avapiscan {} \;
```
