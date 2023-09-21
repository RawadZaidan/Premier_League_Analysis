from enum import Enum

class ErrorHandling(Enum):
    DB_CONNECT_ERROR = "DB Connect Error"
    DB_RETURN_QUERY_ERROR = "DB Return Query Error"
    API_ERROR = "Error calling API"
    RETURN_DATA_CSV_ERROR = "Error returning CSV"
    RETURN_DATA_EXCEL_ERROR = "Error returning Excel"
    RETURN_DATA_SQL_ERROR = "Error returning SQL"
    RETURN_DATA_UNDEFINED_ERROR = "Cannot find File type"
    EXECUTE_QUERY_ERROR = "Error executing the query"
    NO_ERROR = "No Errors"
    PREHOOK_SQL_ERROR = "Prehook: SQL Error"
    PREHOOK_CLOSE_CONNECTION_ERROR = "Error closing connection"
    HOOK_DICT_RETURN_ERROR = "Error returning lookup items as dict"
    DB_RETURN_INSERT_INTO_SQL_STMT_ERROR = "Return insert into sql dataframe error:"
    CSV_ERROR = "Error importing csv files from path"
    PANDAS_NULLS_ERROR = "Error dropping nulls from df"

class InputTypes(Enum):
    SQL = "SQL"
    CSV = "CSV"
    EXCEL = "Excel"
    
class PreHookSteps(Enum):
    EXECUTE_SQL_QUERY = "execute_sql_folder"
    CREATE_SQL_STAGING = "create_sql_staging_tables"

class SourceName(Enum):
    DVD_RENTAL = "public"
    COLLEGE = "college"

class SQLTablesToReplicate(Enum):
    RENTAL = "public.rental"
    FILM = "public.film"
    ACTOR = "public.actor"
    STUDENTS = "college.student"

class IncrementalField(Enum):
    RENTAL = "rental_last_update"
    FILM = "film_last_update"
    ACTOR = "actor_last_update"

class ETLStep(Enum):
    PRE_HOOK = 0
    HOOK = 1

class DESTINATION_SCHEMA(Enum):
    DESTINATION_NAME = "dw_reporting"

class SEASONS(Enum):
    S22_23 = [74910,74911]
    S21_22 = [75289,75290]

class URLS(Enum):
    Players = "https://drive.google.com/file/d/1I3iBSRKtiIZxHG2yAr9JuYqBNbeGIOlI/view?usp=drive_link"
    Player_Valuations = "https://drive.google.com/file/d/1Q1Dw7th4SxyR4OLQdo6M2tt6NRhYE7DE/view?usp=drive_link"
    Games = "https://drive.google.com/file/d/1wEj6Tli0RKy7WsH6PydeWTdZTYx6iNsw/view?usp=drive_link"
    Games_Events = "https://drive.google.com/file/d/1J-5WbdIHZy_hRQMOjlc5N55iUTE5NxMu/view?usp=drive_link"
    Competitions = "https://drive.google.com/file/d/1FdewVTkWwUxjyTGbKFRjNMigSiJxw3Nq/view?usp=drive_link"
    Clubs = "https://drive.google.com/file/d/1SD96aMVyrScGeUTSsCyd58mT9fjS5eFW/view?usp=drive_link"
    Club_Games = "https://drive.google.com/file/d/1CurzNh94a6mRroVWr2sjLFwl6xEjj1yE/view?usp=drive_link"
    Appearances = "https://drive.google.com/file/d/1nmK10IgDtTEIc1oC8zIt0w8aQDNleIKh/view?usp=drive_link"

