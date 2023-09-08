DESCRIPTION:

We use the Internet everyday. Have you ever wondered how your computer communicates with the Global Web? In this stage, we'll learn how to talk to the Internet from your Python script — and interpret the replies! Your program should send an HTTP request to a URL received from the user input. The user input can be a Quotable resource http://api.quotable.io/quotes/-CzNrWMGIg8V. In this case, the program should print out the Quote extracted from the json body response.

The user may also input an invalid URL or a non-existing quote resource, for example, http://api.quotable.io/quotes/1, or a different Quotable page (http://api.quotable.io/authors). Use if-else statements to check the status_code or the json body response. Print out the Invalid quote resource! error message when the response code is different from 200 or when there is no quote in the json body response.

OBJECTIVES:

In this stage, your program should:

Send an HTTP request to a URL received from the user input.

Print out the Quote content extracted from the json body response.

Print out the Invalid quote resource! error message if there's no quote or something goes wrong.

EXAMPLE 1:

Input the URL:

> http://api.quotable.io/quotes/-4WQ_JwFWI

The three great essentials to achieve anything worth while are: Hard work, Stick-to-itiveness, and Common sense.

EXAMPLE 2:

Input the URL:

> http://api.quotable.io/quotes/asdfgh

Invalid quote resource!
