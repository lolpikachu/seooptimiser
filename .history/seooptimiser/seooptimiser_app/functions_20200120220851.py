import requests
from bs4 import BeautifulSoup
import time
import re
import random
from random import shuffle
links = []
keywords = []
def seooptimiser(x, y):

    links.append(x)
    keywords.append(y)
    #-------------------------------Sentence for append------------------------------------
    #===============================Intro phrase list=====================================
    introductory_phrase_1 = [
    ' Само собой разумеется, ',
    ' Можно заметить, что тренды меняются и ',
    ' Хотя на практике оказывается, что заполучить желаемое не так просто и ',
    ' Вместе с тем ',
    ' В дополнение к сказанному, ',
    ' Опять-таки, ',
    ' Должно быть',
    ' Если позволите',
    ' Если угодно',
    ' Знаете ли',
    ' Естественно',
    ' Знаете'
    ]

    introductory_phrase_2 = [
    ' Не нужно долго доказывать, что',
    ' Нет необходимости доказывать, что',
    ' Очевидно, что',
    ' Нет сомнений, что',
    ' Без всякого сомнения,',
    ' Без сомнения,',
    ' Бесспорно,',
    ' Несомненно,',
    ' Ясно,',
    ' Истинно,',
    ' Известная вещь,',
    ' Наверняка,' 
    ]

    introductory_phrase_3 = [
    ' Могу подтвердить из личного опыта, что',
    ' Замечу,',
    ' Кстати,',
    ' Замечу из  личного опыта, что',
    ' Могу подтвердить из личной практики, что',
    ' Замечу попутно,',
    ' Кстати сказать,',
    ' Кстати замечу,',
    ' К слову сказать,',
    ' Между прочим,',
    ' Попутно замечу, что',
    ' На заметку,'
    ]

    introductory_phrase_4 = [
    ' Итак, в большинстве случаев',
    ' Между тем, ',
    ' Вопреки всему, ',
    ' Вдобавок ко всему прочему,',
    ' В конце концов,',
    ' В общем,',
    ' В общем-то,',
    ' Во всяком случае,',
    ' Вообще,',
    ' Вообще говоря,',
    ' Вообще-то,',
    ' В принципе,'
    ]

    introductory_phrase_5 = [
    ' К слову,',
    ' Кстати говоря,',
    ' Попутно замечу,',
    ' Могу подтвердить из личного опыта,',
    ' Из собственных наблюдений замечу,',
    ' Хотелось бы заметить,',
    ' Пожалуй, кратко упомяну,',
    ' Помните,',
    ' Впрочем,',
    ' В самом деле,',
    ' В сущности,',
    ' В сущности говоря,'
    ]

    introductory_phrase_6 = [
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...',
    ' Тематика "egg"...'
    ]

    #===============================Main phrase list=====================================     
    main_phrase_1 = [
    ' тема "egg" требует тщательно продуманного подхода.',
    ' в вопросе "egg" лучше соблюдать инструкцию.',
    ' тема "egg" — может быть сложный вопрос. Но это дело навыка.',
    ' тема "egg" — может быть крепкий не раскалывающийся орех. Но это дело практики.',
    ' инструкция под названием "egg" может отличаться от сегодняшней.',
    ' в будущем, методы в теме "egg" могут отличаться.',
    ' в будущем, способы в теме "egg" могут отличаться.',
    ' в будущем, инструкции в теме "egg" могут отличаться.',
    ' в будущем, принципы в теме "egg" могут отличаться.',
    ' методы в теме "egg" могут отличаться.',
    ' способы в теме "egg" могут отличаться.',
    ' инструкции в теме "egg" могут отличаться.'
    ]

    main_phrase_2 = [
    ' монолог под названием "egg" можно превратить в пространный, но не сегодня.  ',
    ' стиль изложения на тему "egg" мог бы быть научным, но я предпочел просто поговорить.',
    ' полемика "egg" может разжечь желательный спор.',
    ' но спокойная беседа мне больше по душе.',
    ' ответ на практический вопрос "egg" не всегда будет иметь одинаковую основу.',
    ' посетив даже семинарские занятия на тему "egg", экспертом не станешь, так как во многом успех зависит от текущей ситуации.',
    ' открыв последнюю, казалось бы, главу в теме "egg" и выучив все, на практике эти знания не всегда работают.',
    ' только многолетний опыт позволяет мне авторитетно оценить многие вопросы в теме "egg".',
    ' долгая практика позволяет мне авторитетно оценить многие моменты в данной теме "egg".',
    ' материал "egg" может быть охарактеризован по-разному.',
    ' материал "egg" может иметь различные отправные точки.',
    ' у каждого автора материал "egg" имеет легкие отличия.',
    ' у каждого автора материал "egg" описывается различными свойствами.'
    ]

    main_phrase_3 = [
    ' egg — достаточно интересная тема в разговоре.',
    ' egg — популярная тема в разговорах.',
    ' egg — это задача, требующая грамотного подхода.',
    ' egg — достаточно интересная тема для разговора.',
    ' egg — популярная тема для разговора.',
    ' egg — это задача, требующая практического решения.',
    ' egg — достаточно популярная тема.',
    ' egg — достаточно популярный и интересный вопрос.',
    ' egg — это популярная тема.',
    ' egg — это задача, требующая практического подхода.',
    ' egg — это интересный вопрос.',
    ' egg — это интересная тема.'
    ]

    main_phrase_4 = [
    ' изучить принцип "egg" — это всегда безопасный ход.',
    ' изучить принцип "egg" — это всегда стабильный ход.',
    ' изучить принцип "egg" — это всегда надежный ход.',
    ' лучше изучить принцип "egg" сразу.',
    ' изучив принцип "egg", вы перейдете на новый уровень понимания.',
    ' толковые  мысли по теме "egg" приносят гарантированный результат.',
    ' теме "egg" нужно уделить немного времени.',
    ' принципы "egg" не нечто неясное.',
    ' принципы "egg" не вызывают сомнения.',
    ' принципы "egg" не нечто неясное.',
    ' изучить принцип "egg" — целесообразно.',
    ' ознакомиться с принципами "egg" — компетентный ход.'
    ]

    main_phrase_5 = [
    ' если "egg" важная тема для Вас, мой читатель, прошу взять во внимание, что мои  статьи подкреплены личным опытом.',
    ' если "egg" многозначный разговор для Вас, возьмите во внимание, все мои слова базируются на личной практике.',
    ' если "egg" значимый вопрос в Вашем вопроснике, информация в данной статье взята из собственных наблюдений.',
    ' "egg"  — это не самая легкая тема для изучения. ',
    ' "egg"  — это не самая простая тема. ',
    ' если "egg" важный разговор для Вас, возьмите во внимание, вся информация в этой статье взята из личной практики.',
    ' тема "egg"  может быть проблемой. ',
    ' тема "egg"  может выдаться проблемой. ',
    ' "egg"  — это не сложная область знания. ',
    ' "egg"  — это не сложно, но подводные камни быть могут. ',
    ' в принципах "egg"  нет риторических вопросов. ',
    ' в принципах "egg"  нет риторических ответов. '
    ]

    main_phrase_6 = [
    ' Здесь импровизация не всегда хороший вариант.',
    ' Импровизация в данном случае не всегда хороший вариант.',
    ' Импровизация в данном вопросе не всегда хороший вариант.',
    ' Уж точно не буду советовать импровизировать на практике. Здесь лучше узнать все и подготовиться. ',
    ' Не бойтесь нестандартных ситуаций и чаще импровизируйте!', 
    ' Мы уверены, у вас все получится!',
    ' Многолетний опыт Вам точно не понадобится.',
    ' Бдительности терять не следует.',
    ' Лучше не на голодный желудок.',
    ' Многолетний опыт Вам точно не понадобится.',
    ' Подойдите с ответственностью.',
    ' Не откладывайте надолго, если уж взялись.'
    ]

    #-------------------------------Sentences multiplier------------------------------------
    def sentence_complete(intro_phrase_lst, main_phrase_lst, complete_sentence_lst):
        for intro_phrase in intro_phrase_lst:
            for main_phrase in main_phrase_lst:
                complete_sentence_lst.append(intro_phrase + main_phrase)
        return

    complete_sentence_1 = []
    complete_sentence_2 = []
    complete_sentence_3 = []
    complete_sentence_4 = []
    complete_sentence_5 = []
    complete_sentence_6 = []    

    sentence_complete(introductory_phrase_1, main_phrase_1, complete_sentence_1)
    sentence_complete(introductory_phrase_2, main_phrase_2, complete_sentence_2)
    sentence_complete(introductory_phrase_3, main_phrase_3, complete_sentence_3)
    sentence_complete(introductory_phrase_4, main_phrase_4, complete_sentence_4)
    sentence_complete(introductory_phrase_5, main_phrase_5, complete_sentence_5)
    sentence_complete(introductory_phrase_6, main_phrase_6, complete_sentence_6)
    #-------------------------------Alt sentences------------------------------------
    alt_sentences = [
    'egg 2020',
    'egg: Советы',
    'egg: Инструкция',
    'egg: Хитрости',
    'egg: Советы 2020',
    'egg: Инструкция 2020',
    'egg: Хитрости 2020',
    'egg: Лучшее в 2020',
    'egg: Советы в 2020',
    'egg: Инструкция в 2020',
    'egg: Хитрости в 2020',
    'egg: Отзывы',
    'egg: Проверено',
    'Способы: egg',
    'Исследование: egg',
    'Компромиссы: egg',
    'Привелегии: egg',
    'Одобрено: egg',
    'Факты: egg',
    'Эффекты: egg',
    'Практика: egg',
    'на Практике: egg',
    'Опыт: egg',
    'Эксперимент: egg',
    'Эксперименты: egg',
    'Отзывы 2020: egg',
    'Проверено 2020: egg',
    'Способы 2020: egg',
    'Исследование 2020: egg',
    'Компромиссы 2020: egg',
    'Привелегии 2020: egg',
    'Одобрено 2020: egg',
    'Факты 2020: egg',
    'Эффекты 2020: egg',
    'Практика 2020: egg',
    'на Практике 2020: egg',
    'Опыт 2020: egg',
    'Эксперимент 2020: egg',
    'Эксперименты 2020: egg'
    ]

    #-------------------------------Meta sentences------------------------------------
    meta_sentences = [
    ' Информация, которую на тренингах вам продадут за десятки тысяч рублей. ',
    ' Вся необходимая информация за 2 минуты. ',
    ' Детальные советы и секретные приемы.',
    ' Информация от ведущих экспертов в нише.',
    ' Что вы не знали и что не узнаете больше нигде. ',
    ' Рассказываю тайны производства из личного опыта.',
    ' Тайные ходы, приманки, приемы.',
    ' Детальный план действий для прибыли. ',
    ' Что вам не рассказывали и чего не расскажут.',
    ' Секреты, которые вам не рассказывали и не расскажут.',
    ' Собрали всю необходимую информацию на 2020 год. ',
    ' Собрали все данные на 2020 год.',
    ' Полный пакет материала по теме. ',
    ' Вы станете экспертом после пятого слова этой статьи.',
    ' Советы на 2020 год.',
    ' Все самое важное о тематике и малоизвестных способах заработка.',
    ' Вы должны учесть эти важные аспекты.',
    ' Все необходимые сведения на 2020.',
    ' Станьте экспертом за 3 минуты прочитав эту статью.',
    ' Начните зарабатывать прямо сейчас.',
    ' Зарабатывайте с этой минуты зная все тайны ниши.',
    ' Станьте экспертом за 1 минуту прочитав эту статью.',
    ' Вы станете профессионалом прочитав эту статью.',
    ' Станьте профессионалом прочитав эту статью.',
    ' Прибыльные схемы на 2020 год.',
    ' egg — секреты индустрии. ',
    ' egg — стоит ли, нужно ли, чего лучше не делать. ',
    ' egg в общих чертах и подробно о нише.',
    ' egg — малоизвестные методы.',
    ' egg — чего вы не знали.',
    ' egg и не только.',
    ' egg — о чем вы не слышали и не догадывались.',
    ' egg — секретные материалы.',
    ' egg  — главное кратко.',
    ' egg — работающие методы.',
    ' egg — с чего начать и чем закончить.'
    ]

    #-------------------------------Videos------------------------------------
    videos = [
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/NoljxOs4Au0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>', 
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/JuAo6r-vqjs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/qu9jpcUUPIM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/Km-NT6vQccA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/NoljxOs4Au0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>', 
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/JuAo6r-vqjs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/qu9jpcUUPIM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/Km-NT6vQccA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/NoljxOs4Au0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>', 
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/JuAo6r-vqjs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/qu9jpcUUPIM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>',
    '<p><iframe width="560" height="315" src="https://www.youtube.com/embed/Km-NT6vQccA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>'
    ]

    def enumerate(iterable, start = 1):
        n = start
        for i in iterable:
            yield str(n) + '.   ' + str(i)
            n += 1 

    #---------------------Link iteration------------------------
    # for link, key, h1, title, sentence_append, meta, video in zip(links, keywords, h1_list, titles_list, sentences, meta_sentences, videos):
    for link, key, meta, video in zip(links, keywords, meta_sentences, videos):
    #---------------------Sentences for append generator------------------------ 
        sentences = []
        s_1 = random.choice(complete_sentence_1)
        s_2 = random.choice(complete_sentence_2)
        s_3 = random.choice(complete_sentence_3)
        s_4 = random.choice(complete_sentence_4)
        s_5 = random.choice(complete_sentence_5)
        s_6 = random.choice(complete_sentence_6)
        sentences.extend((s_1, s_2, s_3, s_4, s_5, s_6))
        shuffle (alt_sentences)
    #---------------------Request/Response------------------------  
        webpage_response = requests.get(link)
        webpage = webpage_response.content
        soup = BeautifulSoup(webpage, 'html.parser')
    #---------------------Title parser------------------------    
        title = soup.find('title').get_text()    
    #---------------------H1 parser------------------------  
        h1 = soup.find('h1').get_text()   
    #---------------------H2 list generator------------------------ 
        h2_soup = soup.find_all('h2') 
        list_of_h2 = []
        for h2 in h2_soup:
            if len(h2.get_text()) < 25 and '?' not in h2.get_text() and '!' not in h2.get_text():
                list_of_h2.append(key.capitalize() + ': ' + h2.get_text())
    #-----------Paragraphs list generator-------------------    
        p_soup = soup.find_all('p')
        list_of_p = []
        p_alternate = ''
        for p in p_soup:
            if len(p.get_text()) > 250:
                list_of_p.append(p)
        p_alternate = list_of_p[1::2]
        p_final = ''
        for every_other_p, sentence in zip(p_alternate, sentences):
            p_final += every_other_p.get_text() + re.sub(r'egg', key, ''.join(sentence)) +'\n\n' 
    #----------------Alts list generator-------------------
        alts_soup = soup.find_all('img')
        alts = alts_soup[3::]
        alts_final = []
        for alt_final, count_alt in zip(enumerate(alt_sentences), alts):
            alts_final.append(re.sub(r'egg', key.capitalize(), alt_final))
    #----------------Original Alts list generator-------------------        
        og_alts_soup = soup.find_all('img', alt=True)  
        og_alts = og_alts_soup[3::]
    #-----------Meta description list generator-------------------    
        meta_soup = soup.find(attrs={'name':'description'})
        if len(list_of_h2) > 0:
            for h2_element in list_of_h2:
                    h_2_output = '<h2>' + h2_element + '</h2>'           
    #----------------Output----------------------    
        return '<title>' + title + '</title>' + '\n' + '<h1>' + h1 + '</h1>' + '\n' + h_2_output + '\n' + p_final + '\n' +\
               'Дописать атрибут alt на всех картинках и баннерах, где он отсутствует:' + '\n' 


