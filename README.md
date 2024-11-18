<h1>Kniffel-Regeln</h1>

Die Kniffel Spielregeln entnehmen Sie bitte diesem Video: https://www.youtube.com/watch?v=J0mRzX5cMF8

Die einzige Regel, welche in unserer Version von Kniffel nicht gilt:
Es gibt keine Bonuspunkte für erneute Kniffel-Würfe.
Dies soll einen erhöhten Fokus auf mehrfahre Kniffel-Würfe verhindern und den Fokus mehr auf Variität in den Strategien legen.

<h1>Die Spiel-Files</h1>

<h2>Kniffel_Game.py</h2>
Hier befinden sich alle Funktionen, welche zur Simulation des Kniffel-Spiels verwendet werden.
Diese Klasse wird am Tag der Präsentation und von uns zum Testen der Bots (KIs) verwendet.
Daher sollten die Methoden der Klasse nicht verändert werden.
Falls Ihnen während der Bearbeitung Bugs oder Exploits auffallen, bitte ich Sie, diese zu melden.

<h2>Kniffel_Player.py</h2>
Diese File dürfen uns sollten Sie Abändern.
Die Kniffel_Player Klasse ist eine Klasse, welche MINDESTENS die zwei vorhandenen Methoden haben muss. <b>Sie dürfen nach belieben weitere Methoden und Attribute der Klasse hinzufügen.</b>
In der ersten Methode wählen sie die Würfel, welche Sie zurücklegen möchten (siehe Regelwerk) und in der zweiten Methode wählen Sie welches Feld sie beschreiben möchten. 
Die Details zu den Methoden und Datentypen sind in den jeweiligen Methodenbeschreibungen hinterlegt.
Das Kniffel_Player Objekt bleibt über mehrere Spiele bestehen, was es ermöglicht, Attribute über mehrere Spiele zu speichern.
Bei der Endpräsentation wird es ein (für die Noten nicht direkt relevantes) Turnier aller Bots geben. Das Gewinnerteam erhält eine kleine Überraschung.

<h1>Zielsetzung</h1>
<h2>Mindestanforderung</h2>
<ul>
  <li>Sie erstellen zwei Bots für das Kniffel Spiel, und lassen diese in einer Simulationsstudie gegeneinander antreten. Die Bots dürfen aufeinander aufbauen.</li>
  <li>Sie erstellen eine Präsentation (ca. 20 Minuten) über die Erstellung und Vorgehensweise der Bots. Dabei kann sowohl der Werdegang erläutert werden, als auch auf Gründe für bestimmte Strategien eingegangen werden. Zusätzlich sollte in der Präsentation auf die Simulationsstudie eingegangen werden. Hierbei ist empfohlen, Matplotlib für die Visualisierung der Ergebnisse zu verwenden.</li>
</ul>

<h2>Möglichkeiten zur Erweiterung</h2>
<ul>
<li>Sie erstellen ein Interface, welches es einem beliebigen Spieler Erlaubt, selber gegen den Bot Kniffel zu spielen. (Jupyer Notebooks, oder TKinter etc. sind erlaubt) Hierbei sollten Sie als Basis die Kniffe_Game file verwenden.</li>
<li>Umfangreiche Verfahren in der Bot-Strategie. (Insbesondere Methoden des Machine Learnings sind für die Erstellung einer künstlichen Intelligenz gut nutzbar.)</li>
<li>Ausführliche Rechenstudie.</li>
</ul>
