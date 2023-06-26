import os
community_token = os.getenv("COMMUNITY_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")

db_url_object = "postgresql+psycopg2://postgres:blackmor@localhost:5432/Diploma"