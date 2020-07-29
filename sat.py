def compute_percentile(scores):
	totalScore = maths + verbal + writing
	if totalScore >= 2200:
		print("The SAT score is in the 99 percentile.")
	elif 2000 <= totalScore < 2200:
		print("The SAT score is in the 95 percentile.")
	elif 1500 <= totalScore < 2000:
		print("The SAT score is in the 50 percentile.")
	elif totalScore < 1500:
		print("The SAT score is in the 10 percentile.")

def compute_IQ(maths, verbal):
	IQ = (0.095 * maths) + (0.003 * verbal) + 50.241
	return round(IQ,2)

scores = list(map(int, input("Enter scores: ").split()))
verbal = scores[0]
maths = scores[1]
writing = scores[2]

compute_percentile(scores)
print("The IQ score is " + str(compute_IQ(maths,verbal)) + ".")

if maths > 600 and verbal > 600 and writing > 600:
	print("Wow, this is amazing!")
elif compute_IQ(maths,verbal) >= 120:
	print("Wow, this is amazing!")