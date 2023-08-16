#There are questions about improving python skills. 

#CLASSES
"""
ARMSTRONG NUMBER:
x = (input("Enter a value: "))
class Number:
    def __init__(self, x):
        self.x = x


    def findingTheArmstrongNumber(self):
        self.emptyList = list()
        for self.numberIndex in self.x:
            self.emptyList.append(int(self.numberIndex))
        print("List of numbers in entered number: {}".format(self.emptyList))

    def processOnEmptyList(self):
        self.findingTheArmstrongNumber()
        self.emptyList2 = list()
        self.result = 0
        self.basamakIndex = int(len(x))
        for self.numberIndex in self.emptyList:
            self.result = self.numberIndex ** int(self.basamakIndex)
            self.emptyList2.append(int(self.result))
        print("List of total powers as order numbers of values in list of numbers(in entered number): {}".format(self.emptyList2))
        self.processOnEmptyListTwo()

    def processOnEmptyListTwo(self):

        self.total = 0
        for self.itemIndex in self.emptyList2:
            self.total = self.total + self.itemIndex
        print("Total Number in list of total powers: {}".format(self.total))
        if (self.total == int(self.x)):
            print("Finally; {} is an Armstrong Number.".format(self.x))
        else:
            print("Finally; {} is not an Armstrong Number.".format(self.x))

object = Number(x)
(object.processOnEmptyList())

----------------------------------------

AMAZING NUMBER:
class Number:
    def __init__(self, x):
        self.x = x

    def findingTheTamSayi(self):
        self.emptyList = []
        for self.values in range(1,self.x):
            if (self.x % self.values == 0):
                self.emptyList.append(self.values)
        print(self.emptyList)

    def displayAmazing(self):
        self.findingTheTamSayi()
        self.total = 0
        for self.values in self.emptyList:
            self.total = self.total + self.values
        print(self.total)

        if (self.total == self.x):
            condition1 = "{} mükemmel sayıdır.".format(self.x)
            return condition1
        else:
            condition2 = "{} mükemmel sayı değildir.".format(self.x)
            return condition2

x = int(input("enter the number: "))
a = Number(x)
print(a.displayAmazing())

----------------------------------------

MOVIE CLASS:
class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie classı oluşturuldu..")
    #   print("{} filminin yönetmeni {} dur ve film {} sürmüştür.".format(self.title,self.director,self.duration))
   #def __str__(self):
#       a = ("'{}' filminin yönetmeni '{}' ve film {} sürmüştür.".format(m1.title, m1.director, m1.duration))
#       return a
#       print("'{}' filminin yönetmeni '{}' ve film {} sürmüştür.".format(m1.title, m1.director, m1.duration))
    def __str__(self):
        a = "'{}' filminin yönetmeni '{}' ve film {} dakika sürmüştür.".format(self.title,self.director,self.duration)
        return a
    def __len__(self):
        return self.duration
    def __del__(self):
         print("Tanımladığınız m1 objesi silindi...")

m1 = Movie("Fury","Tom Hanks",120)
#print(m1)
#print(len((m1)))
print(m1)

----------------------------------------

QUIZ APPLICATION
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return (self.answer == answer)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print("\nSoru {}: {}".format(self.questionIndex+1,question.text))

        for q in question.choices:
            print("-{}".format(q))
        answer = input("\ncevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("\nTaken score is: {}".format(self.score))

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitmiştir...")
        else:
            print(" Question {} of {} ".format(questionNumber,totalQuestion).center(100,"*"))


q1 = Question("En iyi programlama dili hangisidir ?" , ["C#","python","javascript","java"],"python")
q2 = Question("En popüler programlama dili hangisidir ?" , ["python","C#","java","javascript"],"python")
q3 = Question("En çok kazandıran programlama dili hangisidir ?" , ["javascript","java","C#","python"],"python")
q4 = Question("en çok sevilen programlama dili hangisidir ?" , ["C#","python","javascript","java"],"python")
q5 = Question("en zor programlama dili hangisidir ?" , ["PYTHON","C#","java","javascript"],"python")

questions = [q1,q2,q3,q4,q5]
quiz = Quiz(questions)
quiz.loadQuestion()

----------------------------------------------------------------------------

ODD NUMBERS BETWEEN 1 AND 100
class SpecialNumber:
    def __init__(self):
        self.emptyList = []
    def findingTheOddNumbers(self):
        for self.numbers in range(1,100):
            self.numbers = 2 * self.numbers
            self.emptyList.append(self.numbers)
        return self.emptyList
result = SpecialNumber()
print(result.findingTheOddNumbers())
"""

