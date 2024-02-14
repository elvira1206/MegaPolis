def readfile(songs.csv):
    '''
    Read file and create list of students
    :param namefile: str, name file
    :return: list of students
    '''
    f=open(songs.csv,'r',encoding='utf-8')
    songs=[]
    for i in range(200):
        songs.append(f.readline().strip().split(';'))
        if songs[i][0]=='0':
            songs[i][0]='0'
    return songs


def repl():
    '''Замена ошибочной оценки 'None' на среднюю орифметическую по классу
    '''
    day,month,year=int(songs[i][3].split('.'))
    for i in range(1,200):
        if songs[i][4]=='0':
            songs[i][4] = str(((01-int(day))+(01-int(month))+(2002-int(year))/(len(songs[i][1].)+len(songs[i][2])))*10000)

def findstudent(f,im):
    '''
    Find student project
    param f: str, family
    param i: str, name'''
    for i in range(1,200):
        if int(year)>'2002':
            print(f'Название: {songs[i][2]}, артист - {songs[i][1]}, кол-во прослушиваний - {songs[i][0]}')

def writefile(name):
    '''
    Write new file with hash-key
    :param name: str, name file
    '''
    f = open(songs_new.csv, 'w', encoding='utf-8')
    f.write(','.join(songs[0])+'\n')
    for i in range(1,200):
        f.write(','.join(songs[i]) + '\n')
    f.close()

'''
songs=readfile('songs.csv')
repl()
findstudent('Хадаров','Владимир')
writefile('student_new.csv')
'''