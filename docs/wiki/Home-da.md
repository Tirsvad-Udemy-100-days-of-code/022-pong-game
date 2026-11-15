[English](Home) · **Dansk** · [Bahasa Melayu](Home-ms)

# Pong Game

Det klassiske Pong-arkadespil for to spillere med Python turtle-grafik: hold bolden i spil, og scor, når den anden spiller misser.

![Pong-spillets vindue midt i spillet, stilling 3 mod 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/raw/branch/main/docs/images/pong.png)

## Hvad er det?

Dag 22 af Udemy-kurset *100 Days of Code: The Complete Python Pro Bootcamp*. Et sort vindue på 800 gange 600 med titlen "Pong" åbner med en hvid bat i hver side og en hvid bold i midten. Den højre spiller flytter den højre bat med piletasterne <kbd>Up</kbd> og <kbd>Down</kbd>, den venstre spiller flytter den venstre bat med <kbd>W</kbd> og <kbd>S</kbd>. Bolden preller af på top- og bundvæggen og på en bat, og hvert slag med en bat gør den hurtigere. Når en bat misser, får den anden spiller et point, bolden vender tilbage til midten, skifter retning, og farten nulstilles. Pointene vises øverst: den venstre spiller til venstre, den højre spiller til højre. Et klik på vinduet lukker det. Spillereglerne, der ikke kræver en skærm, ligger i `rules.py`, så de testes uden et vindue.

## Hvad øvelsen lærer dig

- At sætte skildpaddeskærmen op og tegne to bat og en bold som `Turtle`-objekter
- At flytte bolden billede for billede med `tracer`, `update` og `sleep` og lade den prelle af på væggene og batene
- At skrive klasserne `Paddle`, `Ball` og `Scoreboard` som underklasser af `Turtle`
- At binde to spilleres taster til to bat
- At finde et slag ud fra afstand og position, gøre bolden hurtigere og nulstille den, når en bat misser
- At holde reglerne fri af skærmen i `rules.py`, så de kan testes uden et vindue

## Hvad det gør

- To bat, en til hver spiller: Up og Down for den højre bat, W og S for den venstre bat
- En bold, der preller af på væggene og batene og bliver hurtigere ved hvert slag med en bat
- Et point til den anden spiller, når en bat misser; bolden vender tilbage til midten, og farten nulstilles
- En pointtavle med begge point øverst i vinduet
- Ingen afhængigheder ved kørsel ud over Pythons standardbibliotek

## Videre

- [Kom godt i gang](Getting-Started-da)
- [Projektdokumenter](Project-Documents-da)
