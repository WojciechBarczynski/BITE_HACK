# LevelMind

LevelMind jest aplikacją webową, która ma na celu umożliwienie użytkownikom nauki wszystkiego, gdzie zadania będą automatycznie dostosowywały się do poziomu użytkownika. Każde zadanie ma swój poziom trudności, który ustalany jest na podstawie poprawności rozwiązań użytkowników. Dodatkowo za każdą poprawną odpowiedź, która jest rozwiązana szybciej niż średni czas rozwiązywania zadania, użytkownik otrzymuje dodatkowe punkty. Wszystko to dzięki zmodyfikowanej wersji algorytmu TrueSkill.

## Wymagania
Do uruchomienia aplikacji potrzebne są:
- npm
- Python 3.10
-- Flask
-- Flask-Cors
-- Pandas
-- Numpy
-- PyMySQL
Oraz połączenie z AGH VPN (wymagane do połączenia z bazą danych).

## Jak uruchomić aplikację?
Aby uruchomić aplikację należy:
- uruchomić za pomocą Pythona plik './backend/rest_api/api.py': `python3 ./backend/rest_api/api.py`
- wejść do folderu './frontend': `cd ./frontend`, pobrać zalżności npm: `npm install` i uruchomić aplikację: `npm start`

# Algorytmy i struktury danych
Główną częścią aplikacji są algorytmy odpowiedzialne za dostosowywanie poziomu trudności zadań do poziomu użytkownika. Aby to zrobić, wykorzystane zostało założenie, że zadanie to również użytkownik, który współdzieli ustandaryzowany ranking razem z innymi użytkownikami. Różnica polega na tym, że zadania nie wybierają użytkowników, tylko są tak naprawdę 'NPC' czekającymi na walkę z użytkownikiem. Jeżeli zadanie nie zostanie poprawnie rozwiązane, to zostaje uznane za trudniejsze niż było w rzeczywistości, jeżeli jednak użytkownik rozwiąże rozwiązanie, to zadanie zostaje uznane za łatwiejsze i dodatkowo użytkownik może dostać dodatkowe punkty za szybkość rozwiązania. Wszystko to dzięki zmodyfikowanej wersji algorytmu TrueSkill.

## TrueSkill
TrueSkill jest algorytmem do oceny umiejętności graczy w grach. Jest on oparty na rozkładzie Gaussa, który jest w stanie określić średnią i odchylenie standardowe. W naszym przypadku, średnia reprezentuje poziom trudności zadania, a odchylenie standardowe reprezentuje jego niepewność. Wartość średniej jest aktualizowana wraz z rozwiązywaniem zadań, a wartość odchylenia standardowego jest aktualizowana wraz z rozwiązywaniem zadań. Dzięki temu algorytmowi, zadania są w stanie dostosowywać się do poziomu użytkownika, a użytkownik jest w stanie dostosowywać się do poziomu zadań. Dodatkowo jesteśmy w stanie utrzymać względny balans w rankingu użytkowników, ponieważ algorytm TrueSkill jest w stanie określić, kto jest lepszy od kogo, a także jak bardzo jest lepszy. Dodatkowo własna implementacja, pozwoliła na uwzględnienie czasu rozwiązywania zadań, dzięki czemu użytkownik dostaje kilka dodatkowych punktów za szybkie rozwiązanie, a jeżeli rozwiąże wolniej niż oczekiwano, to dostanie 1 punkt mniej niż osoba, która rozwiązała to rozwiązanie w czasie oczekiwanym. Zastosowanie takiego algorytmu pozwala na określenie kto jest od kogo lepszy oraz przewidywanie wyniku bitwy użytkownika z zadaniem. Jednocześnie wykorzystanie sprawdzonego modelu ratingowego pozwala na utrzymanie względnego balansu w rankingu użytkowników.

# Symulacja
Aby zaprezentować proces nauki napisany został mały model osoby, która rozwiązuje zadania, a jednocześnie posiada umiejętność uczenia się, co widać na poniższym wykresie.

![](https://github.com/WojciechBarczynski/BITE_HACK/blob/main/rating.gif)



