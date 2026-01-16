My Awesome Lib

   Prosta biblioteka z kilkoma funkcjami:

  -is_empty() -> sprawdza, czy wartość jest pusta  
  -modulo() -> reszta z dzielenia  
  -multiply() -> mnożenie dwóch liczb  
  -word_count() -> liczy słowa w tekście  

   Instalacja

1. Sklonuj repozytorium lub skopiuj folder `my_awesome_lib` do swojego projektu.
2. Dodaj folder do `sys.path`, jeśli potrzebujesz importów w testach.

   Jeżeli uruchomienie pliku nie działa, zastosuj na początku kodu :
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

teraz import działa:
from math_tools import modulo, multiply  