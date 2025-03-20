import re

def normalize_event_name(event_name):
    # Lowercase
    event_name = event_name.lower()
    # Remove words like "tournament:" or sport categories
    event_name = re.sub(r'(tournament:|ncaa|nba|mlb| - )', '', event_name)
    # Remove punctuation
    event_name = re.sub(r'[^\w\s]', '', event_name)
    # Extract team names split by 'vs'
    teams = [team.strip() for team in event_name.split('vs')]
    # Sort alphabetically and rejoin for consistency
    if len(teams) == 2:
        teams.sort()
        event_name = " vs ".join(teams)
    return event_name.strip()