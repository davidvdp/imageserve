# Video Server with Flask

## Description
Creates a webpage that streams images from a specified source directory.

This project was inspired by ckieric http://www.chioka.in/

## Installation
```sudo pip3 install .``` in root directory.

## Execution
```python3 -m imageserve <sourcedir>```
Where sourcedir contains the jpg images that are served.

For usage help:

```python3 -m imageserve -h```

## SystemD Unit (Linux)
Move the service file to ```/usr/lib/systemd/system```

Start the service:

```sudo systemctl enable imageserve```

```sudo systemctl start imageserve.service```

Verify using:

```journalctl -u imageserve -f```


