# TODO:
# Read in the csv
# Total amount of gun deaths in each state
# Total amount of negative tweets in each state
# Save each of these in two arrays
# Write a new CSV with these numbers

# Load the Pandas libraries with alias 'pd'
import csv
import pandas as pd

# Initialize the arrays
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
          'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
state_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
               'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
state_populations = [4887871, 737438, 7171646,
                     3013825, 39557045, 5695564, 3572665, 967171, 21299325, 10519475, 1420491, 1754208, 12741080, 6691878, 3156145, 2911505, 4468402, 4659978, 1338404, 6042718, 6902149, 9995915, 5611179, 2986530, 6126452, 1062305, 1929268, 3034392, 1356458, 8908520, 2095428, 19542209, 10383620, 760077, 11689442, 3943079, 4190713, 12807060, 1057315, 5084127, 882235, 6770010, 28701845, 3161105, 626299, 8517685, 7535591, 1805832, 5813568, 577737]
state_deaths = [0] * 50
state_injured = [0] * 50
state_incidents = [0] * 50

# Read data from file 'data.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
def ingest():
    data = pd.read_csv('data.csv')
    data.drop(['incident_id', 'city_or_county', 'address', 'incident_url', 'source_url', 'incident_url_fields_missing', 'congressional_district', 'gun_stolen', 'gun_type', 'incident_characteristics', 'latitude', 'location_description', 'longitude', 'n_guns_involved', 'notes', 'participant_age', 'participant_age_group', 'participant_gender', 'participant_name', 'participant_relationship', 'participant_status', 'participant_type', 'sources', 'state_house_district', 'state_senate_district'], axis=1, inplace=True)
    print('dataset loaded with shape', data.shape)
    print(data)
    return data


data = ingest()
total_injured = 0 
total_deaths = 0
total_incidents = 0


def preprocess(data):
    for row in data.itertuples():
        global total_injured
        total_injured += row.n_injured
        global total_deaths
        total_deaths += row.n_killed
        global total_incidents
        total_incidents += 1
        for i in range(50):
            if states[i] == row.state:
                state_deaths[i] += row.n_killed
                state_injured[i] += row.n_injured
                state_incidents[i] += 1


preprocess(data)
print("Total Injured: ", total_injured)
print("Total Killed: ", total_deaths)
print(state_deaths)
print(state_injured)
print(state_incidents)
print(total_incidents)
print(sum(state_incidents))

myFile = open('processed.csv', 'w')
with myFile:
   writer = csv.writer(myFile)
   writer.writerow(['state', 'code', 'injured', 'killed', 'incidents', 'death_rate'])
   for i in range(50):
       death_rate = ( state_deaths[i] / state_populations[i] ) * 10000
       row = [states[i], state_codes[i], state_injured[i], state_deaths[i], state_incidents[i], death_rate]
       print(row)
       writer.writerow(row)