# Openweather API App

Copyright 2020 Splunk, Inc.

This app is used to collect Openweather API Data. 

## Installation

1. Clone the app into $SPLUNK_HOME/etc/apps/
2. Modify $SPLUNK_HOME/etc/apps/connect_openweatherapi/bin/get_one_api_call.py
* Modifying this file means adjusting your specific lat/lon and adding in your specific API Key. 
3. Enable the Scripted Input via the Splunk GUI. 

## Future State/Plans

Package this app with Add-on Builder for an even easier/more secure setup process. 
