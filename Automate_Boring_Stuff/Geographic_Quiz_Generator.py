import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Creating 2 files: test and answers
numberOftests = 1
for number in range(numberOftests):
    test = open('%s.  test of capital cities.txt' % (number+1), 'w')
    answersKey = open('%s. Answers.txt' % (number+1), 'w')

    # Head for test number, name and date
    test.write('Test no. %s' % (number+1))
    test.write('\n\n Name: ')
    test.write('\n\n Date: ')

    states = list(capitals.keys())
    random.shuffle(states)
    print(states[0])
    print(capitals[states[0]])
    # print(len(capitals))

    for numberOfQuestion in range(50):
        test.write('\n\n %s. Capital city of %s' %  ((numberOfQuestion+1), states[numberOfQuestion]))

        correctAnswer = capitals[states[numberOfQuestion]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongPropositions = random.sample(wrongAnswers, 3)
        possibleAnswers = wrongPropositions + [correctAnswer]
        # print(len(possibleAnswers))
        random.shuffle(possibleAnswers)
        # print(possibleAnswers)
        for i in range(4):
            test.write('\n    %s. %s' % ('ABCD'[i], possibleAnswers[i]))

        answersKey.write('%s.%s\n' % ((numberOfQuestion+1), 'ABCD'[possibleAnswers.index(correctAnswer)]))















test.close()
answersKey.close()