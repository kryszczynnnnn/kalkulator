#  Kalkulator Python

## Opis projektu
Jest to prosta aplikacja kalkulatora napisana w Pythonie.  
Pozwala wykonywać podstawowe operacje matematyczne, takie jak:
- dodawanie
- odejmowanie
- mnożenie
- dzielenie

Projekt ma charakter edukacyjny i pokazuje podstawy logiki kalkulatora oraz pracy z funkcjami w Pythonie.

---

## Uruchamianie

1. Upewnij się, że masz zainstalowanego Pythona (3.x)
2. Wejdź do folderu projektu:
```bash
cd python
```
Uruchom program:
```bash
python main.py
```

## Funkcje
```
add(a, b) → dodawanie
subtract(a, b) → odejmowanie
multiply(a, b) → mnożenie
divide(a, b) → dzielenie (z zabezpieczeniem przed 0)
```
## ⚠️ Uwagi
Program działa w konsoli
Brak interfejsu graficznego
Projekt edukacyjny
## Autor
Serhii Skyba

---

# Kalkulator Web (HTML / CSS / JS)

## Opis projektu
Jest to kalkulator działający w przeglądarce, napisany w:
- HTML
- CSS
- JavaScript

Projekt symuluje działanie klasycznego kalkulatora (np. Windows) i zawiera dodatkowe funkcje jak historia działań.

---

## Funkcje

### Operacje matematyczne
- dodawanie
- odejmowanie
- mnożenie
- dzielenie
- procenty
- zmiana znaku (+/-)
- pierwiastek
- potęga (x²)
- odwrotność (1/x)

---

### Funkcje kalkulatora
- zapis poprzedniego działania
- historia obliczeń
- możliwość ponownego kliknięcia wyniku z historii
- czyszczenie ekranu (C / CE)
- backspace (usuwanie ostatniej cyfry)

---

## Testy

Do projektu użyto testów jednostkowych technologi <b>Jest</b>.

Testy sprawdzają m.in.:
- poprawność działań matematycznych
- reset kalkulatora
- operacje specjalne
- obsługę błędów (np. dzielenie przez 0)

Uruchomienie testów:
```bash
npx jest
```
## Uruchomienie projektu
Otwórz folder:
html, css, js
Otwórz plik:
index.html
Uruchom w przeglądarce
## Struktura projektu
- index.html
- style.css
- script.js
## Cel projektu

Projekt został stworzony w celu:

- nauki JavaScript
- pracy z DOM
- obsługi zdarzeń
- testów jednostkowych
- logiki aplikacji
# Autor
Krystian Tarnowski

---

# Calcy – Stylowy i wydajny kalkulator

Calcy to prosty kalkulator, który obsługuje skróty klawiaturowe.

## Skróty klawiaturowe

Skróty są intuicyjne w użyciu. Wszystkie odpowiadają przyciskom kalkulatora, z wyjątkiem:

**S** – zmienia wartość liczby z dodatniej na ujemną i odwrotnie

**T** – oblicza pierwiastek sześcienny z liczby

**R** – oblicza pierwiastek kwadratowy z liczby

**F** – oblicza silnię

**C** – czyści pole wprowadzania

**P** – podnosi liczbę do potęgi kolejnej liczby

**L** – oblicza logarytm liczby

## Wymagania systemowe

**System operacyjny:** Windows 10 64-bit

**Procesor:** Dowolny

**Pamięć:** 256 MB RAM

**Grafika:** Dowolna

**Miejsce na dysku:** 5 MB kodu źródłowego + 200 KB programu

## Autorzy

**Kod i projekt:** Serhii Skyba

--- 

# Kalkulator Java (Swing)
## Opis projektu

Jest to graficzny kalkulator napisany w języku Java z wykorzystaniem biblioteki Swing (JFrame).

Aplikacja umożliwia wykonywanie podstawowych oraz zaawansowanych operacji matematycznych w interfejsie graficznym oraz zapis historii działań.

## Funkcje

## Operacje matematyczne
- dodawanie (+)
- odejmowanie (-)
- mnożenie (*)
- dzielenie (/)
- procenty (%)
- zmiana znaku (+/-)
- pierwiastek kwadratowy (√)
- potęga kwadratowa (x²)
  
## Funkcje kalkulatora
- wyświetlacz główny (wynik)
- wyświetlacz historii działania
- zapis historii obliczeń (klikane przyciski)
- możliwość ponownego użycia wyniku z historii
- obsługa błędu dzielenia przez zero
- przycisk „C” (reset kalkulatora)
- Historia działań


## Uruchamianie projektu
1. Wymagania
- Java JDK 8+
- dowolne IDE

2. Uruchomienie
- Skompiluj i uruchom klasę:
```
javac calculator.java
java calculator
```
lub uruchom bezpośrednio z IDE.

## Testy (konsolowe)

W metodzie main() znajdują się proste testy:

System.out.println("2 + 3 = " + calc.calculate(2.0, 3.0, "+"));

Testy sprawdzają:

- poprawność działań
- obsługę dzielenia przez 0
- działanie metody calculate()
## ⚠️ Uwagi
- Projekt używa Swing (GUI desktopowe)
- Brak zewnętrznych bibliotek
- Kalkulator działa lokalnie
##  Struktura pliku
calculator.java
## Autor
Krystian Tarnowski

# Kalkulator Android

## Opis projektu

Projekt: Repozytorium GitHub

Opis projektu

„Kalkulator” to aplikacja mobilna na system Android umożliwiająca wykonywanie podstawowych działań matematycznych.
Projekt został pierwotnie stworzony przy użyciu technologii webowych (HTML, CSS oraz JavaScript), a następnie przekonwertowany na aplikację mobilną Android z wykorzystaniem frameworka Tauri.

Dzięki temu aplikacja zachowuje lekki i szybki interfejs webowy, jednocześnie działając jako natywna aplikacja mobilna.

## Funkcjonalności
- dodawanie,
- odejmowanie,
- mnożenie,
- dzielenie,
- obsługa liczb dziesiętnych,
- wyświetlanie wyniku działań,
- czyszczenie aktualnego działania,
- prosty i responsywny interfejs użytkownika.
## Wykorzystane technologie

- HTML
- CSS
- JavaScript
- Tauri

Tauri zostało użyte do opakowania aplikacji webowej jako aplikacji mobilnej działającej na Androidzie.

## Aplikacja posiada prosty interfejs składający się z:

- wyświetlacza działań,
- wyświetlacza wyniku,
- przycisków cyfr,
- operatorów matematycznych,
- przycisku usuwania danych,
- przycisku obliczania wyniku.

## Uruchomienie projektu
**Wymagania**
```
- Node.js
- npm
- Android Studio
- Android SDK
- Rust
- Tauri CLI
```


## Autorzy
Serhii Skyba
Krystian Tarnowski
