# Openweather API App

Copyright 2020 Splunk, Inc.

This app is used to collect Openweathermap API Data. 

## Requirements

In order to use this app, you will still need to agree and follow Openweathermap API Rules and sign-up for an account on their system. More information on that here: https://openweathermap.org/api

## Installation

1. Clone the app into $SPLUNK_HOME/etc/apps/
2. Modify $SPLUNK_HOME/etc/apps/connect_openweatherapi/bin/get_one_api_call.py
* Modifying this file means adjusting your specific lat/lon and adding in your specific API Key. 
3. Enable the Scripted Input via the Splunk GUI. 

## Future State/Plans

Package this app with Add-on Builder for an even easier/more secure setup process. 
