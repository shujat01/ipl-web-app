from flask import Flask,render_template,request #this request is flask ka function
import requests # and this requests is our library which is sed to hit api
app=Flask(__name__)

import pandas as pd
import numpy as np

ipl_ball = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu6cb6Pj8C9elJc5ubswjVTObommsITlNsFy5X0EiBY7S-lsHEUqx3g_M16r50Ytjc0XQCdGDyzE_Y/pub?output=csv"
balls = pd.read_csv(ipl_ball)

@app.route('/')
def home():
    # response=requests.get('http://127.0.0.1:5000/api/teams')
    # teams=response.json()['teams']
    return render_template('home.html')

@app.route('/team1VSteam2')
def team1VSteam2():
    response=requests.get('http://127.0.0.1:5000/api/teams')
    teams=response.json()['teams']
    return render_template('teamvteam.html',teams=sorted(teams))

@app.route('/teamVteam')
def team_vs_team():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    
    response=requests.get('http://127.0.0.1:5000/api/teams')
    teams=response.json()['teams']

    response1=requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1,team2))
    response1=response1.json()
    return render_template('teamvteam.html',result=response1,teams=sorted(teams))

@app.route('/teamoverallrecord')
def teamRecord():
    response=requests.get('http://127.0.0.1:5000/api/teams')
    teams=response.json()['teams']
    return render_template('teamrecord.html',teams=sorted(teams))

@app.route('/teamRecord')
def team_record():
    team=request.args.get('team')

    response=requests.get('http://127.0.0.1:5000/api/teams')
    teams=response.json()['teams']

    response1=requests.get('http://127.0.0.1:5000/api/team-record?team={}'.format(team))
    response1=response1.json()
    return render_template('teamrecord.html',result=response1,teams=sorted(teams))
   
@app.route('/batsmanoverallrecord')
def batsmanRecord():
    batters=list(balls['batter'].unique())
    return render_template('battingrecord.html',batters=sorted(batters))

@app.route('/batsmanRecord')
def batsman_record():
    batsman=request.args.get('batsman')

    batters=list(balls['batter'].unique())
    
    response=requests.get('http://127.0.0.1:5000/api/batting-record?batsman={}'.format(batsman))
    response=response.json()
    return render_template('battingrecord.html',result=response,batters=sorted(batters))
    

@app.route('/bowleroverallrecord')
def bowlerRecord():
    bowlers=list(balls['bowler'].unique())
    return render_template('bowlingrecord.html',bowlers=sorted(bowlers))

@app.route('/bowlerRecord')

def bowler_record():
    bowler=request.args.get('bowler')

    bowlers=list(balls['bowler'].unique())
    
    response=requests.get('http://127.0.0.1:5000/api/bowling-record?bowler={}'.format(bowler))
    response=response.json()
    return render_template('bowlingrecord.html',result=response,bowlers=sorted(bowlers))
    


app.run(debug=True,port=8000)
