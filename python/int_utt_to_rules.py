def rule(intent):
    exception = []
    final_str = 'version: "3.1"\n\nrules:\n\n'
    intent = intent.split('-')
    intents = []
    utters = []
    for k in intent:
        if '=' not in k:
            intents.append(k)
            k = 'utter_'+k
            utters.append(k) 
        else:
            print (k)
    for i in intents:
        intents[intents.index(i)] = i.replace(' ','')
    if intents[0] == '':
        intents.pop(0)
    for i in utters:
        utters[utters.index(i)] = i.replace(' ','')
    utters.pop(0)
    print(len(intents))
    print(len(utters))
    for i in intents:
        print(i)
        final_str = str(final_str+'- rule: Say '+utters[intents.index(i)]+' anytime the user says '+i+'\n')
        final_str = str(final_str+'  steps:\n')
        final_str = str(final_str+'  -  intent: '+i+'\n')
        final_str = str(final_str+'  -  action: '+utters[intents.index(i)]+'\n\n')
    print (final_str)
    print(exception)
    with open('rules.txt',mode = 'w',encoding='utf8') as file:
        file.write(str(final_str))