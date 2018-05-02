# OPSWAT Splunk Hash API Connector

This Add-On Provides 'Drag and Drop' Splunk integrations for v2 of the OPSWAT Hash public API.

Information about the OPSWAT Hash lookup public API can be found here: 
https://www.opswat.com/products/metadefender/application-and-threat-intelligence-platform
https://onlinehelp.opswat.com/mdcloud/2._Hash_Lookups.html

Simply pass a MD5/SHA1/SHA256 hash to this application from a triggered alert and the handler will query the OPSWAT Hash API and write a result to the index you have specified.

You must have an OPSWAT API key to use this Add-On and this Add-On must be configured after installation.

Note: This application is a community developed application and is not affiliated with OPSWAT. This was made to help the Splunk community easily integrate with the OPSWAT public API. 

This Add-On Requires Splunk CIM to be installed for operation: https://splunkbase.splunk.com/app/1621/
