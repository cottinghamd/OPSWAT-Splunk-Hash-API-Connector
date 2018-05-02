# encoding = utf-8
def query_url(helper, hashvalue, apikey, request_timeout_rate, themethod):
    import json
    import re, urllib
    from httplib2 import Http
    
    if not hashvalue or not apikey:
        helper.log_error('Some parameters are missing. Apikey and hashvalue are required.')
        return
    helper.log_info(request_timeout_rate)
   
    uri = 'https://api.metadefender.com/v2/hash/''{}'.format(hashvalue)
    http = helper.build_http_connection(helper.proxy, timeout=request_timeout_rate)
    data = {
    }
    headers = {
    'apikey' : '{}'.format(apikey)
    }

    resp_headers, content = http.request(uri, method=themethod,
                                     body=urllib.urlencode(data), headers=headers)
    if resp_headers.status not in (200, 201, 204):
        helper.log_error('Failed to query api. url={}, HTTP Error={}, content={}'.format( url, resp_headers.status, content))
    else:

        helper.log_info('Successfully queried url {}, content={}'.format(hashvalue, content))
        contenttemp = json.loads(content)
        contenttemp['requested'] = hashvalue
        
        if 'data_id' in contenttemp:
            contenttemp['found'] = 'yes'
        else:
            contenttemp['found'] = 'no'
        
        content = json.dumps(contenttemp)
        return content
        
def process_event(helper, *args, **kwargs):

    helper.log_info("Alert action opswat started.")
    hashvalue = helper.get_param("hashvalue")
    helper.log_info("hashvalue={}".format(hashvalue))

    apikey = helper.get_global_setting("apikey") 
    sourcetype_name = helper.get_global_setting("sourcetype")
    index_name = helper.get_global_setting("index")
    source_name = helper.get_global_setting("source")
    host_name= helper.get_global_setting("host")
    request_timeout_rate = helper.get_global_setting("request_timeout_rate")
    request_timeout_rate = int(request_timeout_rate)
    content = query_url(helper, hashvalue, apikey, request_timeout_rate, 'GET')  

    helper.addevent(content, sourcetype_name)
    helper.writeevents(index_name, host_name, source_name)
    return 0
