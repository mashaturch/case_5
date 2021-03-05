"""Case-study #5 Парсинг web-страниц
Разработчики:
Турчинович М. 50%, Зубарева Т. 40%, Костылев М. 40%
"""
import urllib.request

#opening file
with open ('input.txt') as f_in:
    with open ('output.txt', 'w') as f_out:
        for line in f_in:
            url = line
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str (s)
            part_name = text.find("nfl-c-player-header__title")
            name = text[text.find('>', part_name) + 1:text.find('</h1', part_name)]
            total = text.find('TOTAL')
            end_str = text.find('</tfoot>', total)
            str_1 = text[total: end_str]
            str_1 = str_1.replace('</th>', ' ')

            #counting comp index
            name_comp = '<th aria-label="passingCompletions" scope="col">'
            part_comp = str_1.find(name_comp) + len(name_comp) + 3
            while str_1[part_comp] != ' ':
                part_comp += 1
            comp = int(str_1[part_comp: str_1.find('n', part_comp) - 1])

            #counting att index
            name_att = '<th aria-label="passingAttempts" scope="col">'
            part_att = str_1.find(name_att) + len(name_att) + 3
            while str_1[part_att] != ' ':
                part_att += 1
            att = int(str_1[part_att: str_1.find('n', part_att) - 1])

            #counting yds index
            name_yds = '<th aria-label="passingYards" scope="col">'
            part_yds = str_1.find(name_yds) + len(name_yds) + 3
            while str_1[part_yds] != ' ':
                part_yds += 1
            yds = int(str_1[part_yds: str_1.find('n', part_yds) - 1])

            #counting td index
            name_td = '<th aria-label="passingTouchdowns" scope="col"'
            part_td = str_1.find(name_td) + len(name_td) + 3
            while str_1[part_td] != ' ':
                part_td += 1
            td = int(str_1[part_td: str_1.find('n', part_td) - 1])

            #counting int index
            name_int = '<th aria-label="passingInterceptions" scope="col">'
            part_int = str_1.find(name_int) + len(name_int) + 3
            while str_1[part_int] != ' ':
                part_int += 1
            int_1 = int(str_1[part_int: str_1.find('n', part_int) - 1])

            #counting passing rate index
            name_rate = '<th aria-label="passingPasserRating" scope="col">'
            part_rate = str_1.find(name_rate) + len(name_rate) + 3
            while str_1[part_rate] != ' ':
                part_rate += 1
            rate = float(str_1[part_rate: str_1.find('n', part_rate) - 1])
            print('{:<20s}{:<7d}{:<7d}{:<7d}{:<7d}{:<7d}{:<7.2f}'.format(name, comp, att, yds, td, int_1, rate), file = f_out)