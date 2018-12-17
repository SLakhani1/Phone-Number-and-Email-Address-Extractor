# Phone-Number-and-Email-Address-Extractor
It will extract the phone no. and email address from text copied, directly from clipboard.We does not need to paste the content anywhere it will directly read the content from clipboard.

## Prerequisites
- Python
- pip
- pyperclip

## How to Use?
1. Download the python script - extrctor.py
2. Copy the content using Ctrl-A , Ctrl-C 
3. Run the script normally as you run any other python file.

 
You will get the result on output screen.

### Format for Phone-Numbers
- 1234567890
- 123-456-7890
- (123)(456)(7890)
- 123.456.7890
- (123) (456-7890)

And various other using combination of space, '-', '()', '.' as separator.

### Format for Email-Address
- abcd@efg.xyz
- abcd@xxx.yy.zz

### Running the test
1. Open the file named-'test-data'.
2. Copy its content using Ctrl-A, Ctrl-C.
3. Run extractor.py.

Following will be the output--

Found 7 results:
1234567890
(123)(456)(7890)
1234567890
123456(7890)
1234567890
sample-data@gmail.com
lakhnkk-kkk@ghjkjk.co.in






