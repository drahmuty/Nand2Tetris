class Parser():

    def __init__(self, file):
        with open(file) as file_object:
            self.file = file_object.readlines()
        self.current_command = ''

    def has_more_commands(self):
        if self.file:
            return True
        else:
            return False

    def advance(self):
        next_command = self.file.pop(0).split('//')[0].strip()
        if next_command:
            self.current_command = next_command
        else:
            self.advance()

    def command_type(self):
        command = self.current_command[0]
        if command == '@':
            return 'A_COMMAND'
        elif command == 'A' or command == 'D' or command == 'M':
            return 'C_COMMAND'
        elif command.isdigit():
            return 'C_COMMAND'
        elif command == '(':
            return 'LABEL'
        else:
            return 'OTHER'

    def is_symbol(self):
        if self.current_command[1:].isdigit():
            return False
        else:
            return True

    def symbol(self):
        if '(' in self.current_command:
            return self.current_command[1:].split(')')[0]
        else:
            return self.current_command[1:]

    def dest(self):
        if '=' in self.current_command:
            return self.current_command.split('=')[0]
        else:
            return ''

    def comp(self):
        if '=' in self.current_command:
            temp = self.current_command.split('=')[1]
        else:
            temp = self.current_command
        return temp.split(';')[0]

    def jump(self):
        if ';' in self.current_command:
            return self.current_command.split(';')[1]
        else:
            return ''
