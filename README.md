# ECCorrect
A python software which can detect &amp; correct the encoding of your file. Powered  by [Chardet](https://github.com/chardet/chardet).

The currently routine of this software is:

1. Detect the encoding of your file.
2. Decode the file using the encoding detected.
3. Encode the content with 'UTF-8' and save to the file.


## Install



In the project directory.

	$ python setup.py install
	
if you encountered permission problem, use sudo.

	$ sudo python setup.py install

## Usage

	$ eccorrect filename
	
## License
[MIT License](https://github.com/LathamZ/ECCorrect/blob/master/LICENSE)