#----------------------------------------------------------------------------

#FUNCTIONS
"""
GRADİNG QUESTION:
a = int(input('midterm: '))
b = int(input('assignment: '))
c = int(input('final: '))
def score(a,b,c):
    Overallscoreis = ((a*30)/100 + (b*30)/100 + (c*40)/100)
    print("Overall score: ",Overallscoreis)
    return Overallscoreis
def letterGrade(Overallscoreis):
    if Overallscoreis > 100:
        theCorrespondigLetterGradeis = "Error"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    elif Overallscoreis >= 85:
        theCorrespondigLetterGradeis = "AA"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    elif Overallscoreis >= 75:
        theCorrespondigLetterGradeis = "BA"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    elif Overallscoreis >= 70:
        theCorrespondigLetterGradeis = "BB"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    elif Overallscoreis >= 65:
        theCorrespondigLetterGradeis = "CB"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    elif Overallscoreis >= 60:
        theCorrespondigLetterGradeis = "CC"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    elif Overallscoreis >= 55:
        theCorrespondigLetterGradeis = "DC"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    elif Overallscoreis >= 40:
        theCorrespondigLetterGradeis = "DD"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    else:
        theCorrespondigLetterGradeis = "FF"
        print("The corresponding letter grade: ", theCorrespondigLetterGradeis)
    return theCorrespondigLetterGradeis
total = letterGrade(score(int(a),int(b),int(c)))

----------------------------------------

COMPLICATED ENCRYPTION APPLICATION 
import string
import os

alfabe= string.ascii_lowercase
max_karakter= len(alfabe)

temizle= ("cls" if os.name == "nt" else "clear")

def seçenekler():
	while True:
		os.system(temizle)
		seçenek= input("Ne yapmak istersin: ").lower()
		if seçenek in ("şifrele","şifreleme","şifreleme yap","şifreleme yapmak","şifreleme yapmak isterim"):
			şifreleme()
		elif seçenek in ("şifre çöz,şifreyi çöz"):
			şifre_çöz()
		else:
			print("Şifreleme yapmak için (%s) yazın, şifre çözmek için (%s) yazın." % ("şifrele","şifre çöz"))

def şifreleme():
	metin= input("Şifrelenecek metni girin: ").lower()
	şifreleme_anahtarı= şifrelemeAnahtarı()
	şifrelenmiş_metin= ""
	for karakter in metin:
		if karakter.isalpha():
			karakter_sıra_no= ord(karakter)
			karakter_sıra_no += şifreleme_anahtarı

			if karakter_sıra_no > ord("z"):
				karakter_sıra_no -= max_karakter

			elif karakter_sıra_no < ord("a"):
				karakter_sıra_no += max_karakter

			şifreli_karakter= chr(karakter_sıra_no)
			şifrelenmiş_metin += şifreli_karakter

		else:
			şifrelenmiş_metin += karakter
	os.system(temizle)
	print("%s kelimesinin %d anahtarıyla şifrelenmiş hali %s" % (metin,şifreleme_anahtarı,şifrelenmiş_metin))
	input("Devam etmek için bir tuşa basın")

def şifre_çöz():
	şifreli_metin= input("Çözülecek şifreli metni girin: ").lower()
	şifreleme_anahtarı= şifrelemeAnahtarı()
	çözülmüş_metin= ""
	for karakter in şifreli_metin:
		if karakter.isalpha():
			karakter_sıra_no= ord(karakter)
			karakter_sıra_no -= şifreleme_anahtarı

			if karakter_sıra_no > ord("z"):
				karakter_sıra_no -= max_karakter

			elif karakter_sıra_no < ord("a"):
				karakter_sıra_no += max_karakter

			çözülmüş_karakter= chr(karakter_sıra_no)
			çözülmüş_metin += çözülmüş_karakter
			
		else:
			çözülmüş_metin += karakter
	os.system(temizle)
	print("%s şifreli metnin %d anahtarıyla çözülmüş hali %s" % (şifreli_metin,şifreleme_anahtarı,çözülmüş_metin))
	input("Devam etmek için bir tuşa basın")

def şifrelemeAnahtarı():
	anahtar= int(input("Şifreleme anahtarı girin (1-%s):" % max_karakter))
	if anahtar >=1 and anahtar <= max_karakter:
		return anahtar
	else:
		return 1

if __name__ == "__main__":
	seçenekler()
    
----------------------------------------

21 DECEMBER 2020
PROJECT 2
ENGLISH TURKISH DICTIONARY

import os
kelimeler = {"get":["etmek","olmak","varmak"],
	      "break":["ara","mola","dinlenme"],
	      "winner":["kazanan","galip"]
			 }
#for no , kelime in list(enumerate(kelimeler,1)) = YANLIŞ BİR DURUM DEĞİLDİR.  YİNE AYNI SONUCU VERECEKTİR.

def kelimeleriListele():

	for no,kelime in (enumerate(kelimeler,1)):
		print("{}.{}".format(no,kelime))
	#firstuser = input("Devam etmek için lütfen bir tuşa basın: ")
def kelimeCevir(kelime,kelimeler):

	if kelime in kelimeler:
		print("'{}' anlamları:".format(kelime))
		print(kelimeler[kelime])
	else:
		print("'{}' kelimeler içerisinde yer almamaktadır.".format(kelime))
	seconduser = input("Devam etmek için lütfen bir tuşa basın: ")
def kelimeEkle(kelime,kelimeler):

	if kelime in kelimeler:
		mevcutAnlamlar = set(kelimeler[kelime])
		newUserEnters = input("Girmek istediğiniz kelimenin kelimeler içerisindeki mevcut anlamları: {}.\nYeni bir anlam girmek ister misiniz?(E/H)".format(mevcutAnlamlar))
		if newUserEnters.lower() == "e":
			yeniAnlam = input("Eklemek istediğiniz anlam veya anlamları, aralarına virgül koyarak yazınız: ")
			bölünenYeniAnlamlar = set(yeniAnlam.split(","))
			kelimeler[kelime] = list(mevcutAnlamlar | bölünenYeniAnlamlar)
			print("Girdiğiniz anlamlar kaydedildi. Mevcut anlamlar listesinin son hali: {}".format(kelimeler[kelime]))

		elif newUserEnters.lower() == "h":
			print("Hiç bir anlam eklemediniz. Görüşmek üzere...")
		else:
			print("Yanlış tuşladınız. Lütfen tekrar deneyiniz.")

	else:

		newMeaning = input("{} mevcut kelime sözlüğü içerisinde bulunmamaktadır. Girmek istedğiniz anlamları arasına virgül koyarak giriniz:\n".format(kelime))
		variable = set(newMeaning.split(","))
		kelimeler[kelime] = list(variable)

		for element, kelime in list(enumerate(kelimeler,1)):
			print("{}.{}: {}".format(element,kelime,kelimeler[kelime]))
	#thirduser = input("Devam etmek için lütfen bir tuşa basın: ")
while True:
	#os.system("cls") #Her döngüde karşımıza çıkacak olan ekranı temizleyecek otomatik olarak.
	print('''\nİNGİLİZCE-TÜRKÇE SÖZLÜK UYGULAMASINA HOŞGELDİNİZ:\nAşağıda programın bazı fonksiyonları bulunmaktadır. Hangi fonksiyonu yerine getirmek isterseniz yanındaki sayıyı girebilirsiniz:
[1]Kelimeleri Listelemek
[2]Kelimeleri Çevirmek
[3]Kelime Eklemek
[4]Programdan Çıkış
	''')

	whatDoYouWant = int(input("Yapmak istediğinizi işlemi belirtiniz: "))
	if whatDoYouWant == 1:
		kelimeleriListele()
	elif whatDoYouWant == 2:
		kelime = input("Çevirmek istedğiniz kelimeyi giriniz: ")
		kelimeCevir(kelime,kelimeler)
	elif whatDoYouWant == 3:
		kelime = input("Eklemek istediğiniz kelimeyi giriniz: ")
		kelimeEkle(kelime,kelimeler)
	elif whatDoYouWant == 4:
		print("Programdan çıkışınız yapılıyor...")
		break

----------------------------------------

COMPLICATED MOVIE APPLICATION
filmler= {
	
	"Kara Korsanın Laneti":{"Yapım Yılı":1957,"Imdb":8.2,"Tür":"Korku"},
	"Sineğin İntikamı":{"Yapım Yılı":2957,"Imdb":1.2,"Tür":"Belgesel"}

}

def filmEkle():
	film_adı = input("Film adı girin: ")
	global filmler

	if film_adı:
		yapım_yılı = input("Yapım yılını girin: ")
		imdb = input("İmdb puanını girin: ")
		film_türü = input("Film türünü girin: ")

		filmler[film_adı]= {"Yapım Yılı":yapım_yılı,"Imdb":imdb,"Tür":film_türü}

		print("Film başarıyla eklendi")
	else:
		print("Film adı boş bırakılamaz.")

def filmSil():
	film_adı = input("Film adı girin: ")
	if film_adı:

		filmler.pop(film_adı)
		print("Film başarıyla silindi")

	else:
		print("Film adı boş bırakılamaz.")

def filmGetir():
	aranan_film_adı= input("Aradığını filmin adını girin: ")
	if aranan_film_adı in filmler.keys():
		film = filmler.get(aranan_film_adı)
		yapım_yılı= film.get("Yapım Yılı","Yapım yılı girilmemiş")
		imdb= film.get("Imdb","Imdb puanı girilmemiş")
		film_türü= film.get("Tür","Film türü girilmemiş")

		print("Film adı: {}  Yapım Yılı: {}  Imdb: {}  Tür: {}".format(aranan_film_adı,yapım_yılı,imdb,film_türü))
	else:
		print("Film mevcut değil")
		
def filmleriListele():
	for film in filmler:
		film_adı = film
		yapım_yılı= filmler[film_adı].get("Yapım Yılı","Yapım yılı girilmemiş")
		imdb= filmler[film_adı].get("Imdb","Imdb puanı girilmemiş")
		film_türü= filmler[film_adı].get("Tür","Film türü girilmemiş")
		print("Film adı: {}  Yapım Yılı: {}  Imdb: {}  Tür: {}".format(film_adı,yapım_yılı,imdb,film_türü))
		print("="*80)
	input("Devam etmek için bir tuşa basın.")

while True:

	print("""
