import pandas

df = pandas.read_csv("La_liga_2.0.csv")

print("----------------------------------------------ALL TEAMS----------------------------------------------")
print(
    'Alaves, Albacete, Almeria, Ath Bilbao, Ath Madrid, Barcelona, Betis, Cadiz, Celta, Compostela, Cordoba, Eibar, Elche, Espanol, Extremadura, Getafe, Gimnastic, Girona, Granada, Hercules, Huesca, La Coruna, Las Palmas, Leganes, Lerida, Levante, Logrones, Malaga, Mallorca, Merida, Murcia, Numancia, Osasuna, Oviedo, Real Madrid, Recreativo, Salamanca, Santander, Sevilla, Sociedad, Sp Gijon, Tenerife, Valencia, Valladolid, Vallecano, Villareal, Villarreal, Xerez, Zaragoza')


def get_all_results():
    f_team = input("first team: ")
    s_team = input("s team: ")
    f_team_goals = 0
    s_team_goals = 0
    f_team_wins = 0
    s_team_wins = 0
    draws = 0
    total = 0

    print("----------------------------------------------RESULTS----------------------------------------------")
    for x, y in df.iterrows():
        if y["HomeTeam"] == f_team and y["AwayTeam"] == s_team or y["HomeTeam"] == s_team and y["AwayTeam"] == f_team:
            print(
                f"{y['HomeTeam']} vs {y['AwayTeam']} played on {y['Date']}. The result was {y['HomeTeam']} {y['FTHG']} - {y['FTAG']} {y['AwayTeam']}.")
            if y["HomeTeam"] == s_team:
                s_team_goals = s_team_goals + y["FTHG"]
                f_team_goals = f_team_goals + y["FTAG"]
            else:
                s_team_goals = s_team_goals + y["FTAG"]
                f_team_goals = f_team_goals + y["FTHG"]
            total += 1
            if y["FTR"] == "D":
                draws += 1
            elif y["FTR"] == f_team:
                f_team_wins += 1
            elif y["FTR"] == s_team:
                s_team_wins += 1
    if total > 0:
        print(
            "----------------------------------------------WON MATCHES AND PERCENTAGES----------------------------------------------")
        print(
            f"{f_team} has won {f_team_wins} matches against {s_team}. {f_team} won {round(f_team_wins * 100 / total, 2)}% of the matches")
        print(
            f"{s_team} has won {s_team_wins} matches against {f_team}. {s_team} won {round(s_team_wins * 100 / total, 2)}% of the matches")
        print(f"{f_team} and {s_team} have tied {draws} times. {round(draws * 100 / total, 2)}% were a tie.")
        print(
            "----------------------------------------------TOTAL MATCHES----------------------------------------------")
        print(f"They have played a total of {total} times.")
        print("----------------------------------------------TOTAL GOALS----------------------------------------------")
        print(
            f"{f_team} has scored {f_team_goals} against {s_team}\n{s_team} has scored {s_team_goals} against {f_team}.")
    else:
        print(f"{f_team} has never played against {s_team}")


get_all_results()
