for i in range(1800, 2011):
	basic_query = "select count(1) from profiles where birth_year is not null and death_year is not null and birth_year > 1700 and birth_year <= {} and death_year >= {}".format(i, i)
	print(basic_query + ";")
	print(basic_query + " and gender = 'male';")
	print(basic_query + " and gender = 'female';")
