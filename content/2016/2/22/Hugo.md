+++
title="Hallo Hugo"
author="Dr. Azrael Tod"
issoid="blog/1636"
date = "2016-02-22T11:00:00"
aliases = "blog/1636"
tags = ["Quählkot", "Softwareschrott", "Technik", "g33ky.de", "Open-Source"]
+++
Früher™ hatte ich mal ein tag "G33KY.de wird eingestellt/stirbt" (oder so ähnlich) und habe es absichtlich in jedem 2. Eintrag angehängt. Das war sowohl passend als ich auf Blogger feststellte dass ich "kaum noch" sinnvolle Sachen schrieb, ebenso als ich zu Wordpress wechselte, erst recht als ich 1-2 Jahre später feststellte wie unfassbar scheiße beides war und erst recht als ich meinen eigenen Python/Django-Frickelscheiß schrieb um das alles selber besser zu machen.

Das tag gibt es schon lange nicht mehr, bei einer der vielen Migrationen (ich glaube Wordpress -> WebChao) ist es wohl verloren gegangen. Was jedoch noch immer vorhanden ist sind die alten Beiträge. Lesen will die zum Glück keiner mehr.

Jedenfalls hat WebChao als eigene Frickellösung jetzt bisher noch am längsten durchgehalten. Irgendwann nach der [Domain-Umstellung Anfang 2008](/2008/4/28/Aus..-%C3%A4h-Umziehen%21/) begonnen, habe ich es jetzt glaube 6-7 Jahre aktiv verwendet und mal auf einer [Via NANO-Kiste](/2008/11/16/Homeservergeh%C3%A4use/), mal auf einer [Linksys NSLU2](/2009/9/15/Slug-Linksys-NSLU2/) und dann auf 2-3 VServern laufen lassen.

Und doch hat mich das Gefrickel immer genervt. Der selbstgeschriebene Code war schnell, bot alle Funktionen die ich ursprünglich haben wollte, war aber nie klein oder gar elegant. Überhaupt... Für jede Anfrage ein Python-Script laufen lassen und ständig den Code auf neue Django-Versionen zu portieren war nichts das ich so auf Dauer belassen wollte.

Nachdem ich auf [Dreigeparkt](http://dreigeparkt.de) nun schon eine Weile mit [Hugo](http://gohugo.io) rumgespielt habe und ich generell die Idee dieser Static-Site-Generatoren gut finde, bot sich dies als Ausweg ja an.

Also habe ich vor ein paar Wochen mal alle Posts per wget gesichert

    wget -i http://g33ky.de:8000/blog/list -x

Alles gelöscht was nicht Beitrag ist und dann aus dem Rest per kurzem Python-Script alle Metadaten, Kommentare und den eigentlichen Inhalt extrahiert und in eine neue Datei schreiben lassen:
{{% gist a9c52e8d6932060bbd79 %}}

Dann noch kurz dieses Script über alle Dateien laufen lassen und die alten Daten löschen:

    find content/ -iname '*.old' -type f -exec ./convert.py {} \;
    rm content/*/*/*/*.old

...und schon hat man alle Dateien schön Hugo-kompatibel in einem Verzeichnis gestapelt.

[Isso](https://posativ.org/isso/) hatte eh schon auf WebChao das alte Kommentarsystem ersetzt, also war auch das kein großes Problem. Einfach die passende ID rauskramen und Teplates kurz anpassen und schon tut das wieder.

Das Ergebnis seht ihr dann gerade.

Nebeneffekte sind dann z.B.:

- dass ich jetzt direkter Markdown oder ähnliches für neue Beiträge hinwerfen kann (HTML geht natürlich trotzdem weiterhin)
- Autoren sind nicht auf jene 3 Personen eingeschränkt, denen ich Accounts in die DB gefrickelt habe und denen ich zutraue keinen Scheiß mit dem Admin-Backend zu bauen. (Sehen wir es realistisch: niemand von denen kennt sein Passwort noch). Wenn jemand einen Beitrag schreibt braucht er mir nur eine Markdown-Datei schicken und ich werf' sie ins Verzeichnis
- schneller
- kein Django \o/

Hugo-Code-Beispiel anhand dieses Beitrags:

{{% gist fa31b683c79a33a9c33d %}}
