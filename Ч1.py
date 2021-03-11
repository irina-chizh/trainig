"C:\\Users\\Admin\\Desktop\\Ч_данные.txt"
with open('Чижова_данные.txt', mode='r', encoding="utf-8") as f:
    lines = f.readlines()
print(lines)
class Library():
    """Библиотека"""
    
    total=0 
    def __init__(self): # конструктор, инициализация нового объекта
        self.__x = []
        self.__workHours = [9,18]
        
        
    @staticmethod
    def status():#количество книг в библиотеке
        print("\nВсего книг в библиотеке сейчас",Library.total)
        
    def __str__(self): 
        rep = "Книжный фонд библиотеки\n"
        for i in self.__x:
            rep += str(i) +'\n'
        return(str(rep))
        
    def __iadd__(self,book): 
        self.__x.append(book)
        Library.total += 1
        return(self) 
        
    def __next__(self): 
        self.__count=self.__count+1 
        if self.__count<=len(self.__x): 
            return(self.__x[self.__count-1]) 
        else: 
            raise StopIteration
        
    def __iter__(self): 
        self.__count=0 
        return(self) 
        
    def imp(self): #импорт
        with open('Чижова_данные.txt',mode='r', encoding="utf-8") as f:
            for i in f: 
                book,author,publishinghouse,year=i.split(',') 
                s=[book,author,publishinghouse,year[:-1]] 
                self.__x.append(s)
                Library.total += 1
            return(self.__x) 
    
    def publishingyear(self,yearv): #количество книг в библиотека year года
        j=-1 
        count=0 
        rep = 'В библиотеке '
        for i in self.__x: 
            j+=1 
            if int(self.__x[j][3])==yearv: 
                count+=1 
        rep += str(count) + ' книги '+str(yearv)+' года'
        return(rep)
    
    def exp(self,way): #экспорт 
        n = open (way,"w",encoding='utf-8') 
        main ="\n{:^90}".format('Книги библиотеки') 
        main += "\n{:^30}{:^30}{:^20}{:^10}".format("Автор","Название","Издательство","Год")
        for i in self.__x: 
            main+="\n{:^30}{:^30}{:^20}{:^10}".format(i[0],i[1],i[2],i[3])
            n = open (way,"w",encoding='utf-8') 
            n.write(main) 
            n.close() 
    
    @property
    def workHours(self):
        return self.__workHours

    @workHours.setter
    def workHours(self, workHours):
        if workHours[0] < 0: self.__workHours[0] = 0
        elif workHours[0] > 24: self.__workHours[0] = 24
        else: self.__workHours[0] = workHours[0]

        if workHours[1] < 0: self.__workHours[1] = 0
        elif workHours[1] > 24: self.__workHours[1] = 24
        else: self.__workHours[1] = workHours[1]

        if self.__workHours[0] > self.__workHours[1]: self.__workHours.sort()
        
        
book1=Library() # новый объект
book1.imp() # импортируем файл
print('\n')
#print(book1)
newbook=['Стивен Строгац','Удовольствие от X','Эксмо','2013']
book1 += newbook
book1 += ['Памела Треверс','Мэри Поппинс','Амфора','2013']
print(book1) # выводит 

print(book1.publishingyear(2013)) # сколько книг из библиотеки издавались в этом году
Library.status() # cколько всего книг в библиотеке

book1.exp('Чижова_таблица.txt')

print('\nЧасы работы библиотеки')
print(book1.workHours)
book1.workHours = [10,17]
print(book1.workHours)

