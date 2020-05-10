# Splunk connector Library

You can use this library for consume data from splunk directly by making server calls instead of webcall. After that you can play around your data.

# Things to remember!

  - You can either give a credential file or pass params for commandline access
    ex  : file - python connector.py -f <filepath>
    ex  : cmds - python connector.py connector.py -f <filepath> |-H <host>  -P            <port> -u <username> -p <password> -q <searchquery> -email <email_ids>
  - Or you can access the data by the given method getsplunkdata .

### File format 

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