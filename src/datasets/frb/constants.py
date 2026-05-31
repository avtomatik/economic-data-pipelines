FILE_NAME_G17 = "FRB_G17.csv"

FILE_NAME_H15 = "FRB_H15.zip"

SERIES_ID = "CAPUTL.B00004.S"

SERIES_IDS = (
    "CAPUTL.B00004.S",  # Use This
    "CAPUTL.GMF.S",
)

API_URL = "https://www.federalreserve.gov/datadownload/Output.aspx?rel=g17&filetype.zip"

XPATH = ".//frb:DataSet"

G17_NAMESPACE = {
    "kf": (
        "http://www.federalreserve.gov/structure/"
        "compact/G17_IP_MAJOR_INDUSTRY_GROUPS"
    )
}

DEFAULT_OBSERVATION_COLUMNS = (
    "TIME_PERIOD",
    "OBS_VALUE",
)
