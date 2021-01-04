import csv
import statistics


def horo_comp(horoLis):
    #https://www.kaggle.com/aagghh/python-vs-astrology-testing-zodiac-predictions
    horoDict = {}
    with open('Horo.csv', newline='') as csvfile:
        horoFile = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in horoFile:
            temp = row[0]
            horoDict[temp[:temp.find(',')]] = temp[temp.find(',')+1:]

    compats = []
    for i in horoLis:
        for x in horoLis:
            if not i == x:
                compats.append(float(horoDict[i+x]))
    return statistics.mean(compats)

def mbti_comp(mbtiLis):
    #https://www.erikthor.com/relationships/
    mbtiDict = {}
    with open('MBTI.csv', newline='') as csvfile:
        mbtiFile = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in mbtiFile:
            temp = row[0]
            mbtiDict[temp[:temp.find(',')]] = temp[temp.find(',')+1:]

    compats = []
    for i in mbtiLis:
        for x in mbtiLis:
            if not i == x:
                try:
                    compats.append(float(mbtiDict[i+'-'+x]))
                except:
                    compats.append(float(mbtiDict[x+'-'+i]))
    return statistics.mean(compats)

def ennea_comp(enneaLis):
    #https://enneagram.bz/en/types/compatibility
    enneaDict = {}
    with open('Ennea.csv', newline='') as csvfile:
        enneaFile = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in enneaFile:
            temp = row[0]
            enneaDict[temp[:temp.find(',')]] = temp[temp.find(',')+1:]

    compats = []
    for i in enneaLis:
        for x in enneaLis:
            if not i == x:
                compats.append(float(enneaDict[i+':'+x]))
    return statistics.mean(compats)

def overall_comp(horo, mbti, ennea):
    overall = statistics.mean([horo,mbti,ennea])
    return round(overall)

def test_partner(lisNames):
    dict = {'hList':[], 'mList':[], 'eList':[]}
    hList = []; mList = []; eList = []
    for i in lisNames:
        dict['hList'].append(input(i + " horoscope: "))
        dict['mList'].append(input(i + " myers-briggs: "))
        dict['eList'].append(input(i + " enneagram: "))
    return dict

def group_match():
    num = input('number of people in the group: ')
    people = []
    for i in range(int(num)):
        people.append(input('name ' + str(i+1) + ': ') + "'s")
    return test_partner(people)

def single_match():
    partner = input('who are you testing compatibility with ;) ? ')
    return test_partner(['your', partner + "'s"])

# Script code
if __name__ == '__main__':
    choice = input('single or group compatibility? ' )
    if choice == 'single':
        all = single_match()
    else:
        all = group_match()

    cHoro = horo_comp(all['hList'])
    cMBTI = mbti_comp(all['mList'])
    cEnnea = ennea_comp(all['eList'])
    cOverall = overall_comp(cHoro, cMBTI, cEnnea)

    print('your horoscope compatibility: '+str(cHoro)+' %')
    print('your myers-briggs compatibility: '+str(cMBTI)+' %')
    print('your enneagram compatibility: '+str(cEnnea)+' %')
    print('your overall compatibility: '+str(cOverall)+' %')
