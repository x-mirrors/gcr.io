## Usage

- change dir

```
cd tools
```

- create env

```
virtualenv venv
```

- use env

```
source ./venv/bin/activate
```

- install dep

```
pip3 install -r requirements.txt
```

- help

```
$ python3 render.py --help
usage: render.py [-h] [--readme | --no-readme | -r] [--images | --no-images | -i]

Render README.md and images list

optional arguments:
  -h, --help            show this help message and exit
  --readme, --no-readme, -r
                        render readme (default: False)
  --images, --no-images, -i
                        render images (default: False)

$ python3 render.py --readme
$ python3 render.py --images
```
