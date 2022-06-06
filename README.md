# onecron

[![Latest PyPI version](https://img.shields.io/pypi/v/package_name.svg)](https://pypi.python.org/pypi/onecron)

sleep until next specified time.

## Usage

You can use this script with pipe`|`.

```
$ onecron 12:00 --debug 2>/dev/null
[I|16910|200522 10:04:05.773 root:MainThread:onecron:56] Wait for 2020-05-22 12:00:00
^C
$ onecron "0 12 * * *" --debug 2>/dev/null
[I|17467|200522 10:04:20.802 root:MainThread:onecron:56] Wait for 2020-05-22 12:00:00
^C
$ onecron 0 12 --debug 2>/dev/null
[I|17717|200522 10:04:30.514 root:MainThread:onecron:56] Wait for 2020-05-22 12:00:00
$ ./onecron 6 10 && echo $(date)
2020年 5月 22日 金曜日 10:06:00 JST
```

## Installation

```
pip install onecron
```

### Requirements

python 3.7 or above.

## Compatibility

## Licence

## Authors

package\_name was written by [fx-kirin](fx.kirin@gmail.com).
