usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']

input_username = input('Enter username: ')

if input_username in usernames:
    print('Access Granted')
else:
    print('Access Denied')
