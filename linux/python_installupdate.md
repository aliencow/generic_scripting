# How to install and upgrade Python


Upgrade and isntall Python https://phoenixnap.com/kb/upgrade-python

Install multiple versions in linux:
https://www.rosehosting.com/blog/how-to-install-and-switch-python-versions-on-ubuntu-20-04/

``` bash
sudo apt install python2 -y
sudo apt install python3 -y
sudo apt install python3.5 -y
sudo apt install python3.7 -y
# .. etc

#Execute the following commands one by one:

sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 3
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 4
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 5

#To set version sellection

sudo update-alternatives --config python

# update-alternatives output
  0            /usr/bin/python3.7   4         auto mode
  1            /usr/bin/python2.7   1         manual mode
  2            /usr/bin/python3.5   2         manual mode
  3            /usr/bin/python3.6   3         manual mode
  4            /usr/bin/python3.7   4         manual mode
* 5            /usr/bin/python3.8   0         manual mode

Press  to keep the current choice[*], or type selection number:4

```

