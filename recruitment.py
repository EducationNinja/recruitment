def main():
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}
	name = input("Name: ")
	age = input("Age: ")
	experience = input("Experiance: ")

	cv['name'] = name
	cv['age'] = age
	cv['experience'] = experience
	cv['skills'] = []

	for index, value in enumerate(skills):
		print(f"{index+1}. {value}")

	skill = input("Skill: ")
	dj_khaled = input("Another One: ")

	cv['skills'].append(skills[int(skill)-1])
	cv['skills'].append(skills[int(dj_khaled)-1])

	if (25<int(cv['age'])<40) and (int(cv["experience"]) > 5) and (skills[5] in cv['skills']):
		print("accepted")
	else:
		print("rejected")


if __name__ == '__main__':
	main()