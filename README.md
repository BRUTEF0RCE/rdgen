# RDGen, a RustDesk client generator to use with your self-hosted RustDesk server

The client generator is currently hosted [here](https://rdgen.crayoneater.org).
If you would like to host the generator yourself, see [here](setup.md)

## Features

- Embed server and key into client
- Custom app name
- Custom icon/logo
- Set default settings for the client
- Support for rustdesk advanced settings (https://rustdesk.com/docs/en/self-host/client-configuration/advanced-settings/)

## Generate RustDesk clients from command line instead of using a web browser

Save your configuration from the rdgen web interface, or generate your own, then use that json file with [@AlekseyLapunov's rdgen-cli](https://github.com/AlekseyLapunov/rdgen-cli) to build from the command line on Windows, Linux, or MacOS like this: `python rdgen-cli -f my_config.json --set-version 1.4.5 --set-platform windows -s https://rdgen.crayoneater.org`

## Notes

- Icons should be square (256x256 recommended)
- Avoid special characters or non-English characters in app name and file name
- Build time is currently 30 - 45 minutes



## How to manage
Suppose the original project is:

text
https://github.com/bryangerlach/rdgen.git
And your fork is:

text
https://github.com/BRUTEF0RCE/rdgen.git
Your initial setup:

bash
cd /data/
git clone https://github.com/BRUTEF0RCE/rdgen.git
cd rdgen
git remote add upstream https://github.com/bryangerlach/rdgen.git
git fetch upstream

git switch -c rdgen-runner-customizations
git push -u origin rdgen-runner-customizations



Later, when bryangerlach releases changes:

bash
git fetch upstream

git switch master
git merge --ff-only upstream/master
git push origin master

git switch rdgen-runner-customizations
git rebase master
git push --force-with-lease origin rdgen-runner-customizations
Your custom branch then contains:

text
upstream project history
        +
your custom commits, replayed on top
That is the maintainable way to continuously consume source-repository updates while preserving your fork-specific changes.