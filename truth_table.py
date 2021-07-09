class TruthTable:

	def logical_true(self, condition):
		return True

	def tautology(self, x, y):
		return True
		return not (x and y) or (x or y)

	def logical_false(self, condition):
		return False

	def contradiction(self, x, y):
		return not (x or y) and (x and y)
		return (not x and not y) and (x and y)
		return not (not (x and y) or (x or y))
		return not x and not y and x and y
		return False

	def logical_identity(self, condition):
		return condition

	def logical_negation(self, condition):
		return False if condition else True
		if condition:
			return False
		else:
			return True

	def logical_conjunction(self, x, y):
		return x and y
		if x:
			if y:
				return True
		else:
			return False

	def logical_disjunction(self, x, y):
		if x:
			return True
		if y:
			return True

	def logical_equality(self, x, y):
		return not (x or y) or (x and y)
		return not ((not x or not y) and (x or y))
		return not (not (x and y) and (x or y))
		return not ((not y and x) or (not x and y))
		return True if x == y else False
		if x == y:
			return True
		else:
			return False

	def logical_nand(self, x, y):
		return not (x and y)
		return not x or not y
		return self.logical_negation(x) or self.logical_negation(y)
		return self.logical_negation(self.logical_conjunction(x, y))

	def logical_nor(self, x, y):
		return not x and not y
		return not (x or y)
		return not x and not y
		return self.logical_negation(x) and self.logical_negation(y)
		return self.logical_negation(self.logical_disjunction(x, y))

	def converse_nonimplication(self, x, y):
		return not x and y
		return not (x or not y)
		return self.logical_negation(
			self.logical_disjunction(x, self.logical_negation(y)
			)
		)

	def logical_implication(self, x, y):
		return not x or y
		return self.logical_disjunction(self.logical_negation(x), y)

	def converse_implication(self, x, y):
		return not y or x
		return x or not y
		return self.logical_disjunction(x, self.logical_negation(y))

	def material_nonimplication(self, x, y):
		return not y and x
		return x and not y
		return not (not x or y)
		return self.logical_negation(
			self.logical_disjunction(
				self.logical_negation(x), y
			)
		)

	def exclusive_disjunction(self, x, y):
		return not (x and y) and (x or y)
		return (not x or not y) and (x or y)
		return (x or y) and not (x and y)
		return (not y and x) or (not x and y)
		return (x and not y) or (not x and y)
		return self.logical_disjunction(
			self.logical_conjunction(x, self.logical_negation(y)),
			self.logical_conjunction(self.logical_negation(x), y)
		)

	def negate_first(self, x, y):
		return not x
		return self.logical_negation(x)

	def negate_second(self, x, y):
		return not y
		return self.logical_negation(y)

	def project_first(self, x, y):
		return x

	def project_second(self, x, y):
		return y

	def __repr__(self):
		return '''
        True
        False
        not True
        not False

        x and y                     - logical conjunction
        not x and y                 - logical nonimplication
        not y and x                 - material nonimplication
        not (x and y)               - logical NAND - not and
        not (x and y) and (x or y)  - XOR - exclusive or
        not (x or y) and (x and y)  - contradiction

        x or y                      - logical disjunction
        not x or y                  - logical implication
        not y or x                  - converse implication
        not (x or y)                - logical NOR - not or
        not (x or y) or (x and y)   - logical equality aka logical biconditional
        not (x and y) or (x or y)   - tautology == logical true
        '''