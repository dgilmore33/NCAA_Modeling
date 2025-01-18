import pickle
import cbbpy.mens_scraper as s

def get_season(year : int, pbp : bool = False, output_path : str = "tmp_output.pkl"):
    pkl_result = s.get_games_season(season=year, pbp=pbp)
    with open(output_path, "wb") as out:
        pickle.dump(obj=pkl_result, file=out)