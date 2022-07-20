def rule(intents,utters):
    exception = []
    final_str = 'version: "3.1"\n\nrules:\n\n'
    intents = intents.split('-')
    utters = utters.split('-')
    for i in intents:
        intents[intents.index(i)] = i.replace(' ','')
    if intents[0] == '':
        intents.pop(0)
    for i in utters:
        utters[utters.index(i)] = i.replace(' ','')
    if utters[0] == '':
        utters.pop(0)
    print(intents)
    for i in intents:
        if '=' not in i:
            final_str = str(final_str+'- rule: Say '+utters[intents.index(i)]+' anytime the user says '+i+'\n')
            final_str = str(final_str+'  steps:\n')
            final_str = str(final_str+'  -  intent: '+i+'\n')
            final_str = str(final_str+'  -  action: '+utters[intents.index(i)]+'\n\n')
        else:
            exception.append(i)
    print (final_str)
    print(exception)
    with open('rules.txt',mode = 'w',encoding='utf8') as file:
        file.write(str(final_str))