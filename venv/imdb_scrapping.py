from bs4 import BeautifulSoup
import requests
from xlwt import Workbook
from tkinter.filedialog import asksaveasfile

def main():
    movie_name = input("Enter the movie name : ")

    std_url = 'https://www.imdb.com/find?s=tt&q=' + movie_name + '&href_=nv_sr_sm'
    page = requests.get(std_url)
    data = page.content

    soup = BeautifulSoup(data , 'html5lib')

    movie_id = soup.select(".findList tr a")[0].get('href')
    movie_link = 'https://www.imdb.com' + movie_id

    movie_page = requests.get(movie_link)
    data2 = movie_page.content
    soup2 = BeautifulSoup(data2, 'html5lib')

    movie_title = soup2.select('.title_wrapper h1')[0].text
    movie_title = movie_title.strip()
    movie_name = movie_title[:-7]
    movie_year = movie_title[-5:-1]

    # print("Name  - {0}".format(movie_name))
    # print("Yaer Of Release Is - {0}".format(movie_year))


    movie_rating = soup2.select(".ratingValue span")[0].text

    # print("Rating  - {0}/10".format((movie_rating)))
    movie_time = soup2.select(".subtext time")[0].text.strip()

    # print("Movie time - {0}".format(movie_time))

    movie_genre = [i.text for i in soup2.select(".subtext a")][:-1]
    movie_genre = ', '.join(movie_genre)
    # print("Genre - {0}".format(movie_genre))

    movie_release_date = [i.text for i in soup2.select(".subtext a")][-1:][0][:-1]
    # print("Release date - {0}".format(movie_release_date))

    for i in soup2.findAll("div", "txt-block"):
        if i.h4:
            if i.h4.text == "Country:":
                movie_country = i.h4.next_sibling.next_element.text
                # print("Country - {0}".format(movie_country))

            if i.h4.text == "Language:":
                movie_language = ", ".join([k.string for k in i.findAll('a')])
                # print("Movie Languages - {0}".format(movie_language))

            if i.h4.text == "Budget:":
                movie_budget= i.h4.next_element.next_element.strip()
                # print("Budget - {0}".format(movie_budget))

            if i.h4.text == "Opening Weekend USA:":
                movie_opening = i.h4.next_element.next_element[:-2]
                # print("Opening Weekend USA - {0}".format(movie_opening))

            if i.h4.text == "Gross USA:":
                movie_gross = i.h4.next_element.next_element
                # print("Gross USA - {0}".format(movie_gross))

            if i.h4.text == "Cumulative Worldwide Gross:":
                movie_ww_gross = i.h4.next_element.next_element
                # print("Cumulative Worldwide Gross - {0}".format(movie_ww_gross))

            if i.h4.text == "Aspect Ratio:":
                movie_aspect = i.h4.next_element.next_element.strip()
                # print("Aspect Ratio - {0}".format(movie_aspect))

            if i.h4.text == "Taglines:":
                movie_tag1 = i.h4.next_element.next_element.strip()
                # print("Tagline - {0}".format(movie_tag1))

    for i in soup2.findAll("div", "credit_summary_item"):
        if i.h4:
            if i.h4.text == "Stars:":
                star_cast = ", ".join([k.string for k in i.findAll('a')])[:-22]
                # print("Stars - {0}".format(star_cast))

    Wb__obj = Workbook()
    my_sheet = Wb__obj.add_sheet('MOVIES')
    my_sheet.write(0, 0, movie_name)
    my_sheet.write(0, 1, movie_year)
    my_sheet.write(0, 2, movie_rating)
    my_sheet.write(0, 3, movie_time)
    my_sheet.write(0, 4, movie_genre)
    my_sheet.write(0, 5, movie_release_date)
    my_sheet.write(0, 6, movie_tag1)
    my_sheet.write(0, 7, movie_country)
    my_sheet.write(0, 8, movie_language)
    my_sheet.write(0, 9, movie_budget)
    my_sheet.write(0, 10, movie_opening)
    my_sheet.write(0, 11, movie_gross)
    my_sheet.write(0, 12, movie_ww_gross)
    my_sheet.write(0, 13, movie_aspect)
    my_sheet.write(0, 14, star_cast)

    f = asksaveasfile(mode='app', defaultextension='.csv')
    if f is not None:
        Wb__obj.save(f.name)
        f.close()

if __name__ == '__main__':
    main()
