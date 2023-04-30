import os, sys, requests, json
from bs4 import BeautifulSoup
from rich import print
from rich.table import Table
from rich.console import Console
from webbrowser import open

cmd = 'mode 120,50'
os.system(cmd)

def GetListTop(page=1):
    global currentList
    currentList = "Top Agents"
    url = f"https://api.intruderfps.com/agents?orderBy=stats.level:desc&page={page}&perPage=25"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    data = json.loads(soup.text)
    return data

def GetListSearch(search, page=1):
    global currentList
    currentList = f"Search: {str(search)}"
    url = f"https://api.intruderfps.com/agents/?page={page}&q={search}"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    data = json.loads(soup.text)
    return data

def GetListAdvanced(search, page=1):
    url = f"https://api.intruderfps.com/agents/{search}&page={page}"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    data = json.loads(soup.text)
    return data

def GetStats(steamid):
    url = f"https://api.intruderfps.com/agents/{steamid}/"
    urlStats = f"https://api.intruderfps.com/agents/{steamid}/stats"
    urlVotes = f"https://api.intruderfps.com/agents/{steamid}/votes"
    result = requests.get(url)
    resultStats = requests.get(urlStats)
    resultVotes = requests.get(urlVotes)
    soup = BeautifulSoup(result.content, 'html.parser')
    soupStats = BeautifulSoup(resultStats.content, 'html.parser')
    soupVotes = BeautifulSoup(resultVotes.content, 'html.parser')
    data = json.loads(soup.text)
    dataStats = json.loads(soupStats.text)
    dataVotes = json.loads(soupVotes.text)
    return data, dataStats, dataVotes

