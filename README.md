# Introduction

The idea behind this repo was to determine when an Amazon Dash Button was pressed, and perform some sort of action.

## YouTube

YouTube: https://www.youtube.com/watch?v=xSc5uhywWWQ&feature=youtu.be

## Setup

First, continue through step 5 on the official Amazon dash button setup instructions: https://www.amazon.com/gp/help/customer/display.html?nodeId=201746340

When you arrive on the step to select which product, exit out of the setup. 

## MAC address

How you can determine if the Dash button is pressed, is by it's MAC address. The Dash is usually always off to conserve battery life. Whenever it is pressed, it turns on, connects to the WiFi network it's configured with, and then orders something. So whenever you press it, your network will be sent a request to connect with it's MAC address.

To determine the MAC address of the Dash, connect your computer to the same network that you set up your Dash to connect to. You can then run the MACsniffer.py progam using `sudo python MACsniffer.py`

You may have to install scapy, libnet, and pcapy before you are able to run the python program.

## Other

From what I've determined, it takes 45 seconds before you can press the Dash again.
