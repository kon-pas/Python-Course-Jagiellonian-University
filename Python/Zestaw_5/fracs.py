def reduce_frac(frac):
	if frac[1] == 0:
		return ZeroDivisionError

	a, b = int(frac[0]), int(frac[1])
	while b != 0:
		c = a % b
		a = b
		b = c
	frac[0], frac[1] = int(frac[0] / a), int(frac[1] / a)

	if frac[0] > 0 > frac[1]:
		frac[0], frac[1] = -frac[0], -frac[1]

	return [frac[0], frac[1]]

def add_frac(frac1, frac2):
	return reduce_frac([frac1[0]*frac2[1] + frac2[0]*frac1[1], frac1[
		1]*frac2[1]])

def sub_frac(frac1, frac2):
	return reduce_frac([frac1[0]*frac2[1] - frac2[0]*frac1[1], frac1[
		1]*frac2[1]])

def mul_frac(frac1, frac2):
	return reduce_frac([frac1[0]*frac2[0], frac1[1]*frac2[1]])

def div_frac(frac1, frac2):
	return reduce_frac([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_zero(frac):
	return bool(frac[0] == 0)

def is_positive(frac):
	if is_zero(frac):
		return False
	return bool(frac[0] * frac[1] > 0)

def frac2float(frac):
	return float(frac[0] / frac[1])

def cmp_frac(frac1, frac2):  # -1 | 0 | +1
	difference = frac2float(frac1) - frac2float(frac2)
	if difference > 0:
		return 1
	elif difference == 0:
		return 0
	else:
		return -1
