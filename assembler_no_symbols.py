from class_parser import Parser
from class_code import dest, comp, jump, int_to_bin

def assemble(file):
	
	# Initialize source file
	x = Parser(file)

	# Create destination filename
	output_filename = file[:-4] + '.hack'

	# Create temporary array to store output
	output_array = []

	# Main loop
	while x.has_more_commands():

		# Move to next command
		x.advance()
		
		# Return binary code based on command type
		command_type = x.commandType()

		if command_type == 'A_COMMAND':
			binary_command = '0' + int_to_bin(x.symbol())
			output_array.append(binary_command)
			print(binary_command)

		elif command_type == 'C_COMMAND':
			c = comp(x.comp())
			d = dest(x.dest())
			j = jump(x.jump())
			binary_command = '111' + c + d + j
			output_array.append(binary_command)
			print(binary_command)

	# Write to destination file
	with open(output_filename, 'w') as output_file:
		for t in output_array:
			output_file.write(t + '\n')