#[1] Tüm filmleri listele
#[2] Film ara
#[3] Film ekle
#[4] Film sil
""")

	secenek= int(input("Seçiminizi yapın: "))
	if secenek == 1:
		filmleriListele()
	elif secenek == 2:
		filmGetir()
	elif secenek == 3:
		filmEkle()
	elif secenek == 4:
		filmSil()

----------------------------------------

BASIC ENCRYPTION APPLICATION
harfler= "abcdefgğhıijklmnoöprsştuüvyz"

kelime= "Hey"
kelime= kelime.lower()

şifreli_kelime= harfler[harfler.index(kelime[0]) + 1] + harfler[harfler.index(kelime[1]) + 1] + harfler[harfler.index(kelime[2]) + 1]

print(kelime[0] + "------>" + harfler[harfler.index(kelime[0])+1])
print(kelime[1] + "------>" + harfler[harfler.index(kelime[1])+1])
print(kelime[2] + "------>" + harfler[harfler.index(kelime[2])+1])

print(kelime," kelimesinin şifreli hali:", şifreli_kelime)

şifresi_kırılmış_hali= harfler[harfler.index(şifreli_kelime[0]) - 1] + harfler[harfler.index(şifreli_kelime[1]) - 1] + harfler[harfler.index(şifreli_kelime[2]) - 1]

print(şifreli_kelime[0] + "------>" + harfler[harfler.index(şifreli_kelime[0])-1])
print(şifreli_kelime[1] + "------>" + harfler[harfler.index(şifreli_kelime[1])-1])
print(şifreli_kelime[2] + "------>" + harfler[harfler.index(şifreli_kelime[2])-1])
print(şifreli_kelime," kelimesinin şifresi çözülmüş hali:", şifresi_kırılmış_hali)

----------------------------------------

MULTIPLICATION TABLE BETWEEN 1 AND 10
def findingOutTheMultiplication():
    for i in range(1,11):
        print("".center(100,"*"))
        for j in range(1,11):

            result = i * j
            a = "{} * {} = {}".format(i,j,result)
            print(a)

total = findingOutTheMultiplication()

----------------------------------------

PRIMARY NUMBERS
number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
def findingThePrimaryNumbers(number1, number2):
    asalList = []
    nonAsalList = []
    for value in range((number1 - 1) , number2):
        total = ((value % 2 == 0) or (value % 3 == 0 ))
        experiments = ((value % 5 == 0) or (value % 7 == 0))
        enson = ((value % 1 == 0) or (value % value == 0))
        if (total or experiments):
            nonAsalList.append(value)
        elif (enson):
            asalList.append(value)

    return asalList,nonAsalList
x = findingThePrimaryNumbers(number1,number2)
print(x)

----------------------------------------

def my_first_function():
    print("hello World")
my_first_function()

----------------------------------------

def my_first_function(x,*args):
    emptyList = []
    for eleman in args:
        eleman = eleman + x
        emptyList.append(eleman)
    return emptyList
print(my_first_function(2,3,6,9))

----------------------------------------

mystring = "Solving Python quizzes is awesome. Can I have more, please?"
x = mystring.find("zz")
y = mystring.count(",")
z = mystring.index("o")
d = mystring[5:9].endswith("P")
e = mystring[5:8]
print(x)
print(y)
print(z)
print(d)
print(e)
if " " not in mystring or mystring.find("zz") <= 15:
    print("Great job!")

----------------------------------------

mynum = 2500
a = (100 - 5 ** 2 * 2 ** 2)
x = mynum / (100 - 5 ** 2 / 5 * 2 + 10) < 29
print(a)
print(mynum / (100 - 5 ** 2 / 5 * 2 + 10))
if a:
    print("Awesome!")
elif x:
    print("Amazing!")

----------------------------------------

mynum = 2500
a = mynum % pow(5, 2)
b = abs(10 % 2 - mynum)
c = type(mynum / 50)
print(a,b,c)
if a < 100:
    print("Awesome!")
elif b < 2019:
    print("Amazing!")
elif c is not int:
    print("Cool!")
else:
    print("Whatever!")

----------------------------------------

x = int(input("enter the number: "))
def kare(x):
    a = x*x
    return a
y = kare(x)
print(y)
print(type(y))

----------------------------------------

liste = [1,2,3,4,5,6]
x = liste.

----------------------------------------

# r = int(input("enter the r: "))
pi = 3.14
def evaluating(r):
    cevre = int(2 * pi * r)
    alan = int(pi * (r**2))
    print("Dairenin çevresi: {}, Alanı ise {} dir.".format(cevre,alan))
evaluating(4)

----------------------------------------

r = int(input("enter the r: "))
pi = 3.14
def cevreHesapla(r):
    a = int(2 * pi * r)
    return a
def alanHesapla(r):
    b = int(pi * (r ** 2))
    return b
print("Dairenin çevresi: {} iken Alanı: {} dır.".format(cevreHesapla(r),alanHesapla(r)))

----------------------------------------

def normalize(a):
    a = [3.2 , 2.52 , 6.2 , 3.7 , 6.1]
    b = []
    for value in a:
        total = (value - min(a))/(max(a)-min(a))
        b.append(total)
    print(b)
    return a
normalize(5)

-----------------------------------------------

def reverseflash(b):
    if (b[::1] == b[::-1]):
        print("True")
        return b
    else:
        print("False")
        return b
isPalindrome = reverseflash(b)

-----------------------------------------------

def multiplywiththree(a):
    print("first function is worked.")
    return a*3
def addwithtwo(a):
    print("second function is worked.")
    return a+2
def dividewithfour(a):
    print("third function is worked.")
    return a//4
allprocessis = dividewithfour(addwithtwo(multiplywiththree(5)))
totalis = addwithtwo(allprocessis)
print(allprocessis)
print(totalis)

--------------------------------------------------

PALINDROME WITH RECURSIVITY
import sys
def is_palindrome_iterative(numbers):
    for item in range(0, int(len(numbers)/2)):
        if numbers[item] != numbers[len(numbers) - item - 1]:
            return False
        return True
    
def is_palindrome_recursive(numbers):
    if len(numbers) < 1:
        return True
    else:
        if numbers[0] == numbers[-1]:
            return is_palindrome_recursive(numbers[1:-1])
        else:
            return False

def main():
    enteredword = str(sys.argv[1])
    totally = is_palindrome_iterative(enteredword)

    if(totally):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
"""

