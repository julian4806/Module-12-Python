numbers = []


def fout():
    print("uhhhh dat is niet helemaal goed...")


def goed():
    print("goedzo")


print("Welkom bij dit geweldige spelletje!")

antwoord = input("Klaar om te beginnen?! (ja) ")
score = 0
totaal_aantal_vragen = 10

if antwoord.lower() == "ja":
    antwoord = input("1. Wat is 3 * 3? ")
    if antwoord == "9":
        score += 1
        numbers.append(9)
        goed()
    else:
        fout()

    antwoord = input("2. Wat is 34 * 6? ")
    if antwoord == "204":
        score += 1
        numbers.append(204)
        goed()
    else:
        fout()

    antwoord = input("3. Wat is 2+2? ")
    if antwoord == "4":
        score += 1
        numbers.append(4)
        goed()
    else:
        fout()

    antwoord = input("4. Wat is 8 / 2? ")
    if antwoord == "4":
        score += 1
        numbers.append(4)
        goed()
    else:
        fout()

    antwoord = input("5. Wat is 53 * 2? ")
    if antwoord == "106":
        score += 1
        numbers.append(106)
        goed()
    else:
        fout()

    antwoord = input("6. Wat is 3 + 33? ")
    if antwoord == "36":
        score += 1
        numbers.append(36)
        goed()
    else:
        fout()

    antwoord = input("7. Wat is 23 * 1? ")
    if antwoord == "23":
        score += 1
        numbers.append(23)
        goed()
    else:
        fout()

    antwoord = input("8. Wat is 22 + 22? ")
    if antwoord == "44":
        score += 1
        numbers.append(44)
        goed()
    else:
        fout()

    antwoord = input("9. Wat is 342 * 2? ")
    if antwoord == "684":
        score += 1
        numbers.append(684)
        goed()
    else:
        fout()

    antwoord = input("10. Wat is 23 + 2? ")
    if antwoord == "25":
        score += 1
        numbers.append(25)
        goed()
    else:
        fout()

    print(
        "Je hebt de game afgerond goed gedaan!\n",
        "dit zijn al je ingevulde antwoorden",
        numbers,
        "je hebt in totaal",
        score,
        "van de 10 vragen goed vragen goed",
    )
