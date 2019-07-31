from class_parser import Parser
from class_symbol_table import Symbol_Table
from class_code import dest, comp, jump, int_to_bin

def assemble(file):
	
	# Initialize source file for first pass
	x = Parser(file)

	# Initialize symbol table
	st = Symbol_Table()

	# Create destination filename
	output_filename = file[:-4] + '.hack'

	# Create temporary array to store output
	output_array = []

	# Set ROM address to 0
	rom_address = 0

	# First pass
	while x.has_more_commands():

		# Move to the next command
		x.advance()

		# Get command type and symbol
		command_type = x.command_type()
		label = x.symbol()

		# Add labels to symbol table
		if command_type == 'LABEL':
			if not st.contains(label):
				st.add_entry(label, rom_address)

		# Incrememnt ROM address for A and C commands
		elif command_type == 'A_COMMAND' or command_type == 'C_COMMAND':
			rom_address += 1

	# Initialize source file for second pass
	x = Parser(file)

	# Second pass
	while x.has_more_commands():

		# Move to the next command
		x.advance()
		
		# Get command type
		command_type = x.command_type()

		# Handle A commands
		if command_type == 'A_COMMAND':

			# Get A command value
			symbol = x.symbol()

			# Handle symbols
			if x.is_symbol():

				# Return symbol address for existing symbols in table
				if st.contains(symbol):
					temp = st.get_address(symbol)
					binary_command = '0' + int_to_bin(temp)

				# Add new symbol to table if it doesn't already exist
				else:
					st.add_entry(symbol, st.next_rom_address())
					temp = st.get_address(symbol)
					binary_command = '0' + int_to_bin(temp)

			# Handle integers
			else:
				binary_command = '0' + int_to_bin(symbol)
			
			# Add binary command to output array
			output_array.append(binary_command)
			print(binary_command)

		# Handle C commands
		elif command_type == 'C_COMMAND':
			c = comp(x.comp())
			d = dest(x.dest())
			j = jump(x.jump())
			binary_command = '111' + c + d + j
			output_array.append(binary_command)
			print(binary_command)

	# # Write to destination file
	with open(output_filename, 'w') as output_file:
		for t in output_array:
			output_file.write(t + '\n')
