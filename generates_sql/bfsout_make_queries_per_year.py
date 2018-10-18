for i in range(1800, 1900):
	basic_query = "select count(1) from profiles_bfsjoined where birth_year is not null and death_year is not null and birth_year > 1700 and birth_year <= {} and death_year >= {}".format(i, i)
	print(basic_query + ";")
	#print(basic_query + " and gender = 'male';")
	#print(basic_query + " and gender = 'female';")
for i in range(1900, 2011):
	basic_query = "select count(1) from profiles_bfsjoined where birth_year is not null and birth_year > 1700 and birth_year <= {} and ((death_year is not null and death_year >= {}) or is_alive = true)".format(i, i)
	print(basic_query + ";")
	#print(basic_query + " and gender = 'male';")
	#print(basic_query + " and gender = 'female';")
