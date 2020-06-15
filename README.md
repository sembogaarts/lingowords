# Lingowords [![Build Status](https://travis-ci.org/sembogaarts/lingowords.svg?branch=master)](https://travis-ci.org/sembogaarts/lingowords)
Ontwikkeld voor VKBEP dit is deelopdracht 1, zorgt voor het importeren van de woorden. Deze repo staat live op [sembogaarts.nl](lingo.sembogaarts.nl).

## Installatie
Vereist is Python 3 en Pip 3.

```$xslt
pip install -r requirements.txt
```

Nadat dit process klaar is maak je je eigen enviroment bestand aan door het onderstaande commando. Pas hier ook vervolgens de variables in aan zodat ze kloppen voor jouw systeem.

```$xslt
cp .env.example .env
```

**Belangrijk!** Om de database te gebruiken draai je de lingogame applicatie in de andere repository, zorg ervoor dat de database als eerst wordt ingesteld!

## Tests
Ik maak gebruik van UnitTests om alle helpers te testen. Travis test bij elke wijziging, om de tests handmatig uit te voeren voer je de volgende commando's uit.

```$xslt
php artisan dusk
php vendor/phpunit/phpunit/phpunit
```

## Security Audits
Omdat het om een prototype gaat is er gebruik gemaakt van tokens die gegenereert worden en als cookie worden toegevoegd. Dit zou geen veilige manier zijn op het moment dat dit in productie gaat. Mensen kunnen namelijk token stelen om zo voor te doen als iemand anders. Omdat er geen persoonlijke informatie wordt opgeslagen maakt het inprincipe voor nu niets uit.

Als de applicatie in productie zou gaan zou ik wel aanraden om over te gaan naar account i.p.v. het opvullen van tokens.

## Code Coverage
In de repo zit een afbeelding van de code coverage met XDebug. In PHPStorm dit eenvoudig worden nageboots, indien gewenst.

## Continous Integration (CI)
Voor CI maak ik gebruik van [TravisCI](https://travis-ci.org/). Travis is gratis voor opensource projecten en geeft ook in deze repo weer of een branch goedgekeurd is.

## Continous Deployment (CD)
De applicatie wordt niet gedeploy en runt  momenteel alleen lokaal.
