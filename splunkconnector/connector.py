#!/usr/bin/python

import sys
import getopt
import os
import json
from splunkconnector.src import splunkconsumer


def main(argv):
    host = ''
    port = ''
    username = ''
    password = ''
    email = ''
    file_path = ''
    query = ''
    args = None
    try:
        opts, args = getopt.getopt(
            argv, "H:P:u:p:e:f:q", ["host=", "port=", "username=", "password=", "email=", "file=", "query="])
    except getopt.GetoptError:
        print('connector.py -f <filepath> |-H <host>  -P <port> -u <username> -p <password> -email <email_ids>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('connector.py -f <filepath> |-H <host>  -P <port> -u <username> -p <password> -email <email_ids>')
            sys.exit()
        elif opt in ("-f", "--file"):
            file_path = arg
            break
        elif opt in ("-H", "--host"):
            host = arg
        elif opt in ("-P", "--port"):
            port = arg
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-email", "--email"):
            email = arg
        elif opt in ("-q", "--query"):
            query = arg

    if file_path:
        if not '.json' in file_path:
            print("Not a valid file. Accepts only json format")
            sys.exit(2)
        try:
            with open(file_path, encoding='utf-8') as file_data:
                connector_data = json.loads(file_data.read())

                if "host" in connector_data and connector_data['host']:
                    host = connector_data['host']
                    del connector_data['host']
                if "port" in connector_data and connector_data['port']:
                    port = connector_data['port']
                    del connector_data['port']
                if "username" in connector_data and connector_data['username']:
                    username = connector_data['username']
                    del connector_data['username']
                if "password" in connector_data and connector_data['password']:
                    password = connector_data['password']
                    del connector_data['password']
                if "email" in connector_data and connector_data['email']:
                    email = connector_data['email']
                    del connector_data['email']
                if "query" in connector_data and connector_data['query']:
                    query = connector_data['query']
                    del connector_data['query']
                args = connector_data

        except OSError:
            print("Not a valid file path")
            sys.exit(2)
        errorfile = open(file_path, 'r')
        error_dict = json.loads(errorfile.read())

    if not host:
        host = __getvalidinput("host", isEmptyError=False)

    if not port:
        port = __getvalidinput("port", isEmptyError=False)

    if not username:
        username = __getvalidinput("username", isEmptyError=False)

    if not password:
        password = __getvalidinput("password", isEmptyError=False)

    if not query:
        query = __getvalidinput("query", isEmptyError=False)

    if email and ',' in email:
        email = email.split(",")

    print("args :", args)

    splunkdata = splunkconsumer.getsplunkdata(
        host, port, username, password, query, ismockcall=True, **args)

    print("splunkdata :", splunkdata)


def __getvalidinput(key, isEmptyError=False):
    msg = "Please enter the "+key+" :"
    if isEmptyError:
        msg = key + " cannot be empty. Enter a valid value:"
    print(msg)
    value = input()
    if not value or value.strip() == '':
        return __getvalidinput(key, isEmptyError=True)
    return value


if __name__ == "__main__":
    main(sys.argv[1:])
