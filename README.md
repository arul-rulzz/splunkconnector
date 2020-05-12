# Splunk connector Library

You can use this library for consume data from splunk directly by making server calls instead of webcall. After that you can play around your data.

# Things to remember!
  - Clone this repo by
```sh
  git clone https://github.com/arul-rulzz/splunkconnector.git
```

  - You can either give a credential file or pass params for commandline access
  - ex  : file -
```sh
  cd splunkconnector
  python connector.py -f <filepath>
```
  - ex  : cmds - 
```sh
  cd splunkconnector
  python connector.py -H <host>  -P <port> -u <username> -p <password> -q <searchquery> -email <emails>
```
  - Or you can access the data by the given method getsplunkdata in your python code like below.

```sh
  import splunkconnector.src as splunkconsumer
  s = splunkconsumer.getsplunkdata(...)
```

### Output

```sh
 {
    "json_data":[],
    "message_data":[]
 }
 
 - json_data : result from the splunk server as json
 - message_data : messages(logs) from query execution
 
```

### Arguments(both commandline and method arguments):

```sh
host : Splunk server host(mandatory)
port : Splunk server host(mandatory)
username : Splunk user name(mandatory)
password : Splunk password(mandatory)
query : Splunk seacrh query(mandatory)
emails : email ids which going to get output data
...
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
    kwargs...
}
```



### Installation

Splunk Connector requires [Python](https://www.python.org/) v3.7+ to run.

Install the dependencies and devDependencies.

```sh
$ pip install "library-filepath"
```
