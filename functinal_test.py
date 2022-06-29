from selenium import webdriver

browser = webdriver.Firefox()

# User: Chap runs a grocery store. He heard about `baskett` and wanted
# to check it out.
browser.get('http://localhost:8000')

# Chap notices the page title
assert 'baskett - build your site in minutes' in browser.title

# Chap is presented with Log in or sign up option in the center left
# There is logo in the right center of the page.


# The header has option to go to about page and search businesses page


browser.quit()
