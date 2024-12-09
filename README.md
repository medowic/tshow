# tshow
Fast display of CPU temperature in Linux
## Requirements
- Python 3 and higher
> [!NOTE]
> If `python3` doesn't exist on your machine, you will try to install it. Otherwise, install it manually.
# Install
```sh
git clone https://github.com/medowic/tshow.git
cd tshow
sudo bash install.sh
```
# Uninstall
In same `tshow` folder run `uninstall.sh` script
```sh
sudo bash uninstall.sh
```
# Usage
```sh
tshow [OPTIONS]
```
## Options
- `-h, --human-readable` - print temperature in human-readable format (e.g.: 50.0C). Usually prints in raw format (e.g.: 50000).
- `--help` - display help page and exit
- `--version` - display version information and exit
### Examples
This is standard output
```sh
$ tshow
50000
```
You can use `-h` flag to display it in human-readable format
```sh
$ tshow -h
50.0C
```
# License
This is project is under the [MIT License](https://raw.githubusercontent.com/medowic/tshow/master/LICENSE)
