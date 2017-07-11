## Icebreaker challenge

Give the students the chatbot interface and the base.py version and let them reverse engineer something similar in their chosen programming language

## Example enhancements

- Create a personality dictionary and use it to answer questions
	e.g. 
		chatbot = {
			'age': 14,
			'name': 'John',
			'favourite colour': 'blue',
			...
		}

- Use python's regular expressions library to deal with variations in spelling and phrasing (use "import re"). Tutorial: https://regexone.com/ 

- Remember previous topics and questions
	e.g.
		What's your name?
		>>> I already told you that!

- Make response time proportional to response length and add occasional typos to make it seem more human

- Add easter eggs

- (Advanced) Do some sentence comprehension so that you can work out the subject and object of the input
	This could be done with python's nltk library (use "pip install nltk" to get it). Tutorial: http://www.nltk.org/book/ch08.html
	
- (Advanced, requires a dataset of human text) Use a Markov Chain to create human-like responses to questions. For example: http://www.onthelambda.com/2014/02/20/how-to-fake-a-sophisticated-knowledge-of-wine-with-markov-chains/
http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/


