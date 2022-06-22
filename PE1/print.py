print('Hello, Wolrd!')

# invocação da função
# function_name(argument)

# newline
print()

# ex:
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

# The itsy bitsy spider climbed up the waterspout.

# Down came the rain and washed the spider out.

# caractere de escape (\)
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

# The itsy bitsy spider
# climbed up the waterspout.

# Down came the rain
# and washed the spider out.

#  strings
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

# output
# The itsy bitsy spider climbed up the waterspout.

print("My name is", "Python.")
print("Monty Python.")

# My name is Python.
# Monty Python.

print("My name is", "Python.", end=" ")
print("Monty Python.")

# My name is Python. Monty Python.

print("My name is ", end="")
print("Monty Python.")

# My name is Monty Python.

print("My", "name", "is", "Monty", "Python.", sep="-")

# My-name-is-Monty-Python.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

# My_name_is*Monty*Python.*

print("    *\n   * *\n  *   *\n *     *\n*       *\n***   ***\n  *   *\n  *   *\n  *****")
 
#     *
#    * *
#   *   *
#  *     *
# *       *
# ***   ***
#   *   *
#   *   *
#   *****

print("string" * 2)
# stringstring

print(0o123)
# 83

print(0x123)
# 291