def CompareStats(stats1, stats2):
    while True:
        table = Table(title=f"[cyan]{stats1[0]['name']}[/cyan] vs [orange3]{stats2[0]['name']}[/orange3]")

        table.add_column("Name", justify="right")
        table.add_column(stats1[0]['name'], justify="right", style="cyan")
        table.add_column(stats2[0]['name'], justify="left", style="orange3")

        level_1, level_2 = str(stats1[1]['level']), str(stats2[1]['level'])
        pickups_1, pickups_2 = str(stats1[1]['pickups']), str(stats2[1]['pickups'])
        captures_1, captures_2 = str(stats1[1]['captures']), str(stats2[1]['captures'])
        networkHacks_1, networkHacks_2 = str(stats1[1]['networkHacks']), str(stats2[1]['networkHacks'])
        kills_1, kills_2 = str(stats1[1]['kills']), str(stats2[1]['kills'])
        deaths_1, deaths_2 = str(stats1[1]['deaths']), str(stats2[1]['deaths'])
        arrests_1, arrests_2 = str(stats1[1]['arrests']), str(stats2[1]['arrests'])
        gotArrested_1, gotArrested_2 = str(stats1[1]['gotArrested']), str(stats2[1]['gotArrested'])
        knockdowns_1, knockdowns_2 = str(stats1[1]['knockdowns']), str(stats2[1]['knockdowns'])
        gotKnockedDown_1, gotKnockedDown_2 = str(stats1[1]['gotKnockedDown']), str(stats2[1]['gotKnockedDown'])
        survivals_1, survivals_2 = str(stats1[1]['survivals']), str(stats2[1]['survivals'])
        suicides_1, suicides_2 = str(stats1[1]['suicides']), str(stats2[1]['suicides'])
        teamDamage_1, teamDamage_2 = str(stats1[1]['teamDamage']), str(stats2[1]['teamDamage'])
        teamKills_1, teamKills_2 = str(stats1[1]['teamKills']), str(stats2[1]['teamKills'])
        teamKnockdowns_1, teamKnockdowns_2 = str(stats1[1]['teamKnockdowns']), str(stats2[1]['teamKnockdowns'])
        matchesWon_1, matchesWon_2 = str(stats1[1]['matchesWon']), str(stats2[1]['matchesWon'])
        matchesLost_1, matchesLost_2 = str(stats1[1]['matchesLost']), str(stats2[1]['matchesLost'])
        matches_1, matches_2 = stats1[1]['matchesWon'] + stats1[1]['matchesLost'], stats2[1]['matchesWon'] + stats2[1]['matchesLost']
        matchesWon_1_int, matchesWon_2_int = int(matchesWon_1), int(matchesWon_2)
        try:
            matchesWonPercent_1 = matchesWon_1_int / matches_1 * 100
            matchesWonPercent_1 = round(matchesWonPercent_1, 1)
            matchesWonPercent_1 = str(matchesWonPercent_1)
        except:
            matchesWonPercent_1 = "0"
        try:
            matchesWonPercent_2 = matchesWon_2_int / matches_2 * 100
            matchesWonPercent_2 = round(matchesWonPercent_2, 1)
            matchesWonPercent_2 = str(matchesWonPercent_2)
        except:
            matchesWonPercent_2 = "0"
        roundsLost_1, roundsLost_2 = str(stats1[1]['roundsLost']), str(stats2[1]['roundsLost'])
        roundsTied_1, roundsTied_2 = str(stats1[1]['roundsTied']), str(stats2[1]['roundsTied'])
        roundsWonElimination_1, roundsWonElimination_2 = str(stats1[1]['roundsWonElimination']), str(stats2[1]['roundsWonElimination'])
        roundsWonCapture_1, roundsWonCapture_2 = str(stats1[1]['roundsWonCapture']), str(stats2[1]['roundsWonCapture'])
        roundsWonHack_1, roundsWonHack_2 = str(stats1[1]['roundsWonHack']), str(stats2[1]['roundsWonHack'])
        roundsWonCustom_1, roundsWonCustom_2 = str(stats1[1]['roundsWonCustom']), str(stats2[1]['roundsWonCustom'])
        roundsWon_1 = int(roundsWonCapture_1) + int(roundsWonCustom_1) + int(roundsWonElimination_1) + int(roundsWonHack_1)
        roundsWon_2 = int(roundsWonCapture_2) + int(roundsWonCustom_2) + int(roundsWonElimination_2) + int(roundsWonHack_2)
        roundsWon_1, roundsWon_2 = str(roundsWon_1), str(roundsWon_2)
        rounds_1, rounds_2 = int(roundsWon_1) + int(roundsLost_1), int(roundsWon_2) + int(roundsLost_2)
        try:
            roundsWonPercent_1 = int(roundsWon_1) / rounds_1 * 100
            roundsWonPercent_1 = round(roundsWonPercent_1, 1)
            roundsWonPercent_1 = str(roundsWonPercent_1)
        except:
            roundsWonPercent_1 = "0"
        try:
            roundsWonPercent_2 = int(roundsWon_2) / rounds_2 * 100
            roundsWonPercent_2 = round(roundsWonPercent_2, 1)
            roundsWonPercent_2 = str(roundsWonPercent_2)
        except:
            roundsWonPercent_2 = "0"
        votes_1, votes_2 = str(stats1[2][0]['positive'] - stats1[2][0]['negative']), str(stats2[2][0]['positive'] - stats2[2][0]['negative'])
        timePlayed_1, timePlayed_2 = stats1[1]['timePlayed'] / 60 / 60 , stats2[1]['timePlayed'] / 60 / 60
        timePlayed_1, timePlayed_2 = round(timePlayed_1, 1), round(timePlayed_2, 1)
        timePlayed_1, timePlayed_2 = str(timePlayed_1), str(timePlayed_2)
        timePlayedDemoted_1, timePlayedDemoted_2 = stats1[1]['timePlayedDemoted'] / 60 / 60 , stats2[1]['timePlayedDemoted'] / 60 / 60
        timePlayedDemoted_1, timePlayedDemoted_2 = round(timePlayedDemoted_1, 1), round(timePlayedDemoted_2, 1)
        timePlayedDemoted_1, timePlayedDemoted_2 = str(timePlayedDemoted_1), str(timePlayedDemoted_2)
        heals_1, heals_2 = str(stats1[1]['heals']), str(stats2[1]['heals'])
        gotHealed_1, gotHealed_2 = str(stats1[1]['gotHealed']), str(stats2[1]['gotHealed'])
        role_1, role_2 = stats1[0]["role"], stats2[0]["role"]

        table.add_row("Level", level_1, level_2)
        table.add_section()
        table.add_row("Pickups", pickups_1, pickups_2)
        table.add_row("Captures", captures_1, captures_2)
        table.add_row("Hacks", networkHacks_1, networkHacks_2)
        table.add_section()
        table.add_row("Kills", kills_1, kills_2)
        table.add_row("Deaths", deaths_1, deaths_2)
        table.add_row("Survivals", survivals_1, survivals_2)
        table.add_row("Arrests", arrests_1, arrests_2)
        table.add_row("Got Arrested", gotArrested_1, gotArrested_2)
        table.add_row("Knockdowns", knockdowns_1, knockdowns_2)
        table.add_row("Got Knocked Down ", gotKnockedDown_1, gotKnockedDown_2)
        table.add_row("Suicides", suicides_1, suicides_2)
        table.add_section()
        table.add_row("Team Damage", teamDamage_1, teamDamage_2)
        table.add_row("Team Kills", teamKills_1, teamKills_2)
        table.add_row("Team Knockdowns", teamKnockdowns_1, teamKnockdowns_2)
        table.add_section()
        table.add_row("Matches Won", matchesWon_1, matchesWon_2)
        table.add_row("Matches Lost", matchesLost_1, matchesLost_2)
        table.add_row("Matches W/L", matchesWonPercent_1 + "%", matchesWonPercent_2 + "%")
        table.add_section()
        table.add_row("Rounds Won", roundsWon_1, roundsWon_2)
        table.add_row("Rounds Lost", roundsLost_1, roundsLost_2)
        table.add_row("Rounds W/L", roundsWonPercent_1 + "%", roundsWonPercent_2 + "%")
        table.add_row("Rounds Tied", roundsTied_1, roundsTied_2)
        table.add_row("Won Elimination", roundsWonElimination_1, roundsWonElimination_2)
        table.add_row("Won Capture", roundsWonCapture_1, roundsWonCapture_2)
        table.add_row("Won Hack", roundsWonHack_1, roundsWonHack_2)
        table.add_row("Won Custom", roundsWonCustom_1, roundsWonCustom_2)
        table.add_section()
        table.add_row("Heals", heals_1, heals_2)
        table.add_row("Got Healed", gotHealed_1, gotHealed_2)
        table.add_section()
        table.add_row("Time Played", timePlayed_1 + "h", timePlayed_2 + "h")
        table.add_row("Played Demoted", timePlayedDemoted_1 + "h", timePlayedDemoted_2 + "h")
        table.add_row("Votes", votes_1, votes_2)
        table.add_row("Role", role_1, role_2)

        console = Console()
        console.print(table)
        listTable = Table(title="")
        listTable.add_column("Commands", justify="", style="")
        listTable.add_row("0) Main menu")
        console.print(listTable)
        command = input()
        if command == "0":
            break
        else:
            continue

