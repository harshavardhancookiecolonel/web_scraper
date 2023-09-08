DESCRIPTION:

In previous stages, we retrieved the results and printed them out on the screen. It's handy for one-time running programs or for debugging, but if we want to reuse the data (and that's the case most of the time), storing it is more effective. The simplest way to store data is to write it to a file on your computer.

In this stage, we are going to store the state of a webpage at the moment when the program is executed. It means that we need to get its source code, the content, and save it to an .html file.

OBJECTIVES:

Create a program that retrieves the page's source code from a user input URL. Please, don't decode the page's content.

Save the page's content to the source.html file. Please, write the file in binary mode.

Print the Content saved. message if everything is OK (Don't forget to add a check for the status_code).

If something is wrong, print the message The URL returned X, where X is the received error code.

EXAMPLE 1:

Input the URL:

> https://www.facebook.com/

Content saved.

EXAMPLE 2:

Input the URL:

> http://google.com/asdfg

The URL returned 404!
