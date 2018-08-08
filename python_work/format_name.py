def get_formatted_name(first_name, middle_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('Franklin', 'the', 'Turtle')
print(musician)

musician = get_formatted_name('Jimmi', '', 'Hendrix')
print(musician)