# print(seooptimiser('https://www.zonecash.ru/kak-zarabotat-na-hayp-proektah/', 'рррррррррррррррррр'))
    # #-----------------H2 paragraph------------------- 

    #     
    # #--------------------Alts paragraph---------------------
    #     font = p.add_run('Дописать атрибут alt на всех картинках и баннерах, где он отсутствует:').font
    #     font.highlight_color = WD_COLOR_INDEX.GRAY_25
    #     for re_alt in alts_final:
    #         p = document.add_paragraph('   ' + re_alt)
    # #--------------------Original Alts paragraph---------------------        
    #     # for og_alt in og_alts:
    #     #     p = document.add_paragraph(og_alt['alt'])
    # #--------------------Meta description paragraph----------------      
    #     p = document.add_paragraph()    
    #     font = p.add_run('Изменить meta description на:').font
    #     font.highlight_color = WD_COLOR_INDEX.GRAY_25
    #     p = document.add_paragraph(str(meta_soup['content']) + str(re.sub(r'egg', key, meta)))
    #     run = p.add_run()   
    #     run.add_break()
    #     run.add_break()
    # #----------------------Video paragraph------------------------    
    #     font = p.add_run('Добавить видео:').font
    #     font.highlight_color = WD_COLOR_INDEX.GRAY_25
    #     p = document.add_paragraph(video)
    #     document.save('C:\\Users\\Cute but evil\\Documents\\vs code\\seo programmes\\' + doc_name + ".docx")
    #     time.sleep(1)   

    