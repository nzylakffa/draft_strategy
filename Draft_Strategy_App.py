import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import ax_text, fig_text
import requests
from matplotlib.font_manager import FontProperties
import tempfile
import os

###################
##### Sidebar #####
###################
st.sidebar.image('ffa_red.png', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center;'>Read This!</h1>", unsafe_allow_html=True)
st.sidebar.markdown("* Click Fullscreen at the bottom for a better user experience")
st.sidebar.markdown("* To use this tool, first input your leagues scoring and roster settings into the first three drop downs.")
st.sidebar.markdown("* Next, select the position you'd like to look at.")
st.sidebar.markdown("* The first dot (green) indicates the first round where selecting that position is optimal in your format. The second dot (yellow) indicates the last round selecting that position is optimal in your format.")
st.sidebar.markdown("* For example: Let's say you play in a PPR, 3 WR and 2 FLEX league and you want to know what the best range is to draft your third WR. In the '3rd WR' row the green dot indicates round 3 and the yellow dot indicates round 6. This means that the optimal range to select your 3rd WR in this format is any of rounds 3 through 6.")

st.markdown("<h3 style='text-align: center;'>Click Fullscreen at the bottom for a better user experience!</h3>", unsafe_allow_html=True)


scoring = st.selectbox(
    "Select a Scoring Format:",
    ('PPR', 'Half PPR'))

wr_count = st.selectbox(
    "How Many WR's Does Your League Start?",
    ('2', '3'))

flex_count = st.selectbox(
    "How Many FLEX Spots(NOT SuperFlex!) Does Your League Start?",
    ('1', '2'))

pos = st.selectbox(
    "What Position Would You Like to Look at?",
    ('RB', 'WR', 'TE', 'QB'))


###############################################
########## Load Fonts From Github #############
###############################################

# Function to load font from a URL and create FontProperties
def load_font_from_url(url, font_name):
    # Send request to get the font
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Save the font to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(url)[-1]) as temp_font_file:
        temp_font_file.write(response.content)
        temp_font_file.flush()  # Ensure all data is written to disk
        
        # Load this temporary font file into FontProperties
        font_prop = FontProperties(fname=temp_font_file.name)
    
    # Register the font
    plt.rcParams['font.family'] = font_name
    return font_prop

# URLs to the font files on GitHub
url_grotesk_bold = 'https://raw.githubusercontent.com/nzylakffa/draft_strategy/main/FamiljenGrotesk-Bold.ttf'
# url_pally_regular = 'https://raw.githubusercontent.com/nzylakffa/draft_strategy/main/Pally-Regular.otf'
url_grotesk_regular = 'https://raw.githubusercontent.com/nzylakffa/draft_strategy/main/FamiljenGrotesk-VariableFont_wght.ttf'

# Load the fonts
grotesk_font_bold = load_font_from_url(url_grotesk_bold, 'Familjen Grotesk')
grotesk_font = load_font_from_url(url_grotesk_regular, 'Familjen Grotesk')
# pally_font_regular = load_font_from_url(url_pally_regular, 'Pally')

########################################################################
############# Create Dataframes Based off Sleeper Research #############
########################################################################

# Do we have to create a massive if else for all of these? Probably the easiest way

if scoring == 'PPR' and wr_count == '2' and flex_count == '1' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 14, 12, 10, 8, 6, 4, 3],
        "Last Optimal Round": [15, 15, 15, 13, 11, 9, 7, 6]})
    
elif scoring == 'PPR' and wr_count == '2' and flex_count == '2' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [14, 13, 12, 10, 8, 6, 3, 3],
        "Last Optimal Round": [15, 15, 15, 13, 12, 9, 8, 7]})
    
elif scoring == 'PPR' and wr_count == '2' and flex_count == '1' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 12, 10, 9, 5, 3, 2, 1],
        "Last Optimal Round": [15, 14, 13, 12, 10, 8, 5, 1]})
    
elif scoring == 'PPR' and wr_count == '2' and flex_count == '2' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 12, 10, 8, 4, 3, 2, 1],
        "Last Optimal Round": [15, 13, 13, 12, 10, 6, 5, 2]})
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '1' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 14, 12, 10, 8, 6, 4, 3],
        "Last Optimal Round": [15, 15, 15, 13, 11, 9, 7, 6]})
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '2' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 13, 12, 9, 8, 7, 6, 3],
        "Last Optimal Round": [15, 15, 13, 13, 12, 10, 9, 8]})
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '1' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [13, 12, 9, 5, 4, 3, 2, 1],
        "Last Optimal Round": [15, 15, 13, 12, 9, 6, 4, 1]})
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '2' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [12, 9, 7, 5, 4, 3, 2, 1],
        "Last Optimal Round": [15, 14, 13, 12, 9, 6, 4, 1]})

elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '1' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [14, 13, 10, 9, 8, 3, 2, 1],
        "Last Optimal Round": [15, 15, 15, 12, 10, 9, 7, 5]})
    
elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '2' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [14, 12, 10, 10, 4, 3, 2, 1],
        "Last Optimal Round": [15, 13, 13, 12, 10, 8, 5, 5]})
    
elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '1' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [16, 14, 11, 11, 7, 6, 4, 1],
        "Last Optimal Round": [17, 15, 15, 13, 11, 9, 8, 7]})
    
elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '2' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 13, 11, 8, 7, 6, 2, 1],
        "Last Optimal Round": [17, 16, 15, 13, 10, 9, 7, 6]})
    
elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '1' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [17, 13, 8, 6, 4, 3, 2, 1],
        "Last Optimal Round": [18, 15, 13, 11, 9, 5, 4, 1]})
    
elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '2' and pos == 'WR':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 15, 8, 5, 4, 3, 2, 1],
        "Last Optimal Round": [17, 17, 16, 16, 12, 5, 3, 2]}) 

elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '1' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [14, 13, 12, 9, 8, 6, 5, 1],
        "Last Optimal Round": [17, 16, 15, 13, 10, 9, 8, 6]}) 
    
elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '2' and pos == 'RB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [15, 11, 10, 8, 8, 6, 3, 1],
        "Last Optimal Round": [17, 15, 15, 14, 12, 9, 8, 6]}) 

elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '1' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 17, 14, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 15]}) 
    
elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '2' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 18, 10, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 15]})  
    
elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '1' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 16, 12, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 15]})  
    
elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '2' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 15, 12, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 15]})  

elif scoring == 'PPR' and wr_count == '2' and flex_count == '1' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 15, 13, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 13]})  
    
elif scoring == 'PPR' and wr_count == '2' and flex_count == '2' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 14, 12, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 13]})     
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '1' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 18, 18, 13, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 14]})  
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '2' and pos == 'TE':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 18, 16, 14, 1],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 15]})  
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '2' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 16, 13, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 15]})
    
elif scoring == 'PPR' and wr_count == '3' and flex_count == '1' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 15, 12, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 12]})
    
    
elif scoring == 'PPR' and wr_count == '2' and flex_count == '2' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 17, 13, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 15]})
    
elif scoring == 'PPR' and wr_count == '2' and flex_count == '1' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 16, 12, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 12]})

elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '2' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 15, 13, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 11]})
    
elif scoring == 'Half PPR' and wr_count == '2' and flex_count == '1' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 16, 15, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 6]})
    
elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '2' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 17, 13, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 6]})
    
elif scoring == 'Half PPR' and wr_count == '3' and flex_count == '1' and pos == 'QB':
    df = pd.DataFrame({
        f"{pos}": [f"8th {pos}", f"7th {pos}", f"6th {pos}", f"5th {pos}", f"4th {pos}", f"3rd {pos}", f"2nd {pos}", f"1st {pos}"],
        "1st Optimal Round": [20, 20, 20, 20, 20, 16, 15, 3],
        "Last Optimal Round": [20, 20, 20, 20, 20, 20, 20, 13]})    

else:
    st.write("Combo not calculated yet!")
    