def PrintList(agentList):
    global page
    global currentList
    global LIST
    LIST = agentList
    searchTable = Table(title="", caption=f"Page {page} - {currentList}")
    searchTable.add_column("#", justify="")
    searchTable.add_column("Name", justify="", style="")
    searchTable.add_column("Level", justify="", style="")
    searchTable.add_column("Status", justify="", style="")
    n = 0
    for agent in agentList["data"]:
        if agentList['data'][n]['status']['online'] == False:
            status = 'Offline'
        else:
            status = 'Online'
        searchTable.add_row(f"{n + 1}", agentList['data'][n]['name'], str(agentList['data'][n]['stats']['level']), status)
        n = n + 1
    console.print(searchTable)

def PrintStats(agentStats):
    totalXp_1 = str(agentStats[1]['totalXp'])
    levelXpRequired_1 = str(agentStats[1]['levelXpRequired'])
    levelXp_1 = str(agentStats[1]['levelXp'])
    level_1 = str(agentStats[1]['level'])
    pickups_1 = str(agentStats[1]['pickups'])
    captures_1 = str(agentStats[1]['captures'])
    networkHacks_1 = str(agentStats[1]['networkHacks'])
    kills_1 = str(agentStats[1]['kills'])
    deaths_1 = str(agentStats[1]['deaths'])
    arrests_1 = str(agentStats[1]['arrests'])
    gotArrested_1 = str(agentStats[1]['gotArrested'])
    knockdowns_1 = str(agentStats[1]['knockdowns'])
    gotKnockedDown_1 = str(agentStats[1]['gotKnockedDown'])
    survivals_1 = str(agentStats[1]['survivals'])
    suicides_1 = str(agentStats[1]['suicides'])
    teamDamage_1 = str(agentStats[1]['teamDamage'])
    teamKills_1 = str(agentStats[1]['teamKills'])
    teamKnockdowns_1 = str(agentStats[1]['teamKnockdowns'])
    matchesWon_1 = str(agentStats[1]['matchesWon'])
    matchesLost_1 = str(agentStats[1]['matchesLost'])
    matches_1 = agentStats[1]['matchesWon'] + agentStats[1]['matchesLost']
    matchesWon_1_int = int(matchesWon_1)
    try:
        matchesWonPercent_1 = matchesWon_1_int / matches_1 * 100
        matchesWonPercent_1 = round(matchesWonPercent_1, 1)
        matchesWonPercent_1 = str(matchesWonPercent_1)
    except:
        matchesWonPercent_1 = "0"
    roundsLost_1 = str(agentStats[1]['roundsLost'])
    roundsTied_1 = str(agentStats[1]['roundsTied'])
    roundsWonElimination_1 = str(agentStats[1]['roundsWonElimination'])
    roundsWonCapture_1 = str(agentStats[1]['roundsWonCapture'])
    roundsWonHack_1 = str(agentStats[1]['roundsWonHack'])
    roundsWonCustom_1 = str(agentStats[1]['roundsWonCustom'])
    roundsWon_1 = int(roundsWonCapture_1) + int(roundsWonCustom_1) + int(roundsWonElimination_1) + int(roundsWonHack_1)
    roundsWon_1 = str(roundsWon_1)
    rounds_1 = int(roundsWon_1) + int(roundsLost_1)
    try:
        roundsWonPercent_1 = int(roundsWon_1) / rounds_1 * 100
        roundsWonPercent_1 = round(roundsWonPercent_1, 1)
        roundsWonPercent_1 = str(roundsWonPercent_1)
    except:
        roundsWonPercent_1 = "0"
    votes_1 = str(agentStats[2][0]['positive'] - agentStats[2][0]['negative'])
    timePlayed_1 = agentStats[1]['timePlayed'] / 60 / 60
    timePlayed_1 = round(timePlayed_1, 1)
    timePlayed_1 = str(timePlayed_1)
    timePlayedDemoted_1 = agentStats[1]['timePlayedDemoted'] / 60 / 60
    timePlayedDemoted_1 = round(timePlayedDemoted_1, 1)
    timePlayedDemoted_1 = str(timePlayedDemoted_1)
    heals_1 = str(agentStats[1]['heals'])
    gotHealed_1 = str(agentStats[1]['gotHealed'])
    role_1 = agentStats[0]["role"]
    if role_1 == "AUG":
       role_1 = "[cyan]AUG[/cyan]"
    if role_1 == "Demoted":
        role_1 = "[red]Demoted[/red]"
    if role_1 == "Developer":
        role_1 = "[green1]Developer[/green1]"
    else:
        role_1 = role_1
    while True:
        if int(votes_1) > 0:
            votes_1 = f"[green]{votes_1}[/green]"
            break
        if int(votes_1) < 0:
            votes_1 = f"[red]{votes_1}[/red]"
            break
        else:
            votes_1 = votes_1
            break

    if agentStats[0]['status']['online'] == False:
        lastSeen = str(agentStats[0]['lastLogin'])[0:10] + ' ' + str(agentStats[0]['lastLogin'])[11:19]
        online = f'[bright_black]Offline ◦ Last seen {lastSeen}[/bright_black]'
    elif agentStats[0]['status']['room'] == None:
        online = '[spring_green2]Online • Main Menu[/spring_green2]'
    else:
        mapId = agentStats[0]['status']['room']['currentMap']['id']
        for aMap in range(len(agentStats[0]['status']['room']['maps'])):
            if agentStats[0]['status']['room']['maps'][aMap]['id'] == mapId:
                mapName = agentStats[0]['status']['room']['maps'][aMap]['name']
            else:
                continue
        lastSeen = str(agentStats[0]['status']['room']['name']) + ' - ' + str(mapName)
        online = f'[spring_green2]Online • {lastSeen}[/spring_green2]'


    statsTable = Table(title=f"\n{agentStats[0]['name']} | {online}")
    statsTable.add_column("XP", justify="right", style="")
    statsTable.add_column("Actions", justify="right", style="")
    statsTable.add_column("Matches", justify="right", style="")
    statsTable.add_column("Team", justify="right", style="")
    statsTable.add_column("Other", justify="right", style="")
    statsTable.add_row(f"Level: {level_1}", f"Pickups: {pickups_1}", f"Matches Won: {matchesWon_1}", f"Heals: {heals_1}", f"Time Played: {timePlayed_1}h")
    statsTable.add_row(f"{levelXp_1}/{levelXpRequired_1} XP", f"Captures: {captures_1}", f"Matches Lost: {matchesLost_1}", f"Got Healed: {gotHealed_1}", f"Played Demoted: {timePlayedDemoted_1}h")
    statsTable.add_row(f"", f"Hacks: {networkHacks_1}", f"Matches W/L: {matchesWonPercent_1}%", f"", f"")
    statsTable.add_row(f"Total: {totalXp_1} XP", f"Survivals: {survivals_1}", f"", f"Team Damage: {teamDamage_1}", f"Votes: {votes_1}")
    statsTable.add_row(f"", f"Kills: {kills_1}", f"Rounds Won: {roundsWon_1}", f"Team Kills: {teamKills_1}", f"")
    statsTable.add_row(f"", f"Arrests: {arrests_1}", f"Rounds Lost: {roundsLost_1}", f"Team Knockdowns: {teamKnockdowns_1}", f"Role: {role_1}")
    statsTable.add_row(f"", f"Knockdowns: {knockdowns_1}", f"Rounds W/L: {roundsWonPercent_1}", f"", f"")
    statsTable.add_row(f"", f"Deaths: {deaths_1}", f"Rounds Tied: {roundsTied_1}", f"", f"")
    statsTable.add_row(f"", f"Got Arrested: {gotArrested_1}", f"Won Elimination: {roundsWonElimination_1}", f"", f"")
    statsTable.add_row(f"", f"Got Knocked Down: {gotKnockedDown_1}", f"Won Capture: {roundsWonCapture_1}", f"", f"")
    statsTable.add_row(f"", f"Suicides: {suicides_1}", f"Won Hack: {roundsWonHack_1}", f"", f"")
    statsTable.add_row(f"", f"", f"Won Custom: {roundsWonCustom_1}", f"", f"")

    bigTable = Table(title="", caption=f"")
    bigTable.add_column(f"{agentStats[0]['name']} | {online}", justify="center", style="")
    bigTable.add_row(statsTable)

    console = Console()
    console.print(statsTable)

