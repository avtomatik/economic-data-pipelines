DEFAULT_SCHEMA = {
    "columns": {
        "period": 0,
        "series_id": 10,
        "value": 12,
    },
    "parse_dates": False,
}

STATCAN_SCHEMAS = {
    310004: {
        "columns": {
            "category": 4,
            "component": 5,
            "period": 0,
            "prices": 2,
            "series_id": 6,
            "value": 8,
        },
        "parse_dates": False,
    },
    2820011: {
        "columns": {
            "classofworker": 2,
            "geo": 1,
            "industry": 3,
            "period": 0,
            "series_id": 5,
            "sex": 4,
            "value": 7,
        },
        "parse_dates": True,
    },
    2820012: {
        "columns": {"period": 0, "series_id": 5, "value": 7},
        "parse_dates": False,
    },
    3790031: {
        "columns": {
            "geo": 1,
            "naics": 4,
            "period": 0,
            "prices": 3,
            "seas": 2,
            "series_id": 5,
            "value": 7,
        },
        "parse_dates": True,
    },
    3800084: {
        "columns": {
            "est": 3,
            "geo": 1,
            "period": 0,
            "seas": 2,
            "series_id": 4,
            "value": 6,
        },
        "parse_dates": True,
    },
    3800102: {
        "columns": {"period": 0, "series_id": 4, "value": 6},
        "parse_dates": False,
    },
    3800106: {
        "columns": {"period": 0, "series_id": 3, "value": 5},
        "parse_dates": False,
    },
    3800518: {
        "columns": {"period": 0, "series_id": 4, "value": 6},
        "parse_dates": False,
    },
    3800566: {
        "columns": {"period": 0, "series_id": 3, "value": 5},
        "parse_dates": False,
    },
    3800567: {
        "columns": {"period": 0, "series_id": 4, "value": 6},
        "parse_dates": False,
    },
    14100027: {
        "columns": {"period": 0, "series_id": 10, "value": 12},
        "parse_dates": False,
    },
    14100235: {
        "columns": {"period": 0, "series_id": 8, "value": 10},
        "parse_dates": True,
    },
    16100053: {
        "columns": {"period": 0, "series_id": 9, "value": 11},
        "parse_dates": False,
    },
    36100096: {
        "columns": {
            "category": 5,
            "component": 6,
            "geo": 1,
            "industry": 4,
            "period": 0,
            "prices": 3,
            "series_id": 11,
            "value": 13,
        },
        "parse_dates": False,
    },
    36100207: {
        "columns": {"period": 0, "series_id": 9, "value": 11},
        "parse_dates": True,
    },
    36100303: {
        "columns": {"period": 0, "series_id": 9, "value": 11},
        "parse_dates": False,
    },
    36100305: {
        "columns": {"period": 0, "series_id": 9, "value": 11},
        "parse_dates": False,
    },
    36100434: {
        "columns": {"period": 0, "series_id": 10, "value": 12},
        "parse_dates": True,
    },
    14100355: {"columns": {}, "parse_dates": True},
    16100109: {"columns": {}, "parse_dates": True},
    14100238: {"columns": {}, "parse_dates": True},
    16100111: {"columns": {}, "parse_dates": True},
    36100108: {"columns": {}, "parse_dates": True},
    14100221: {"columns": {}, "parse_dates": True},
    10100094: {"columns": {}, "parse_dates": True},
}


MAP_ARCHIVE_ID_FIELD = {
    310004: {
        "columns": {
            "period": 0,
            "prices": 2,
            "category": 4,
            "component": 5,
            "series_id": 6,
            "value": 8,
        },
        "parse_dates": False,
    },
    2820011: {
        "columns": {
            "period": 0,
            "geo": 1,
            "classofworker": 2,
            "industry": 3,
            "sex": 4,
            "series_id": 5,
            "value": 7,
        },
        "parse_dates": True,
    },
    2820012: {
        "columns": {"period": 0, "series_id": 5, "value": 7},
        "parse_dates": False,
    },
    3790031: {
        "columns": {
            "period": 0,
            "geo": 1,
            "seas": 2,
            "prices": 3,
            "naics": 4,
            "series_id": 5,
            "value": 7,
        },
        "parse_dates": True,
    },
    3800084: {
        "columns": {
            "period": 0,
            "geo": 1,
            "seas": 2,
            "est": 3,
            "series_id": 4,
            "value": 6,
        },
        "parse_dates": True,
    },
    3800102: {
        "columns": {"period": 0, "series_id": 4, "value": 6},
        "parse_dates": False,
    },
    3800106: {
        "columns": {"period": 0, "series_id": 3, "value": 5},
        "parse_dates": False,
    },
    3800518: {
        "columns": {"period": 0, "series_id": 4, "value": 6},
        "parse_dates": False,
    },
    3800566: {
        "columns": {"period": 0, "series_id": 3, "value": 5},
        "parse_dates": False,
    },
    3800567: {
        "columns": {"period": 0, "series_id": 4, "value": 6},
        "parse_dates": False,
    },
    36100096: {
        "columns": {"period": 0, "series_id": 11, "value": 13},
        "parse_dates": False,
    },
    36100303: {
        "columns": {"period": 0, "series_id": 9, "value": 11},
        "parse_dates": False,
    },
    36100305: {
        "columns": {"period": 0, "series_id": 9, "value": 11},
        "parse_dates": False,
    },
    36100236: {
        "columns": {"period": 0, "series_id": 11, "value": 13},
        "parse_dates": False,
    },
}


TO_PARSE_DATES = {
    k for k, v in STATCAN_SCHEMAS.items() if v.get("parse_dates")
}
