import pygame  # importeer de pygame module (pip install pygame)

X = 50  # de grootte van de stapjes waarmee het blokje op e x-as loopt
Y = 50  # de grootte van de stapjes waarmee het blokje op e y-as loopt
WIDTH = 50  # de breedte van het blokje
HEIGHT = 50  # hoogte van het blokje
SCREEN_WIDTH = 300  # de breedte van het spelscherm
SCREEN_HEIGHT = 300  # de hoogte van het spelscherm

pygame.init()  # initialiseer alle geïmporteerde pygame modules

WINDOW = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)  # defineer de breedtje en hoogde van het speelscherm in een tuple
pygame.display.set_caption("Moving Block")  # Titel van het spelletje

run = True  # variable met booleanwaarde True
while run:  # de while loop is True
    pygame.time.delay(100)  # update het scherm elke 100ms
    for (
        event
    ) in (
        pygame.event.get()
    ):  # deze code zorgt ervoor dat je op het kruisje kunt klikken om de game af te sluit
        if event.type == pygame.QUIT:
            run = False  # zet de main-game loop op false
    keys = pygame.key.get_pressed()  # luister naar toetsen die ingedrukt worden
    if (
        keys[pygame.K_a] and X > 0
    ):  # als X groter is dan 0 en de a-toets is ingedrukt voer dan uit anders niet dit zorgt voor een simpele collision-detection dit werkt hetzelfde voor de andere toetsen
        X -= WIDTH
    if (
        keys[pygame.K_d] and X < SCREEN_WIDTH - WIDTH
    ):  # hier gaat het net wat anders omdat we naar rechts gaan en de collision van het blokje linksboven aan het blokje zit moet en we ook nog de width van de screen-width afhalen
        X += WIDTH
    if keys[pygame.K_w] and Y > 0:
        Y -= HEIGHT
    if keys[pygame.K_s] and Y < SCREEN_HEIGHT - HEIGHT:
        Y += HEIGHT
    if keys[pygame.K_ESCAPE]:  # escape geklikt? we zetten de loop op False
        run = False

    WINDOW.fill(
        (0, 0, 0)
    )  # we vullen het scherm met een geheel zwarte kleur zodat we nieuwe dingen naar het scherm kunnen schrijven
    pygame.draw.rect(
        WINDOW, (255, 0, 0), (X, Y, WIDTH, HEIGHT)
    )  # draw het rode blokje de code spreekt voor zich
    pygame.display.update()  # en dan update je de display en voer je alles uit
pygame.quit()  # als de while loop stopt, sluiten we het venster