def CommandWindowStats(agentId):
    global comparison_1
    global comparison_2
    while True:
        print("Loading...")
        PrintStats(GetStats(agentId))
        listTable = Table(title="")
        listTable.add_column("Commands", justify="", style="")
        listTable.add_row("1) Add to comparison [cyan](Water)[/cyan]\n2) Add to comparison [orange3](Fire)[/orange3]\n0) Back")
        console.print(listTable)
        command = input()
        if command == "1":
            comparison_1 = agentId
            print("Agent added to comparison as [cyan]Water[/cyan]")
            break
        elif command == "2":
            comparison_2 = agentId
            print("Agent added to comparison as [orange3]Fire[/orange3]")
            break
        elif command == "0":
            break
        else:
            continue

def CommandWindowAdvanced():
    global page
    while True:
        print("Loading...")
        PrintList(GetListAdvanced(advancedFilter, page))
        listTable = Table(title="")
        listTable.add_column("Commands", justify="", style="")
        listTable.add_row("1-25) View stats\nz) Next page\nx) Previous page\nc) Jump to page\n0) Back")
        console.print(listTable)
        command = input()
        if command == "z":
            page = page + 1
        elif command == "x":
            if not page < 2:
                page = page - 1
            else:
                continue
        elif command == "c":
            pageJump = input("Enter page number: ")
            if pageJump.isnumeric():
                pageJump = int(pageJump)
                if pageJump < 1:
                    page = 1
                else:
                    page = pageJump
            else:
                continue
        elif command == "0":
            break
        elif command.isnumeric():
            try:
                int(command) > 0 and int(command) < 26
            except:
                continue
            intCommand = int(command) - 1
            try:
                currentId = LIST['data'][intCommand]['steamId']
                CommandWindowStats(int(currentId))
            except:
                continue
        else:
            continue




