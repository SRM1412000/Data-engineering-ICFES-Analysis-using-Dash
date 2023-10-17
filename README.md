# Data-engineering-ICFES-Analysis-using-Dash

* Project by: David Oviedo Salamanca [@fonzo004](https://github.com/fonzo004), Jose Álvarez Medina [@JoseAlvarezMedina](https://github.com/JoseAlvarezMedina), Germán David Plazas Cayachoa [@DavPlazas](https://github.com/DavPlazas), Santiago Rodríguez Morales [@SRM1412000](https://github.com/SRM1412000)

## Index
- [Problem.](#problem)
- [Relational Model in Third Normal Form.](#model)
- [Description of analyses developed.](#desc)
- [Discussions of developed analyses.](#disc)
- [Conclusions.](#conc)

## Problem
The ICFES Saber-11 state exam evaluates the degree of knowledge in the academic areas of students who are about to finish high school.
of students who are about to finish high school. In addition to the individual results, this test also collects socioeconomic data that can be associated with the results of some population groups and reflect certain strengths and weaknesses of the students and reflect certain strengths and weaknesses in the country's education. Due to the above, this project seeks to analyze and represent existing relationships between some variables and data obtained from the test variables and data obtained from the test.

The data used in this project were obtained from: https://www.datos.gov.co/EducaciÕn/Saber-11-2019-2/ynam-yc42/data, government project.

## Relational Model in Third Normal Form. <a name="model"></a>
![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/c15d5cee-7bae-4478-bbdd-559b4e6ffdce)

## Description of analyses developed. <a name="desc"></a>

- As a first analysis, it is possible to determine the schools that excelled the most in the ICFES in the ICFES Saber 11 2019-II tests at the departmental level. Here, a variety of comparisons can be comparisons that allow us to conclude how the overall average score of the best schools in the departments most neglected by the State is much lower than the average score of the best schools in the departments most neglected by the State, is much lower than in departments with a high level of socio-economic intervention.
socioeconomic intervention by the state.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/15d8cc01-c57f-4ffc-b5e5-1eb87b07531a)

*Figure 1: Bar chart of best schools by department.* 

- With respect to Figure 2, the user can select the department for which he/she wishes to perform the analysis, and then a bar chart is displayed showing the first seven schools that stood out in that department. Figure 1 shows the respective schools for the department of Boyacá. Figure 2 shows the drop-down menu in which the user can select one of the 32 departments.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/9174eb67-da89-4de3-813a-64deb61c29a3)

*Figure 2: Department selection for the Department Bar Chart.* 

- In the following analysis, we wanted to compare the scores of each subject by stratum. Figure 3 shows a bar chart in which it is evident how the overall average where it is evident how the general average of the subjects increases from stratum 1 to stratum 3, in which the average score per subject is around 48 points, on the other hand, strata 4 to 6 have around 53 points per subject. The subject of social social studies was the component that remained high throughout all strata. The reading component also stands out in the higher strata.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/c929fcd5-b03d-4f52-8564-9d35fb9c4795)

*Figure 3: Slider of the scores for each subject by stratum.*

- In another analysis, we want to know how good is the performance in the area of English and therefore the command of the second language at the departmental level of the students. For this purpose, we made a heat map divided by departments in which the performance of the students in the second language is reflected which reflects the average score of the English proficiency in the tests
Saber 11. We obtain a very interesting result for our analysis, in which we conclude that, as shown, the level of English is higher in the more populated areas of the country, especially in the central region and the capital city. This contrasts with the low performance in remote or more disadvantaged areas.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/4c5e3e30-c688-4bbd-b2a1-4a68abccb54e)

*Figure 4: Heat map with average English test scores per period. 2019-II by department*

- The database used in our project provides personal data on students that may reflect socioeconomic characteristics of the country.
Because of the above, the group decided to look for a representation of the distribution of student strata, hypothesizing that a large number of students would be found. The distribution of the student strata can be seen in Figure 5. As can be seen, the most common strata are the low strata (1,2,3), while the high strata (5,6) barely exceed 2 % of the population, which reflects a great social inequality in the population. This reflects a great social inequality in Colombian education.


![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/ebc6a8cf-798a-485f-b581-d328757c4b0a)

*Figure 5: Pie chart of the distribution of student strata.*

- The group decided to make a comparison of the global score averages in each stratum of the country. Figure 6 shows a bar chart in which the averages above 250 points stand out, corresponding to strata 3, 4 and 5, with stratum 4 being the best performing stratum. The lower averages are found at both extremes, corresponding to strata 1 and, to the surprise of the group, strata 2. We concluded stratum 4 students belong to educational institutions where they are better prepared for the tests. similarly, this is the case with strata 3 and 5.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/ddd60f5f-c278-4719-8a56-c090d75b0fa0)

*Figure 6: Bar chart of the global score by stratum.*

- The ICFES Saber-11 exam, in addition to evaluating aspects of education throughout the country, is also an opportunity for some educational institutions to acquire prestige based on their results, thus attracting parents to enroll their children. As we can see in Figure 7, a bar chart is made with the averages of the global scores. From the figure we can see that the three best schools were Centro Educativo Antares, Liceo Campo David and Instituci'on Alberto Merani.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/47be13f7-9a2a-431b-88fe-0b660c0c5857)

*Figure 7: Horizontal bar chart of the scores of the top ten schools in Colombia*

- Figure 8 compares the performance in this test between public and private schools, and it is concluded that official schools have a slightly lower performance than private schools, since the overall average score of public schools is slightly lower than that of private schools is 263.39, while the score for the public schools is between is oscillating between 240 and 241 points.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/e4456829-cff3-4ce9-b837-1c264b6a9f0d)


