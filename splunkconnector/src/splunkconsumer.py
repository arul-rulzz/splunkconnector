
from splunklib import client
import datetime
import splunklib.results as results
import re
from dateutil.parser import parse
import json
from splunkconnector.utils import validateutils
import os
import test


test_file_path = os.path.join(os.path.dirname(test
                                              .__file__), 'test.json')
mock_dict = dict()
with open(test_file_path, encoding='utf-8') as file_data:
    mock_dict = json.loads(file_data.read())


# kwargs: scheme, host, port, username, password


def getsplunkdata(host, portnumber, username, password, searchquery, email_ids=None, ismockcall=False, ** kwargs):
    """This function connects and logs in to a Splunk instance.

    This function is a shorthand for :meth:`Service.login`.
    The ``connect`` function makes one round trip to the server (for logging in).

    :param host: The host name.
    :type host: ``string``
    :param port: The port number.
    :type port: ``integer``
    :param `username`: The Splunk account username, which is used to
                       authenticate the Splunk instance.
    :type username: ``string``
    :param `password`: The password for the Splunk account.
    :type password: ``string``
    :param `searchquery`: Search query for splunk.
    :type searchquery: ``string``
    :param `email_ids`: Email ids to send the results.
    :type email_ids: ``list``
    :param `ismockcall`: Return mock data.
    :type ismockcall: ``boolean``
    :param `**kwargs`: splunk required params to connect the client
    :type ismockcall: ``tuple``
    """
    isvaliddata, errors = validateutils.__isvaliddata(
        host, portnumber, username, password)
    if not isvaliddata:
        return {"errors": errors}

    if ismockcall:
        return mock_dict

    try:  # Without throwing error, we are going to return the error

        service = client.connect(
            host=host,
            port=portnumber,
            username=username,
            password=password)

        searchquerykwargs = validateutils.__getvalidkwargsfromrequest(**kwargs)

        emails, email_id_format_errors = validateutils.__getvalidemails(
            email_ids)
        if len(email_id_format_errors) > 0:
            error_msg = validateutils.error_dict["errors.email.validate"]
            if len(email_id_format_errors) > 1:
                error_msg = validateutils.error_dict["errors.emails.validate"]
            return {"errors": error_msg+",".join(email_id_format_errors)}

        if len(emails) > 0:
            emailformat = "raw"
            emailsub = "myresults"
            email = ",".join(emails)
            is_pdf_to_be_attach = "true"
            if "email_format" in kwargs and validateutils.__isnotempty(kwargs["email_format"]):
                emailformat = kwargs["email_format"]
            if "email_sub" in kwargs and validateutils.__isnotempty(kwargs["email_sub"]):
                emailsub = kwargs["email_sub"]
            if "is_pdf_to_be_attach" in kwargs and validateutils.__isnotempty(kwargs["is_pdf_to_be_attach"]) and (kwargs["is_pdf_to_be_attach"] == "true" or
                                                                                                                  kwargs["is_pdf_to_be_attach"] == "false"):
                is_pdf_to_be_attach = kwargs["is_pdf_to_be_attach"]

            searchquery += "| sendemail to=\"" + \
                email + \
                "\" format="+emailformat+" subject="+emailsub + \
                " server=mail.splunk.com sendresults=true"+"sendpdf="+is_pdf_to_be_attach

        if not 'search' in searchquery:
            searchquery = 'search '+searchquery

        result_set = service.jobs.export(searchquery, **searchquerykwargs)

        reader = results.ResultsReader(result_set)

        resultsetasdict = []
        resultsetasmessage = []
        for result in reader:
            if isinstance(result, dict):
                resultsetasdict.append(dict(result))
            elif isinstance(result, results.Message):
                resultsetasmessage.append(("%s" % result))

        return {"json_data": resultsetasdict,
                "message_data": resultsetasmessage}
    except BaseException as error:
        return {"error": (validateutils.error_dict["errors.common.excpetion"]+' {}'.format(error))}
