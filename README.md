# Amazon-products-details-scraping-Credicxo
Script build using python, selenium and requests

1. Executing the chrome webdriver for scraping content
2. Opening the csv file and saving the asin and country value in respective variable to be used for generating the url
3. for loop to iterate over the process of scraping at each url(every alternate url)
4. Now for each loop, getting the http request status code
5. if block to check the status code to be 200, to move for futher scraping steps, else gives the status code for broken urls
6. Opening the particular link, and implementing implicit_wait to get the complete data without moving further
7. Scraping the title, img url, price and details of product using find_element with Xpath in a dictionary
8. Appending the now formed dictionary of the required 4 info into a list
9. Loops to all the urls performing the same task, and then loading the list so formed into the json file 

#Json output file couldn't be made, due to the urls returned status_code of 200 even if it should be 404.
