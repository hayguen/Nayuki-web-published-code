from primrecfunc import *


tests = [
	# Primitive functions
	(Z, [0], 0),
	(Z, [1], 0),
	(Z, [2], 0),
	(Z, [5], 0),
	
	(S, [0], 1),
	(S, [1], 2),
	(S, [2], 3),
	(S, [5], 6),
	
	(I(1,0), [0], 0),
	(I(1,0), [3], 3),
	(I(2,0), [4, 5], 4),
	(I(2,1), [4, 5], 5),
	(I(3,0), [7, 8, 9], 7),
	(I(3,1), [7, 8, 9], 8),
	(I(3,2), [7, 8, 9], 9),
	
	# Boolean functions
	(prnot, [0], 1),
	(prnot, [1], 0),
	
	(prand, [0, 0], 0),
	(prand, [0, 1], 0),
	(prand, [1, 0], 0),
	(prand, [1, 1], 1),
	
	(pror, [0, 0], 0),
	(pror, [0, 1], 1),
	(pror, [1, 0], 1),
	(pror, [1, 1], 1),
	
	(prxor, [0, 0], 0),
	(prxor, [0, 1], 1),
	(prxor, [1, 0], 1),
	(prxor, [1, 1], 0),
	
	(mux, [0, 0, 0], 0),
	(mux, [0, 0, 1], 1),
	(mux, [0, 1, 0], 0),
	(mux, [0, 1, 1], 1),
	(mux, [1, 0, 0], 0),
	(mux, [1, 0, 1], 0),
	(mux, [1, 1, 0], 1),
	(mux, [1, 1, 1], 1),
	(mux, [0, 3, 7], 7),
	(mux, [1, 3, 7], 3),
	(mux, [0, 5, 2], 2),
	(mux, [1, 5, 2], 5),
	
	# Comparison functions
	(z, [0], 1),
	(z, [1], 0),
	(z, [2], 0),
	(z, [5], 0),
	
	(nz, [0], 0),
	(nz, [1], 1),
	(nz, [2], 1),
	(nz, [5], 1),
	
	(eq, [0, 0], 1),
	(eq, [0, 1], 0),
	(eq, [0, 2], 0),
	(eq, [1, 0], 0),
	(eq, [1, 1], 1),
	(eq, [1, 2], 0),
	(eq, [2, 0], 0),
	(eq, [2, 1], 0),
	(eq, [2, 2], 1),
	(eq, [5, 0], 0),
	(eq, [6, 6], 1),
	(eq, [3, 7], 0),
	
	(neq, [0, 0], 0),
	(neq, [0, 1], 1),
	(neq, [0, 2], 1),
	(neq, [1, 0], 1),
	(neq, [1, 1], 0),
	(neq, [1, 2], 1),
	(neq, [2, 0], 1),
	(neq, [2, 1], 1),
	(neq, [2, 2], 0),
	(neq, [5, 0], 1),
	(neq, [6, 6], 0),
	(neq, [3, 7], 1),
	
	(lt, [0, 0], 0),
	(lt, [0, 1], 1),
	(lt, [0, 2], 1),
	(lt, [1, 0], 0),
	(lt, [1, 1], 0),
	(lt, [1, 2], 1),
	(lt, [2, 0], 0),
	(lt, [2, 1], 0),
	(lt, [2, 2], 0),
	(lt, [5, 0], 0),
	(lt, [6, 6], 0),
	(lt, [3, 7], 1),
	
	(le, [0, 0], 1),
	(le, [0, 1], 1),
	(le, [0, 2], 1),
	(le, [1, 0], 0),
	(le, [1, 1], 1),
	(le, [1, 2], 1),
	(le, [2, 0], 0),
	(le, [2, 1], 0),
	(le, [2, 2], 1),
	(le, [5, 0], 0),
	(le, [6, 6], 1),
	(le, [3, 7], 1),
	
	(gt, [0, 0], 0),
	(gt, [0, 1], 0),
	(gt, [0, 2], 0),
	(gt, [1, 0], 1),
	(gt, [1, 1], 0),
	(gt, [1, 2], 0),
	(gt, [2, 0], 1),
	(gt, [2, 1], 1),
	(gt, [2, 2], 0),
	(gt, [5, 0], 1),
	(gt, [6, 6], 0),
	(gt, [3, 7], 0),
	
	(ge, [0, 0], 1),
	(ge, [0, 1], 0),
	(ge, [0, 2], 0),
	(ge, [1, 0], 1),
	(ge, [1, 1], 1),
	(ge, [1, 2], 0),
	(ge, [2, 0], 1),
	(ge, [2, 1], 1),
	(ge, [2, 2], 1),
	(ge, [5, 0], 1),
	(ge, [6, 6], 1),
	(ge, [3, 7], 0),
	
	(even, [0], 1),
	(even, [1], 0),
	(even, [2], 1),
	(even, [3], 0),
	(even, [4], 1),
	(even, [5], 0),
	
	(divisible, [0, 0], 1),
	(divisible, [1, 0], 0),
	(divisible, [2, 0], 0),
	(divisible, [0, 1], 1),
	(divisible, [1, 1], 1),
	(divisible, [2, 1], 1),
	(divisible, [0, 2], 1),
	(divisible, [1, 2], 0),
	(divisible, [2, 2], 1),
	(divisible, [3, 2], 0),
	(divisible, [0, 3], 1),
	(divisible, [1, 3], 0),
	(divisible, [2, 3], 0),
	(divisible, [3, 3], 1),
	(divisible, [4, 3], 0),
	(divisible, [5, 3], 0),
	(divisible, [6, 3], 1),
	(divisible, [7, 5], 0),
	(divisible, [25, 5], 1),
	
	(prime, [ 0], 0),
	(prime, [ 1], 0),
	(prime, [ 2], 1),
	(prime, [ 3], 1),
	(prime, [ 4], 0),
	(prime, [ 5], 1),
	(prime, [ 6], 0),
	(prime, [ 7], 1),
	(prime, [ 8], 0),
	(prime, [ 9], 0),
	(prime, [10], 0),
	(prime, [11], 1),
	(prime, [12], 0),
	(prime, [13], 1),
	(prime, [14], 0),
	(prime, [15], 0),
	(prime, [16], 0),
	(prime, [17], 1),
	(prime, [18], 0),
	(prime, [19], 1),
	(prime, [20], 0),
	(prime, [21], 0),
	(prime, [22], 0),
	(prime, [23], 1),
	(prime, [24], 0),
	(prime, [25], 0),
	(prime, [26], 0),
	(prime, [27], 0),
	(prime, [28], 0),
	(prime, [29], 1),
	(prime, [30], 0),
	
	# Arithmetic functions
	(const(0), [0], 0),
	(const(0), [9], 0),
	(const(1), [0], 1),
	(const(1), [1], 1),
	(const(1), [3], 1),
	(const(2), [0], 2),
	(const(2), [1], 2),
	(const(2), [2], 2),
	(const(3), [0], 3),
	(const(3), [3], 3),
	(const(3), [5], 3),
	
	(pred, [0], 0),
	(pred, [1], 0),
	(pred, [2], 1),
	(pred, [3], 2),
	(pred, [9], 8),
	
	(add, [0, 0], 0),
	(add, [0, 1], 1),
	(add, [0, 3], 3),
	(add, [1, 0], 1),
	(add, [2, 0], 2),
	(add, [1, 1], 2),
	(add, [2, 5], 7),
	(add, [6, 3], 9),
	
	(sub, [0, 0], 0),
	(sub, [0, 1], 0),
	(sub, [0, 2], 0),
	(sub, [1, 0], 1),
	(sub, [1, 1], 0),
	(sub, [1, 2], 0),
	(sub, [2, 0], 2),
	(sub, [2, 1], 1),
	(sub, [2, 2], 0),
	(sub, [2, 3], 0),
	(sub, [3, 0], 3),
	(sub, [5, 2], 3),
	(sub, [7, 6], 1),
	
	(subrev, [0, 0], 0),
	(subrev, [1, 0], 0),
	(subrev, [2, 0], 0),
	(subrev, [0, 1], 1),
	(subrev, [1, 1], 0),
	(subrev, [2, 1], 0),
	(subrev, [0, 2], 2),
	(subrev, [1, 2], 1),
	(subrev, [2, 2], 0),
	(subrev, [3, 2], 0),
	(subrev, [0, 3], 3),
	(subrev, [2, 5], 3),
	(subrev, [6, 7], 1),
	
	(diff, [0, 0], 0),
	(diff, [0, 1], 1),
	(diff, [0, 2], 2),
	(diff, [1, 0], 1),
	(diff, [1, 1], 0),
	(diff, [1, 2], 1),
	(diff, [2, 0], 2),
	(diff, [2, 1], 1),
	(diff, [2, 2], 0),
	(diff, [5, 0], 5),
	(diff, [6, 6], 0),
	(diff, [3, 7], 4),
	
	(min, [0, 0], 0),
	(min, [0, 1], 0),
	(min, [0, 2], 0),
	(min, [1, 0], 0),
	(min, [1, 1], 1),
	(min, [1, 2], 1),
	(min, [2, 0], 0),
	(min, [2, 1], 1),
	(min, [2, 2], 2),
	(min, [3, 0], 0),
	(min, [5, 2], 2),
	(min, [7, 6], 6),
	
	(max, [0, 0], 0),
	(max, [0, 1], 1),
	(max, [0, 2], 2),
	(max, [1, 0], 1),
	(max, [1, 1], 1),
	(max, [1, 2], 2),
	(max, [2, 0], 2),
	(max, [2, 1], 2),
	(max, [2, 2], 2),
	(max, [3, 0], 3),
	(max, [5, 2], 5),
	(max, [7, 6], 7),
	
	(mul, [0, 0], 0),
	(mul, [0, 1], 0),
	(mul, [0, 2], 0),
	(mul, [1, 0], 0),
	(mul, [3, 0], 0),
	(mul, [1, 1], 1),
	(mul, [1, 2], 2),
	(mul, [2, 1], 2),
	(mul, [2, 2], 4),
	(mul, [3, 7], 21),
	(mul, [5, 8], 40),
	
	(exp, [0, 0], 1),
	(exp, [0, 1], 0),
	(exp, [0, 2], 0),
	(exp, [1, 0], 1),
	(exp, [1, 1], 1),
	(exp, [1, 2], 1),
	(exp, [2, 0], 1),
	(exp, [2, 1], 2),
	(exp, [2, 2], 4),
	(exp, [2, 3], 8),
	(exp, [2, 4], 16),
	(exp, [2, 5], 32),
	(exp, [2, 6], 64),
	(exp, [2, 7], 128),
	(exp, [2, 8], 256),
	(exp, [2, 9], 512),
	(exp, [3, 1], 3),
	(exp, [3, 2], 9),
	(exp, [4, 3], 64),
	(exp, [5, 3], 125),
	(exp, [6, 2], 36),
	
	(div, [ 0, 0], 0),
	(div, [ 1, 0], 1),
	(div, [ 2, 0], 2),
	(div, [ 3, 0], 3),
	(div, [ 0, 1], 0),
	(div, [ 1, 1], 1),
	(div, [ 2, 1], 2),
	(div, [ 3, 1], 3),
	(div, [ 0, 2], 0),
	(div, [ 1, 2], 0),
	(div, [ 2, 2], 1),
	(div, [ 3, 2], 1),
	(div, [ 4, 2], 2),
	(div, [11, 2], 5),
	(div, [14, 2], 7),
	(div, [ 0, 3], 0),
	(div, [ 1, 3], 0),
	(div, [ 2, 3], 0),
	(div, [ 3, 3], 1),
	(div, [ 4, 3], 1),
	(div, [ 5, 3], 1),
	(div, [ 6, 3], 2),
	(div, [11, 3], 3),
	(div, [18, 3], 6),
	(div, [ 8, 4], 2),
	(div, [ 0, 4], 0),
	(div, [23, 4], 5),
	(div, [20, 5], 4),
	(div, [21, 5], 4),
	(div, [ 5, 6], 0),
	(div, [30, 6], 5),
	(div, [ 2, 7], 0),
	(div, [19, 7], 2),
	
	(mod, [0, 0], 0),
	(mod, [1, 0], 1),
	(mod, [2, 0], 2),
	(mod, [3, 0], 3),
	(mod, [0, 1], 0),
	(mod, [1, 1], 0),
	(mod, [2, 1], 0),
	(mod, [3, 1], 0),
	(mod, [0, 2], 0),
	(mod, [1, 2], 1),
	(mod, [2, 2], 0),
	(mod, [3, 2], 1),
	(mod, [0, 3], 0),
	(mod, [1, 3], 1),
	(mod, [2, 3], 2),
	(mod, [3, 3], 0),
	(mod, [4, 3], 1),
	(mod, [5, 3], 2),
	(mod, [7, 4], 3),
	(mod, [21, 5], 1),
	(mod, [30, 6], 0),
	(mod, [19, 7], 5),
	
	(factorial, [0], 1),
	(factorial, [1], 1),
	(factorial, [2], 2),
	(factorial, [3], 6),
	(factorial, [4], 24),
	(factorial, [5], 120),
	(factorial, [6], 720),
]


if __name__ == "__main__":
	print("Testing {} cases...".format(len(tests)))
	failed = False
	for (f, arg, ans) in tests:
		actual = f.eval(arg)
		if actual != ans:
			if not failed:
				print("One or more tests failed:")
				failed = True
			print("    {} {} = {} != {}".format(str(f), str(arg), str(actual), str(ans)))
	if not failed:
		print("All tests passed")
