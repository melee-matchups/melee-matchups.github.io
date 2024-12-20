import json

template = """
<html>
	<head>
		<title>Smash - Melee - Marth VS {name}</title>
		<link rel="stylesheet" href="./../css/dark-mode.css">
		<link rel="stylesheet" href="./../css/main.css">
	</head>
	<body class="fd_bg">
		<div id="bar">
			<center style="width: 100%;">
				<a class="bar-a" href="./../index.html" style="float: left;">
					<svg id="marth_sword_img" height="125" width="125" viewBox="0 0 256 256">
						<path id="marth_sword_img_path" style="fill:#FFFFFF; stroke:#FFFFFF" d="m 210.35584,45.644161 c -5.02604,-5e-6 -11.99452,-1.263729 -17.63347,4.375223 -5.63895,5.638953 -5.19282,12.308078 -5.19282,12.308078 l -9.8111,9.811106 c -3.37848,-1.295991 -7.59342,-1.105514 -11.86614,0.419845 l -11.07064,-16.99266 -22.56113,-0.817592 -10.98225,15.62264 5.01604,21.854019 9.34707,-18.009126 6.65122,0.375651 6.38606,12.484854 -4.44152,12.750019 -82.996654,68.633552 -15.556349,41.89607 41.896077,-15.55635 68.633556,-82.99665 12.75001,-4.44152 12.48486,6.38606 0.37565,6.65122 -18.00913,9.34707 21.85402,5.01604 15.62264,-10.98225 -0.81759,-22.56113 -16.99266,-11.070636 c 1.52536,-4.272724 1.71584,-8.487656 0.41985,-11.866136 l 9.8111,-9.811106 c 0,0 6.66913,0.446137 12.30808,-5.192816 5.63895,-5.638952 4.37522,-12.607443 4.37522,-17.633475 z M 172.7908,83.209209 c 2.30924,2.309248 0.90763,7.445063 -3.11569,11.468388 -4.02333,4.023325 -9.15914,5.424933 -11.46839,3.115689 -2.30925,-2.309248 -0.90764,-7.445063 3.11569,-11.468388 4.02332,-4.023324 9.15914,-5.424937 11.46839,-3.115689 z"></path>
					</svg>
				</a>
				<img width=48 height=48 src="./../img/stocks/{name_lower}.png">
				<h1 style="display: inline; font-size: 40px;">{name}</h1>
				<a class="bar-a" href="./../guides.html"><button class="bar-button">Guides & Tech</button></a>
                <a class="bar-a" href="./../tech.html"><button class="bar-button">Tech Table</button></a>
				<a class="bar-a" href="./../framedata.html"><button class="bar-button">Framedata</button></a>
				<a class="bar-a" href="./../matchups.html"><button class="bar-button">MatchUps</button></a>
				<a class="bar-a" href="./../stages.html"><button class="bar-button">Stages</button></a>
				<a class="bar-a" href="./../options.html"><button class="bar-button">options</button></a>
			</center>
		</div>
		<br>
		<div id="main-content">
			<div style="width: 100%;">
				<button onclick='document.querySelectorAll("details").forEach((detail) => {{detail.open = false;}})' style="font-size: 20px;">-</button>
				<button onclick='document.querySelectorAll("details").forEach((detail) => {{detail.open = true;}})' style="font-size: 20px;">+</button>
				<a target="_blank" href="https://meleeframedata.com/{framedata}"><button style="font-size: 20px;">{name}'s Frame Data</button></a>
			</div>
			<details open>
				<summary style="display: inline;"><h1>Neutral</h1></summary>
				<div class="indent-tab">
					<details open>
						<summary style="display: inline;"><h2>Goals / Advantageous Positioning / Movement</h2></summary>
						<div class="indent-tab">
							{movement}

                            <details open>
                                <summary style="display: inline;"><h2>Advantageous Positions<h2></summary>
                                <div class="indent-tab">
                                    {pos}
                                </div>
                            </details>
						</div>
					</details>
					<details open>
						<summary style="display: inline;"><h2>General Game plan</h2></summary>
						<div class="indent-tab">
							{gameplan}
						</div>
					</details>
					<details open>
						<summary style="display: inline;"><h2>Options to respect</h2></summary>
						<div class="indent-tab">
							{respect}
						</div>
					</details>
	
					<details open>
						<summary style="display: inline;"><h2>Options to not respect / Can be punished</h2></summary>
						<div class="indent-tab">
							{not_respect}
						</div>
					</details>
				</div>
			</details>

			<details open>
				<summary style="display: inline;"><h1>Punish Game</h1></summary>
				<div class="indent-tab">
					<details open>
						<summary style="display: inline;"><h2>Punish routes</h2></summary>
						<div class="indent-tab">
							{punish}
						</div>
					</details>
					<details open>
						<summary style="display: inline;"><h2>Key Combos</h2></summary>
						<div class="indent-tab">
							{combos}
						</div>
					</details>

					<details open>
						<summary style="display: inline;"><h2>Edge Guarding</h2></summary>
						<div class="indent-tab">
							{edge_guarding}
						</div>
					</details>

					<details open>
						<summary style="display: inline;"><h2>Throw follow ups<h2></summary>
						<div class="indent-tab">
							{throws}
						</div>
					</details>
				</div>
			</details>

			<details open>
				<summary style="display: inline;"><h1>Defence</h1></summary>
				<div class="indent-tab">
					{defence}
                    
					<details open>
						<summary style="display: inline;"><h2>Recovery</h2></summary>
						<div class="indent-tab">
							{recovery}
						</div>
					</details>
				</div>

			</details>

			<details open>
				<summary style="display: inline;"><h1>Stages (ordered)</h1></summary>
				<div class="indent-tab">
					{stages}
				</div>
			</details>

			<details open>
				<summary style="display: inline;"><h1>Resources</h1></summary>
				<div class="indent-tab">
					{resources}
				</div>
			</details>
		</div>
	</body>
</html>
"""

