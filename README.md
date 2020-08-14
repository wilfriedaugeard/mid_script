<p align="center">
  <img alt="mid_script" src="https://github.com/wilfriedaugeard/mid_script/blob/master/assets/logo.png" />
</p>
<p align="center">
  <img alt="Version : 1.0.0" src="https://img.shields.io/badge/version-1.1.0-green" target="_blank" />
  <img alt="Python : v3.6.9" src="https://img.shields.io/badge/python-v3.6.9-blue?logo=python&logoColor=white" target="_blank" />
  <a href="https://github.com/wilfriedaugeard/mid_script/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://github.com/wilfriedaugeard/mid_script/commits">
    <img alt="Last commit" src="https://img.shields.io/github/last-commit/wilfriedaugeard/mid_script"/>
  </a>
</p>

A little script to make a man in the middle attack easily. You will find a console interface to interact with the script to scan the network and choose the target. 

## Prerequisites
- python 3.*
- sslstrip
- dns2proxy
- arpspoof
- nmap


## Installation
Go to the mid_script directory and run *install.py*. That clone ![sslstrip](https://github.com/moxie0/sslstrip) and ![dns2proxy](https://github.com/LeonardoNve/dns2proxy) repo if you don't have them. 
```sh
git clone https://github.com/wilfriedaugeard/mid_script
cd mid_script/ ; python3 install.py
```

## Interface
### Menu
![menu](https://github.com/wilfriedaugeard/mid_script/blob/master/assets/menu.png)


### Scanning network
The network scan display a pretty display of nmap output. You can choose the rooter and the victim by selecting the corresponding number.

![scan](https://github.com/wilfriedaugeard/mid_script/blob/master/assets/scan.png)


### Collecting data
After choosing both ip the script collect the data. You can stop at anytime by pressing the *enter* key.
The collected data are stocked in the *sslstrip.log* file.

![data](https://github.com/wilfriedaugeard/mid_script/blob/master/assets/data.png)


## About this project
### Authors
👤 **Wilfried Augeard**
- Github: [@Exyos](https://github.com/wilfriedaugeard)
- Website: [waugeard.com](https://waugeard.com)

### License

- [MIT license](https://github.com/wilfriedaugeard/mid_script/blob/master/LICENSE)<br/>
- Copyright © 2020 [Exyos](https://github.com/wilfriedaugeard)
