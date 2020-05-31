This simple script allows a user to retrieve dividend information from the website Nasdaq.com for their stock portfolio. Dividend information is extremely important, and rarely do brokerages keep track of upcoming dividend information.

The script is pretty straightforward as in it takes a `.txt` file of ticker symbols (preferably speparated by newlines) and outputs a `.csv` with the most recent dividend transaction for each stock.

A few requirements:
1) All of the libraries imported in the script. They are all either Python 3.6 standard or can be  `pip` installed.
2) A driver for selenium in your PATH. The website has tables that load interactively, and therefore, selenium is needed to scrape the website.
3) Change the variable CURRENT_STOCKS to the path of your `.txt` file that contains the ticker symbols.