if scoring == "PPR":
    
    color_lose, color_win = "#28A87D", "#EFAC00" 
    color_lose_dark, color_win_dark = "#1e8563", "#aa7c05"

    # changed team_name to rb_name and bayern_much to rb_round_1

    fig, ax = plt.subplots(figsize=(7,5))

    # horizontal lines
    my_range = range(df[f'{pos}'].nunique())
    ax.hlines(y=my_range, xmin=df['1st Optimal Round'], xmax=df['Last Optimal Round'], color='grey', alpha=0.4)

    # points
    ax.scatter(df['1st Optimal Round'], my_range, color=color_lose, zorder=2, s=80)
    ax.scatter(df['Last Optimal Round'], my_range, color=color_win, zorder=2, s=80)

    # add team names
    n = len(df)
    for i in range(df[f'{pos}'].nunique()):

        # team names
        rb_name = df[f"{pos}"][i]
        if rb_name == f"1st {pos} Round":
            font = grotesk_font_bold
            rb_round_1 = df[df[f"{pos}"] == rb_name]
            ax.hlines(y=i, xmin=rb_round_1[f'1st {pos} Round'], xmax=rb_round_1['Last Optimal Round'], linewidth=2, color='black', zorder=1)

        else:
            font = grotesk_font
        ax_text(0.05, i,
                f"<{rb_name}>",
                ha='right', va='center',
                fontproperties=grotesk_font,
                highlight_textprops=[
                    {"color": "black",
                     "font": font,
                     "size": 12}
                ]
            )

        # 1st Optimal Round
        losses = df['1st Optimal Round'][i]
        ax_text(
            losses-0.42, i,
            f"<{int(losses)}>",  # Changed here to display as an integer
            ha='right', va='center',
            fontproperties=grotesk_font,
            highlight_textprops=[
                {"color": color_lose_dark,
                 "font": font}
            ]
        )

        # Last Optimal Round
        wins = df['Last Optimal Round'][i]
        ax_text(
            wins+0.42, i,
            f"<{int(wins)}>",
            ha='left', va='center',
            fontproperties=grotesk_font,
            highlight_textprops=[
                {"color": color_win_dark,
                 "font": font}]
        )

    # title
    text = f"<1st Optimal Round> & <Last Optimal Round> \n <             {wr_count} WR | {flex_count} FLEX | {scoring} Leagues>"
    fig_text(
        0.45, 1,
        text,
        fontsize=20,
        fontproperties=grotesk_font,
        ha='center', va='center',
        highlight_textprops=[
            {"color": color_lose_dark,
             "font": grotesk_font_bold},

            {"color": color_win_dark,
             "font": grotesk_font_bold},

            {"font": grotesk_font_bold},
        ]
    )

    # credit
    text = "<Data: Collected from over 1 million Sleeper teams from 2021-2023"
    fig_text(
        0, 0.04,
        text,
        fontsize=8,
        fontproperties=grotesk_font,
        color='grey',
        ha='left', va='center',
        highlight_textprops=[
            {"font": grotesk_font_bold}
        ]
    )

    # remove axis
    ax.set_axis_off()
    st.pyplot(fig)
    
else:
    
    color_lose, color_win = "#28A87D", "#EFAC00" 
    color_lose_dark, color_win_dark = "#1e8563", "#aa7c05"

    # changed team_name to rb_name and bayern_much to rb_round_1

    fig, ax = plt.subplots(figsize=(7,5))

    # horizontal lines
    my_range = range(df[f'{pos}'].nunique())
    ax.hlines(y=my_range, xmin=df['1st Optimal Round'], xmax=df['Last Optimal Round'], color='grey', alpha=0.4)

    # points
    ax.scatter(df['1st Optimal Round'], my_range, color=color_lose, zorder=2, s=80)
    ax.scatter(df['Last Optimal Round'], my_range, color=color_win, zorder=2, s=80)

    # add team names
    n = len(df)
    for i in range(df[f'{pos}'].nunique()):

        # team names
        rb_name = df[f"{pos}"][i]
        if rb_name == f"1st {pos} Round":
            font = grotesk_font_bold
            rb_round_1 = df[df[f"{pos}"] == rb_name]
            ax.hlines(y=i, xmin=rb_round_1[f'1st {pos} Round'], xmax=rb_round_1['Last Optimal Round'], linewidth=2, color='black', zorder=1)

        else:
            font = grotesk_font
        ax_text(0.05, i,
                f"<{rb_name}>",
                ha='right', va='center',
                fontproperties=grotesk_font,
                highlight_textprops=[
                    {"color": "black",
                     "font": font,
                     "size": 12}
                ]
            )

        # 1st Optimal Round
        losses = df['1st Optimal Round'][i]
        ax_text(
            losses-0.42, i,
            f"<{int(losses)}>",  # Changed here to display as an integer
            ha='right', va='center',
            fontproperties=grotesk_font,
            highlight_textprops=[
                {"color": color_lose_dark,
                 "font": font}
            ]
        )

        # Last Optimal Round
        wins = df['Last Optimal Round'][i]
        ax_text(
            wins+0.42, i,
            f"<{int(wins)}>",
            ha='left', va='center',
            fontproperties=grotesk_font,
            highlight_textprops=[
                {"color": color_win_dark,
                 "font": font}]
        )

    # title
    text = f"<1st Optimal Round> & <Last Optimal Round> \n <        {wr_count} WR | {flex_count} FLEX | {scoring} Leagues>"
    fig_text(
        0.45, 1,
        text,
        fontsize=20,
        fontproperties=grotesk_font,
        ha='center', va='center',
        highlight_textprops=[
            {"color": color_lose_dark,
             "font": grotesk_font_bold},

            {"color": color_win_dark,
             "font": grotesk_font_bold},

            {"font": grotesk_font_bold},
        ]
    )

    # credit
    text = "<Data: Collected from randomly selected Sleeper leagues from 2021-2023"
    fig_text(
        0, 0.04,
        text,
        fontsize=8,
        fontproperties=grotesk_font,
        color='grey',
        ha='left', va='center',
        highlight_textprops=[
            {"font": grotesk_font_bold}
        ]
    )

    # remove axis
    ax.set_axis_off()
    st.pyplot(fig)
