---
title: "Anpassung von Ink/Stitch"
permalink: /de/docs/customize/
excerpt: ""
last_modified_at: 2019-03-15
toc: true
---

## Tastenkürzel

Die Arbeit mit Ink/Stitch und Inkscape kann erheblich beschleunigt werden, wenn Tastenkombinationen zugewiesen werden. Unter: `Bearbeiten > Einstellungen > Benutzeroberfläche > Tastenkürzel` können die gewünschten Tastenkombinationen eingetragen werden. [Inkscape anpassen (en)](http://wiki.inkscape.org/wiki/index.php/Customizing_Inkscape)

Die folgende Liste wurde von @lexelby vorgeschlagen:

Tastenkürzel | Effekt
------------ | ------
<nobr><key>Strg</key>+<key>Umschalt</key>+<key>O</key></nobr> | Objektübersicht (Objekt -> Objekte...)
<nobr><key>Strg</key>+<key>Umschalt</key>+<key>P</key></nobr> | Erweiterungen > Parameter (ohne Einstellungen)
<nobr><key>Strg</key>+<key>Umschalt</key>+<key>L</key></nobr> | Erweiterungen > Simulierung (Live Simulation)
<nobr><key>Strg</key>+<key>Umschalt</key>+<key>E</key></nobr> | Erweiterungen > Sticken (ohne Einstellungen)
<nobr><key>Strg</key>+<key>Umschalt</key>+<key>Bild↑</key></nobr> | Auswahl > Objekt anheben (ab Inkscape Version 0.92.2)*
<nobr><key>Strg</key>+<key>Umschalt</key>+<key>Bild↓</key></nobr> | Auswahl > Objekt absenken (ab Inkscape Version 0.92.2)*
<nobr><key>Strg</key>+<key>R</key></nobr> | Auswahl > Richtung umkehren**

*Die Funktionen "Objekt anheben" und "Objekt absenken" gibt es seit der Inkscape Version 0.92.2. Sie ermöglichen es die Objektreihenfolge zu manipulieren, auch wenn sich die Objekte sich nicht überlappen. Das ist sehr nützlich in Kombination mit dem Objektfenster (`Objekte > Objekte ...`). Die Objektreihenfolge gibt an, in welcher Reihenfolge die Elemente gestickt werden (von unten nach oben).
{: style="font-size: 70%" }

**Umkehr der Pfadrichtung. Bei Plattstich (Satinstich) und Laufstich kann die Stichrichtung geändert werden. Verwende dies mit der Inkscape-Einstellung und den Einstellung des Knoten-Tools `Pfadrichtung auf Konturen anzeigen`. Wenn man mit dem Knoteneditor nur ein Stützpunkt auswählt und Strg+R drückt, kehrt Inkscape nur einen Pfad in einem Objekt um. Dadurch wird sichergestellt, dass beide Ränder in einer Satinkolumne in die gleiche Richtung zeigen.
{: style="font-size: 70%" }

### Simulator Tastenkürzel

Der Ink/Stitch [Simulator](/de/docs/simulate/) hat bereits vordefinierte Tastenkürzel.

## Gitter

Um Vektoren richtig auszurichten, sollte die Rasterfunktion von Inkscape verwendet werden. Gehe zu `Ansicht` und aktiviere das `Seiten Gitter`. Stelle in `Einrasten-Kontrollleiste` sicher, dass `Am Gitter einrasten` aktiviert ist. Es ist auch möglich, den Abstand und den Ursprung der Gitter unter `Datei > Dokumenteinstellungen > Gitter` anzupassen.

![Gitter](https://user-images.githubusercontent.com/11083514/40359052-414d3554-5db9-11e8-8b49-3be75c5e9732.png)

## Aktivierung von Pfadkonturen & Pfadrichtungen

Die Kenntnis über die Pfadrichtungen sind wichtig, um mit Ink/Stich arbeiten zu können. Wir empfehlen daher, die Kontrollkästchen **Umriss zeigen** und **Zeige temporär Umrandung für ausgewählte Pfade** unter `Bearbeiten > Einstellungen > Werkzeuge > Knoten` zu aktivieren.

Stelle sicher, dass auch **Zeige Entwurfspfad** in der Werkzeugleiste wie in der folgenden Abbildung zu sehen ist, aktiviert ist.
[![Path outlines & directions](https://user-images.githubusercontent.com/11083514/40360721-f294ef0a-5dbe-11e8-9d4d-98f469ff1fba.png)](https://user-images.githubusercontent.com/11083514/40360721-f294ef0a-5dbe-11e8-9d4d-98f469ff1fba.png)

## Arbeiten mit Vorlagen

Wenn man Ink/Stitch häufiger verwendet, möchte man nicht die gleichen arbeiten immer und immer wiederholen. In diesem Fall kann eine Vorlage für die grundlegende Stickkonfiguration erstellt werden. Nachdem alles nach Wunsch organisiert wurde, speichere die Datei einfach in dem Vorlagenverzeichnis. Nun kann mit `Datei > Neu aus Vorlage` darauf zugegriffen werden.

Betriebssystem | Vorlagenverzeichnis
---|---
Linux   | `~/.config/inkscape/templates`
Windows | `C:\Users\%USERNAME%\AppData\Roaming\inkscape\templates`

Es sollte das Benutzerverzeichnis für Erweiterungen in den Inkscape Einstellungen überprüft werden. [Mehr dazu](/de/docs/faq/#ich-habe-die-aktuelle-version-heruntergeladen-und-entpackt-was-soll-ich-jetzt-machen).

**Tip:** Hier gibt es [Vorlagen](/de/tutorials/resources/templates/) die du nutzen kannst.
{: .notice--info }
