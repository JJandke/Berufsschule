---
typora-copy-images-to: /img

---

>  **Präambel:**
>
>  Dies ist ein Versuch den gesamten Stoff für die IHK-Zwischenprüfung (FiSi etc.) zusammenzufassen. 
>  Als Grundgerüst dient die Themengliederung der IHK. Inhaltlich wurden Hefteinträge aus der Berufsschule, Websiten und eigenes Wissen genutzt. 
>  Sicherlich ist diese Übersicht keineswegs vollständig und zu 100% richtig, wenngleich ich mir größte Mühe dabei gebe. 
>  Änderungsvorschläge können gerne per [Issue auf GitHub](https://github.com/JJandke/Berufsschule/issues) eingereicht werden.
>
>  Dieses Dokument existiert in mehreren Versionen. Es ist wahlweise als gerendertes **Markdown** über die Plattform [**Hedgedoc**](http://hedgedoc.ddns.net:3000/s/SwqeuauoT) `(http!)` aufrufbar. Diese bietet den Vorteil eines dauerhaft präsenten Inhaltsverzeichnisses. 
>  Eine Weitere Version steht als **[HTML](http://hedgedoc.ddns.net/)** zu Verfügung `(http!)` Hier ist die Formatierung *(vor allem die Größe der Bilder und manche Formeln)* besser. Allerdings existiert nur ein Inhaltsverzeichnis am Anfang der Seite. 
>  Die dritte Möglichkeit besteht darin den [Markdown-Quellcode](https://github.com/JJandke/Berufsschule/blob/master/Zwischenpr%C3%BCfung/Stoffsammlung.md) selbst zu rendern. Dazu empfehle ich die Software [Typora](https://typora.io/). 
>
>  Die Datei wird soweit möglich laufend erweitert und hoffentlich zeitnah fertiggestellt. Da es unter Umständen vorkommen kann, dass es unterschiedliche Versionen gibt *(Prozess:  Quellcode/ Git –> HTML und händisch Hedgedoc)*, verweise ich mit dem **Timestamp** auf die **aktuell** **gezeigte** **Version**. Tendenziell ist die **HTML-Version die aktuellste**, da diese nach jedem Git-Push automatisch aktualisiert wird. (Latenz <= 5min)
>
>  Timestamp: `16-02-2024 21:19`

 

# Inhaltsverzeichnis

[TOC]



> [!TIP]
>
> **Ein paar lernenswerte Themen:**
>
> - OSI-Modell
> - `ifconfig` und `arp-a`
> - IPv6
> - VPNs
> - Rechnung: Übertragungsgeschwindigkeit, `Bit` vs. `Byte`
> - Rechnung: Netzteil
> - Malwareformen
> - It-Service Formen
> - CAD-Arbeitsplatz (Ergonomie)
> - Steckertypen
> - Kaufvertrag





------



# 1 Arbeitsaufgaben in Abstimmung mit Geschäftsprozessen

## 1.1 Projekmanagement

### Strukturplan

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/PSP_Umzug.jpg" align=left alt="Projektstrukturplan – Wikipedia" style="zoom: 80%;" />



### Netzplan

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/netzplantechnik-beispiel-teamevent.pngwidth%3D600%26name%3Dnetzplantechnik-beispiel-teamevent.png" align=left alt="Grafik Netzplantechnik Beispiel Teamevent" style="zoom:;" /> ![Grafik Netzplantechnik Vorgangsknoten](https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/netzplantechnik-vorgangsknoten.pngwidth%3D363%26name%3Dnetzplantechnik-vorgangsknoten.png)

| Bez. | Bedeutung                                                    |
| ---- | ------------------------------------------------------------ |
| Nr.  | Vorgangsnummer                                               |
| D    | Vorgangsdauer                                                |
| FAZ  | früheste Anfangszeit des Vorgangs                            |
| FEZ  | früheste Endzeit des Vorgangs                                |
| SAZ  | späteste Anfangszeit für den planmäßigen Gesamtvorgang       |
| SEZ  | späteste Endzeit für den Vorgang zur Einhaltung des Projektendtermins |
| GP   | Gesamtpuffer (wie weit kann Vorgang verschoben werden, ohne Endtermin zu beeinträchtigen) |
| FP   | freier Puffer (wie weit kann Vorgang verschoben werden, ohne nächsten zu beeinträchtigen) |

Kritischer Pfad: Sobald verzögerter Prozess e. GP von 0 hat lander er auf dem kritischen Pfad



### Gantt-Diagramm

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/parts-of-gantt-chart%402x.png" align=left alt="Aufbau von Gantt Digrammen | Lucidchart" style="zoom:67%;" />

- Kritischer Weg
- Pufferzeiten
- fristgerechte Terminierung
- Meilensteine



### Projektphasen & SMART

<img src="https://www.factro.de/wp-content/uploads/2021/11/Graph2.png" align=left alt="Graphik eines iterativen Projektphasenmodells" style="zoom: 25%;" /> <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Wordpress_SMART-Methode-1024x576.jpg" alt="SMART Methode • Definition & Beispiele · [mit Video]" style="zoom: 41%;" />

1. **Start** (klärung grundsätzl. Bedingungen, Projektsteckbrief, SWOT-Analyse) –> Realisierbarkeit, Zweck, Wert
2. **Planung** (Zeitraum, Beteiligte, Ausgangssituation, Sach- Terminziel, Budget) 
3. **Durchführung** (Aufgabenverteilung, hängt mit `4. Steuerung` zusammen)
4. **Steuerung** (Status, Fortschritt, potent. Probleme)
5. **Abschluss** (Abschlussbericht)

### Projektmerkmale

Einmalig – Einzigartig – Begrenzte Ressourcen – Festgelegte Zeit – birgt Risiko – konkretes Ziel – komplex



### Vorgehensmodelle

| Traditionell                                               | Agil                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Wasserfall**: Schritte werden nach und nach abgearbeitet | **Scrum**: kleines Team unter Leitung von Scrum Master (beseitigt Hürden)<br />arbeit in Sprints (zweiw. Zyklen), tägliche Meetings |
|                                                            | **Kanban**: Arbeit mit Kanban Board –> Einteilung in z.B. ToDo \| In Progress \| On Hold \| Done |



### Teambildung

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/tuckman-phasenmodell-forming-storming-norming-performing.png" align=left alt="Forming, storming, norming, performing: In 4 Phasen zum perfekten Team" style="zoom: 67%;" /> 

















- Reflektion, Ich-Botschaft, gute Feedback-Kultur, Lessons-Learned…





## 1.2 Machbarkeit von Projekten

### Machbarkeitsanalyse

- **organisatorische** Umsetzung
- **wirtschaftliche** Machbarkeit (z. B. Kostenrahmen, Finanzierung)
- **technische** Machbarkeit
- **Ressourcen** und Verfügbarkeit (z. B. Mensch, Maschinen, Flächen, Material und Zeit)
- **zeitliche** Umsetzung
- **rechtliche** Umsetzung (**DSGVO**, **BDSG**)



### Stakeholderanalyse

| **Schritt 1**                                                | **Schritt 2**                                                | **Schritt 3**                                                | **Schritt 4**                                                |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Identifikation** der Stakeholder                           | Darstellung der **Beziehungen**                              | Interpretation und **Analyse**                               | Ableitung von **Maßnahmen**                                  |
| **Wer** ist an dem Projekt beteiligt?<br />Wer hat Interesse am Projekt / ist davon betroffen?<br />Welche Prozesse werden beeinflusst? | **Interne** / **externe** Stakeholder<br />Bedeutung der Stakeholder<br />Intensität der Beziehungen | **Erwartungen** an das Projekt<br />Ziele / **Interessen** <br />Einfluss, Macht und Einstellung zum Projekt | Einschätzung von **Chancen** / Risiken<br />Umsetzungsstrategie<br />Maßnahmen- / Kommunikationsplan<br />Beteiligung im Projekt |



### Risikoanalyse

- **Technische** Risiken
- **Planungsrisiken**
- **Vertragliche** Risiken
- **Kaufmännische** Risiken
- **Personelle** Risiken
- **Politik**- und **Umweltrisiken**
- **Chancenanalyse**



### Abklärung von Rahmenbedinungen

- wirtschaftlich, technisch, rechtlich, terminlich



### Stamm- Bewegungsdaten

- **Stammdaten**: Geburtsdatum, Kundennummer etc.
- **Bewegungsdaten**: Rechnungsnummer, Preis, Bestellte Ware etc.





## 1.3 Arbeitsaufgaben planen

### Support

| First-Level                                                  | Second-Level                                                 | Third-Level                                                  | Anwender-Support                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| erste Anlaufstelle<br />häufige Probleme<br />breites, allgemeines Wissen | besser geschultes Personal<br />tiefes Fachwissen<br />bekannte Probleme | komplexe, nie dagewesene Probleme<br />kein dir. Kundenkontakt | Unterstützung d. Kunden<br />bei bekannten Problemen,<br />Einrichtung etc. |



### Managemet-Arten

| Fehlermanagement                                             | Störungsmanagement                                          |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| häufige Probleme/ Anfragen<br />Spezifizieren, kategorisieren, priorisieren | Abweichung d. norm. Betriebs (Störung)<br />Supportanfragen |







---

# 2 Kundenberatung

## 2.1 Marktsituationen

### Marktformen

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Screenshot_20240207-181705-1707641582463-25.png" alt="Screenshot_20240207-181705" align=left style="zoom: 45%;" />



### Organisationsformen

<img src="https://d1g9li960vagp7.cloudfront.net/wp-content/uploads/2023/06/WP_Einlinienorganisation-1024x576.jpg" alt="Organisationsformen • Definition, Formen und Beispiele · [mit Video]" style="zoom:33%;" /> <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/WP_Mehrlinienorganisation-1024x576.jpg" alt="Organisationsformen • Definition, Formen und Beispiele · [mit Video]" style="zoom:33%;" /> 

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Stablinienorganisation-1024x576.jpg" alt="Organisationsformen • Definition, Formen und Beispiele · [mit Video]" style="zoom:33%;" /> <img src="https://d1g9li960vagp7.cloudfront.net/wp-content/uploads/2023/06/WP_Matrixorganisation-1024x576.jpg" alt="Organisationsformen • Definition, Formen und Beispiele · [mit Video]" style="zoom:33%;" /> 



### Vertragsgestaltung

![Screenshot_20240208-164551](https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Screenshot_20240208-164551-1707641582463-26.png)



**Kaufvertragsstörungen:**

- Falschlieferung
- Montagemangel
- fehlerhafte Montageanleitung
- Quantitätsmangel
- Qualitätsmangel



## 2.2 Bedarfsanalyse

- Zielgruppengerecht z.B. CAD-Designer
- Bedarfs- Betreffsgerechte Präsentation
- Eigene Datenerhebung
- Auswertung v. Daten –> z.B. Anforderung an Büroarbeitsplätze

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Ergonomie-am-Arbeitsplatz-Definition-Licht-Buerostuhl-Tipps-Infografik.png" align=left alt="Ergonomie am Arbeitsplatz: Tipps + Beispiele für das Büro" style="zoom: 67%;" />



## 2.3 Kundenberatung

### Kommunikationsmodelle

#### Sender- Empfängermodell

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Sender-Empf%C3%A4nger-Beispiel.png" align=left alt="Sender-Empfänger Modell - Schritt für Schritt erklärt (+Beispiel)" style="zoom: 67%;" />



#### Eisbergmodell

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Eisbergmodell_WP_Bild_1-1024x576.jpg" align=left alt="Eisbergmodell • Kommunikationsmodell, Freud · [mit Video]" style="zoom:50%;" />



#### 4-Ohren Modell

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/4-Seiten-einer-Nachricht-Schulz-von-Thun.jpeg" align=left alt="4-Ohren-Modell: Einfach erklärt + Beispiele" style="zoom:50%;" />



## 2.4 Informationsaufbereitung

- Technische und nicht-technische Texte   
- Digitale Suchabfragen unter Verwendung von Suchoperatoren  –> Google Suche (“”, *, etcl.)
- Auswertung von englischen Texten   
- Qualitätsmerkmale von **Präsentationen**   
  - Stichpunkte, keine Sätze
  - gut lesbar
  - nicht zu viel auf einer Folie
  - Prägnant
  - Man selbst ist der Vortrag, Präsentation nur unterstützend
- Medienkompetenz   



## 2.5 Marketingaktivitäten

### Nutzwertanalyse

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/peco-nutzwertanalyse-beispiel-neue-website-xl.png" align=left alt="Die Nutzwertanalyse - Peterjohann Consulting" />

### Vertriebsformen

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/vertriebsarten.pngwidth%3D601%26name%3Dvertriebsarten.png" alt="Vertriebsarten im Überblick" style="zoom: 67%;" /> 



---

# 3 IT-Systeme

## 3.1 IT-Systeme beurteilen

### Hardwareprodukte

- **CPU** 

- **Motherboard**

- **Speicher**: SSD, HDD, Tape

- **Netzteile**: Berechnung siehe  [3.3 Leistungsfähigkeit bestimmen](## 3.3 Leistungsfähigkeit bestimmen) 

- **Netzwerkkomponenten**:

  - **RJ45** Stecker: 8 Adern, LEDs an Port nicht genormt, Leuchten steht für Link erfolgreich, blinken für Link aktiv![image-20240208181413050](https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/image-20240208181413050.png)

    

  - (Q)**SFP**(+): Für Glasfasfaser, meist LC oder MPO-Kabel verwendet, bis zu 800Gbit/s

    <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/education-Singlemode-vs-multimode-lg.jpg" align=left alt="What is the difference between single mode vs. multimode fiber?- TC  Communications" style="zoom:50%;" /> <img src="https://www.glsunmall.com/resource/image/guideImage/transceivers.jpg" align=right alt="Differences Between SFP, SFP+, SFP28, QSFP+ and QSFP28" style="zoom:45%;" />

  









- **DSL** (16Mbit/s) – VDSL(50Mbit/s, 100Mbit/s) – SDSL(250Mbit/s)

- **Steckertypen**: Naja, was n HDMI/Display Port Stecker is, braucht ma wohl nicht extra aufschreiben oder?

  

### Softwareprodukte

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/fff1090_w.jpg" align=left alt="Betriebssystem - Lexikon der Physik" style="zoom:50%;" />

**Methoden des Softwaretestings**

- **Black-Box-Test:**Testet die Funktionalität einer Software, ohne Kenntnisse über die interne Struktur. Fokus auf den Input und die erwartete Ausgabe.
- **White-Box-Test:**Prüft die interne Struktur einer Software, einschließlich des Codes.Ziele sind Codeabdeckung, Pfadüberdeckung und Strukturanalyse.
- **Komponententest:**Einzelne Softwarekomponenten werden isoliert getestet.Ziel ist die Überprüfung der Korrektheit und Funktionalität jeder Komponente.
- **Unittest:**Testet einzelne Einheiten (z. B. Funktionen oder Methoden) des Quellcodes.Fokussiert auf die Isolation und Überprüfung kleiner Codeabschnitte.
- **Modultest:**Prüft, ob Module oder Teile eines Systems korrekt zusammenarbeiten.Umfasst mehrere Einheiten, die eine bestimmte Funktionalität bieten.
- **Integrationstest:**Überprüft die Interaktion zwischen verschiedenen Komponenten oder Modulen.Ziel ist es, Fehler in der Kommunikation und Zusammenarbeit aufzudecken.
- **Systemtest:**Testet das gesamte System als Ganzes.Überprüft, ob alle Komponenten integriert funktionieren und die Anforderungen erfüllen.
- **Abnahmetest:**Kunden oder Benutzer führen Tests durch, um sicherzustellen, dass die Software ihren Anforderungen entspricht.Ziel ist die Bestätigung der Benutzerfreundlichkeit und Erfüllung der Anforderungen.
- **Lasttest:**Simuliert eine hohe Belastung, um die Leistungsfähigkeit eines Systems zu überprüfen.Identifiziert Engpässe und Probleme unter Stressbedingungen.





### Virtualisierungen

| Pro                                                          | Contra                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - Stromersparnis (Weniger physi. Hardware)<br />- weniger Platzverbrauch<br />- schnelle Serverprovisionierung (Einrichtung, Bereitstellung)<br />- Anpassung an Kundenwünsche<br />- geringe Ausfallzeiten, Redundanzen durch Cluster<br />- IT-Sicherheit z.B. Remote Desktop | - Viel Leistung benötigt<br />- schnelles Netzwerk benötigt<br />- manche (leistungsintensive) Programme nicht für Virutalisierung geeignet |

- **Virtualisierung** Prozess,  Software zur Simulation von physischen Ressourcen
- **Hypervisoren**: Programm dass  virtuelle Maschinen erstellen und ausführen kann

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenprüfung/img/0uOG3TpWM2BlBYkbg.png" align=left alt="Type 1 and Type 2 Hypervisors: What Makes Them Different ..." style="zoom:50%;" />



### Cloudlösungen

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/iaas-paas-saas-diagram5.1-1638x1046.png" align=left  alt="img" style="zoom:50%;" />



## 3.2 Einsatzbereiche v. IT-Systemen

### Datenbanksysteme

- Organisation in **Clustern** für hohe Verfügbarkeit
- Hardware mit **performanten** (flash) Speicher Arrays und Networking benötigt 



### Netzwerkkomponenten

#### Router

| Eigenschaften                                                | Symbol                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - Layer 3<br />- Verbindung von Netzen<br />- **IP-Adressen**<br />- IS-IS, OSPF, I- bzw. EGP, BGP als Protokoll<br />- Häufig als “Gateway” bezeichnet | <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/router-1707641582464-27.png" align=left alt="router" style="zoom:25%;" /> |



#### Switch

| Eigenschaften                                                | Symbol                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - **Layer 2** (häufig mit L3 Funktionen wie VLAN-Routing etc.)<br />- Verbindung mehrere Netzelemente<br />- MAC Adressen<br />- **Forwarding** Rate in `packets/sec`. vs. **Switching** capacity in `Bit/sec`<br />- evt. **PoE**(+) Fähigkeiten<br />- **ARP-Speichergröße**: #speicherbare MAC-Adressen<br />- **Buffer Size**: Zwischenspeicher für Store-Forward Modus<br />- **Cut-Trough**: Weiterleitung ohne Prüfung der FCS (Frame Check Sequence)<br />- **Store-Forward**: Zwischenspeicherung d. Pakete und Berechnung d. Prüfsumme<br />- Bildung von **VLANs** für Sicherheit, Managing etc. | <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/switch-1707641582464-28.png" align=left alt="switch" style="zoom:25%;" /> |



**AP**: Bereitstellung von W-LAN

**HUB**: Nutzt kein Mensch mehr (Außer in USB-Dockingstations)



#### Topologien

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/6230eed9d9792f3709c5ffd6_5f1086baa37c842a30184650_network-topology-types-diagram.png" alt="What is Network Topology? Definition and FAQs | HEAVY.AI" style="zoom: 25%;" />



### Netzwerkprotokolle

#### OSI-Modell

[Erklärung und Video von SimpleClub](https://simpleclub.com/lessons/fachinformatikerin-grundlagen-osi-modell)

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/seven-layers-of-OSI-model.png" align=left alt="TCP/IP vs. OSI: Was ist der Unterschied? | FS Community" style="zoom: 80%;" />

`1-7 englisch`: **P**hysiker **D**ie **N**icht **T**rinken **S**ind **P**otentielle **A**ttentäter 



### Einheiten der Informatik

Ein ungeschriebener Standard ist, dass **Speichergrößen** (Datei bzw. Ornder) in **Byte** `B` angegeben werden, da man mind. 8 Bit benötigt um ein Zeichen z.B. `A` zu speichern.

**Übertragungsgeschwindigkeiten** beim Kopieren von Dateien werden in **Byte/s** `B/s` angegeben .
Anders ist das bei **Netzwerkgeschwindigkeiten**, diese werden in **bit/s** `b/s` angegeben. 
Das rührt daher, dass bei Dateiübertragungen interessant ist, wie viel einer Datei pro Sekunde übertragen werden kann, während bei Netzwerkgeschwindigkeiten das physische Übertragen der einzelnen Bits ([Leitungscodierung](https://www.elektroniktutor.de/internet/codes.html)) interessiert. 



**Binär- vs. Dezimalsystem** (oder was Microsoft nachwievor falsch macht…)

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenprüfung/img/ukuran-penyimpanan-data-byte.png" align=left alt="img" />

Binär: $$2^x$$ 													Dezimal: $$10^x$$ 



**Umrechnung Bit < – > Byte**

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenprüfung/img/Imagen6-69ea70bd-7e92-4432-9c97-106f491415fb.jpg" align=left alt="Bits, Bytes, Mebibyte: ¿Qué son y cómo resolverlos?" style="zoom: 40%;" />



**Übertragungsgeschwindigkeit**

geg: Datei $$F = 1 GB$$, eigener Upload: $$U = 75,7 Mbit/s$$, serverseitiger Download: $$D = 10 Gbit/s$$

ges: Übertragungszeit $$t$$

Rechnung:

> $$ 1 GB \times 8 \quad \widehat{=} \quad 8 Gbit$$	// Umrechnung in gleiche Einheiten
>
> $$\dfrac{8.000 Mbit} {75,7 Mbit/s} = 105,6s$$	// Umwandlung Gbit in Mbit und gleichzeitig durch den Upload (weil kleiner als Download) dividieren
>
> $$105,6 \div 60 \approx 2min$$	// Umrechnung in Minuten











## 3.3 Elektrotechnik

### Wirkungsgrad

$$\eta = \dfrac{\Delta E_{nutz}}{\Delta E_{zu}} \qquad \widehat{=} \qquad \eta = \dfrac{\Delta P_{nutz}}{\Delta P_{zu}}$$

| Bezeichner          | Name                   | Einheit    |
| ------------------- | ---------------------- | ---------- |
| $$\eta$$            | **Wirkungsgrad**, eta  | %          |
| $$\Delta E_{nutz}$$ | **Nutzenergie**        | z.B. $$W$$ |
| $$\Delta E_{zu}$$   | **zugeführte** Energie | z.B. $$W$$ |



### Strom, Spannung, Leistung

$$P_{El} = U * I$$​

| Bezeichner | Name                     | Einheit      |
| ---------- | ------------------------ | ------------ |
| $$P_{El}$$ | elektrische **Leistung** | Watt $$W$$   |
| $$U$$      | **Spannung**             | Volt $$V$$   |
| $$I$$      | **Strom**                | Ampere $$A$$ |



### Leistungsaufnahme

$$W = P_{El} * t$$​ 

| Bezeichner | Name                    | Einheit             |
| ---------- | ----------------------- | ------------------- |
| $$W$$      | **Arbeit**              | Wattsekunden $$Ws$$ |
| $$P_{El}$$ | elektische **Leistung** | Watt $$W$$          |
| $$t$$      | **Zeit**                | Sekunden $$s$$      |



### Widerstand

$$ R = \dfrac{U}{I} $$​

| Bezeichner | Name           | Einheit          |
| ---------- | -------------- | ---------------- |
| $$R$$      | **Widerstand** | Ohm $$\ohm$$     |
| $$U$$      | **Spannung**   | Volt $$V$$ $$W$$ |
| $$I$$      | **Strom**      | Ampere $$A$$     |



### Netzteil

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/power-supply-chart04.jpg" align=left alt="5 Things to Pay Attention to When Choosing A Power Supply" style="zoom: 33%;" />

|                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/image-20240216175251134.png" align=left alt="image-20240216175251134" style="zoom: 25%;" /> | - Aufteilung in mehrere Schienen, da sonst die Kabel zu dick werden<br /><br />- Maximallast (700W) darf nicht überschritten werden, auch wenn Summe der Einzelströme größer ist |





### 3.4 Wirtschaftlichkeit v. IT-Systemen

- Abschaffungs-, Betriebskosten 
- Varibale-, Fixkosten
- Kostenvergleich (Leasing, Kauf, Miete, Pay-per-use)
- [Nutzwertanalyse](###Nutzwertanalyse)





---

# 4 Erstellen von IT-Lösungen

## 4.1 IT-Systeme konzeptionieren

### Bedarfsanalyse

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Bedarfsanalyse-Zielgruppe-oder-Stakholder-und-ihre-Bedarfe.png" align=left alt="Bedarfsanalyse" style="zoom: 33%;" />



### Lasten- Pflichtenheft

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Lastenheft-Pflichtenheft-1707641582469-31.png" align=left alt="Lastenheft-Pflichtenheft" style="zoom: 50%;" />



### Betriebssysteme

- **Linux**: Server, Workstations, CPS
- **Windoof**: Workstations, Büro-PC, Thin-Clients
- **MacOS**: für alle die’s unbedingt brauchen, kreative, Berater etc.





## 4.2 Auswahl von Hardware

- Desktops, Notebooks, Thin-Client, Workstation entsprechend der benötigten Anforderungen
- **Barrierefreiheit**: zwei Monitore, Lautsprecher, Mikro…
- Immer an gegebene Bedingungen angepasst –> [Bedarfsanalyse](## 2.2 Bedarfsanalyse) 





## 4.3 Auswahl von Software

-   [Betriebssysteme](#### Betriebssysteme), Nutzeroberfläche für Kunden  

- **Anwendungssoftware**: Lösung von Benutzerproblemen, -anforderungen

- Integrierte Entwicklungsumgebung (IDE) –> vereinfachte Programmierung, Kompilieren etc.

- Standard- oder Individualsoftware –> Word und Spezialsoftware für die Verwaltung von IP-Adressen

- Open Source vs. Proprietäre Software 

  | Open Source vs. Proprietary | Open Source                                                  | Proprietary                                                  |
  | --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | **Kosten**                  | meist freie Nutzung und Anpassbarkeit<br />Quellcode frei verfügbar/ einsehbar | meist kostenpflichtig/ Lizenzmodelle<br />Quellcode nicht einsehbar |
  | **Updates<br />Wartung**    | meist reguläre Updates und sofortige Sicherheitspatches<br />–> hängt von Software/ Projekt ab<br />durch offenen Sourcecode weniger anfällig für Sicherheitslücken | (garantierte) reguläre Updates<br />meist sofortige Sicherheitspatches<br />kann unbekannte Sicherheitslücken enthalten |
  | **Flexibilität**            | meist frei veränder- anpassbar<br />kann auf eigene Bedürfnisse zugeschnitten werden | kein Zugang zum Quellcode, daher weniger flexibel            |
  | **Support**                 | bei Community-Projekten kaum Support<br />bei Produkten von Firmen (z.B. RHEL) guter Support –> Finanzierungsmodell | Normalerweise Kundensupport verfügbar                        |





## 4.4 Lizenzmodelle

- **EULA** (End User License Agreement): Lizenztvereinbarung, der der Nutzer zustimmen muss.
  - Endbenutzer-Lizenzvereinbarung
  - Lizenvereinbarung zwischen Hersteller einer Software & Endbenutzer
  - Endbenutzer muss Vereinbarung vor Nutzung der Software zustimmen
  - legt detailliert Rechte & Einschränkungen fest, die für die Nutzung der Software gelten
  - WICHTIG ist der Begriff: "nutzen" --> keine Eigentumsrechte an der Software




- **OEM** für den Weiterverkauf z.B. ein Dell-Rechner mit vorinstalliertem Windoof
  - Original Equipment Manufacturer / Originalausrüstungshersteller / Erstausrüster
  - rein lizenztechnisch ist Verkauf von OEM-Software nur in Verbindung mit Hardware erlaubt
  - Beispiel: Microsoft verkauft günsitgere OEM-Versionen von Windows 10 an Hersteller, die dann aber vertraglich die Software mit dem neuen PC ausliefern müssen



- **GNU GPL** Copyright-Richtlinie für Open-Source Projekte(Ausführung, Änderung, Erweiterung,  Wiederverwendung –> *nur mit gleichem Lizenzmodell*)
  - GNU GPL --> GNU General Public License
  - Copyright-Richtlinie für Open-Source-Software
  - beschreibt wie Nutzer das Programm kopieren, modifizieren & weitergeben dürfen

**Generell:**

- beidseitiger Vertrag, indem der Inhaber bestimmter Produkte seine Rechte bezüglich des Produktes vollumfänglich oder nur zum Teil auf einen anderen übertragt
- darin wird geregelt, wie häufig, in welchem Umfang & wo die Produkte eingesetzt werden dürfen
- meist zeitlich begrenzt --> sobald Vertrag endet darf das Produkt nicht weiter genutzt werden





## 4.5 Installation und Konfiguration

### Formatierung/ Partitionierung

![image-20240210165340532](https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/image-20240210165340532.png)

- **Aufteilung e. Festplatte** in mehrere versch. Partitionen z.B
  Partition 1 für BIOS/GRUB Informationen
  Partition 2 für Linux
  Partition 3 für Windoof
- **Dateisystem = Formatierung** e. Partition: ntfs, ext4, fat32…
- Jede phys. Festplatte besitzt mind. eine Partition mit einem Dateisystem, mehre Partitionen auch möglich

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/image-20240210165806009.png" align=left alt="image-20240210165806009" style="zoom: 50%;" />



### Netzwerkanbindung, Ip-Konfiguration

#### ifconfig/ ipconfig

Gibt Auskunft über die IP-Konfiguration des Hosts. Es können wahlweise alle Netzwerkschnittstellen oder nur Einzelne (wie in diesem Beispiel `eth0`) angezeigt werden. Auf Windoof heißt der Befehl `ipconfig`.

```sh
╭─user@host ~ 
╰─$ ifconfig eth0 # Befehl: ifconfig; Ausgewähltes Interface: eth0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.28.6  netmask 255.255.255.0  broadcast 192.168.28.255 # (lokale) IPv4 Adr. | Subn. Maske | Broadcast Adr.
        inet6 2003:cf:2700:bd00:e168:587:caff:ee00 # IPv6 durch ISP zugewiesen, beginnt mit 2003 bei Telekom
        inet6 2003:cf:2700:bd00:b00b:saa7:dead:beef # IPv6 durch ISP zugewiesen, beginnt mit 2003 bei Telekom
        inet6 fd00::fdc1:1fce:238a:75a1 # ULA-Adresse, für Kommunikation im lokalen Netz
        inet6 fe80::2dae:7419:3391:6dab # Linklokale IPv6, nicht routbar, nur im lokalen Netz, keine Nutzdatenübertragung
        ether c8:7f:87:05:99:8a # MAC-Adresse
```

Da es mehr IPv6 Adressen gibt, als genutzt werden können, weißen ISPs oft mehrere IPv6 Adressen zu, die für versch. Zwecke verwendet werden können.
Da in diesem Beispiel NAT zu Verwendung kommt, wird eine lokale IPv4 Adresse angezeigt. 



#### arp -a

Gibt die ARP-Tabelle des Hosts aus. In dieser werden Informationen zu Netzelementen im eigenen Netz gespeichert und für die Kommunikation (auf L2-Ebene) verwendet. Die Daten wurden zuvor per Boradcast ermittelt. 

```sh
╭─user@host ~ 
╰─$ arp -a                     
fritz.box (192.168.28.1) at 1c:e1:ce:ba:be:d5 [ether] on eth0
prod-nas (192.168.28.89) at 5a:11:ab:0a:70:de [ether] on eth0
pi.hole (192.168.28.77) at e4:7a:11:a1:ec:af [ether] on eth0
# Hostname | IPv4 | MAC-Adresse | Netzwerkinterface
```

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/ARP-table-diagram.png" align=left alt="img" style="zoom:50%;" />



#### dig

Wird verwendet um DNS-Auflösungen anzufordern. Z.B. Domain zu IP-Adresse

```java
╭─user@host ~ 
╰─$ dig telekom.de // Domain, von der ich die IP-Adresse möchte 
[...]

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;telekom.de.			IN	A

;; ANSWER SECTION:
telekom.de.		600	IN	A	80.158.67.40 // IP-Adresse hinter telekom.de

;; Query time: 35 msec
;; SERVER: 192.168.28.77#53(192.168.28.77) (UDP) // DNS-Server, der meine Anfrage beantwortet hat
;; WHEN: Fri Feb 16 21:26:59 CET 2024
;; MSG SIZE  rcvd: 55
```



#### traceroute/ tracert

Unter Windoof `tracert`


```java
╭─user@host ~ 
╰─$ traceroute google.de 
traceroute to google.de (142.251.36.227), 30 hops max, 60 byte packets
 1  fritz.box (192.168.28.1)	// FritzBox daheim
 2  p3e9bf396.dip0.t-ipconnect.de (62.155.243.150)	// Router der Telekom 
 3  m-ef2-i.M.DE.NET.DTAG.DE (217.5.93.206)	// Router der Telekom 
 4  m-ef2-i.M.DE.NET.DTAG.DE (217.5.93.206)	// Router der Telekom 
 5  80.150.169.10	// Router der Telekom 
 6  192.178.105.183	// Router in den USA
 7  192.178.105.115	// Router in den USA
 8  216.239.63.97  108.170.228.33	// Router in den USA
 9  muc11s22-in-f3.1e100.net (142.251.36.227)	// Router von Google

```



## 4.6 Programmiersprachen

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Execution-Flow.jpg" align=left alt="Executable Generation Flow" style="zoom: 67%;" />

- **Linker**: fasst Code zusammen (auch ext. Liraries) und kreiert ausführbare Datei

- **Compiler**: generiert ausführbare Datei vor Laufzeit

- **Interpreter**: übersetzt während der Laufzeit Code in maschinenlesbare Befehke

- **Prozedurale** Herangehensweise: Scripting, Befehle werden nacheinander abgearbeitet *(SH, PowerShell, Fortran, Cobol, C, …)*

- **Objektorientierte** Herangehensweise: Klassen, Funktionen können voneinander aufgerufen und vererbt werden *(Java, C++, Python, Swift, …)*



### Datentypen & Strukturen

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/ds-introduction2.png" align=left alt="What are Data Structures? Definition and Types - javatpoint" style="zoom:80%;" />



### Kontrollstrukturen

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/control-structures-in-c.jpg" align=left alt="C++ Control Structures | Conditonal & Loops - Simple Snippets" style="zoom: 80%;" />



### Klassen & Vererbung

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/wJrAh11ciqUZ-uVxplOWnnX03ofWdb5EoJzZQBm3LCEkoLKZJ6u2IbMl9CcrG0qFsNfLwGfPey3QSCKpr3lgyG-FJOrvaqcFvNhCSW4MqSaEZucjcf4Vg9tEELsd3OnNDUYlGx52mGvcN6SKJPLkndGSMBGutNgqFsZnDaVtR4omVdla.png" align=left alt="Inheritance training in Java (in quite simple language) - ShopingServer Wiki" style="zoom: 67%;" />




### Skriptsprachen

- Shell-Skript
- Macros in z.B. Excel
- Visual Basics for Applications (VBA)



### Logikgatter

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/1.png" align=left alt="schoolphysics ::Welcome::" />



### Bibliotheken vs. Frameworks

**Bibliothek**: *You Call Us* –> keine eigenständige, ausführbare Einheit, enthält Codesammlung die in eigenen Code eingebunden werden können
			–> sehr flexibel, volle Kontrolle

**Framework**: *We Call You* –> Programmgerüste, liefern Bauplan und Grundgerüst der Anwendung, teilt Programmierer mit, was er benötigt
			–> Rad muss nicht neu erfunden werden, vorhandenes Grundgerüst schließt grobe Fehler aus



## 4.7 Programmierwerkzeuge

### PAP

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/9606a172-7cc7-4db3-a7a3-6c32a8b0bc63-1707645516999-13.png" align=left alt="img" style="zoom:50%;" />



### UML

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/sw-architektur-62304-2.png" align=left alt="UML Unified Modeling Language: Nicht nur für Software-Architekturen" style="zoom:48%;" />

- Wird durch Sprache, ähnlich wie LaTex/Markdown erstellt, 
- ER-Diagramm ist mehr oder weniger eine visuelle Repräsentation



### Struktogramm

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/8c04d2a1-92ea-400e-9971-0eded7e84bf7.png" align=left alt="img" style="zoom:60%;" />





## 4.8 Datenbankgrundlagen

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/fa13d8b2dc34239e95059ff1b.png" align=left alt="img" style="zoom: 80%;" />

**Datenintegrität** = Daten sind in sich und übergreifend widerspruchsfrei

**Datenkonsistenz** = Wenn Daten mehrfach (redundant) gespeichert sind, müssen sie immer Dasselbe aussagen.

**Redundanz** = Mehrfachspeicherung gleicher Information

**Integrierte Informationsverarbeitung** = Beinhaltet *Datenintegration* & *Vorgangsintegration*.

**Datenintegration** = Ist dann gegeben, wenn mehrere betriebliche Funktionsbereiche eine Datenbasis gemeinsam benutzen.

**Datenbasis** = Die Informationen, die in einer Datenbank stehen.

**Vorgangs, Funktions, Prozessintegration** = Ist dann gegeben, wenn mehrere Abteilungen die eigenen Vörgänge eines Prozesses abwickeln.

**Voraussetzung** für integrierte Informationsverarbeitung = **geeignetes Datenbankverwaltungssystem** ([DBMS](https://de.wikipedia.org/wiki/Liste_der_Datenbankmanagementsysteme) = Datenbankmanagementsystem)





### ER-Modelle

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/b3f971d63740325083623c474.jpg" align=left alt="img" style="zoom:67%;" />



### Einfache Syntax

Ausgegeben werden sollen: `Zeitstempel` und `ChipsID` aller **abgelehnten** Zutritte.
Es soll nach **Zeit** **absteigen** sortiert werden

```sql
SELECT Zeitstempel, tblChips_ChipsID
FROM tblZutrittsversuche
WHERE Ergebnis='Zutritt abgelehnt'
ORDER BY Zeitstempel DESC;
```



Ausgegeben werden sollen: jede `ChipsID`, die **mehr als 10** erfolgreiche **Zutritte** hat

```sql
SELECT tblChips_ChipsID, COUNT(*) AS Anzahl
FROM tblZutrittsversuche
WHERE Ergebnis = "Zutritt gestattet"
GROUP BY tblChips_ChipsID
HAVING Anzahl > 10;
```



---

# 5 Qualitätssicherung

## 5.1 Grundverständnis

- **Qualität nach ISO 9000**

  > Grad, in dem ein Satz inhärenter Merkmale eines Objekts Anforderungen erfüllt.

  - Qualität gibt an, in welchem Maße ein Produkt (Ware oder Dienstleistung) den bestehenden Anforderungen entspricht.

  - **Objektive Qualität**: messbar, lässt sich anhand versch. Kriterien quantifizieren
  - **Subjektive Qualität**: wahrgenommenes Maß an Bedürfnisserfüllung. Z.B. No-Name vs. Markenprodukte

- **QS-Norm** ISO 9001: Einhaltung der vom Qualitätsmanagement festgelegten Maßnahmen. 

- **Audit**: Überprüfung, durch die festgestellt werden soll, ob Richtlinien, Anforderungen oder auch Prozesse in einem Unternehmen die geforderten Standards erfüllen

- [QM-Systeme](##5.2 Qualitätsmanagement)



## 5.2 Qualitätsmanagement

- Verbesserung der Prozess-, Arbeits- und Produktqualität
- **Qualitätsplanung**: Ist-Zustand ermitteln, Ziel-Zustand festlegen
- **Qualitätslenkung**: Umsetzung der Planphase
- Softwarequalität

### PDCA-Plan

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/grafik-pdca-zyklus-001-lexoffice-1024x706.webp" align=left alt="PDCA-Zyklus: Plan-Do-Check-Act einfach erklärt!" style="zoom: 67%;" />





---

# 6 IT-Sicherheit

## 6.1 IT-Grundschutz

### Organisatorische Maßnahmen

- IT-**Sicherheitsbeauftragter** im Betrieb
- Erstellen von **Sicherheitsrichtlinien** –> für Passwörter etc.
- **Schulungen** v. Mitarbeitern –> gegen Social-Engineering 
- Normen, [Branchenstandards](### Normen & Standrads) befolgen



### Technische Maßnahmen

- Virenschutzsystem
- Firewall
- Anti-Spam Filter
- Privacy/ Security by Design

#### Arten von Malware

Es empfiehlt sich sehr, die verlinkten Artikel zu den einzelnen Typen zu lesen. Nicht für die ASP aber fü’s eigene Leben, dass am am Satus-Quo ist, was derzeit so passiert… 

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenprüfung/img/Types-of-Malware-DE.pngwidth%3D664%26height%3D474%26name%3DTypes-of-Malware-DE.png" align=left alt="Malware | Definition und Funktionsweise | Avast" />

- **Hacking**: gezieltes Ausnutzung von Sicherheitslücken, Umgehen von Sicherungsmechanismen
- **Malware**: "malicious" (bösartig) & "software, häufig Handlung des Benutzers erforderlich
- **[Ransomware](https://de.wikipedia.org/wiki/Lockbit#:~:text=Lockbit%20ist%20eine%20russischsprachige%20Gruppe,auch%20ein%20Affiliate%2DProgramm%20besteht.)**: Verschlüsselung aller Dateien. Erpressung (meist Bitcoin, Ether) damit die Dateien nicht veröffentlich und entschlüsselt werden
- **[Spyware](https://de.wikipedia.org/wiki/Pegasus_(Spyware))**: unbemerktes Sammeln von Nutzerinfirmationen (Tastatureingaben, Zwischenspeicher, Screen-Capture…)
- **Adware**: Ungewünschte Werbung (Chip-Softwaredownload) meist durch [Black Paterns](https://de.wikipedia.org/wiki/Dark_Pattern) initiiert 
- **[Würmer](https://de.wikipedia.org/wiki/WannaCry)**: verbreitet sich selbst durch’s Netzwerk, USB-Sticks etc. Meist Ausnutzung von ([Zero-Day](https://www.kaspersky.de/resource-center/definitions/zero-day-exploit)) Sicherheitslücken
- **[Trojaner](https://de.wikipedia.org/wiki/Emotet)**: Tarnung als legitime Software, läd andere Schadsoftware nach
- **[Botnets](https://de.wikipedia.org/wiki/Mirai_(Computerwurm))**: Werden durch andere Schadsoftware erstellt. Z.B. ein Wurm breitet sich aus und macht alle “berfallenen” Geräte zum Mitglied eines Botnetzes, dieses wird für DDoS-Attacken genutzt (durch automatische Skripte)
- **[DDos](https://www.zdnet.com/article/aws-said-it-mitigated-a-2-3-tbps-ddos-attack-the-largest-ever/)** (Distributet Denial-of-Service): Oft durch Botnetze durchgefürht, da mehr Netzwerkpower. Durch verschiedene Methoden wird das Ziel in die Knie gezwungen. Z.B. Syn-Flooding etc. 
- **Phishing**: Versuch über gefälschte Websites, E-Mails etc. an vertrauenswürdige Daten zu kommen um noch bessere Phishing Attacken oder weitere Schadsoftware zu implementieren



### Datenschutzgesetze

- DSGVO, BDSG

- Definition personenbezogener Daten:

  > alle Informationen, die sich auf eine identifizierte oder identifizierbare natürliche Person [...] beziehen

- **Datenminimierung**: Personenbezogene Daten müssen dem **Zweck** **angemessen** und auf das dadurch notwendige Maß beschränkt sein

- **Zweckbindung**: nur für festgelegte, eindeutige & legitime Zwecke verwendbar –> z.B. Nutzeradresse nicht für Werbung

- **Verbot mit Erlaubnisvorbehalt**

  - Generell besteht ein Verbot der Nutzung & Verarbeitung von personenbezogenen Daten
  - Daten dürfen nur genutzt &/oder verarbeitet werden, wenn eine Erlaubnis erteilt wurde *(z. B. durch Bestätigung der betroffenen Person oder weil die Verarbeitung zur Vertragserfüllung notwendig ist)*

- **Datenrichtigkeit**: Daten müssen sowohl **sachlich** als auch **inhaltlich** korrekt & aktuell sein

- **Rechtmäßigkeit & Transparenz**: Daten müssen nachvollziehbar rechtmäßig verarbeitet werden

- **Datenintegrität/-vertraulichkeit & -sicherheit (TOM)**: *Siehe unten*

- **Speicherbegrenzung** Speicherung in einer Form, die die Identifizierung der betroffenen Personen nur so lange ermöglicht, wie es für den Verwendungszweck nötig ist



### Normen & Standrads

- [ISO 2700x](https://de.wikipedia.org/wiki/ISO/IEC-27000-Reihe)
- **CIA-Triade**
  - **Confidentiality** (*Vertraulichkeit*): Daten nur von autorisierten Benutzern zugänglich –> Nutzerauthorisierung
  - **Integrity** (*Integrität*): Keine unbemerkte Veränderung –> Prüfsummen wie CRC-64, MD5, SHA
  - **Availablility** (*Verfügbarkeit*): Verhinderung von Systemausfällen –> Redundante Speicherung durch [RAID](### RAID-Systeme), Servercluster, Backups

- Weitere **Schutzziele**:
  - **Authenticity** (*Authentizität*): Echtheit, Vertrauenswürdigkeit von Daten –> digitale signaturen z.B. in PDFs, HTTPS

  - **Accountability vs. Anonymity** (*Zurechenbarkeit vs. Anonymität*): (keine) Rückführung auf einzelne Person mögl. z.B. Usertracking auf Insta vs. anonymes surfen durch [Tor](https://de.wikipedia.org/wiki/Tor_(Netzwerk))

  - **Resilence** (*Resilenz*): Widerstandsfähigkeit ggü. Ausspähungen, irrtümlichen oder mutwilligen Beschädigungen –> Loadbalancer, DDos-Schutz…

- BSI IT-Grundschutz: Katalog mit grundlegenden Sicherheitsanforderungen



## 6.2 Schutzbedarfsanalyse

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Abb_2_09_Varianten.png" align=left alt="BSI - Lerneinheit 2.9: Wahl der Vorgehensweise" />

- Analyse, **welche** **Bereiche** d. Unternehmens **welchen** **Schutz** erfordern. 

- **Anpassung** an **Tätigkeit**/Ausrichtung des Unternehmens (Bäckerei vs. IT-Dienstleister für Bundestag)
- Betrachtung von Netzwerk (Sicherheit), Gebäude (Einbruch, Zugangskontrolle), E-Mail-Client (Viren-/ Phishing-Erkennung) etc., deren Wert und Bedrohungsgrad

**Ablauf** e. Schutzbedarfsanalyse:

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/738x415_f5f5f5.jpg" align=left alt="Der übliche Ablauf einer Schutzbedarfsanalyse." style="zoom: 80%;" />

Gute [Seite](https://www.computerwoche.de/a/it-sicherheit-das-kalkulierte-risiko) dazu.



## 6.3 Sicherheitskonzept entwickeln

- **Bausteine aus Grundschutzkatalog**

  |                                                              |                                                              |                                                              |
  | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Abb_5_02_Schichtenmodell.png" align=left alt="Das Schichtenmodell des IT-Grundschutz-Kompendiums - Einzelheiten werden im Text erläutert." style="zoom: 50%;" /> | ISMS<br />ORP<br />CON<br /><br />OPS<br />DER<br />APP<br />SYS<br />IND<br />NET<br />INF<br /> | Sicheritsmanagement<br />Organisation und Personal<br />Konzeption und Vorgenehsweisen (Kryptokonzept, Datenschutz,<br />Datensicherung, Auswahl von Software, …)<br />Aufteilung d. Betriebs<br />Detektion und Reaktion v. sicherheitsrelevanten Ereignissen, Audits, IT-Forensik<br />Anwendungen (Browser, Webserver, Outlook, etcl.)<br />IT-Systeme (Server, Virtualisierung, Clients, Laptops, Handys)<br />Industrielle IT (Betriebs-/ Steuerungstechnik, Sensoren und Aktoren)<br />Netze und Kommunikation (Netzarchitektur und -design, Netzmanagement)<br />Infrastruktur (Gebäude, Serverräume, Verkabelung, Homeoffice) |

- **Schutzbedarfskategorien**

  - **normal**: Kein Imageverlust beim Kunden, Schaden unter 50.000€
  - **hoch**: Ansehen wird erheblich beeinträchtigt, 50.000€ < Schaden < 500.000€
  - **sehr hoch**: Ansehen wird grundlegend und nachhaltig beschädigt, Schaden > 500.000€



- **IT-Sicherheitsmanagement implementieren**
  - **ISMS-Scoping**: klärt grundlegende Dinge wie Sicherheitsniveau, Aufwand d. Implementierung etc.
  - **Abstimmung/ Planung** von Sicherheitsmaßnamen, Erstellung von benötigten Unterlagen und Sicherheitsregeln
  - **Einführung** der ISMS in der Organisation
  - **Verbesserung** im laufenden Betrieb



## 6.4 Umsetzung d. Sicherheitskonzepts



- **IT-Sicherheitsmanagement** (s.o., Grundlagen zu Passwort-Policy etc. Sensibilisierung zum Thema Phishing, Testweise konzerninterne Alibi Phishingmails versenden und Mitarbeiter die drauf reinfallen gleich ne IT-Security Schulung zuweisen 
- **Technische, Infrastrukturelle Schutzmaßnahmen**: Zugangs- und Zugriffskontrolle (Sowohl Gebäude als auch interne Software-Tools), Netzwerksicherheit, Aufstellen von [Honeypots](https://www.kaspersky.de/resource-center/threats/what-is-a-honeypot), Implementierung von LDAP, VPN-Zugriff, Verschlüsselung d. Daten, regelm. Updates, abgeschottete Serverumgebung (keine direkte Verbindung zw. zentr. Datenspeicher und Internet), …
- **Security by Design/ Default**: z.B. sind per Default alle Ports an einer Firewall blockiert, nur bei bedarf werden die benötigten Ports für genau definierte IPs freigegeben, es wird grundsätzlich verboten sich im Firmennetz am LDAP-Server anzumelden, nur explizit registrierte MAC-Adressen dürfen sich anmelden etc.
- DNS-/IP-Blocking bekannter Server von Schadsoftware bzw. Controlserver von Botnetzen
- Falls es drankommt: **SSH vs. Telnet**. Telnet ist ungefähr so sicher wie Bungeejumping an Gummibärchenschlangen. Also **NEIN**!!!



### VPNs

> [!NOTE]
>
> [Entgegen der medialen Werbung schützt ein VPN nicht vor Hackern, Angriffen oder ähnlichem.](https://www.youtube.com/watch?v=vq6j47k1whw) Es ist lediglich dafür nutzbar, Traffic von einem Ort zu einem anderen zu routen, ohne dass die Zwischenstationen etwas mitkriegen. 
>
> Es ist richtig, dass VPNs den Traffic verschlüsseln. Das tut aber SSL (also HTTP**S**) ohnehin schon. Heißt, man würde nur eh schon verschlüsselten Traffic nochmal verschlüsseln. Das macht die ganze Geschichte langsam. Es würde also nur was bringen, wenn man auf HTTP-Seiten surft.
> Und ja, es ist zwar nur die Kommunikation mit den Websites, nicht aber die DNS-Anfrage verschlüsselt (Zumindest zu 88%). Ein VPN bringt dann aber nur, dass zwar nicht der Anbieter des WLANs (z.B. Cafee) sondern eben der VPN-Provider deine DNS-Anfragen mitließt. Irgendwer muss ja die Seiten auflösen. 
>
> Einen Sicherheitsvorteil bietet ein VPN also nur in zwei Fällen
>
> - du nutzt unverschlüsstelten Verkehr (Websites, Netzwerklaufwerke)
> - Du hast den VPN-Server, zu dem die Verbindung aufgebaut wird, selbst gehostet und dieser löst DNS-Anfragen selbst auf oder leitet die via DoT oder DoH weiter.
>
> Ein riesiger Vorteil besteht natürlich darin, dass man mit einem VPN in z.B. das Firmen-/ Heimnetz kommt und auf Services zugreifen kann, die nicht im Internet sondern im lokalen Netz verfügbar sind. (Dann muss man z.B. das NAS daheim nicht fü’s Internet freigeben und ist so sicherer gegen Angriffe)
> Außerdem kann man natürlich mit VPNs Geoblocking umgehen. 
>
> Wenn man wirklich anonym surfen will, sollte man [Tor](http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/index.html) verwenden. Und nein, das hat an sich nix mit dem Darknet *(uhh gruselig ( ⚆ _ ⚆ ) )* zu tun…

Aaaalso. Genug gemotzt, wie funktioniert ein VPN?

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenprüfung/img/vpn.jpg" align=left alt="vpn" style="zoom: 40%;" />

Möchte man z.B. Remote-Arbeiter und weitere Geschäftsstellen an das Firmennetz anbinden, baut man ein (am besten redundantes) [VPN Netz](https://www.mpcservice.com/mpls/mpls-vpn-oder-ipsec-vpn/) auf. Hier wird entweder direkt am Client oder am VPN-Server/ Router der Traffic verschlüsselt und gezielt zum Ziel (Anderer Router, in anderer Geschäftsstelle) geroutet. 





### Datensicherung, Backup-Verfahren

> [!IMPORTANT]
>
> Es sollte IMMER die [3-2-1 Regel](https://it-service.network/blog/2021/09/13/3-2-1-regel/) für Backups befolgt werden.



|                                  | Voll           | Differential                    | Inkrementiell                         |
| -------------------------------- | -------------- | ------------------------------- | ------------------------------------- |
| **Speicherplatz**                | Viel           | mittel bis viel                 | wenig                                 |
| **Backup Geschwindigkeit**       | langsam        | schnell                         | am schnellsten                        |
| **Wiederherstellung**            | am schnellsten | schnell                         | am langsamsten                        |
| **Benötigte Versionen**          | nur das Neuste | das letzte Voll- und Teilbackup | das letzte Voll- und alle Teilbackups |
| **Doppelt gespeicherte Dateien** | sehr viele     | einige                          | keine                                 |

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/types-of-backup-full-differential-incremental.png" align=left  alt="A basic graphic displaying the difference between full backup, differential backup, and incremental backup." style="zoom: 80%;" />





### RAID-Systeme

> [!WARNING]
>
> RAID ist KEIN Backup!!!

#### RAID 0

Zwei **Festplatten** (eigentlich [Partitionen](### Formatierung/ Partitionierung
)) werden zu einer logischen Platte (Partition) **zusammengefügt**. Beide **Partitionen** müssen **gleich** **groß** sein.

|                                                              | Vorteil                                                      | Nachteil                                                     | Berechnung d. Speicherplatzes |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------- |
| <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/1280px-RAID_0.svg-1707843979228-10.png" alt="undefined" style="zoom: 25%;" /> | **hohe Lesegeschwindigkeit**<br />–> es kann von beiden Platten gleichzeitig gelesen werden<br /><br />**höhere Schreibgeschwindigkeit**<br />–> es muss nur 1/2 der Daten auf jede Platte geschrieben werden | Der Ausfall einer Platte führt zu einem **Totalausfall**<br /><br />Die Partitionsgröße orientiert sich an der kleineren Festplatte -> `3TB + 2TB = 4TB` nutzbarer Speicher | $$TB_{Platte} \times 2$$      |



#### RAID 1

Zwei **Festplatten** werden 1:1 **gespiegelt**. Beide Partitionen müssen gleich groß sein. 

|                                                              | Vorteil                                                      | Nachteil                                                     | Berechnung d. Speicherplatzes |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------- |
| <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/1280px-RAID_1.svg.png" alt="undefined" style="zoom: 25%;" /> | **hohe Lesegeschwindigkeit**<br />–> es kann von beiden Platten gleichzeitig gelesen werden<br /><br />**Sehr hohe Redundanz**<br />–> Eine Platte darf ausfallen<br /><br />wenig Zeit zur Wiederherstellung benötigt | Es kann nur die Hälfte des verfügbaren Speicherplatzes genutzt werden<br /><br />Die Partitionsgröße orientiert sich an der kleineren Festplatte -> `3TB + 2TB = 2TB` nutzbarer Speicher | $$TB_{Platte} : 2$$           |



#### RAID 5

Die Datei wird in mehrere Teile (Hier 3) aufgeteilt und verteilt gespeichert. Zusätzlich wird die Paritätsinformation berechnet (XOR) und alternierend auf den Platten verteilt (keine extra Paritäts-Platte). Alle Partitionen müssen gleich groß sein.

|                                                              | Vorteil                                                      | Nachteil                                                     | Berechnung d. Speicherplatzes                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------- |
| <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/2560px-RAID_5.svg.png" alt="undefined" style="zoom:50%;" /> | **hohe Lesegeschwindigkeit**<br />–> es kann von mehreren Platten gleichzeitig gelesen werden<br /><br />**Sehr hohe Redundanz**<br />–> gleiche Redundanz wie Raid 1 bei geringeren Kosten/Redundanz<br /><br />**Mehr Speicherplatz** bei gleicher Redundanz im Vergleich zu RAID 1 | Es wird bei der Wiederherstellung **Rechenzeit** benötigt<br /><br />Alle Partitionen müssen gleich groß sein | $$(\#_{Festplatten} - 1) \times TB_{Platte}$$ |



#### JBOD

Streng genommen kein RAID. Alle Festplatten (unbegrenzt) werden in ihrer vollen Kapazität genutzt.
*Im Bild wird irrtümlich eine augenscheinliche Zerteilung einer Datei (in 95 Teile) dargestellt. Es sind in diesem Fall aber 95 verschiedene Dateien.*

|                                                              | Vorteil                                                      | Nachteil                                                     | Berechnung d. Speicherplatzes                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------- |
| <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/1920px-JBOD.svg.png" alt="undefined" style="zoom: 25%;" /> | Nutzung aller verfügbaren Festplatten in ihrer vollen Größe<br /><br />kein Stripping (Zerteilung der Dateien) wie bei RAID 0 | Keine Redundanz<br /><br />Bei einem Plattenausfall gehen alle Daten der betroffenen Platte verloren | $$TB_{Platte_1} + TB_{Platte_2} + TB_{Platte_n}$$ |



#### Vermischte Typen

Es ist auch möglich mehrere RAID-Typen zu mischen. So kann aus zwei RAID 0 Verbünden ein RAID 1 Verbund erstellt werden.
Auch ein RAID 15 etc. ist somit möglich *(wird teilw. auch genutzt)*. Für mehr Infos ist dieser [Wikipedia-Artikel](https://de.wikipedia.org/wiki/RAID) sehr interessant.

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/1920px-RAID_10.svg.png" alt="undefined" style="zoom:13%;" /><img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/RAID_51.png" alt="undefined" style="zoom:40%;" />        





### USV

**[Typen](https://fachinformatikerpruefungsvorbereitung.de/abschlusspr%C3%BCfungteil1/systemintegration/usv/) von unterbrechungsfreien Stromversorgungseinheiten:**

| Name                    | Schutz bei                                                   | Umschaltzeit | Funktionsweise                                               |                                                              |
| ----------------------- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Offline USV**         | Netzausfall<br />große Über-/ Unterspannung                  | 3-10ms       | Weiterleitung der Netzspannung. Bei Netzausfall wird auf Batteriebetrieb umgeschalten. <br />Gibt die Netzspannung ungefiltert durch. evtl. schädlich für empfindliche Geräte | <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Akkurat-Offline-USV%40741x-8-600x283.png" alt="img" style="zoom: 200%;" />                                                                                                                              .                                                                                                                                                                                                                                                                                                                                                                         .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              . |
| **Netzinteraktive USV** | Netzausfall<br />Über-/ Unterspannung<br />Schwankungen der Netzspannung | < 4ms        | Weiterleitung und “Glättung” der Netzspannung. Zusätzlich werden Schwankungen ausgeglichen. | ![img](https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Akkurat-Line-Interactive-USV-600x304.png) |
| **Online USV**          | Netzausfall<br />Über-/ Unterspannung<br />Schwankungen der Netzspannung und Netzfrequenz | keine        | Die eingehende Netzspannung wird konstant gefiltert und geglättet. Spannungsspitzen und -täler werden durch die Batterie ausgeglichen. Auch Frequenzsschwankungen werden ausgeglichen. | <img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenpr%C3%BCfung/img/Akkurat-Online-USV-600x334.png" alt="img"  /> |

Online USVen sind logischerweise wesentlich teurer und rentieren sich nur bei empfindlicher oder hochverfügbarer IT-Hardware. Eine Netzinteraktive USV ist meist der Kompromiss zwischen den anderen beiden Varianten. 

Man bemerke, dass die meisten Server-/ Computernetzteile von sich aus Spannungslücken von >= 16ms (ATX-Standard) kompensieren können. Daher sollte auch die Umschaltung einer Offline-USV i.d.R. keine/kaum Beeinträchtigungen darstelt.



**Berechnung der benötigten USV:**

- **Wirkleistung**: realer Stromverbrauch der angeschlossenen Geräte, Einheit Watt $$W$$ 
- **Blindleistung**: wird zwischen Erzeuger und Verbraucher übertragen.
- **Scheinleistung**:  $$Wirkleistung + Blindleistung$$ , Einheit Voltampere $$VA$$ 
- **Autonomiezeit**: Überbrückungsdauer bei Netzausfall

Ein Unternehmen betreibt ein Rechenzentrum, das aus vier Racks besteht. Jedes Rack benötigt eine Leistung von 2,75 kW. Das Rechenzentrum ist mit einer USV-Anlage mit einer Nennleistung von 15 kVA abgesichert. Die USV-Anlage wird mit einer Blei-Säure-Batterie betrieben, die eine Kapazität von 6 kWh hat.

**Berechnung der Autonomiezeit**: 

> $$\dfrac{Batteriekapazität}{Leistung}$$ –> $$\dfrac{6kWh}{2,75kW \times 4} = 0,54h$$	// Berechnung in Stunden
>
> $$60h \times 0,54 = 32min$$	// Umrechnung in Minuten



**Berechnung der USV-Größe:**

Zur Berechnung sollte immer die $$VA$$-Angabe d. Netzteiler *(oder entsprechende Messergebnisse)* genutzt werden. Diese können einfach addiert werden. 
Ist keine Angabe in $$VA$$ verfügbar *(wie in diesem Beispiel)*, gilt wie folgt vorzugehen:

> $$2,75kW \times 4 = 11kW$$
>
> $$11kW \times 1,6 = 17,6kVA$$	// 1,6 als ungefähren Faktor für die Umrechnung
>
> $$17,6kVA \times 1,3 = 22,88kVA$$	// +30% Puffer

Ich glaube aber nicht, dass die zweite Aufgabe gefragt wird, da das im Endeffekt ne Milchmädchenrechnung ist, weil die 1,6 nur eine Annäherung an den cosPhi sind…





---



# 7 Leistungserbringung

## 7.1 Vertragsarten

Siehe [Vertragsgestaltung](### Vertragsgestaltung)



## 7.2 Unternehmensleitbild

**Bestandteile:**

- **Slogan**: beschreibt kurz und Prägnant das Selbstverständnis d. Unternehmens
- **Vision**: beschreibt Ziele die das Unternehmen erreichen will. Sollten nicht unbedingt realistisch sein
- **Mission**: Zweck, den das Unternehmen verfolgt
- **Unternehmenskultur/ -philosophie**: Umgang miteinadner (innerhalb und außerhalb d. Unternehmens)

–> soll für positives Image in der Öffentlichkeit sorgen



## 7.3 Leistungsdokumentation

- Kontinuierliche Prüfung d. vertraglich vereinbarten Vorgaben
- Stillegung von Altsystemen, Inbetriebname von Neuen
- Archivierung von Daten
- Vollständige Doku erbrachter Leistungen siehe [Arten der Dokumentation](### Arten der Dokumentation)



## 7.4 Umsetzung der Leistungserbringung

- **Leistungserbringung** vor Ort vs. Remote
  - **Vor Ort**: einfacher Einstieg da Teamkontakt, gute Kommunikation, fördert Kreativität  –> gut bei Projektanfang, schweren Phasen
  - **Remote**: geringere Kosten, weniger Stress, bessere Auswahl an Mitarbeitern, flexibleres arbeiten –> Während einem längeren Projekt

- **Kundenvorgaben** bei Leistungserbringung: Termin, Erfüllungsort, Spezifikationen
- techn. **Voraussetzungen** klären
- **Rolloutprozesse**: Vorbereitung (Onboarding d. Kunden, Scope definieren, Schulung auf z.B. neue Software) Formailitäten

- **Ertragsziele:** alles was mit den begriffen Umsatz, Gewinn & Kapital zusammenhängt
- **Marktziele:** vom Unternehmen selbst festgelegt, was es erreichen möchte
- **Leistungsziel:** gewisse Qualitätsstandards, Sicherstellung der Arbeitsplätze



## 7.5 Leistungserbringung gem. Aufbauorganisation

Siehe [Organisationsformen](### Organisationsformen)

- **Anpassung an** jew. **Organisationsform** (Wer entscheidet welchen Schritt, wirkt an welchem Teilprojekt mit, etc.)



## 7.6 Veränderungsprozesse

Wie kann Veränderung richtig kommuniziert und begleitet werden?

- **Motivierte** Herangehensweise, **betonung** v. **Chancen**
- Identifizierung, Darstellung v. **Veränderungsschritten**
- **Einbeziehung** d. Mitarbeiter in Veränderungsprozess 
  - Mitarbeiter(neu)qualifizierung
  - Erkennen von Bremsern/ Skeptikern und Förderern

- **Ursachen** **von** **Widerständen** gg. Veränderung: Angst vor Kompetenzverlust, Wissenslücken, pers. Historie



## 7.7 Einweisung

### Inhalt d. Abnahmeprotokolls

- Gegenstand der Abnahme

- beteiligte Personen (mit ihrer Funktion)

- Ort, Datum und Uhrzeit

- Art und Ergebnis der Prüfungen

- Vereinbarte Maßnahmen zur Nacherfüllung

- Nicht geprüfte Kriterien

  

### Arten der Dokumentation

- Nutzerhandbuch
- Schnittstellendokumentation
- Netzwerkdokumentation
- Testprotokolle
- Programmdokumentation (z.B. im Code)



### Mängel, -arten

- Schlechtleistung –> fehlende Funktionalität
- Falschlieferung –> Software erfüllt nicht den geforderten Zweck
- Minderlieferung –> Software erfüllt nicht alle beschriebenen Anforderungen



## 7.8 Leistungserbringung bewerten

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenprüfung/img/grafik-soll-ist-vergleich-ablauf-002-1024x706.webp" align=left alt="Ablauf eines Soll-Ist-Vergleichs" style="zoom: 67%;" />

**Soll-Ist Vergleich**

<img src="https://raw.githubusercontent.com/JJandke/Berufsschule/master/Zwischenprüfung/img/herobild_510x340_76.jpg" align=left alt="Plan-Ist-Vergleich" style="zoom: 50%;" />     1 und 2 werden einmalig durchgeführt

​     3, 4 und 5 wer während dem Projekt mehrmals wiederholt





1. Ziele Setzen und planen –> Was soll erreicht werden
2. Werter erfassen –> wann ist das Projekt erfolgreich
3. Soll-Ist-Vergleich erstellen –> Werte aus 1 und 2 werden den aktuellen Werten gegenüber gestellt 
4. Abweichungen analysieren –> Ursache muss ausfindig gemacht werden
5. Maßnahmen etablieren –> 
6. Erfolge messen



**Bestätigung erbr. Leistungen**

- Anhand von konkreten Zielen: SMART



**Abweichungsanalyse**

während Punkt 4, Unterscheidung in mehrere Gruppen z.B.:

- **Kostenstelle**nabweichungen
- Abweichungen in der **Erlösrechnung** 
- Abweichungen der **Beschaffungsseite**































ifcon
