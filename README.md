# Splunk connector Library

You can use this library for consume data from splunk directly by making server calls instead of webcall. After that you can play around your data.

# Things to remember!

  - You can either give a credential file or pass params for commandline access
  - ex  : file -
```sh
  cd splunkconnector
  python connector.py connector.py -f <filepath>
```
  - ex  : cmds - 
```sh
  cd splunkconnector
   python connector.py connector.py -H <host>  -P <port> -u <username> -p <password> -q <searchquery> -email <emails>
```
  - Or you can access the data by the given method getsplunkdata in your python code like below.

```sh
  import splunkconnector.src as splunkconsumer
  s = splunkconsumer.getsplunkdata(...)
```

### File format to access from commandline

```sh
{
    "host": <host>,
    "port": <port>,
    "username": <username>,
    "password": <password>,
    "query": <query>,
    "email": <email>,
    "output_mode": <output_mode>"
    ...
}
```

### Installation

Splunk Connector requires [Python](https://www.python.org/) v3.7+ to run.

Install the dependencies and devDependencies.

```sh
$ pip install "library-filepath"
```
