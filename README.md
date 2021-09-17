# Connect Openweathermap API to Splunk

Copyright 2020 Splunk, Inc.

This app is used to collect Openweathermap API Data. 

## Requirements

In order to use this app, you will still need to agree and follow Openweathermap API Rules and sign-up for an account on their system. More information on that here: https://openweathermap.org/api

## Installation

1. Clone the app into $SPLUNK_HOME/etc/apps/
2. Modify $SPLUNK_HOME/etc/apps/connect_openweatherapi/bin/get_one_api_call.py
* Modifying this file means adjusting your specific lat/lon and adding in your specific API Key inside of the get_one_api_call.py file. 

```
#lat/lon
#Uncomment these lines for Staten Island NY
#lat = "40.643501"
#lon = "-74.076202"

#api_key
api_key=""
```

3. Enable the Scripted Input via the Splunk GUI. 

## Scripted Input

By default, the scripted input will run once every 10 minutes. There is no need to increase this as Openweathermap API Only updates once every 10 minutes. Setting this any more frequent is at your own discretion. 

## Future State/Plans

Package this app with Add-on Builder for an even easier/more secure setup process. 
