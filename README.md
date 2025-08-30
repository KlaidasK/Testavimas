# Selenium registracijos formos testas

Šis Python skriptas automatizuoja registracijos formos užpildymą svetainėje https://fill.dev/form/registration-simple. Skriptas atidaro Chrome naršyklę, užpildo laukus (el. paštą, vartotojo vardą, slaptažodį, slaptažodžio patvirtinimą) ir pateikia formą.

## Reikalavimai

- Python 3.8 arba naujesnė versija
- Google Chrome naršyklė
- Įdiegtas Selenium paketas (pip install selenium)
- ChromeDriver, atitinkantis jūsų Chrome versiją, įtrauktas į PATH

## Naudojimas

1. Atsisiųskite failą form_test.py
2. Paleiskite komandą: python form_test.py
3. Skriptas atidarys naršyklę, užpildys formą ir paspaus „Submit“ mygtuką
4. Po 30 sekundžių naršyklė automatiškai užsidarys

