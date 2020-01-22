
import logging
import inspect
from bs4 import BeautifulSoup
import requests
from scrapy.selector import Selector
import json
import random
from scrapy.selector import Selector
import json
import pandas as pd
import re



# Create or get the logger
logging.basicConfig(filename='logfn.log', filemode='w', format='%(filename)s:%(lineno)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
# set log level
logger.setLevel(logging.INFO)


def get_movie_id(titleid):
    try:
        movie_id = titleid
        return {'Movie_id': movie_id}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


def get_recommended_movie(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        for movie in soup.find_all("div", {"class": "title_wrapper"}):
            mv = movie.h1.get_text()
            mv_strip = mv[:-7]
        rating = soup.find("span", {"itemprop": "ratingValue"}).get_text()
        year = soup.find('span', {'id': 'titleYear'}).get_text()
        release_year = year[1:5]
        return {'Movie': mv_strip, 'Rating': rating, 'Year': release_year}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)

def get_imdb_meta(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        meta_page = requests.get(url)
        soup = BeautifulSoup(meta_page.text, 'html.parser')
        meta = soup.find_all("div", {"class": "credit_summary_item"})
        metas = {}
        for m in meta:
            values = []
            name_ids = []
            for a in m.find_all('a'):
                name_id = a['href'].strip('/')[5:]
                name_ids.append(name_id)
            value = ", ".join(name_ids)
            meta_text = m.find("h4").get_text()
            if 'Director' in meta_text or 'Writers' in meta_text or 'Stars:' in meta_text:
                metas[meta_text] = value
        return metas
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)

def imdb_similarmovie_title(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        poster = soup.find_all("div", {"class": "rec-title"})

        pos_value = []
        for post in poster:
            plot_text = post.find('a').get_text()
            pos_value.append(plot_text)

        return {'SimilarMovieTitle': pos_value}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)

def get_similar_movies_id(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        poster_id = soup.find_all("div", {"class": "rec-title"})
        pos_id = []
        for post in poster_id:
            title_id_list = post.find('a').get("href")
            post_title_id_list = title_id_list.replace("/title/", "").replace("/", "")
            pos_id.append(post_title_id_list)
        return {'SimilarMovies_id': pos_id}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


def get_imdb_similarmovie_path(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        poster_path = soup.find("div", {"class": "poster"}).img["src"]
        return {'SimilarMovie Path': poster_path}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


def get_imdb_duration(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        duration = soup.find("div", {"class": "subtext"}).time.get_text()
        time = duration.strip()
        return {'Duration': time}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


def get_imdb_budget(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        html_doc = requests.get(url)
        sel = Selector(html_doc)
        budget = ' '.join(sel.css(".txt-block:contains('Budget')::text").extract()).strip()
        return {'Budget': budget}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


# Opening Weekend USA
def get_imdb_weekend(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        html_doc = requests.get(url)
        sel = Selector(html_doc)
        opening_weekend = ' '.join(sel.css(".txt-block:contains('Opening Weekend USA')::text").extract()).strip()
        return {'Opening Weekend USA': opening_weekend}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


# Gross USA
def get_imdb_gross(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        html_doc = requests.get(url)
        sel = Selector(html_doc)
        opening_weekend = ' '.join(sel.css(".txt-block:contains('Gross USA')::text").extract()).strip()
        return {'Gross USA': opening_weekend}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


# Cumulative Worldwide Gross
def get_imdb_cumulativegross(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        html_doc = requests.get(url)
        sel = Selector(html_doc)
        cumulative_gross = ' '.join(sel.css(".txt-block:contains('Opening Weekend USA')::text").extract()).strip()
        return {'Cumulative Worldwide Gross': cumulative_gross}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)



def get_imdb_released_date(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        html_doc = requests.get(url)
        sel = Selector(html_doc)
        release_date = ' '.join(sel.css(".txt-block:contains('Release Date:')::text").extract()).strip()
        strip_date = re.sub("[\(\[].*?[\)\]]", "", release_date)
        return {'Release Date': strip_date}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)
def get_imdb_cast(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        cast_page = requests.get(url)
        soup = BeautifulSoup(cast_page.text, 'html.parser')
        cast_list = soup.find("table", {"class": "cast_list"})

        key_app = []
        value_app = []
        for idx, row in enumerate(cast_list.find_all("tr"), start=0):
            if idx != 0:
                if len(row.find_all("td")) == 4:
                    key = row.select_one("td:nth-child(2)")
                    value = row.select_one("td:nth-child(4)")
                    if key.find("a") is None:
                        v_key = key.get_text()
                    else:
                        v_key = key.find("a").get_text()
                        key_strip = v_key.strip()
                        key_app.append(key_strip)
                    if value.find("a") is None:
                        v_value = value.get_text()
                    else:
                        v_value = value.find("a").get_text()
                        value_app.append(v_value)
        return {'Cast': key_app,'Stars':value_app}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)

def get_imdb_summary(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        movie_page = requests.get(url)
        soup = BeautifulSoup(movie_page.text, 'html.parser')
        summery = soup.find("div", {"class": "summary_text"}).get_text().strip()
        return {'Summery': summery}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


def get_imdb_lang_country_alsoknownas(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        widgets = soup.find("div", {"id": "titleDetails"})
        widget = widgets.find_all("div", {"class": "txt-block"})
        cl_title = {}
        also_known = {}
        for w in widget:
            title = w.find('h4')
            if title:
                title_text = title.get_text()
                titles = title_text.replace(":", "")

                if 'Country' in titles or 'Language' in titles:
                    all_values = []
                    values = w.find_all('a')
                    for v in values:
                        all_values.append(v.get_text().strip())
                    #value = ','.join(all_values)
                    cl_title[titles] = all_values

                if 'Also Known As' in titles:
                    see_all_a = w.find_all('a')
                    for a in see_all_a:
                        if 'See more' in a.get_text():
                            a_link = a.get("href")
                            # print(a_link)

                            html_doc_all = requests.get(url + a_link)
                            if html_doc_all.status_code == 200:
                                soup_all = BeautifulSoup(html_doc_all.content, 'html.parser')
                                table = soup_all.find("table", {
                                    "class": "ipl-zebra-list ipl-zebra-list--fixed-first release-dates-table-test-only"})
                                t_value = []
                                for tr in table.find_all("tr", {"class": "ipl-zebra-list__item release-date-item"}):
                                    # t_value = []
                                    trs = tr.get_text().strip()
                                    trs_split = " ".join(trs.split())
                                    # print(trs_split)
                                    t_value.append(trs_split)
                                also_known[titles] = t_value
                    lang_dict = {**cl_title, **also_known}

        return lang_dict
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)



def imdb_plotkeyword(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        site = 'https://www.imdb.com'
        see_more = soup.select('.see-more.inline.canwrap')
        for see in see_more:
            see_title = see.find('h4').get_text()
            if 'Plot Keywords' in see_title:
                see_all_a = see.find_all('a')
                for a in see_all_a:
                    if 'See All' in a.get_text():
                        a_link = a.get("href")
                        html_doc_plot = requests.get(site + a_link)
                        if html_doc_plot.status_code == 200:
                            soup_plot = BeautifulSoup(html_doc_plot.content, 'html.parser')
                            plots = soup_plot.select('.sodatext')
                            # print(plots)
                            plots_all = []
                            for plotblock in plots:
                                plot_text = plotblock.find('a').get_text()
                                plots_all.append(plot_text)
                            return {'Plots': plots_all}
    except:
            pass

def get_award_detail(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid + '/awards'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        awards = []
        level1 = soup.select('.article.listo > h3')  # main headings
        for level1_head in level1:
            award = {}
            heading = level1_head.text.strip().replace('\n ', ' - ')  # replace spaces in heading
            table = level1_head.find_next_sibling("table")
            level2 = table.select('.title_award_outcome')  # nominee
            award.update({'award': heading})

            prev_tds = 0
            for idx, level2_head in enumerate(level2, start=1):
                level2_count = int(level2_head.get('rowspan'))
                # level2_head_text = level2_head.find('b').text + ' - ' + level2_head.find('span').text
                award_type = level2_head.find('b').text.strip().lower()  # change to lowercase
                award1_type = level2_head.find('span').text.strip().lower()
                join_award_type = award_type + ' - ' + award1_type
                tds = [desc.text.strip().replace('\n', ' - ') for desc in table.select('.award_description')]
                if len(level2) == idx:
                    award.update({join_award_type: tds[prev_tds:]})
                else:
                    award.update({join_award_type: tds[prev_tds:level2_count]})
                prev_tds += level2_count
            awards.append(award)
        return {'FilmAwards':  awards}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str(e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)


def imdb_film_location(titleid):
    try:
        url = 'https://www.imdb.com/title/' + titleid
        page = requests.get(url)
        film_soup = BeautifulSoup(page.text, 'html.parser')
        film = film_soup.select('.txt-block')
        for f in film:
            film_title = f.find('h4')
            if film_title:
                title_text = film_title.get_text()
                if 'Filming Locations' in title_text:
                    see_more = f.find_all('a')
                    for a in see_more:
                        if 'See more' in a:
                            a_link = a.get("href")
                            # print(a_link)

                            html_doc = requests.get(url + a_link)
                            film1_soup = BeautifulSoup(html_doc.content, 'html.parser')
                            #film_soup = soup.find("section", {"id": "filming_locations"})
                            film_title = film1_soup.find_all("dt")
                            f_value = []
                            for film_a in film_title:
                                film_text = film_a.a.text
                                fdt = film_text.strip()
                                f_value.append(fdt)
                            return {'Film Locations': f_value}
    except Exception as e:
        frame = inspect.currentframe()
        (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)
        out = inspect.getframeinfo(frame)
        logger.error("Exception occurred || Title id: " + str(titleid) + " || Error :" + str( e) + " || Function : " + function_name + " || File: " + filename, exc_info=False)

def main():
    jstr = []
    i = 0
    df=pd.read_csv("titleid.csv")
    df_to_list=df['tconst'].tolist()
    title_id_list = df_to_list[:3]

    for titleid in title_id_list:
        movie_id = get_movie_id(titleid)
        movie_detail = get_recommended_movie(titleid)
        imdb_meta = get_imdb_meta(titleid)
        imdb_similar_movie_title = imdb_similarmovie_title(titleid)
        imdb_similar_movie_id = get_similar_movies_id(titleid)
        imdb_poster_path = get_imdb_similarmovie_path(titleid)
        imdb_duration = get_imdb_duration(titleid)
        imdb_budget = get_imdb_budget(titleid)
        imdb_weekend = get_imdb_weekend(titleid)
        imdb_gross = get_imdb_gross(titleid)
        imdb_cumulative_gross = get_imdb_cumulativegross(titleid)
        imdb_releasedate = get_imdb_released_date(titleid)
        imdb_cast = get_imdb_cast(titleid)
        imdb_summary = get_imdb_summary(titleid)
        imdb_lang_country = get_imdb_lang_country_alsoknownas(titleid)
        imdb_plot = imdb_plotkeyword(titleid)
        imdb_awards = get_award_detail(titleid)
        film_location = imdb_film_location(titleid)
        if film_location is None:
            film_location = {}


        dict1 = {}
        dict1.update(movie_id)
        dict1.update(movie_detail)
        dict1.update(imdb_meta)
        dict1.update(imdb_similar_movie_title)
        dict1.update(imdb_similar_movie_id)
        dict1.update(imdb_poster_path)
        dict1.update(imdb_duration)
        dict1.update(imdb_budget)
        dict1.update(imdb_weekend)
        dict1.update(imdb_gross)
        dict1.update(imdb_cumulative_gross)
        dict1.update(imdb_releasedate)
        dict1.update(imdb_cast)
        dict1.update(imdb_summary)
        dict1.update(imdb_lang_country)
        dict1.update(imdb_plot)
        dict1.update(imdb_awards)
        dict1.update(film_location)
        jstr.insert(i, dict1)
        i = i + 1
    with open('imdbmovie_file.json', 'a') as outfile:
        json.dump(jstr, outfile)

if __name__ == "__main__":
        main()



#award_detail = get_imdb_cast(titleid)
#print(award_detail)