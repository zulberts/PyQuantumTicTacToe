Należy stworzyć program umożliwiający rozgrywanie partii w kwantowe kółko i krzyżyk między człowiekiem a graczem komputerowym. Należy stworzyć co najmniej dwa rodzaje graczy komputerowych:

wybierający w każdej turze losowo jeden z możliwych do wykonania ruchów
wybierający w każdej turze najlepszy ruch według pewnych prostych kryteriów

Zasady gry:
1. Podczas kazdego ruchu gracz wybiera po dwa pola na ktorych chce postawic swoj znak(x/o)
kazdy znak ma indeks (od 1 do nawet9)(postawione w tej samej turze znaki maja ten sam indeks)
2. ten gracz ktory gra pierwszy ma indeksy nieparzyste, gracz ktory zagra drugi ma indeksy parzyste
3. jezeli powstanie cykl czyli:
np 3 pola sa splatane bo w polu nr 1 jest x5 i o6, w polu nr 2 jest o6 i x7 a w polu nr 3 jest x7 i x5 
przez to ze w polu gdzie znajduje sie x5 jest o6 a w polu gdzie jest o6 jest x7, a nastepnie w polu 3 jest x7 ktore przez x5 wraca do x5 to powstaje splatanie.
4. Gracz ktory mial swoja ture i doprowadzil do cykl, nie wybiera pola w ktorym chce postawic (x/o) lecz gracz drugi. 
5. w tym przypadku do cykl doprowadzilo postawienie x7 wiec gracz o wybiera pole gdzie ma stanac x7, nastepnie gracz x wybiera gdzie postawic o6 i zostaje jedno pole dla x5(Nie wiem czy w takiej kolejnosci!!!!)

6. przypadkiw ktorych dochodzi do cykl:
- w dwoch polach sa: x1 o2 i w drugim x1 i o2
- jak w dwoch polach w przykladzie powyzej dojdzie do cykl a w jednym z pol znajduje sie x7 i w innym polu znajduje sie x7
i w tym polu nie ma zadnego innego o to wtedy autmatycnzie pole staje sie X.
- jak zachodzi to samo co w przykladzie pierwszym tyle ze np w 3 polach (powstaja tak jakby niekonczonce sie petle)
wymagania:
petle musza byc stworzone przy uzyciu o i x, sam x stawiajac w tych samych polach tych samych znakow nie doprowadzi do cykl

7. jezeli na tablicy w poziomie, pionie, na przekatnych beda trzy te same znaki to gracz x/o wygrywa.


1. Stworzyc klase board, w której będzie przechowywany aktualny stan board i automatycznie po ruchu gracza 
board bedzie aktualizowal i jezeli jest mozliwosc aby zaszedl "cykl", to gracz ktory, nie doprowadzil do cyklu
ma aktualnie ruch i wybiera pola ktore 
ma przejac on, nastepnie gracz przeciwny wybiera pole, jezeli cykl powstal np na 4 polach i kazde pole posiada albo o albo x to
nastepnie gracz pierwszy wybiera drugie pole, a ostatnie pole zostaje dla gracza drugiego i automatycznie mu je przypisuje.
Jezeli zostsaly pola ktore biora udzial w cyklu a nie maja x/o to zostaja automatycznie zamienione w X/O bez mozliwosci 
przejecia tego pola przez gracza drugiego pomimo tego ze to on zaczyna wybierac ktore pole z cyklu chce przejac.
Po stawianiu X lub O moglo dojsc do wygranej lub remisu, trzeba to sprawdzic, jezli do tego nie doszlo to nalezy pozwolic dla gracza
pierwszego mozliwosc stawiania kolejnych znakow x/o




2. stworzyc klase gracz ktory wybiera losowo
- kazde pole ma index i dzieki temu bedzie losowo

3. stworzyc klase ktora wybiera najlepszy ruch
            Strategia:
            nie ma idealnej strategi, jedynie gracz ktory zaczyna moze tak grac by doprowadzic za kazdym razem do remisu, poniewaz doprowadzi do powstania w tej samej chwili dwoch rzedow x i o na raz. dzieki czemu bedzie remis
            strategia opiera sie o to by zaczynac x1 lub o1 w przeciwnych rogach
            nastepnie x lub o nie moze grac kolejnych x/o na pola gdzie juz znajduje sie twoja figura, poniewaz gdy dojdzie do cykl
            a w polu gdzie doszlo do cykl bedzie znajdowal sie x7 a w innym polu bedzie znajdowal sie samotny x7 to zyskujemy jedno
            pole automatycznie.
            

            jezeli zmienic zasady gry na takie ze gracz ktory stworzy cykl wybiera pole to wtedy moze wygrac w 100% zaczynajac od rogow w poziomie w pierwszym i ostatnim rzedzie 

