import json
import re
import datetime
from dateutil.parser import parse
import os

import splunkconnector.errors as errors

error_file_path = os.path.join(os.path.dirname(errors
                                               .__file__), 'error.json')


error_dict = dict()
with open(error_file_path, encoding='utf-8') as file_data:
    error_dict = json.loads(file_data.read())


def __geterrormsg(key, lang="en-US"):
    if dict(error_dict) and lang in error_dict and key in error_dict[lang]:
        return error_dict[lang][key]
    return ""


def __getvalidkwargsfromrequest(**kwargs):
    newkwargs = {}
    if kwargs:
        if "output_mode" in kwargs and kwargs["output_mode"]:
            newkwargs["output_mode"] = kwargs["output_mode"]

        if "latest_time" in kwargs and __isvalidtime(kwargs["latest_time"]):
            newkwargs["latest_time"] = kwargs["latest_time"]
        else:
            # Default time
            newkwargs["latest_time"] = "-24h"

        if "earliest_time" in kwargs and __isvalidtime(kwargs["earliest_time"]):
            newkwargs["earliest_time"] = kwargs["earliest_time"]
    return newkwargs


def __isvalidtime(val, fuzzy=False):
    if __isnotempty(val):
        try:
            parse(val, fuzzy=fuzzy)
            return True

        except ValueError:
            return False
    return False


def __isnotempty(val):
    return val and isinstance(val, str) and val.strip() != ""


def __isnoneempty(values):
    if values and len(values) > 0:
        for val in values:
            if not __isnotempty(val):
                return False
    return False


def __isvaliddata(host, portnumber, username, password):
    error_data = []
    if not __isnoneempty([host, portnumber, username, password]):
        __fill_error(error_data, host, "host")
        __fill_error(error_data, portnumber, "portnumber")
        __fill_error(error_data, username, "username")
        __fill_error(error_data, password, "password")
    return len(error_data) == 0, error_data


def __isvalidemailid(email):
    return re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)


def __getvalidemails(emails):
    email_ids = []
    email_id_format_errors = []
    if emails and len(emails) > 0:
        for email in emails:
            if __isnotempty(email):
                if __isvalidemailid(email):
                    email_ids.append(email)
                else:
                    email_id_format_errors.append(email)
    return email_ids, email_id_format_errors


def __fill_error(error_data, val, key):
    if not __isnotempty(val):
        error_data.append({key: key+__geterrormsg("errors.empty.common.msg")})
