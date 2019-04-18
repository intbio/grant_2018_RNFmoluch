# 2018_RNFmoluch

## Отчеты
- [Научный отчет за 2018-2019 год](https://docs.google.com/document/d/1MgiTv9Y7oDxZVsyYMMmA1XoqaD91gS-Xr6jwO9oTrZo/edit?usp=sharing). [Планы на 2019-2020](https://docs.google.com/document/d/1SHfygFOKcSMbt5_Fusf5XzfqY-HAFtzPZONseLaMvXw/edit?usp=sharing)

## Папки
- Ссылка на [Google Drive](https://drive.google.com/open?id=1BLPmT5rsuVZjckfTOFIWQs-CRNsxXfuB)

## Планы

- [На первый год](plan_results1year.pdf)
- [На все время](plan-zadach.pdf)

## Задачи и ссылки

### Задача 1.1. Годы 1-2
Построить модели конформационных перестроек димеров H3-H4 в нуклеосомах необходимых для взаимодействий с ремоделерами SNF2h и SWI/SNF.  
План на первый год:
- Подготовка полноатомных моделей димеров и тетрамеров H3-H4. (*отчет Настя*)
   - Репозиторий с моделями [https://github.com/intbio/nucl_gmx](https://github.com/intbio/nucl_gmx) (*Настя* - просьба причесать репозиторий)
- Разработка возможных обобщенных переменных на основе известных экспериментальных данных, отражающих конформационные перестройки димера в эксперименте. *(Гриша)* (метадинамика с увеличением подвижности H4I29, L49, L50, V57 + попытка деформировать ДНК) (*отчет Гриша*)
   - Анализ экспериментальных данных и постановка задачи. [Описание](1_1_h3-h4_plast_exp.md).
- Изучение влияния дисульфидных сшивок (типа H3F104C- H4V43C) на динамику димеров и тетрамеров гистонов (пункт переставлен с низу)(отчет - *Юнона*).
   - Нужно сделать картинки с положением связей и мутаций в нуклеосоме. В виде картинки, nglview модели в html файле и ipython notebook, который генерит. [гуглдок](https://docs.google.com/document/d/1dfYppMz-SxjIPgbBzS3_SMfUuycidbD16K6E7HF0CRE/edit?usp=sharing) *(Юнона)*.
   - Равновесная динамика H3-H4 с и без ДНК, с мутациями и без, в том числе с применением REMD (температура до 350). Ссылка на проект: https://github.com/intbio/2018_h3-h4_dyn/blob/master/h3-h4-free_vs_mut.md 
   - Разница динамики димера с/без сшивок и димера в тетрамере
- Подбор параметров методов метадинамики, ускоренной динамики, адиабатически смещенной динамики, динамики с обменом репликами для моделирования пластичности димера гистонов. (*отчет Настя*)
   - Можно ориентироваться на тьюториал https://github.com/intbio/MolModEdu/tree/master/PLUMED
- Проведение тестовых и основных расчетов различными методами. *(Гриша)* (*отчет Гриша*)
   - В первую очередь нам нужно провести ABMD динамику димера и тетрамера, с уменьшением числа контактов у H4I29, L49, L50, V57. Это нужно, чтобы закрыть ТЗ в части результатов см. ниже!!! *(Гриша)*
   - Расчеты методом ABMD по кручению или спрямлению ДНК относительно димера из положения SHL2. *(Гриша)* 
   - Расчеты методом MetaD по CV, полученным из PCA (это пока опционально для отчета).
- Разработка алгоритмов оценки конформационных и динамических перестроек димеров. (*отчет Настя*)
   - По сути это репозиторий gmx_template, но его надо расширить.
   
Результаты в первом году: 
- Построена атомистическая модель пластичности (файлы PDB для нескольких конформаций, видео) димера и тетрамера гистонов H3-H4, согласующаяся с экспериментальными данными. (*отчет Гриша*)
   - Файл с результатами...
- Проведён анализ влияния дисульфидный сшивок на пластичность. (*отчет Юнона*)
   - Файл с результатами...

### Задача 2.1. Годы 1-2
Провести структурный и энергетический анализ известных взаимодействий пептидов/ мотивов белков с кислотным лоскутом нуклеосомы (включая пептид LANA, белок CENP-C, антитело PL2-6).  
План на первый год: 
- Провести анализ всех имеющихся структур нуклеосом с белками на предмет деталей их взаимодействия с кислотным лоскутом нуклеосомы. (*отчет Лиза*)
   - Дать определение кислотного лоскута *(картинка от Гриши)*. [Определение](https://www.nature.com/articles/s41586-019-1038-1.pdf): H2AE56, E61, E64, D90, E91, E92; H2BE105, E113.
   - Поиск всех структур в PDB: https://github.com/intbio/2018_nucl_pept/tree/master/data. Текст с анализом для отчета (простейшая статистика по количеству структур, еще хорошо бы по филетическому составу - из каких организмов): ...
   - Анализ структур с помощью PLATINUM. Ссылка на код и на результаты, ссылка на файл для отчета.
   - bar-plot: 6_1_analysis, seqtools
- Обобщить данные в виде модели фармакофора.
   - mTm-align: MSA *(Для анализа Ане)*
   - Нужно изобразить некое подобие фармакофора - см. сервис pharmit http://pharmit.csb.pitt.edu (димер с пептидом, переименованным в лиганд)
- Разработать методы автоматизированного анализа взаимодействий.
   - MYSOFT/structure_analysis
   - *Гриша*: попробовать установить vmd+python в moldyn [**он там давно стоит, но версия питона 3.7**](https://github.com/Eigenstate/vmd-python)
- Провести изучение строения поверхности кислотного лоскута в плане его электростатических , гидрофобных свойств и способностей образовывать контакты с пептидами. (*отчет Лиза*)
   - Построить поверхность электростатическую APBS или DELPHI. *(Гриша)*
   - В остальном это должно закрываться PLATINUMом.
- Создать молекулярно динамические модели нуклеосом, взаимодействующих с пептидами в области кислотного лоскута, включая пептид LANA, пептид CENP-C (в этом случае будет использовать вариант центромерной нуклеосомы), фрагмент антитела PL2-6 (в этом случае будет использоваться модель построенная по гомологии) (моделер). (*отчет Лиза*)
   - Ссылки на модели: https://github.com/intbio/2018_nucl_pept/tree/master/moldyn
- Провести молекулярно-динамические расчеты и оценить стабильность и динамику взаимодействий пептидов с нуклеосомой. Обязательно построить карты контактов! (*отчет Лиза*)
   - Результаты расчетов: видеофайлы с динамикой 
   - Обязательно построить карты контактов!
- Провести оценку энергии связывания пептидов с нуклеосомой с помощью эмпирических подходов (таких, как FoldX). *(Рома)* (*отчет Рома*)
   - Результаты расчетов FoldX.
   - Энергия в зависимости от мутаций пептида (в частности, [онко-](https://www.nature.com/articles/s41586-019-1038-1.pdf))
- Сформулировать рациональные предложения по оптимизации энергии связывания пептидов с кислотным лоскутом. 
   - *Рома*: в зависимости от мутаций 
   - *Лиза*: в зависимости от взаимодействий (+ структурное выравнивание всех, взаимодействующих с кислотным лоскутом => консенсусный сиквенс)
- Сформулировать рациональные предложения по оптимизации энергии связывания пептидов с кислотным лоскутом. (*отчет Рома*)

Результаты в первом году - повторяют задачи.

### Задача 3.1. Годы 1-2
Анализ и классификация всех имеющихся в открытом доступе данных по взаимодействию нуклеосом с белками хроматина у человека.

План на первый год: 
- Создать обновленный список всех известных генов гистонов человека (исключая псевдогены) и соответствующих им белков, включая сплайс изоформы. (*отчет Аня*)
   -  Ссылка на таблицу https://github.com/intbio/2018_nucl_int/blob/master/histone_genes.csv
   -  Текст с описанием того, что сделано ....
- Разработать автоматизированный программный код, который будет подгружать информацию о взаимодействиях гистонов и других белков из баз данных IntAct, BioGRID, STRING и др.  (*отчет Аня*)
   - По ссылке, который обрабатвает данные STRING .....
   - По ссылке, который обрабатвает данные BioGRID .....
   - Описание результатов 
   - Текст для отчета ...
- Реализовать прозрачную конвертацию информации о взаимодействиях между различными форматами, включая идентификаторы генов и/или белков.  (*отчет Аня*)
   - Ссылка на код, который конвертирует название генов гистонов и интеракторов.
   - Текст для отчета.
- Составить схему для рациональной функциональной иерархической классификации белков взаимодействующих с нуклеосомами на основе анализа литературы (напр. ремоделеры разных типов, белки взаимодействующие с пост-трансляционными модификациями гистонов, шапероны различных классов, пионерные транскрипционные факторы и т.д.).  (*отчет Аня*)
   - По ссылке, код ...
   - Файл на JSON и его отрисовка в CytoScape. Скрипт, который делает кртинку.
   - Список  проанализированных источников: базы данных (GO, EpiFactor, .... ) + литература + поиск по PubMed. Домены?
   - Текст для отчета ...
- Оценить качество имеющейся в базах данных информации ( в том числе исходя из первичных данных литературы) и выработать критерии отбора данных по уровню имеющегося качества данных.  (*отчет Аня*)
   - Анализ интеракторов в зависимости от уровней в каналах.
   - Текст и результаты ...
   - Алгоритм коррекции данных.
   - Описание проблемы и алгоритма.
- Провести анализ полученного интерактома, в том числе используя различные онтологии ( такие, как Gene Ontology), данные о биохимических/сигнальных путях (KEGG?) взаимодействий и собственную разработанную иерархическую классификацию.  (*отчет Аня*)
   - Распеределение по GO, по нашей классификации. 
   - В Cytoscape размером точки количество белков данного класса.
   - Анализ мотивов в последовательнсотях. Acidic Patch Binding, AT-hook, SPKK.
   -  CENP-C-motif "R....P..[YFW]W” [PMID 23723239], AT-hook "..[RPKST]GRP[RPKS]” [PMID: 9742243], SPKK-motif "SP[RK][RK]” [PMID: 2556263], where “.” - meant any symbol and square brackets denote that any of the amino acids listed within the brackets is allowed in this position.
- Разработать автоматизированные методы поиска информации о структурах взаимодействующих комплексов белков хроматина человека и нуклеосом из баз данных PDB и EMDB с учетом анализа комплексов, формируемых гомологичными белками из других организмов.  (*отчет Кирилл*)
   - https://intbio.org/2018_nucl_pept/data/prot_sorted.html
   - сделать таблицу взаимодействующих белков человека
   - тоже самое для EMDB


Результаты в конце первого года - совпадают с планами. 

### Задача 1.2. Год 2-3
Установить влияние различия последовательности гистонов H2A и его варианта H2A.Z на конформацию и динамику H2A-H2B димеров и построить комплексную модель, объясняющую селективность связывания ремоделера Swr1 у дрожжей (аналог p400 и SRCAP человека) с нуклеосомами содержащими гистон H2A. - Год 2-3.  
Ожидаемые результаты (Год 2)
- Проведено сравнительное моделирование димеров гистонов H2A/H2B и H2A.Z/H2B пекарских дрожжей методами атомистической молекулярной динамики, включая “продвинутые” методы МД.
- Установлен характер влияния аминокислотных различий на динамику.

## Формальные данные

Соглашение № 18-74-10006 от 08.08.2018 

научному проекту: "Структурная динамика нуклеосом и их взаимодействий: поиск подходов для диагностики и лечения онкологических заболеваний", руководитель проекта Шайтан Алексей Константинович, биологический факультет,

 № в СЭД МГУ 441 от 24.09.2018.

тема № 9-07/18
