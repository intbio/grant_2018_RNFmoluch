# 2018_RNFmoluch

## Отчеты
- [Научный отчет за 2018-2019 год](https://docs.google.com/document/d/1MgiTv9Y7oDxZVsyYMMmA1XoqaD91gS-Xr6jwO9oTrZo/edit?usp=sharing). [Планы на 2019-2020](https://docs.google.com/document/d/1SHfygFOKcSMbt5_Fusf5XzfqY-HAFtzPZONseLaMvXw/edit?usp=sharing)

## Папки
- Ссылка на [Google Drive](https://drive.google.com/open?id=1BLPmT5rsuVZjckfTOFIWQs-CRNsxXfuB)
- [Dropbox for internal use](https://www.dropbox.com/home/work/mygrants/RNFmoluch2018-2021)
- [RNF internal use](https://grant.rscf.ru/site/user/bids?role=master)
## Планы

- [На первый год](plan_results1year.pdf)
- [На второй год](https://www.dropbox.com/s/wndw7r5d07jlxmk/zadachi-2019-2020.pdf?dl=0)
- [На все время](plan-zadach.pdf)

## Задачи и ссылки

### Задача 1.1. Годы 1-2 (Гриша)
Построить модели конформационных перестроек димеров H3-H4 в нуклеосомах необходимых для взаимодействий с ремоделерами SNF2h и SWI/SNF.  

#### Релевантные репозитории
- https://github.com/intbio/2019_nucl_plast_ak - AK структурирует данные по пластичности нуклеосом
- https://github.com/intbio/2019_nucl_plast_ga - Гриша ведет работу
- https://github.com/intbio/nucl_gmx - модели нуклеосом
- https://github.com/intbio/2018_h3-h4_dyn - динамика димеров, в том числе со сшивками.

#### План на первый год:
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
   
#### Результаты в первом году: 
- Построена атомистическая модель пластичности (файлы PDB для нескольких конформаций, видео) димера и тетрамера гистонов H3-H4, согласующаяся с экспериментальными данными. (*отчет Гриша*)
   - Файл с результатами...
- Проведён анализ влияния дисульфидный сшивок на пластичность. (*отчет Юнона*)
   - Файл с результатами...
   
#### План на второй год:
Обобщение результатов о пластичности димеров H3-H4, полученных ранее, на уровень нуклеосом. Подготовка полноатомных моделей нуклеосом для моделирования. Подбор параметров методов метадинамики, адиабатически смещенной динамики, динамики с обменом репликами для моделирования пластичности нуклеосом. Проведение молекулярно-динамических расчетов, в том числе с прицельным изучением конформационных перестроек вдоль известных координат реакции, вовлеченных в ремоделирование нуклеосом. Разработка алгоритмов оценки конформационных и динамических перестроек нуклеосом, связанных с пластичностью гистонов H3-H4 внутри нуклеосом. Изучение влияния дисульфидных сшивок (типа H3F104C - H4V43C) на динамику и пластичность нуклеосом. Формулировка гипотез на атомистическом уровне относительно механизмов пластичности димеров H3-H4 и нуклеосом в целом, влияющих на работу ремоделеров нуклеосом.


### Задача 1.2.  Год 2-3. (Настя)
Установить влияние различия последовательности гистонов H2A и его варианта H2A.Z на конформацию и динамику H2A-H2B димеров и построить комплексную модель, объясняющую селективность связывания ремоделера Swr1 у дрожжей (аналог p400 и SRCAP человека) с нуклеосомами содержащими гистон H2A. -
#### Релевантные репозитории

#### План на второй год:
Подготовка полноатомных моделей димером гистонов H2A/H2B и H2A.Z/H2B. Подбор параметров методов метадинамики, адиабатически смещенной динамики, динамики с обменом репликами для моделирования пластичности димеров. Проведение молекулярно-динамических расчетов. Проведение сравнительного анализа динамики димеров гистонов H2A/H2B и H2A.Z/H2B. Установление характера влияния аминокислотных различий на динамику.

### Задача 2.1. Годы 1-2 (Рома)
Провести структурный и энергетический анализ известных взаимодействий пептидов/ мотивов белков с кислотным лоскутом нуклеосомы (включая пептид LANA, белок CENP-C, антитело PL2-6).  
#### Релевантные репозитории

#### План на первый год: 
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

#### Результаты в первом году - повторяют задачи.

#### План на второй год:
 На основе предварительных результатов о связывании пептидов с нуклеосомами, полученными ранее, методами равновесной молекулярной динамики и эмпирического метода программы FoldX, будут разрабатывать более точные и гибкие подходы к оценке аффинности связывания пептидов с нукелосомами. Подбор подходов на основе методов молекулярной динамики и метода MM/PBSA для оценки свободной энергии связывания различных известных пептидов в нуклеосомами. Оценка свободной энергии взаимодействия различных известных пептидов с нуклеосомами с помощью подобранных подходов. Подбор алгоритмов и процедур белок-пептидного докинга для проведения докинга пептидов к нуклеосомам. Проведение докинга известных пептидов к поверхости нуклеосомы для оценки воспроизводимости результатов и качества скоринговых функций.

### Задача 2.2. Годы 2-3. (Рома)
Провести дизайн искусственных пептидов с высокой аффинностью связывания с кислотным лоскутом. - 
#### Релевантные репозитории

#### План на второй год:
Проведен дизайн пептидов с повышенной или пониженной аффинностью к нуклеосоме на основе оценки изменения энергии взаимодействия известных пептидов при введении точечных мутаций с использованием методов, разработанных в задаче 2.1.

### Задача 3.1. Годы 1-2 (Аня)
Анализ и классификация всех имеющихся в открытом доступе данных по взаимодействию нуклеосом с белками хроматина у человека.

#### План на первый год: 
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


#### Результаты в конце первого года - совпадают с планами. 

#### План на второй год:
Проведена полуавтоматическая курация сформированного на предыдущем этапе набора белков, взаимодействующих с нуклеосомой (нуклеосомного интерактома), очистка набора от ложноположительных взаимодействий, проверка взаимодействий на основе литературных данных, детальное изучение источников экспериментальных данных и их качества. Продолжены работы по аннотации и классификации собранного набора данных.


### Задача 3.2. (Годы 2-3) (Кирилл, Лавприт)
Разработать базу данных и веб-ресурс, представляющие в интерактивном виде информацию о известных взаимодействиях нуклеосом с белками хроматина, включая информацию по имеющимся трехмерным структурам. 
#### Релевантные репозитории

#### План на второй год:
 Разработка структуры базы данных в виде набора связанных таблиц. Определение ключевых функциональностей будущей базы данных и стэка программных технологий для ее реализации. Определение методов взаимодействия с имеющимися базами данных. Разработка методов обновления базы данных. Оценка объема и характеристик СУБД необходимых для реализации базы данных. Создание тестовой реализации на основе СУБД ( Системы управления базы данных).

=Пакет задач 4. Пакет задач 4. Биоинформатический анализ геномных и транскиптомных данных опухолей с точки зрения организации хроматина на нуклеосомном уровне (Годы 2-3)=
### Задача 4.1. (Годы 2-3) (Аня, Лавприт)
Проанализировать белки, взаимодействующие с гистонами и нуклеосомами, на предмет наличия в них повторяющихся (более чем у одного пациента) мутаций в образцах раковых опухолей по наборам данных международного консорциума раковых геномов и атласа раковых геномов (ICGC, TCGA). Провести структурную интерпретацию этих мутаций с расчетом их влияния на стабильность комплексов (при наличии соответствующих структур). 

#### Релевантные репозитории

#### План на второй год:
Загрузка и подготовка для анализа данных TCGA и ICGC. Анализ распределения мутаций в различных раковых опухолях для всех генов гистонов и для всех белков, взаимодействующих с гистонами. Выделение возможных мутаций “драйверов” по многократной встречаемости в различных образцах. Выделение белков со значительным числом повторяющихся мутаций среди интерактома нуклеосомы. Анализ принадлежности данных белков к различными классам согласно различным онтологиям, включая разработанную нами классификацию.
 
## Формальные данные

Соглашение № 18-74-10006 от 08.08.2018 

научному проекту: "Структурная динамика нуклеосом и их взаимодействий: поиск подходов для диагностики и лечения онкологических заболеваний", руководитель проекта Шайтан Алексей Константинович, биологический факультет,

 № в СЭД МГУ 441 от 24.09.2018.

тема № 9-07/18
