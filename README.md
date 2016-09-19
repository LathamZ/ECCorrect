# ECCorrect
A python software which can detect &amp; correct the encoding of your file. Powered  by [Chardet](https://github.com/chardet/chardet).

The current routine of this software is:

1. Detect the encoding of your file.
2. Decode the file using the encoding detected.
3. Encode the content with preferred encoding(See how to config below) and save to the file.


## Installation



In the project directory.

	$ python setup.py install
	
if you encountered permission problem, use sudo.

	$ sudo python setup.py install

## Usage

	$ eccorrect filename
	
## Configuration

[YAML](http://yaml.org/) Supported.

You could specify your settings in `.eccorrect.yaml` file.

Following are currently supported fields:

* preferred_encoding (default to utf8 if not set)
* ...

The configuration file is located in your HOME directory `~/.eccorrect.yaml`.


## License
[MIT](https://github.com/LathamZ/ECCorrect/blob/master/LICENSE)