stage_names = {
    "fd": "Final Destination",
    "ys": "Yoshi's Story",
    "ps1": "Pokemon Stadium",
    "fod": "Fountin Of Dreams",
    "dl": "Dream Land",
    "bf": "Battle Feild",
}

json_data = json.load(open("data.json", encoding="utf-8"))

for name in json_data:
    format_dict = {
        **{tag: "<div>" + ("<br>".join(json_data[name][tag].split("\n"))) + "</div>" for tag in json_data[name] if type(json_data[name][tag]) == str},
        
        "name": name.title(),
        "name_lower": name.lower(),
        "resources": "<br>".join([f'<a target="_blank" href="{json_data[name]["resources"][n]}">{n}</a>' for n in json_data[name]["resources"]]),
        "framedata": json_data[name]["framedata"],
        "stages": "<h2>Good</h2>" + (
            "".join(
                [
                    f'<span class="stage"><img width=250 src="./../img/stages/{stage}.png"><center>{stage_names[stage]}</center></span>'
                    for stage in list(filter(None, json_data[name]["stages"]["good"].split(",")))
                ]
            )
        ) + "<br><h2>Bad</h2>" + (
            "".join(
                [
                    f'<span class="stage"><img width=250 src="./../img/stages/{stage}.png"><center>{stage_names[stage]}</center></span>'
                    for stage in list(filter(None, json_data[name]["stages"]["bad"].split(",")))
                ]
            )
        ),
        "pos": "<br>".join([f"<h4>{state}</h4>" + ("".join([f'<li>{pos}</li>' for pos in json_data[name]["pos"][state]])) for state in json_data[name]["pos"]]),
    }

    with open("./../matchups/" + name + ".html", "w", encoding="utf-8") as fp:
        fp.write(template.format(**format_dict))



#