#----------------------------------------------------------------------------

#MATHEMATICAL OPERATIONS:

"""
These were performed with import modules.
x0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])

g=9.78033

displacement = x0 +( v0 * t ) - ((g*t**2)/2)
 
stdio.writeln(str(x0) + '+' + str(v0) + '*' + str(t) + '-' + str(g) + '*' + str(t) + '** ' + str(2) + '/' + str(2) + ' = ' + str(displacement))

--------------------------------------------------

a = int(sys.argv[1])
b = int(sys.argv[2])

total = a +  b
diff  = a -  b
prod  = a *  b
quot  = a // b
rem   = a %  b
exp   = a ** b

stdio.writeln(str(a) + ' +  ' + str(b) + ' = ' + str(total))
stdio.writeln(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
stdio.writeln(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
stdio.writeln(str(a) + ' // ' + str(b) + ' = ' + str(quot))
stdio.writeln(str(a) + ' %  ' + str(b) + ' = ' + str(rem))
stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

--------------------------------------------------

TEMPERATURE TRANSFORMER
import stdio
import sys

a = float(sys.argv[1])
b = str(sys.argv[2])

Celcius =  str(Kelvin) - 273.15
Celcius = Fahrenheit - 32 * 5/9
Fahrenheit = 9/5 * Kelvin - 241.15
Fahrenheit = 9/5 * Celcius + 32
Kelvin = Celcius + 273.15
Kelvin = Fahrenheit - 32 * 5/9 + 273.15

if ( b == Celcius):
    stdio.writeln("Celcius:" +  str(a))
    stdio.writeln("Fahrenheit:" + (str(9) + '/' + str(5) +  '*' +  str(Celcius) +  '+' + str(32)))
    stdio.writeln("Kelvin :" + (str(Celcius) +  '+' +  str(273.15)))

elif ( b == Fahrenheit):
    stdio.writeln("Celcius:" + str(fahrenheit) + '-' + str(32) + '*' + str(5) + '/' + str(9))
    stdio.writeln("Fahrenheit:" + str(a))
    stdio.writeln("Kelvin:" + str(Celcius) +  '+' +  str(273.15))

elif ( b == Kelvin):
    stdio.writeln("Celcius:" + str(kelvin) +  '-' + str(273.15))
    stdio.writeln("Fahrenheit:" + str(9) + '/' + str(5) + '*' +  str(Kelvin) +  '-' + str(241.15))
    stdio.writeln("Kelvin:" + str(a))

else:
    stdio.writeln("You can only convert from Celcius , Fahrenheit , Kelvin.")
                  
"""

