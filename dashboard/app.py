import glob

import pandas as pd
import streamlit as st


def read_output(folder):
    files = glob.glob(folder + "/*.csv")
    return pd.read_csv(files[0])


st.title("Cricket Performance Analytics")

st.header("Top Batsmen")
top_batsmen = read_output("output/top_batsmen")
st.dataframe(top_batsmen)

st.header("Orange Cap")
orange_cap = read_output("output/orange_cap")
st.dataframe(orange_cap)

st.header("Top Bowlers")
top_bowlers = read_output("output/top_bowlers")
st.dataframe(top_bowlers)

st.header("Purple Cap")
purple_cap = read_output("output/purple_cap")
st.dataframe(purple_cap)

st.header("Team Win Percentage")
team_win_percentage = read_output("output/team_win_percentage")
st.dataframe(team_win_percentage)

st.header("Average Score By Venue")
average_score = read_output("output/venue_analysis/average_score")
st.dataframe(average_score)

st.header("Powerplay Analysis")
powerplay_analysis = read_output("output/venue_analysis/powerplay_analysis")
st.dataframe(powerplay_analysis)

st.header("MVP Rankings")
mvp_rankings = read_output("output/mvp_rankings")
st.dataframe(mvp_rankings)
