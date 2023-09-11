#Unit tests

from utils import Utils

utils_instance = Utils()

#########################Test reveresed###################################
#Strings
print("[Reversed] Input: hello, Output: "   + str(utils_instance.reversed("hello")))
print("[Reversed] Input: , Output: "        + str(utils_instance.reversed("")))

#Integers
print("[Reversed] Input: 123, Output: "     + str(utils_instance.reversed(123)))
print("[Reversed] Input: 1, Output: "       + str(utils_instance.reversed(1)))
print("[Reversed] Input: 647, Output: "     + str(utils_instance.reversed(647)))

#Floats
print("[Reversed] Input: 0.0, Output: "     + str(utils_instance.reversed(0.0)))
print("[Reversed] Input: 1.0, Output: "     + str(utils_instance.reversed(1.0)))
print("[Reversed] Input: 123.0, Output: "   + str(utils_instance.reversed(123.0)))

#########################Test formatter####################################
#Strings
bin, oct = utils_instance.formatter("hello")
print("[Formatter] Input: hello, Binary: "  + str(bin) + " Octal: " + str(oct))

#Integers
bin, oct = utils_instance.formatter(123)
print("[Formatter] Input: 123, Binary: "  + str(bin) + " Octal: " + str(oct))

bin, oct = utils_instance.formatter(1)
print("[Formatter] Input: 1, Binary: "  + str(bin) + " Octal: " + str(oct))

bin, oct = utils_instance.formatter(647)
print("[Formatter] Input: 647, Binary: "  + str(bin) + " Octal: " + str(oct))

#Floats
bin, oct = utils_instance.formatter(0.0)
print("[Formatter] Input: 0.0, Binary: "  + str(bin) + " Octal: " + str(oct))

bin, oct = utils_instance.formatter(1.0)
print("[Formatter] Input: 1.0, Binary: "  + str(bin) + " Octal: " + str(oct))

bin, oct = utils_instance.formatter(123.0)
print("[Formatter] Input: 123.0, Binary: "  + str(bin) + " Octal: " + str(oct))