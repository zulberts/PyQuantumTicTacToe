# Opis projektu

**Autor:** Albert Skutnik

Projekt to gra kwantowe kółko krzyżyk w termialu.


# Instalacja gry
---
Linux:
Kolejne linijki należy wpisywać w terminalu:
`git clone https://gitlab-stud.elka.pw.edu.pl/askutnik/projekt-pipr-quantum-tic-tac-toe.git`
`cd projekt-pipr-quantum-tic-tac-toe`
`pip install virtualenv`
`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`
`python3 game.py`


# Instrukcja dla graczy
---
Zasady gry:
1. Gracz X zawsze zaczyna.
2. Gracz wybiera po dwa pola w których chce postawić swój znak(x1, o2, itd.).
(Pola w któych znajduje się X lub O są niemożliwe do wybrania.
Maksymalnie gra może toczyć się przez 9 rund.)
3. Znaki (x1, o2, itd.) zamieniają się w X lub O, wtedy kiedy dojdzie do cyklu.
(Splątanie - dwa znaki x1 lub o2 itd tworzą splątanie. Np.: w polu nr 1 i polu nr 3
stoi znak x1. Wtedy te dwa pola są splątane, analogicznie z resztą znaków.
Cykl- zachodzi wtedy kiedy splątane pola tworzą jedno wielkie splątanie(cykl).
Przykładem może być np: w polach nr 1 i nr 2 stoi po znaku x1 i o2. Wtedy pole 1-2
jest splątane przez znak x1 oraz występuje drugie splątanie 2-1 przez znak o2. wtedy
możliwe jest dojście z pola 1 do pola 2 i z powrotem do pola 1 przez drugie splątanie.
Należy sobie to wyobrazić jako możliwość stworzenia ścieżki dzięki której można
z powrtotem dojść do wyjściowego pola poprzez inne splątania, oraz te splątania
są jednokierunkowe.)
4. Jeżeli dojdzie do splątania wszystkie znaki znajdujące się na planszy zamieniają
się w X lub O. Jeżeli w polu występuje tylko x lub tylko o, to wtedy pole całe zamienia
się w X lub O. Jeżeli w polu znajdują się x i o, wtedy losowo na zmiane w danych polach
zamieniają się te pola w X lub O.
5. Następnie dochodzi do wygranej/remisu jeżeli w kolumnie, rzędzie lub przekątnej
powstaną trzy X lub trzy O. Ta gra różni się od klasycznego kółka krzyżyk tym, że
możliwy jest remis poprzez powstanie trzech X i trzech O w danej konfiguracji
tak, że dwóch graczy mogłoby wygrać.
6. Gracz ma do wyboru dwóch graczy z którymi może grać:
-gracz który wybiera pola losowo.
-gracz który wybiera pola strategicznie.(pola bez żadnego x lub o)
Oraz gracz ma możliwość wyboru czy chce grać jako X lub jako O.
7. Gra automatycznie sprawdza, kto wygrał i wyświetla tą wiadomość w terminalu.


# Testy w wirtualnym środowisku
Testując nadleży użyć komendy:
`.venv/bin/pytest`


# Dalsza dokumentacja
Szczegółowa dokumentacja znajduje się w pliku PDF.


# Rozwiązaywanie problemów
Jeżeli pojawią się problemy przy uruchamianiu gry lub przy testowaniu w
wirtualnym środowisku należy z niego wyjść, zainstalować biblioteke numpy
`pip install numpy` i uruchomić program bez użycia venv.
