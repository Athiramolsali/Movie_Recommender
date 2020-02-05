# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:52:19 2020

@author: Athira
"""

import json
import requests
api_key_counter = 0
error_status = False
tv_series_id = '1396'
language = 'en-US'

with open('config.json') as json_file:
    config = json.load(json_file)
    
    api_keys = config["api_keys"]
    language = config["language"]
    tmdb_tv_series_base_url = config["tmdb_tv_series_base_url"]
    tmdb_person_base_url = config["tmdb_person_base_url"]
    

def get_random_api_key():
    # calls the global variable in the function
    global api_keys
    global api_key_counter
    api_key = api_keys[api_key_counter]
    api_key_counter += 1
    if api_key_counter == len(api_keys):
        api_key_counter = 0
    return api_key


    
'''
Place holder for def tmdb_movie function equivalent in jomys code

'''

    
def get_details_tmdb_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_tv_series_url =  tmdb_tv_series_base_url + tv_series_id+ '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_tv_series_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_credits_tv_series(tv_series_id,language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_credits_url =  tmdb_tv_series_base_url + tv_series_id+ '/credits' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_credits_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None
    
def get_keywords_tv_series(tv_series_id, language):
    try:
        tv_series={}
        api_key = get_random_api_key()
        tmdb_keywords_url = tmdb_tv_series_base_url + tv_series_id+ '/keywords' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_keywords_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None
        
def get_recommendations_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_recommendations_url =  tmdb_tv_series_base_url + tv_series_id+ '/recommendations' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_recommendations_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_similar_tv_shows_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_similar_tv_shows_url =  tmdb_tv_series_base_url + tv_series_id+ '/similar' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_similar_tv_shows_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None
    
def get_images_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_images_url =  tmdb_tv_series_base_url + tv_series_id+ '/images' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_images_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_content_ratings_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_content_ratings_url =  tmdb_tv_series_base_url + tv_series_id+ '/content_ratings' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_content_ratings_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_reviews_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_reviews_url =  tmdb_tv_series_base_url + tv_series_id+ '/reviews' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_reviews_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_translations_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_translations_url =  tmdb_tv_series_base_url + tv_series_id+ '/translations' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_translations_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_videos_tv_series(tv_series_id, language):
    try:
        tv_series = {}
        api_key = get_random_api_key()
        tmdb_videos_url =  tmdb_tv_series_base_url + tv_series_id+ '/videos' + '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_videos_url)
        data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None    
    
    
def get_details_tv_seasons(tv_series_id, language):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        n_seasons = series_obj['number_of_seasons']
        for j in range(n_seasons):
            api_key = get_random_api_key()
            tmdb_season_url =  tmdb_tv_series_base_url + tv_series_id+ '/season/'+ str(j+1) + '?api_key=' + api_key + '&language=' + language
            response = requests.request("GET", tmdb_season_url)
            data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None
    
def get_credits_tv_seasons(tv_series_id, language):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        n_seasons = series_obj['number_of_seasons']
        for j in range(n_seasons):
            api_key = get_random_api_key()
            tmdb_credits_tv_seasons_url =  tmdb_tv_series_base_url + tv_series_id + '/season/'+ str(j+1)+'/credits'+ '?api_key=' + api_key + '&language=' + language
            response = requests.request("GET", tmdb_credits_tv_seasons_url)
            data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None
    
def get_images_tv_seasons(tv_series_id, language):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        n_seasons = series_obj['number_of_seasons']
        for j in range(n_seasons):
            api_key = get_random_api_key()
            tmdb_credits_tv_seasons_url =  tmdb_tv_series_base_url + tv_series_id + '/season/'+ str(j+1)+'/images'+ '?api_key=' + api_key + '&language=' + language
            response = requests.request("GET", tmdb_credits_tv_seasons_url)
            data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_videos_tv_seasons(tv_series_id, language):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        n_seasons = series_obj['number_of_seasons']
        for j in range(n_seasons):
            api_key = get_random_api_key()
            tmdb_credits_tv_seasons_url =  tmdb_tv_series_base_url + tv_series_id + '/season/'+ str(j+1)+'/videos'+ '?api_key=' + api_key + '&language=' + language
            response = requests.request("GET", tmdb_credits_tv_seasons_url)
            data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_tv_episodes_details(tv_series_id,season):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        api_key = get_random_api_key()
        tmdb_tv_series_url =  tmdb_tv_series_base_url + tv_series_id+ '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_tv_series_url)
        data = response.json()
        data["seasons"] =[dict(episode_count=k1["episode_count"]) for k1 in data["seasons"]]
        jsonData = json.dumps(data)
        resp = json.loads(jsonData)
        n_seasons = series_obj['number_of_seasons']
        for i in range(0,n_seasons+1):
            season = i
            no_of_episodes = resp['seasons'][season]['episode_count']
            for j in range(1,no_of_episodes+1):
                tmdb_episodes_url =  tmdb_tv_series_base_url + tv_series_id + '/season/'+ str(season) +'/episode/'+str(j)+ '?api_key=' + api_key + '&language=' + language
                response = requests.request("GET", tmdb_episodes_url)
                data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_credits_tv_episodes(tv_series_id,season):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        api_key = get_random_api_key()
        tmdb_tv_series_url =  tmdb_tv_series_base_url + tv_series_id+ '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_tv_series_url)
        data = response.json()
        data["seasons"] =[dict(episode_count=k1["episode_count"]) for k1 in data["seasons"]]
        jsonData = json.dumps(data)
        resp = json.loads(jsonData)
        n_seasons = series_obj['number_of_seasons']
        for i in range(0,n_seasons+1):
            season = i
            no_of_episodes = resp['seasons'][season]['episode_count']
            for j in range(1,no_of_episodes+1):
                tmdb_episodes_url =  tmdb_tv_series_base_url + tv_series_id + '/season/'+ str(season) +'/episode/'+ str(j)+'/credits' +'?api_key=' + api_key + '&language=' + language
                response = requests.request("GET", tmdb_episodes_url)
                data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_images_tv_episodes(tv_series_id,season):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        api_key = get_random_api_key()
        tmdb_tv_series_url =  tmdb_tv_series_base_url + tv_series_id+ '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_tv_series_url)
        data = response.json()
        data["seasons"] =[dict(episode_count=k1["episode_count"]) for k1 in data["seasons"]]
        jsonData = json.dumps(data)
        resp = json.loads(jsonData)
        n_seasons = series_obj['number_of_seasons']
        for i in range(0,n_seasons+1):
            season = i
            no_of_episodes = resp['seasons'][season]['episode_count']
            for j in range(1,no_of_episodes+1):
                tmdb_episodes_url =  tmdb_tv_series_base_url + tv_series_id + '/season/'+ str(season) +'/episode/'+ str(j)+'/images' +'?api_key=' + api_key + '&language=' + language
                response = requests.request("GET", tmdb_episodes_url)
                data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def get_videos_tv_episodes(tv_series_id,season):
    try:
        tv_series = {}
        series_obj = get_details_tmdb_tv_series(tv_series_id, language)
        api_key = get_random_api_key()
        tmdb_tv_series_url =  tmdb_tv_series_base_url + tv_series_id+ '?api_key=' + api_key + '&language=' + language
        response = requests.request("GET", tmdb_tv_series_url)
        data = response.json()
        data["seasons"] =[dict(episode_count=k1["episode_count"]) for k1 in data["seasons"]]
        jsonData = json.dumps(data)
        resp = json.loads(jsonData)
        n_seasons = series_obj['number_of_seasons']
        for i in range(0,n_seasons+1):
            season = i
            no_of_episodes = resp['seasons'][season]['episode_count']
            for j in range(1,no_of_episodes+1):
                tmdb_episodes_url =  tmdb_tv_series_base_url + tv_series_id + '/season/'+ str(season) +'/episode/'+ str(j)+'/videos' +'?api_key=' + api_key + '&language=' + language
                response = requests.request("GET", tmdb_episodes_url)
                data = response.json()
        return(data)
    except Exception as e:
        global error_status
        error_status = True
        print("Function : get_details_tmdb_movie, Movie id: " + tv_series_id +  "\n Error : " + str(e)  )
        print("Tv_series: " + tv_series)
        return None, None

def main():
    
    tmdb_tv_series_details = get_details_tmdb_tv_series(tv_series_id,language)
    tmdb_credits_tv_series = get_credits_tv_series(tv_series_id,language)
    tmdb_keywords_tv_series  = get_keywords_tv_series(tv_series_id, language)
    tmdb_recommendations_tv_series  = get_recommendations_tv_series(tv_series_id, language)
    tmdb_similar_tv_shows_tv_series  = get_similar_tv_shows_tv_series(tv_series_id, language)
    tmdb_images_tv_series  = get_images_tv_series(tv_series_id, language)
    tmdb_content_rating_tv_series = get_content_ratings_tv_series(tv_series_id, language)
    tmdb_reviews_tv_series = get_reviews_tv_series(tv_series_id, language)
    tmdb_translation_tv_series = get_translations_tv_series(tv_series_id, language)
    tmdb_videos_tv_series = get_videos_tv_series(tv_series_id, language)
    tmdb_details_tv_seasons = get_details_tv_seasons(tv_series_id, language)
    tmdb_credicts_tv_seasons = get_credits_tv_seasons(tv_series_id, language)
    tmdb_images_tv_seasons = get_images_tv_seasons(tv_series_id, language)
    tmdb_videos_tv_seasons = get_videos_tv_seasons(tv_series_id, language)
    tmdb_tv_episodes_details =  get_tv_episodes_details(tv_series_id,season)
    tmdb_credits_tv_episodes = get_credits_tv_episodes(tv_series_id,season)
    tmdb_images_tv_episodes = get_images_tv_episodes(tv_series_id,season)
    tmdb_video_tv_episodes_details = get_videos_tv_episodes(tv_series_id,season)
    dict1 = {}
    dict1.update(tmdb_tv_series_details)
    dict1.update(tmdb_credits_tv_series)
    dict1.update(tmdb_keywords_tv_series)
    dict1.update(tmdb_recommendations_tv_series)
    dict1.update(tmdb_similar_tv_shows_tv_series)
    dict1.update(tmdb_images_tv_series)
    dict1.update(tmdb_content_rating_tv_series)
    dict1.update(tmdb_reviews_tv_series)
    dict1.update(tmdb_translation_tv_series)
    dict1.update(tmdb_videos_tv_series)
    dict1.update(tmdb_details_tv_seasons)
    dict1.update(tmdb_credicts_tv_seasons)
    dict1.update(tmdb_images_tv_seasons)
    dict1.update(tmdb_videos_tv_seasons)
    dict1.update(tmdb_tv_episodes_details)
    dict1.update(tmdb_credits_tv_episodes)
    dict1.update(tmdb_images_tv_episodes)
    dict1.update(tmdb_video_tv_episodes_details)

    with open('tmdbseries.json', 'a') as outfile:
        json.dump(dict1, outfile)

if __name__ == "__main__":
        main()