*Figure 8: Bar chart showing the overall score obtained by official and non-official schools.*

- In a final analysis, we wish to show the overall performance in the Saber 11 tests taking into account the student's sex. As can see in Figure 9, men obtained somewhat more satisfactory results in their average for the 5 different areas of the test. The greatest differences in averages between men and women were evident in the area of natural and social sciences; while the reading average is very similar for both sexes, although men maintain a slight advantage.

![image](https://github.com/SRM1412000/Data-engineering-ICFES-Analysis-using-Dash/assets/146349622/291172bc-9c41-41e6-aae9-0336ab00a54f)

*Figure 9: Bar chart of average score by subject. Males and females*

## Discussions of developed analyses <a name="disc"></a>

* **Figure 1 and Figure 2:**
  * **Advantages:** In figure 1 and 2 you can appreciate a pleasant environment and easy to understand for the user. As a first step, the user can enter text to easily locate the department he/she wants to study and can also search for it in the drop-down bar. Then, the user observes in an understandable way the average of the global score obtained by the average global score obtained by the school belonging to the department the user selects, where the user can easily move the mouse over a bar corresponding to the name of a school the mouse over a bar corresponding to the name of a school, and the exact number for the exact number for the average score.

  * **Disadvantages:** In some cases, the name of the educational institution is very large, so that a complete analysis can be difficult at first glance, however, there is a "zoom in" option to make the graph a little larger so that the user can understand it satisfactorily.
    
* **Figure 3:**
  * **Advantages:** Figure 3 stands out for its easy comprehension, organization and provides the option to use a slider to classify the scores according to their stratum providing an easy interaction with the user.

  * **Disadvantages:** Disadvantages: Graphics can become monochrome.

* **Figure 4:**
  * **Advantages:** The design of this heat map is aesthetically pleasing and understandable. It clearly reflects which areas/departments of the country are the best performers on the English tests. The graph provides a spatial notion about the analysis performed.

  * **Disadvantages:** It is not possible to visualize the insular region of San Andres and Providencia in the heat map due to its small size compared to the other regions.
 
* **Figure 5:**
  * **Advantages:** This diagram has the advantage of allowing us to visualize the proportions of a value, in this case the number of students per stratum. It is easy to understand and is practical when inferring the results. In this case, it is easy to reflect the social inequality in Colombian education. In addition, it provides the opportunity to see a numerical value for those who prefer it.

  * **Disadvantages:** The group does not find a significant disadvantage in this figure.
 
* **Figure 6:**
  * **Advantages:** The bar chart is understandable because the chromatic characterization is organized and clear. It has similar advantages to Figure 3.

  * **Disadvantages:** There may be some redundancy between the colors and the scale.

* **Figure 7:**
  * **Advantages:** The horizontal bar chart allows us to see in a hierarchical and understandable way the scores of the top ten schools in Colombia. At the same time, the names of the schools are visualized in a better way than in a vertical bar chart. The scale of scores allows us to visualize that although these schools are the best in the country, there are great differences between them.

  * **Disadvantages:** The diagram is organized from the lowest to the highest score, however, an aspect to improve would be to place them in a countable way. You can also think of a grid that lists the data, in this case, the school.

* **Figure 8:**
  * **Advantages:** For the analysis that concerns this bar chart, we have the advantage that there are only two bars to be contrasted, so it is easy to understand and visualize.

  * **Disadvantages:** We found no major disadvantages in interpreting the results or evaluating their esthetics.

* **Figure 9:**
  * **Advantages:** The gender bar chart highlights the ease of understanding by its attractive and identifiable colors. At the same time, the bars provide a clear visualization for each category.

  * **Disadvantages:** In the future, the labels under each examined area can be modified to facilitate the understanding of the results.

## Conclusions. <a name="conc"></a>

* **On the selection of the data source:**
  About 546000 tuples (number of tests presented in the period 2019-II) were used with the data to perform the required analysis in order to fulfill the project objectives. These selected data are extracted from an official source of the State in order to guarantee a greater veracity in the obtained results. It has been decided to use this data source since its multiple number of columns allows the elaboration of different entities and attributes for a more detailed analysis. In addition, we took advantage of the easy access to these resources of public interest through the Internet, so obtaining them was not a major difficulty.
* **About the design of the database:**
  There are 5 entities (exam, student, school, municipality and department) in our relational model. These are systematically arranged in such a way that the different data are ordered for their correct and efficient analysis. Each one of the entities contains its attributes; these attributes contain primary keys, foreign keys and their respective restrictions according to the rules previously established for the correct functioning of the analysis on the database.
  
  For the entity `exam' we have the attributes `percentile', `global score', `period', `c natural score', `math score', `social score', `English score' and `critical reading score'. With `id student' as a foreign key coming from the entity `student'. The relationship of this entity with the entity `student' is based on the fact that the same student can take several exams. can take several exams.

  For the entity `student' we have the attributes `id student', `date of birth', `status' and `sex'. With `school code' as a foreign key coming from the entity `school' and thus establishing the relationship between the student and his school. This relationship is thought in such a way that a student has only one school, but a school can have many students. For the entity `school' we have the attributes `code', `school name', `schedule', `gender', `location' and `nature'. The foreign key in this case is `code m' coming from the entity `municipality', establishing a relationship such that a municipality can have several schools and not the other way around. For the entity `municipality' we have the attributes `code m', `name m', `evaluated number m' and the foreign key `department d-code'. Following the same line, a department can have many municipalities, but not vice versa. not vice versa.

  Finally for the entity `department' we have the attributes `codigod', `name d' and `evaluated number d'. Conclusion of the procedure: The group considers that an understandable and practical database design was achieved for the queries that the group wanted to develop. In addition, the necessary and identified relationships were established to comply with the rules proposed in the first delivery of the project. The design of the database is in third normal form, as it meets the criteria that these forms require and thus the database becomes easier to manage for the use of dash, queries and data loads. Finally, the group considers that the attributes are the right ones to identify and perform an analysis that can reflect realities of the country in the field of secondary education. The result of this procedure can be seen in the point 2 of this document and in the code of the implementation of the database available in the repository.

* **About the information load:**
  First, we performed the load for the `department' and `municipality' tables from two .csv files available in the project repository.

  Secondly, to continue with the data loading it was necessary to review our first implementation of the `school' table. For the attributes `code' and `school name', the data type was changed to varchar(n) and varchar(30) respectively. Once this was done, the data was loaded from the corresponding .csv file in the repository.

  Thirdly, as was done with the `school' table, some changes were also made to the `student' table. For this data load, it was necessary to modify its corresponding .csv file, because some data for the `date of birth' attribute presented a wrong format that does not contemplate the date attribute of SQL. This was fixed with the file FixingDate.cpp (located in the code folder on GitHub) which adapted the formats of this attribute. At the same time, changes were also made to the attribute stratum, as some students were showing no stratum, and these data were assigned the number -1.

  Finally, for the table `exam', we removed a restriction `not null' that had been implemented to the attribute `English score', this due to the lack of some data in the .csv file. The data load was performed and the procedure was finished.

  Conclusion of the procedure: During the data loading process, the group realized that, in spite of having a planned and designed database against an original idea, large data dictionaries often present inconsistencies, exceptions, spelling and typing errors that generate inconveniences when loading and analyzing them. Because of this, it is necessary that prior to the design and implementation of the database, the data be analyzed as much as possible. However, the group feels that the data loading was successful and met its objectives, which were to distribute and arrange the data in such a way that they could be consulted and analyzed to meet the project's objective.

* **About the connection with the database, the development in dash and the identified analytics:**

  During the connection procedure with the database, there were no problems, and we also tested the operation of different queries to visualize data from our database. The group considers the connection with the database as a simple and very practical procedure, since it allows to consult data from external sources and to make analysis with this.

  During the implementation of Dash in Python the group faced several challenges. One of these challenges was to carry out an idea in which it was proposed to implement a drop-down bar in which the user could interact with the application. Following this, dash documentation was consulted to carry out this idea, which was successfully developed and attached to a bar chart in which you can see the top seven schools in each department. Another challenge to highlight was to implement the heat map of Colombia, in which it was necessary to work with JSON files to carry it out, finally the result was successful. Among other challenges, we also consulted various documentation for the decorators of the application.

  Conclusion of the procedure: The goal of creating an application with the different analyses identified in the database was achieved. The group considers that the application is understandable, manageable and interactive for the users. In addition, the data are concise and clearly presented in the graphics. Therefore, the application is a great tool to analyze the data of the ICFES Saber 11 exam for the period 2019-II, which in turn reflects the situation of the country in the field of education.  