console = Console()
comparison_1 = None
comparison_2 = None

print('@@@@                     @@@@')
print('@@@@@@                   @@@@')
print('@@@@@@@@                 @@@@')
print('@@@@ @@@@                @@@@')
print('@@@@         [red]****[/red]        @@@@')
print('@@@@        [red]******[/red]       @@@@')
print('@@@@         [red]****[/red]        @@@@')
print('@@@@                @@@@ @@@@')
print('@@@@                 @@@@@@@@')
print('@@@@                   @@@@@@')
print('@@@@                     @@@@')

while True:
    page = 1
    doNotBreak = True

    mainTable = Table(title="")
    mainTable.add_column("Main menu", justify="", style="")
    mainTable.add_row("1) Top agents\n2) Search agents\n3) Compare agents\n4) Advanced search\n9) Credits\n0) Exit")
    console.print(mainTable)
    command = input()
    if command == "0":
        sys.exit()
    if command == "9":
        print("Made by VadimTawer. All stats are taken from IntruderFPS.com.\n")
        while True:
            print("1) [bright_red]YouTube[/bright_red]")
            print("2) [dodger_blue1]Telegram[/dodger_blue1]")
            print("3) [medium_purple3]Discord[/medium_purple3]")
            print("4) [blue]GitHub[/blue]")
            print("0) Back")
            command = input()
            if command == "1":
                open("https://youtube.com/@VadimTawer")
            if command == "2":
                open("https://t.me/+ZhVKq6IRBa0yMTQy")
            if command == "3":
                print("VadimTawer#9719")
            if command == "4":
                open("https://github.com/VadimTawer/IntruderAgents")
            if command == "0":
                break
    if command == "3":
        print('Loading...')
        try:
            CompareStats(GetStats(comparison_1), GetStats(comparison_2))
        except:
            print("[red]Error! Add agents to comparison first![/red]")
    if command == "1":
        while True:
            print('Loading...')
            PrintList(GetListTop(page))
            listTable = Table(title="")
            listTable.add_column("Commands", justify="", style="")
            listTable.add_row("1-25) View stats\nz) Next page\nx) Previous page\nc) Jump to page\n0) Main menu")
            console.print(listTable)
            command = input()
            if command == "z":
                page = page + 1
            elif command == "x":
                if not page < 2:
                    page = page - 1
                else:
                    continue
            elif command == "c":
                pageJump = input("Enter page number: ")
                if pageJump.isnumeric():
                    pageJump = int(pageJump)
                    if pageJump < 1:
                        page = 1
                    else:
                        page = pageJump
                else:
                    continue
            elif command == "0":
                break
            elif command.isnumeric():
                try:
                    int(command) > 0 and int(command) < 26
                except:
                    continue
                intCommand = int(command) - 1
                currentId = LIST['data'][intCommand]['steamId']
                CommandWindowStats(int(currentId))
    if command == "2":
        while doNotBreak == True:
            keywordIsValid = False
            keyword = input("Enter name or Steam ID: ")
            if len(keyword) >= 3:
                keywordIsValid = True
            while keywordIsValid == True:
                print('Loading...')
                PrintList(GetListSearch(keyword, page))
                listTable = Table(title="")
                listTable.add_column("Commands", justify="", style="")
                listTable.add_row("1-25) View stats\nz) Next page\nx) Previous page\nc) Jump to page\n0) Main menu")
                console.print(listTable)
                command = input()
                if command == "z":
                    page = page + 1
                elif command == "x":
                    if not page < 2:
                        page = page - 1
                    else:
                        continue
                elif command == "c":
                    pageJump = input("Enter page number: ")
                    if pageJump.isnumeric():
                        pageJump = int(pageJump)
                        if pageJump < 1:
                            page = 1
                        else:
                            page = pageJump
                    else:
                        continue
                elif command == "0":
                    doNotBreak = False
                    break
                elif command.isnumeric():
                    try:
                        int(command) > 0 and int(command) < 26
                    except:
                        continue
                    intCommand = int(command) - 1
                    try:
                        currentId = LIST['data'][intCommand]['steamId']
                        CommandWindowStats(int(currentId))
                    except:
                        continue
    if command == "4":
        while True:
            page = 1
            listTable = Table(title="")
            listTable.add_column("Order by...", justify="", style="")
            listTable.add_column()
            listTable.add_column()
            listTable.add_row("""1) Time played\n2) Captures\n3) Pickups\n4) Hacks\n5) Arrests\n6) Knockdowns\n7) Survivals\n8) Kills\n9) Deaths\n10) Got Arrested""",
            """11) Got Knocked Down\n12) Suicides\n13) Team Damage\n14) Team Kills\n15) Team Knockdowns\n16) Matches Won\n17) Matches Lost\n18) Rounds Won Capture"""+
            """\n19) Rounds Won Hack\n20) Rounds Won Elimination""","""21) Rounds Won Timer\n22) Rounds Won Custom\n23) Rounds Tied\n24) Rounds Lost\n25) Heals\n26) Got Healed\n\n\n\n0) Main menu""")
            console.print(listTable)
            command = input()
            if command == "0":
                doNotBreak = False
                break
            if command == "1":
                advancedFilter = "?orderBy=stats.timePlayed%3Adesc"
                currentList = "Time Played"
                CommandWindowAdvanced()
            if command == "2":
                advancedFilter = "?orderBy=stats.captures%3Adesc"
                currentList = "Captures"
                CommandWindowAdvanced()
            if command == "3":
                advancedFilter = "?orderBy=stats.pickups%3Adesc"
                currentList = "Pickups"
                CommandWindowAdvanced()
            if command == "4":
                advancedFilter = "?orderBy=stats.networkhacks%3Adesc"
                currentList = "Hacks"
                CommandWindowAdvanced()
            if command == "5":
                advancedFilter = "?orderBy=stats.Arrests%3Adesc"
                currentList = "Arrests"
                CommandWindowAdvanced()
            if command == "6":
                advancedFilter = "?orderBy=stats.Knockdowns%3Adesc"
                currentList = "Knockdowns"
                CommandWindowAdvanced()
            if command == "7":
                advancedFilter = "?orderBy=stats.Survivals%3Adesc"
                currentList = "Survivals"
                CommandWindowAdvanced()
            if command == "8":
                advancedFilter = "?orderBy=stats.Kills%3Adesc"
                currentList = "Kills"
                CommandWindowAdvanced()
            if command == "9":
                advancedFilter = "?orderBy=stats.Deaths%3Adesc"
                currentList = "Deaths"
                CommandWindowAdvanced()
            if command == "10":
                advancedFilter = "?orderBy=stats.GotArrested%3Adesc"
                currentList = "Got Arrested"
                CommandWindowAdvanced()
            if command == "11":
                advancedFilter = "?orderBy=stats.GotKnockedDown%3Adesc"
                currentList = "Got Knocked Down"
                CommandWindowAdvanced()
            if command == "12":
                advancedFilter = "?orderBy=stats.Suicides%3Adesc"
                currentList = "Suicides"
                CommandWindowAdvanced()
            if command == "13":
                advancedFilter = "?orderBy=stats.TeamDamage%3Adesc"
                currentList = "Team Damage"
                CommandWindowAdvanced()
            if command == "14":
                advancedFilter = "?orderBy=stats.TeamKills%3Adesc"
                currentList = "Team Kills"
                CommandWindowAdvanced()
            if command == "15":
                advancedFilter = "?orderBy=stats.TeamKnockdowns%3Adesc"
                currentList = "Team Knockdowns"
                CommandWindowAdvanced()
            if command == "16":
                advancedFilter = "?orderBy=stats.MatchesWon%3Adesc"
                currentList = "Matches Won"
                CommandWindowAdvanced()
            if command == "17":
                advancedFilter = "?orderBy=stats.MatchesLost%3Adesc"
                currentList = "Matches Lost"
                CommandWindowAdvanced()
            if command == "18":
                advancedFilter = "?orderBy=stats.RoundsWonCapture%3Adesc"
                currentList = "Rounds Won Capture"
                CommandWindowAdvanced()
            if command == "19":
                advancedFilter = "?orderBy=stats.RoundsWonHack%3Adesc"
                currentList = "Rounds Won Hack"
                CommandWindowAdvanced()
            if command == "20":
                advancedFilter = "?orderBy=stats.RoundsWonElimination%3Adesc"
                currentList = "Rounds Won Elimination"
                CommandWindowAdvanced()
            if command == "21":
                advancedFilter = "?orderBy=stats.RoundsWonTimer%3Adesc"
                currentList = "Rounds Won Timer"
                CommandWindowAdvanced()
            if command == "22":
                advancedFilter = "?orderBy=stats.RoundsWonCustom%3Adesc"
                currentList = "Rounds Won Custom"
                CommandWindowAdvanced()
            if command == "23":
                advancedFilter = "?orderBy=stats.RoundsTied%3Adesc"
                currentList = "Rounds Tied"
                CommandWindowAdvanced()
            if command == "24":
                advancedFilter = "?orderBy=stats.RoundsLost%3Adesc"
                currentList = "Rounds Lost"
                CommandWindowAdvanced()
            if command == "25":
                advancedFilter = "?orderBy=stats.Heals%3Adesc"
                currentList = "Heals"
                CommandWindowAdvanced()
            if command == "26":
                advancedFilter = "?orderBy=stats.GotHealed%3Adesc"
                currentList = "Got Healed"
                CommandWindowAdvanced()
            else:
                continue
            if doNotBreak == True:
                CommandWindowAdvanced()
