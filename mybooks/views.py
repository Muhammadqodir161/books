from django.shortcuts import render
from django.shortcuts import HttpResponse


def book_list(requests):
    response = """
    <h1>Books Lists</h1>   
    
    <ul>
        <li><a href="book/1" style="color: red;">Yulduzli tunlar</a> </li>
        <li><a href="book/2" style="color: red;">Harry Poter</a></li>
    </ul>

    """
    return HttpResponse(response)

def first_book(requests):
    response = """
        <h1>Yulduzli tunlar</h1> 
        <p><b>Author</b>: Primqul Qodirov</p>
        
        <p>
        
       „Yulduzli tunlar“ – ozbek yozuvchisi Pirimqul Qodirov qalamiga mansub tarixiy roman. Asarda Zahiriddin Muhammad Bobur hayoti haqida soz yuritiladi.
       Qodirov mazkur roman ustida on yil (1969—1978) davomida ish olib borgan.
       „Yulduzli tunlar“ga „Boburnoma“ hamda „Humoyunnoma“ asarlari asosiy manba bolib xizmat qilgan.

        </p>
        
        
        
        
        <a href="../" style="color: red;">Back To List</a
    
    """
    return HttpResponse(response)


def second_book(requests):
    response = """
        <h1>Harry Poter</h1> 
        <p><b>Authors</b>: Joan Rouling</p>
        
        <p>
        
        Garri Potter asarlari 7 qismdan iborat bo'lib ilk asar 1997 yilda yozilgan va "Garri Potter va Faylasuflar toshi" deb nomlangan.
        7-asar 2007-yilda chop etilgan va "Garri Potter va Ajal tuhfalari" deb nomlangan. Keyin esa bu asarlarga filmlar ishlangan. 
        Hozirda ko'pchilik bu filmlarni sevib tomosha qilishadi.
        2016-yilga kelib esa Joan Rouling Garri Potter seriyasidagi 8-asar Garri Potter va la'natlangan bolalar asarini yozadi. 
        Bu asar pyesa shaklida yozilgan bo'lib hali ekranlashtirilmagan.

        </p>        
        
        
        <a href="../" style="color: red;">Back To List</a

    
    """
    return HttpResponse(response)