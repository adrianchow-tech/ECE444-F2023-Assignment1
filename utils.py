#Utility functions

class Utils:
    def reversed(self, input):
        output = -1

        if isinstance(input, int):
            input_string    = str(input)
            reversed_input  = input_string[::-1]
            output          = int(reversed_input)
        else:
            print("[Reversed Error] Input must be an integer")

        return output
    
    def formatter(self, input):
        output_bin      = -1
        output_octal    = -1

        if isinstance(input, int):
            output_bin      = bin(input)
            output_octal    = oct(input)
        else:
            print("[Formatter Error] Input must be an integer")

        return output_bin, output_octal