#COMPLICATED OTHER PROGRAMS

"""
GRADING CALCULATOR
21 DECEMBER 2020

def calculator(firstmidterm, secondmidterm, finalexam):
    totalpoint = ((firstmidterm * 30) / 100) + ((secondmidterm * 30) / 100) + ((finalexam * 40) / 100)
    if (totalpoint >= 90):
        print("Your final grade: {} -----> AA".format(totalpoint))
    elif ((totalpoint < 90) and (totalpoint >= 85)):
        print("Your final grade: {} -----> BA".format(totalpoint))
    elif ((totalpoint < 85) and (totalpoint >= 80)):
        print("Your final grade: {} -----> BB".format(totalpoint))
    elif ((totalpoint) < 80 and (totalpoint >= 75)):
        print("Your final grade: {} -----> CB".format(totalpoint))
    elif ((totalpoint) < 75 and (totalpoint >= 70)):
        print("Your final grade: {} -----> CC".format(totalpoint))
    elif ((totalpoint) < 70 and (totalpoint >= 65)):
        print("Your final grade: {} -----> DC".format(totalpoint))
    elif ((totalpoint) < 65 and (totalpoint >= 60)):
        print("Your final grade: {} -----> DD".format(totalpoint))
    elif ((totalpoint) < 60 and (totalpoint >= 55)):
        print("Your final grade: {} -----> FD".format(totalpoint))
    elif totalpoint < 55:
        print("Your final grade: {} -----> FF".format(totalpoint))

options = '''\nWelcome to Final Grade Calculator:
[1]GRADE CALCULATOR
[2]EXIT FROM PROGRAMME
'''
CONTINUE TO ABOVE FUNCTION.
while True:
    print(options)
    userOption = int(input("Enter your option: "))
    if userOption == 1:
        firstmidterm = int(input("Enter your first midterm result: "))
        secondmidterm = int(input("Enter your second midterm result: "))
        finalexam = int(input("Enter your final exam result: "))
        calculator(firstmidterm,secondmidterm,finalexam)
    elif userOption == 2:
        print("Programdan çıkışınız yapılıyor...")
        break

--------------------------------------------------

21 ARALIK 2020
MİNİMUM MAKSİMUM ORTADAKİ SAYIYI BULMA PROGRAMI

username = input("Please Enter Your Name: ")
introduction = ("{}, Welcome to Body Mass Index Calculator.\nIf you want to exit the programme, you have to enter the 'q!".format(username))
height        = float(input("Enter your height such as m.cm: "))
weight        = int(input("Enter your weight: "))
bodyMassIndex = (weight / (height ** 2))


if (bodyMassIndex < 18.5):
    print("{}, your Body Mass Index: {} -----> Weak".format(username,bodyMassIndex))
elif (bodyMassIndex >= 18.5 and bodyMassIndex < 25):
    print("{}, your Body Mass Index: {} -----> Normal".format(username,bodyMassIndex))
elif (bodyMassIndex >= 25 and bodyMassIndex > 30):
    print("{}, your Body Mass Index: {} -----> Overweight".format(username,bodyMassIndex))
elif (bodyMassIndex >= 30):
    print("{}, your Body Mass Index: {} -----> Obese".format(username,bodyMassIndex))

def maxminhalfFounder(firstnumber,secondnumber,thirdnumber):

    if (firstnumber < secondnumber):
        if secondnumber < thirdnumber:
            print("minimum: {}\nmaximum: {}\nhalf: {}".format(firstnumber,thirdnumber,secondnumber))
        elif secondnumber > thirdnumber:
            if firstnumber < thirdnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(firstnumber,secondnumber,thirdnumber))
            elif firstnumber > thirdnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(thirdnumber,secondnumber,firstnumber))

    elif firstnumber < thirdnumber:
        if thirdnumber < secondnumber:
            print("minimum: {}\nmaximum: {}\nhalf: {}".format(firstnumber,secondnumber,thirdnumber))
        elif thirdnumber > secondnumber:
            if firstnumber < secondnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(firstnumber,thirdnumber,secondnumber))
            elif firstnumber > secondnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(secondnumber,thirdnumber,firstnumber))

    elif secondnumber < firstnumber:
        if firstnumber < thirdnumber:
            print("minimum: {}\nmaximum: {}\nhalf: {}".format(secondnumber,thirdnumber,firstnumber))
        elif firstnumber > thirdnumber:
            if secondnumber > thirdnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(thirdnumber,firstnumber,secondnumber))
            elif secondnumber < thirdnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(secondnumber,firstnumber,thirdnumber))

    elif thirdnumber < firstnumber:
        if thirdnumber > secondnumber:
            print("minimum: {}\nmaximum: {}\nhalf: {}".format(secondnumber,firstnumber,thirdnumber))
        elif thirdnumber < secondnumber:
            if firstnumber > secondnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(thirdnumber,firstnumber,secondnumber))
            elif firstnumber < secondnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(thirdnumber,secondnumber,firstnumber))

    elif secondnumber < thirdnumber:
        if thirdnumber < firstnumber:
            print("minimum: {}\nmaximum: {}\nhalf: {}".format(secondnumber,firstnumber,thirdnumber))
        elif thirdnumber > firstnumber:
            if firstnumber > secondnumber:
                print("minimum: {}\nmaximum: {}\half: {}".format(secondnumber,thirdnumber,firstnumber))
            elif firstnumber < secondnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(firstnumber,thirdnumber,secondnumber))

    elif  thirdnumber < secondnumber:
        if secondnumber < firstnumber:
            print("minimum: {}\nmaximum: {}\nhalf: {}".format(thirdnumber,firstnumber,secondnumber))
        elif secondnumber > firstnumber:
            if firstnumber > thirdnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(thirdnumber,secondnumber,firstnumber))
            elif firstnumber < thirdnumber:
                print("minimum: {}\nmaximum: {}\nhalf: {}".format(firstnumber,secondnumber,thirdnumber))

options = '''\nWelcome to Minimum, Maximum and Half Number Evaluater.
[1]Maximum, minimum and half number evaluater
[2]Exit the program.
'''
while True:
    print(options)
    userWish = int(input("Enter your option: "))
    if userWish == 1:
        firstnumber = int(input("Enter the first number: "))
        secondnumber = int(input("Enter the second number: "))
        thirdnumber = int(input("Enter the last number: "))
        maxminhalfFounder(firstnumber,secondnumber,thirdnumber)
    elif userWish == 2:
        print("Programdan çıkışınız yapılıyor...")
        break
        
--------------------------------------------------

21 DECEMBER 2020
CALCULATOR APPLICATION

def additionOperation(firstnumber,secondnumber):
    addingoperation = firstnumber + secondnumber
    totaloperation = ("{} + {} = {}".format(firstnumber,secondnumber,addingoperation))
    return totaloperation

def substractionOperation(firstnumber,secondnumber):
    substractingoperation = firstnumber - secondnumber
    totaloperationfirst = ("{} - {} = {}".format(firstnumber,secondnumber,substractingoperation))
    return totaloperationfirst

def multiplicationOperation(firstnumber,secondnumber):
    productOperation = firstnumber * secondnumber
    totaloperationsecond = ("{} * {} = {}".format(firstnumber,secondnumber,productOperation))
    return totaloperationsecond

def dividingOperation(firstnumber,secondnumber):
    divider = firstnumber / secondnumber
    totaloperationthird = ("{} / {} = {}".format(firstnumber,secondnumber,divider))
    return totaloperationthird

def takingPowersofNumbers(firstnumber,secondnumber):
    takingpower = firstnumber ** secondnumber
    totaloperationfourth = ("{} ** {} = {}".format(firstnumber,secondnumber,takingpower))
    return totaloperationfourth

options = ('''\nWelcome to the CALCULATOR:
You can choose your operation what you want to do as entering the number which is stated in left side of operation.
\n[1]Addition Operations
[2]Substraction Operations
[3]Multiplication Operations
[4]Dividing Operations
[5]Taking PowerS Operations
[6]Exit from Calculator
''')

while True:
    print(options)
    userOption = int(input("Enter your operation: "))

    if userOption == 1:
        firstnumber = float(input("Enter the first number: "))
        secondnumber = float(input("Enter the second number: "))
        firstresult = additionOperation(firstnumber,secondnumber)
        print(firstresult)
    elif userOption == 2:
        firstnumber = float(input("Enter the first number: "))
        secondnumber = float(input("Enter the second number: "))
        secondresult = substractionOperation(firstnumber,secondnumber)
        print(secondresult)
    elif userOption == 3:
        firstnumber = float(input("Enter the first number: "))
        secondnumber = float(input("Enter the second number: "))
        thirdresult = multiplicationOperation(firstnumber,secondnumber)
        print(thirdresult)
    elif userOption == 4:
        firstnumber = float(input("Enter the first number: "))
        secondnumber = float(input("Enter the second number: "))
        fourthresult = dividingOperation(firstnumber,secondnumber)
        print(fourthresult)
    elif userOption == 5:
        firstnumber = float(input("Enter the first number: "))
        secondnumber = float(input("Enter the second number: "))
        lastresult = takingPowersofNumbers(firstnumber,secondnumber)
        print(lastresult)
    elif userOption == 6:
        print("Please wait in order  to exit from the calculator... ")
        break

--------------------------------------------------

USER ENTRY APPLICATION
27 DECEMBER 2020
KULLANICI GİRİŞİ UYGULAMASI
statedUser = "bobersah"
statedParola = "Omer4651998."
def welcomeOurProgramm(newUser,newPassword):
    if ((statedUser == newUser) and (statedParola != newPassword)):
        print("Your password is wrong. Please enter another password.")
    elif ((statedUser != newUser) and (statedParola == newPassword)):
        print("Your username is wrong. Please change your username.")
    elif ((statedUser != newUser) and (statedParola != newPassword)):
        print("Your username and password are wrong. Please change them.")
    elif ((statedUser == newUser) and (statedParola == newPassword)):
        print("Username and password are true. Welcome '{}'...".format(newUser))
options = '''\nWelcome to the User Entering Programme:
[1]Enter the program
[2]Exit
'''
while True:
    print(options)
    userOption = int(input("Enter your choice: "))
    if userOption == 1:
        newUser = input("Enter your username: ")
        newPassword = input("Enter your password: ")
        welcomeOurProgramm(newUser,newPassword)
    elif userOption == 2:
        print("Please wait in order to exit from programme...")
        break
    else:
        print("You entered wrong option. Please try again.")

--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


"""

