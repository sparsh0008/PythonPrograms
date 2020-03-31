import sys
import requests
from bs4 import BeautifulSoup
import xlrd
from tkinter.filedialog import askopenfilename
from xlwt import Workbook
from tkinter.filedialog import asksaveasfile

def main():
    try:
        movie_list = []  # Create an empty list which will have list of movie names

        wb_write = Workbook()  # Instantiate Excel module to write data into excel file
        sheet1 = wb_write.add_sheet('IMDB_Details')

        sheet1.write(0, 0, 'Title')
        sheet1.write(0, 1, 'IMDB Rating')
        sheet1.write(0, 3, 'Length')
        sheet1.write(0, 4, 'Year')
        sheet1.write(0, 5, 'Genre')
        sheet1.write(0, 7, 'Release date')
        sheet1.write(0, 8, 'Rating')
        sheet1.write(0, 10, 'Star Cast')
        sheet1.write(0, 11, 'Country')
        sheet1.write(0, 13, 'Budget')
        sheet1.write(0, 15, 'Gross USA')
        sheet1.write(0, 16, 'Cumulative Worldwide Gross')
        sheet1.write(0, 17, 'Ratio')
        sheet1.write(0, 18, 'Taglines')

        filename = askopenfilename()  # Ask User to open excel file to read data
        wb = xlrd.open_workbook(filename)
        sheet = wb.sheet_by_index(0)

        counter = 1

        for i in range(sheet.nrows):
            if i == 0:
                continue
            movie_list.append(sheet.cell_value(i, 0))

        for movie in movie_list:

            std_url = 'https://www.imdb.com/find?s=tt&q=' + movie + '&href_=nv_sr_sm'
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
            print("Yaer Of Release Is - {0}".format(movie_year))


            movie_rating = soup2.select(".ratingValue span")[0].text

            print("Rating  - {0}/10".format((movie_rating)))
            movie_time = soup2.select(".subtext time")[0].text.strip()

            print("Movie time - {0}".format(movie_time))

            movie_genre = [i.text for i in soup2.select(".subtext a")][:-1]
            movie_genre = ', '.join(movie_genre)
            print("Genre - {0}".format(movie_genre))

            movie_release_date = [i.text for i in soup2.select(".subtext a")][-1:][0][:-1]
            print("Release date - {0}".format(movie_release_date))

            for i in soup2.findAll("div", "txt-block"):
                if i.h4:
                    if i.h4.text == "Country:":
                        movie_country = i.h4.next_sibling.next_element.text
                        print("Country - {0}".format(movie_country))

                    if i.h4.text == "Language:":
                        movie_language = ", ".join([k.string for k in i.findAll('a')])
                        print("Movie Languages - {0}".format(movie_language))

                    if i.h4.text == "Budget:":
                        movie_budget= i.h4.next_element.next_element.strip()
                        print("Budget - {0}".format(movie_budget))

                    if i.h4.text == "Opening Weekend USA:":
                        movie_opening = i.h4.next_element.next_element[:-2]
                        print("Opening Weekend USA - {0}".format(movie_opening))

                    if i.h4.text == "Gross USA:":
                        movie_gross = i.h4.next_element.next_element
                        print("Gross USA - {0}".format(movie_gross))

                    if i.h4.text == "Cumulative Worldwide Gross:":
                        movie_ww_gross = i.h4.next_element.next_element
                        print("Cumulative Worldwide Gross - {0}".format(movie_ww_gross))

                    if i.h4.text == "Aspect Ratio:":
                        movie_aspect = i.h4.next_element.next_element.strip()
                        print("Aspect Ratio - {0}".format(movie_aspect))

                    if i.h4.text == "Taglines:":
                        movie_tag1 = i.h4.next_element.next_element.strip()
                        print("Tagline - {0}".format(movie_tag1))

            for i in soup2.findAll("div", "credit_summary_item"):
                if i.h4:
                    if i.h4.text == "Stars:":
                        star_cast = ", ".join([k.string for k in i.findAll('a')])[:-22]
                        print("Stars - {0}".format(star_cast))

            details = [movie_title, movie_rating, movie_time, movie_year, movie_genre, movie_release_date, movie_rating
                     , star_cast, movie_country, movie_budget, movie_gross, movie_ww_gross, movie_aspect, movie_tag1]

            for desc, i in zip(details, range(len(details))):
                sheet1.write(counter, i, desc)

            counter = counter + 1

        f = asksaveasfile(mode='w', defaultextension=".csv")
        if f is not None:
            wb_write.save(f.name)
        f.close()

    except Exception as e:
        print("Error is: {0}".format(repr(e)))

if __name__ == '__main__':
    main()
