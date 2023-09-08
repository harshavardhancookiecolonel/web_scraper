DESCRIPTION:

We know how to send HTTP requests and get responses. In the previous stage, the example URL responded with the json body, this is how the REST resources communicate with a client. We, humans, go to websites to access the Internet. We also have browsers, but sometimes we need to parse the website's content automatically. Parsing is one of the ways to scrape a webpage.

Parsing website data begins with the inspection of the page source code with browser built-in tools. Usually, the desired information can be distinguished by some unique attributes or a set of attributes, for example, a css class name. We need to determine these attributes and then make our parsing tool (in our case, the beautifulsoup library) do the magic for us.

OBJECTIVES:

Take a link to the nature.com article as input. This is an example of a correct link: https://www.nature.com/articles/d41586-023-00103-3. The link to an article always contains the word "articles" in it.

Download the webpage content, parse it using the beautifulsoup library.

Print out the article's heading and short summary as a dictionary. You can find the heading in the <title> tag. The summary can be found in the <meta> tag with the {'name': 'description'} attribute.

If the link doesn't have an article or is not a nature.com resource, the program should respond with an error message Invalid page!.

EXAMPLE 1:

Input the URL:

> https://www.nature.com/articles/d41586-023-00103-3

{"title": "Green electronics rely on materials that grow on trees", "description": "Compounds derived from eucalyptus and other plants are formulated into an ink for printing electronic components."}

EXAMPLE 2:

Input the URL:

> https://www.imdb.com/name/nm0001191/

Invalid page!

EXAMPLE 3:

Input the URL:

> https://www.google.com/

Invalid page!
