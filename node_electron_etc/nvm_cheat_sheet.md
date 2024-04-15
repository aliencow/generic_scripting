## NVM cheat sheet



nvm is a node version manager software. It manages nvm and iojs versions and run on Mac & Linux.

Github repo: https://github.com/nvm-sh/nvm

Good reads: https://michael-kuehnel.de/node.js/2015/09/08/using-vm-to-switch-node-versions.html

* Installing the latest version of NodeJs:

      nvm install node

* Installing a specific version of NodeJs:

      nvm install 8.11

* Uninstalling a NodeJS version:

      nvm uninstall 8.11

* Locate the path to an installed version:

      nvm which 8.11
      /Users/demo/.nvm/versions/node/v8.11.4/bin/node

* Get the current NodeJs version in use:

      nvm current

* Switch and use latest version of NodeJS:

      nvm use node

* Switch and use a specific version of NodeJS:

      nvm use 8.11

* List all locally installed versions:

      nvm ls

* List available versions of NodeJS and iojs:

      nvm ls-remote

* List only some specific version:

      nvm ls-remote | grep v8

* List only LTS versions:

      nvm ls-remote --lts

* Run a command using a specific node version:

      nvm run 8.11 --version

* Show the path to the installed node version:

      nvm which 0.12.2              

* Show the current installed nvm version:

      nvm current                   

* Set the default node to the installed 0.10.32 version:

      nvm alias default 0.10.32     

* Show nvm help:

      nvm --help                 
