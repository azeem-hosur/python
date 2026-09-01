# Precedence Order
# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	                                         Description
# ()	                                             Parentheses	
# **	                                             Exponentiation	
# +x -x  ~x	                                         Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	                                     Multiplication, division, floor division, and modulus	
# +  -	                                             Addition and subtraction	
# <<  >>	                                         Bitwise left and right shifts	
# &	                                                 Bitwise AND	
# ^	                                                 Bitwise XOR	
# |	                                                 Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	     Comparisons, identity, and membership operators	
# not	                                             Logical NOT	
# and	                                                AND	
# or	                                                OR


# Parentheses has the highest precedence, 
# meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +, 
# and therefore multiplications are evaluated before additions:
print(100 + 5 * 3)

# Left-to-Right Evaluation
# If two operators have the same precedence, the expression is evaluated from left to right.
# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5 + 4 - 7 + 3)