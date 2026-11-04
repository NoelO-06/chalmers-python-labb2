Artillery Game (Python)

Ett klassiskt tvåspelarspel i Python där två spelare turas om att skjuta kanon på varandra. Spelet tar hänsyn till både vinkel, utgångshastighet och en slumpmässig vindstyrka som ändras mellan varje runda.

Projektet är skrivet i Python med fokus på objektorienterad programmering (OOP) och en tydlig uppdelning mellan spellogik (Model) och det grafiska gränssnittet (GUI).

Innehåll:
- gamemodel.py: All spellogik, fysik och regler (Game, Player, Projectile).
- graphicsmain.py: Det grafiska gränssnittet och animationer.
- textmain.py: Textbaserat gränssnitt för att spela i terminalen.
- test.py: Enhetstester för logiken.

Hur du kör spelet:
1. Se till att du har Python 3 och tkinter installerat.
2. Starta det grafiska spelet genom att köra: python3 graphicsmain.py
3. Kör testerna med: python3 test.py