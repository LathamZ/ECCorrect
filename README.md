# ECCorrect
A python software which can detect &amp; correct the encoding of your file. Powered  by [Chardet](https://github.com/chardet/chardet).

The current routine of this software is:

1. Detect the encoding of your file.
2. Decode the file using the encoding detected.
3. Encode the content with preferred encoding(which you can set in conf.yaml) and save to the file.


## Install



In the project directory.

	$ python setup.py install
	
if you encountered permission problem, use sudo.

	$ sudo python setup.py install

## Usage

	$ eccorrect filename
	
## Config

You could specify your settings in `conf.yaml` file.

Following are currently supported fields:

* preferred_encdoing (default to utf8 if not setting)
	
## License
[MIT License](https://github.com/LathamZ/ECCorrect/blob/master/LICENSE)

