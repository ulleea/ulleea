# names=[]
# with open('C:\\Users\\Евгений\\Documents\\names.txt') as file:
#     for line in file:
#         l=line.split()
#         names.append(l[0])
#         names.append(l[1])
# print(names)
# # print(len(names))
# surnames=[]
# with open('C:\\Users\\Евгений\\Documents\\surnames.txt') as file:
#     for line in file:
#         l=line.split()
#         surnames.append(l[0])
#         surnames.append(l[1])
# print(surnames)
# print(len(surnames))
# countries=[]
# with open('C:\\Users\\Евгений\\Documents\\countries.txt') as file:
#     for line in file:
#         l=line.split()
#         countries.append(l[0])
# print(countries)
type=['director','actor','composer']
names=['Cheyne', 'Alexandrine', 'Clark', 'Ariella', 'Darion', 'Chanelle', 'Flurin', 'Dayana', 'Lazarus', 'Dele', 'Maxim', 'Emilie', 'Morell', 'Francena', 'Pollard', 'Isabela', 'Raff', 'Kimberley', 'Ransom', 'Kyleigh', 'Rickie', 'Marionna', 'Rushe', 'Ro', 'Spyros', 'Sienna', 'Walcott', 'Silvana', 'Waverly', 'Silvette', 'Wess', 'Vicky']
surnames=['Clawbreeze', 'Aguenteau', 'Fallenstride', 'Chauvelet', 'Hardvigor', 'Chauvezin', 'Horseshadow', 'Choiffet', 'Nicklesinger', 'Cremeur', 'Phoenixhand', 'Estienas', 'Titandream', 'Ravillon', 'Willowswift', 'Saullac', 'Wolfbraid', 'Saurelli', 'Wyverndane', 'Vasseriou']
countries=['France', 'Spain', 'United States', 'China', 'Italy', 'Turkey', 'Mexico', 'Thailand', 'Germany', 'United Kingdom']
birthdays=['1982-04-07', '1989-10-11', '1992-01-12', '1982-08-01', '1973-03-31', '1972-12-16', '1998-05-10', '1992-10-21', '1981-10-29', '1979-08-25', '1982-03-11', '1983-05-16', '1974-12-31', '1999-11-21', '1977-03-07', '1970-04-16', '1975-11-05', '1992-03-15', '1983-03-02', '1970-11-27', '1982-08-09', '1983-02-04', '1989-11-14', '1974-02-08', '1990-09-25', '1981-04-25', '1972-01-30', '1977-02-09', '1995-09-15', '1981-10-07', '1985-10-20', '1975-08-06', '1980-12-14', '1986-06-05', '1976-08-06', '1973-03-08', '1985-09-29', '1970-07-25', '1988-10-30', '1980-09-06', '1972-03-24', '1996-12-11', '1975-02-22', '1973-10-18', '1973-03-06', '1996-05-22', '1972-12-13', '1982-10-20', '1983-07-10', '1991-03-27', '1980-02-09', '1994-11-10', '1976-02-09', '1970-11-18', '1976-09-29', '1986-06-20', '1976-06-21', '1982-10-25', '1970-08-13', '1984-10-21', '1980-04-16', '1997-09-04', '1999-01-23', '1978-11-19', '1989-10-18', '1980-02-15', '1987-08-26', '1975-09-06', '1979-08-07', '1983-10-29', '1981-12-08', '1997-03-17', '1970-10-23', '1991-11-30', '1975-03-23', '1999-05-09', '1993-02-24', '1994-08-26', '1987-05-27', '1999-05-14', '1985-06-27', '1986-04-06', '1988-04-14', '1975-12-04', '1982-08-04', '1978-05-25', '1992-06-11', '1986-08-17', '1970-12-08', '1996-05-24', '1991-12-20', '1979-06-25', '1996-05-04', '1978-04-10', '1991-05-23', '1996-05-05', '1989-05-16', '1976-09-08', '1985-09-10', '1994-06-09', '1996-09-06', '1987-01-26', '1974-05-26', '1998-09-05', '1971-12-22', '1988-07-15', '1992-05-15', '1975-03-28', '1973-10-27', '1988-09-19', '1972-05-24', '1981-10-13', '1994-04-29', '1991-12-08', '1989-10-01', '1999-09-19', '1994-02-15', '1996-10-24', '1983-06-14', '1990-02-13', '1978-08-25', '1976-01-04', '1990-08-29', '1998-03-06', '1987-04-02', '1987-04-11', '1981-01-05', '1983-12-21', '1986-03-10', '1980-05-21', '1998-01-06', '1978-05-24', '1973-11-16', '1996-11-13', '1997-10-16', '1993-09-11', '1993-08-07', '1999-01-17', '1991-09-17', '1995-02-04', '1991-08-01', '1975-06-18', '1973-08-30', '1998-07-23', '1978-11-05', '1971-04-28', '1984-12-27', '1991-06-17', '1993-04-23', '1984-10-28', '1973-08-06', '1983-01-16', '1972-06-17', '1999-01-08', '1992-01-18', '1973-11-30', '1985-08-24', '1997-06-30', '1995-11-07', '1978-05-04', '1979-07-21', '1994-04-22', '1983-09-18', '1982-06-23', '1983-06-27', '1990-06-07', '1972-06-05', '1980-12-07', '1984-12-11', '1970-11-21', '1984-02-16', '1971-07-17', '1998-10-04', '1989-12-30', '1983-07-17', '1982-06-16', '1988-03-05', '1970-02-05', '1991-10-08', '1978-12-24', '1976-09-05', '1984-11-19', '1982-07-01', '1971-03-14', '1971-12-12', '1992-06-03', '1978-09-29', '1991-11-19', '1993-11-05', '1984-01-15', '1996-07-30', '1994-11-30', '1997-07-17', '1995-08-19', '1977-03-21', '1970-09-24', '1987-03-01', '1992-05-15', '1978-09-24', '1982-12-31', '1970-04-25', '1974-11-17', '1993-03-31', '1999-05-13', '1993-06-20', '1985-03-09', '1977-06-06', '1990-10-23', '1984-11-27', '1986-05-01', '1996-02-12', '1975-01-09', '1981-05-02', '1976-04-23', '1984-02-20', '1976-04-12', '1992-05-02', '1993-07-03', '1981-07-17', '1976-01-03', '1975-09-12', '1989-10-29', '1973-11-06', '1997-06-11', '1981-08-11', '1977-01-09', '1977-10-24', '1983-05-26', '1989-03-18', '1988-08-16', '1988-06-06', '1984-07-16', '1984-02-01', '1985-06-18', '1991-01-05', '1998-05-26', '1985-11-10', '1985-12-17', '1970-02-01', '1976-05-03', '1971-08-22', '1986-04-28', '1982-05-24', '1982-03-27', '1994-11-28', '1979-06-28', '1981-01-25', '1978-02-20', '1972-10-15', '1970-12-21', '1996-04-14', '1975-04-10', '1970-01-18', '1983-05-09', '1995-11-14', '1974-10-27', '1991-08-19', '1980-03-04', '1998-10-06', '1972-08-05', '1975-08-26', '1975-10-27', '1973-12-19', '1994-07-11', '1994-05-03', '1972-01-09', '1996-09-26', '1981-12-05', '1978-06-11', '1992-03-31', '1987-01-23', '1987-08-01', '1985-04-05', '1979-05-07', '1974-03-30', '1978-07-28', '1999-07-17', '1980-06-26', '1987-07-12', '1983-10-23', '1997-10-14', '1979-11-03', '1996-01-27', '1991-05-01', '1985-11-27', '1991-09-08', '1979-10-04', '1971-06-26', '1998-03-22', '1988-12-05', '1992-03-10', '1999-02-13', '1998-11-09', '1988-09-19', '1970-01-04', '1990-04-20', '1995-04-08', '1980-03-31', '1979-02-21', '1987-07-17', '1992-10-02', '1998-01-30', '1985-05-08', '1987-09-16', '1997-03-09', '1993-01-12', '1977-08-10', '1976-05-13', '1977-06-18', '1976-08-29', '1973-09-08', '1994-11-09', '1984-03-19', '1986-09-13', '1970-07-18', '1999-05-28', '1983-02-28', '1973-09-14', '1994-11-10', '1995-01-22', '1978-08-31', '1976-01-17', '1976-02-21', '1996-04-22', '1996-07-13', '1979-02-01', '1975-05-12', '1988-02-14', '1994-11-29', '1979-02-15', '1975-07-23', '1993-03-02', '1979-11-27', '1993-05-11', '1999-10-15', '1976-11-14', '1988-02-18', '1992-11-19', '1978-06-20', '1996-08-06', '1981-04-23', '1994-10-08', '1979-06-09', '1992-09-16', '1999-06-20', '1979-08-02', '1984-02-20', '1990-06-10', '1987-12-03', '1989-12-06', '1980-12-11', '1978-10-04', '1990-05-02', '1996-06-09', '1982-10-06', '1980-05-28', '1983-04-17', '1980-09-30', '1985-08-15', '1981-10-18', '1987-02-27', '1988-03-29', '1999-10-16', '1992-01-16', '1995-01-22', '1998-05-07', '1975-07-20', '1978-02-26', '1983-06-18', '1980-10-29', '1976-04-09', '1998-03-08', '1971-05-25', '1974-04-26', '1974-11-04', '1986-01-25', '1984-11-20', '1994-07-30', '1978-07-06', '1978-09-21', '1978-03-07', '1975-10-31', '1984-07-11', '1995-07-10', '1973-07-14', '1982-09-29', '1992-04-07', '1983-11-02', '1993-04-05', '1995-12-24', '1988-12-22', '1981-11-25', '1989-08-27', '1983-12-17', '1998-09-14', '1973-10-01', '1995-12-07', '1979-03-29', '1972-12-07', '1991-05-31', '1971-11-17', '1970-02-04', '1980-01-25', '1991-03-08', '1988-01-22', '1971-09-06', '1977-09-18', '1982-11-19', '1991-09-17', '1987-06-03', '1987-02-24', '1992-02-11', '1997-02-19', '1978-08-23', '1972-09-15', '1977-06-18', '1975-12-09', '1996-08-31', '1993-01-16', '1985-02-14', '1981-07-10', '1992-06-22', '1980-03-10', '1973-09-05', '1994-12-05', '1982-09-14', '1974-03-18', '1975-12-08', '1981-02-26', '1985-04-26', '1993-11-24', '1985-03-24', '1990-07-17', '1987-06-17', '1997-03-13', '1993-08-16', '1974-03-30', '1983-09-02', '1994-04-14', '1985-02-14', '1978-12-03', '1994-01-27', '1994-02-25', '1982-01-05', '1999-03-22', '1999-01-25', '1976-05-15', '1992-07-24', '1982-01-07', '1997-01-26', '1980-11-04', '1995-08-17', '1980-10-14', '1987-05-21', '1993-01-20', '1970-04-07', '1990-08-22', '1978-12-25', '1983-08-17', '1990-11-27', '1975-11-22', '1975-01-12', '1973-02-04', '1982-09-15', '1995-02-12', '1995-07-15', '1998-11-22', '1993-11-21', '1979-05-10', '1974-02-10', '1975-04-15', '1990-09-23', '1995-07-03', '1970-10-30', '1989-11-02', '1992-10-26', '1978-10-27', '1972-06-09', '1989-10-23', '1983-10-13', '1996-06-23', '1972-09-11', '1997-05-11', '1982-11-10', '1986-09-08', '1973-08-30', '1986-08-22', '1978-11-03', '1978-08-02', '1992-06-09', '1986-03-14', '1978-03-28', '1997-06-20', '1993-06-22', '1988-11-17', '1981-12-10', '1989-02-06', '1979-04-26', '1986-12-06', '1977-09-30', '1971-03-15', '1983-08-18', '1992-01-02', '1974-01-20', '1972-05-24', '1989-04-17', '1984-03-26', '1971-09-13', '1976-02-28', '1999-03-23', '1993-09-28', '1976-01-12', '1986-08-13', '1974-12-16', '1986-06-21', '1971-08-13', '1977-11-18', '1976-05-14', '1983-05-17', '1999-03-13', '1976-10-15', '1996-04-19', '1981-09-30', '1991-11-20', '1991-11-28', '1995-11-28', '1985-09-14', '1998-10-02', '1977-03-11', '1981-11-28', '1973-06-23', '1991-10-15', '1984-07-29', '1986-04-25', '1979-12-31', '1988-04-05', '1987-04-01', '1979-07-06', '1973-10-26', '1973-05-13', '1981-09-14', '1995-06-01', '1970-09-14', '1999-09-06', '1978-09-27', '1990-12-18', '1988-09-16', '1987-06-13', '1978-05-13', '1999-02-19', '1988-06-02', '1974-04-07', '1972-12-30', '1981-06-25', '1980-10-05', '1988-06-13', '1994-11-13', '1981-09-07', '1999-01-30', '1988-12-17', '1971-08-28', '1980-05-31', '1993-06-05', '1971-02-23', '1982-09-17', '1996-10-27', '1995-03-13', '1995-12-06', '1972-05-16', '1985-03-31', '1984-03-08', '1999-06-19', '1993-04-11', '1979-06-09', '1988-09-09', '1995-03-23', '1988-07-15', '1983-03-23', '1974-12-08', '1998-09-21', '1976-09-30', '1989-10-14', '1979-06-06', '1977-08-23', '1975-09-08', '1998-07-12', '1990-03-30', '1976-05-08', '1997-01-04', '1975-06-07', '1974-02-27', '1970-01-12', '1970-06-28', '1981-09-11', '1977-12-10', '1994-07-13', '1983-06-09', '1995-03-11', '1985-09-21', '1985-06-02', '1991-07-16', '1991-05-23', '1971-05-30', '1970-02-16', '1973-10-19', '1989-03-07', '1979-07-27', '1993-12-20', '1980-08-22', '1987-03-25', '1972-05-04', '1970-05-16', '1999-12-23', '1989-06-02', '1978-03-11', '1999-03-16', '1975-04-14', '1982-03-03', '1989-10-04', '1988-10-30', '1986-02-06', '1995-09-19', '1978-09-10', '1971-05-27', '1987-03-11', '1976-08-24', '1973-06-22', '1974-08-02', '1996-05-21', '1974-05-14', '1973-03-05', '1976-06-05', '1972-09-10', '1979-07-27', '1984-08-30', '1972-06-22', '1981-02-09', '1974-09-12', '1980-01-10', '1981-03-05']
genres=['Action','Adventure','Animated','Comedy','Drama','Fantasy','Historical','Horror','Musical','Romance','Science fiction','Thriller','Western']
years_films=['2015', '2024', '2018', '2024', '2020', '2017', '2023', '2020', '2018', '2023', '2023', '2023', '2015', '2015', '2023', '2019', '2015', '2024', '2019', '2017', '2024', '2022', '2022', '2015', '2024', '2024', '2024', '2022', '2023', '2020', '2018', '2015', '2024', '2022', '2020', '2018', '2019', '2023', '2021', '2017', '2018', '2020', '2015', '2023', '2020', '2024', '2017', '2021', '2019', '2021', '2022', '2022', '2024', '2019', '2020', '2017', '2022', '2022', '2024', '2019', '2024', '2017', '2021', '2015', '2018', '2021', '2016', '2018', '2024', '2018', '2015', '2024', '2024', '2016', '2019', '2019', '2021', '2018', '2017', '2020', '2015', '2024', '2024', '2015', '2016', '2017', '2022', '2015', '2015', '2016', '2016', '2023', '2015', '2016', '2022', '2024', '2024', '2015', '2021', '2018', '2016', '2023', '2018', '2015', '2024', '2015', '2015', '2017', '2024', '2023', '2024', '2016', '2016', '2020', '2017', '2022', '2020', '2019', '2017', '2020']
film_title=['Star Wars 1', 'Star Wars 2', 'Star Wars 3', 'Star Wars 4', 'Star Wars 5', 'Star Wars 6', 'Star Wars 7', 'Star Wars 8', 'Lord of the rings 1', 'Lord of the rings 2', 'Lord of the rings 3', 'Lord of the rings 4', 'Lord of the rings 5', 'Lord of the rings 6', 'Lord of the rings 7', 'Lord of the rings 8', 'Harry Potter 1', 'Harry Potter 2', 'Harry Potter 3', 'Harry Potter 4', 'Harry Potter 5', 'Harry Potter 6', 'Harry Potter 7', 'Harry Potter 8', 'Fast and furious 1', 'Fast and furious 2', 'Fast and furious 3', 'Fast and furious 4', 'Fast and furious 5', 'Fast and furious 6', 'Fast and furious 7', 'Fast and furious 8', 'Avatar 1', 'Avatar 2', 'Avatar 3', 'Avatar 4', 'Avatar 5', 'Avatar 6', 'Avatar 7', 'Avatar 8', 'Transformers 1', 'Transformers 2', 'Transformers 3', 'Transformers 4', 'Transformers 5', 'Transformers 6', 'Transformers 7', 'Transformers 8', 'Saw 1', 'Saw 2', 'Saw 3', 'Saw 4', 'Saw 5', 'Saw 6', 'Saw 7', 'Saw 8', 'Iron man 1', 'Iron man 2', 'Iron man 3', 'Iron man 4', 'Iron man 5', 'Iron man 6', 'Iron man 7', 'Iron man 8', 'Thor 1', 'Thor 2', 'Thor 3', 'Thor 4', 'Thor 5', 'Thor 6', 'Thor 7', 'Thor 8', 'Spider man 1', 'Spider man 2', 'Spider man 3', 'Spider man 4', 'Spider man 5', 'Spider man 6', 'Spider man 7', 'Spider man 8', 'Terminator 1', 'Terminator 2', 'Terminator 3', 'Terminator 4', 'Terminator 5', 'Terminator 6', 'Terminator 7', 'Terminator 8', 'Star track 1', 'Star track 2', 'Star track 3', 'Star track 4', 'Star track 5', 'Star track 6', 'Star track 7', 'Star track 8', 'Pirates of Caribbean 1', 'Pirates of Caribbean 2', 'Pirates of Caribbean 3', 'Pirates of Caribbean 4', 'Pirates of Caribbean 5', 'Pirates of Caribbean 6', 'Pirates of Caribbean 7', 'Pirates of Caribbean 8', 'Avengers 1', 'Avengers 2', 'Avengers 3', 'Avengers 4', 'Avengers 5', 'Avengers 6', 'Avengers 7', 'Avengers 8', 'Fantastic Beasts 1', 'Fantastic Beasts 2', 'Fantastic Beasts 3', 'Fantastic Beasts 4', 'Fantastic Beasts 5', 'Fantastic Beasts 6', 'Fantastic Beasts 7', 'Fantastic Beasts 8']
music_title=['Star Wars 1 intro', 'Star Wars 1 soundtrack', 'Star Wars 1 action', 'Star Wars 1 ending', 'Star Wars 2 intro', 'Star Wars 2 soundtrack', 'Star Wars 2 action', 'Star Wars 2 ending', 'Star Wars 3 intro', 'Star Wars 3 soundtrack', 'Star Wars 3 action', 'Star Wars 3 ending', 'Star Wars 4 intro', 'Star Wars 4 soundtrack', 'Star Wars 4 action', 'Star Wars 4 ending', 'Star Wars 5 intro', 'Star Wars 5 soundtrack', 'Star Wars 5 action', 'Star Wars 5 ending', 'Star Wars 6 intro', 'Star Wars 6 soundtrack', 'Star Wars 6 action', 'Star Wars 6 ending', 'Star Wars 7 intro', 'Star Wars 7 soundtrack', 'Star Wars 7 action', 'Star Wars 7 ending', 'Star Wars 8 intro', 'Star Wars 8 soundtrack', 'Star Wars 8 action', 'Star Wars 8 ending', 'Lord of the rings 1 intro', 'Lord of the rings 1 soundtrack', 'Lord of the rings 1 action', 'Lord of the rings 1 ending', 'Lord of the rings 2 intro', 'Lord of the rings 2 soundtrack', 'Lord of the rings 2 action', 'Lord of the rings 2 ending', 'Lord of the rings 3 intro', 'Lord of the rings 3 soundtrack', 'Lord of the rings 3 action', 'Lord of the rings 3 ending', 'Lord of the rings 4 intro', 'Lord of the rings 4 soundtrack', 'Lord of the rings 4 action', 'Lord of the rings 4 ending', 'Lord of the rings 5 intro', 'Lord of the rings 5 soundtrack', 'Lord of the rings 5 action', 'Lord of the rings 5 ending', 'Lord of the rings 6 intro', 'Lord of the rings 6 soundtrack', 'Lord of the rings 6 action', 'Lord of the rings 6 ending', 'Lord of the rings 7 intro', 'Lord of the rings 7 soundtrack', 'Lord of the rings 7 action', 'Lord of the rings 7 ending', 'Lord of the rings 8 intro', 'Lord of the rings 8 soundtrack', 'Lord of the rings 8 action', 'Lord of the rings 8 ending', 'Harry Potter 1 intro', 'Harry Potter 1 soundtrack', 'Harry Potter 1 action', 'Harry Potter 1 ending', 'Harry Potter 2 intro', 'Harry Potter 2 soundtrack', 'Harry Potter 2 action', 'Harry Potter 2 ending', 'Harry Potter 3 intro', 'Harry Potter 3 soundtrack', 'Harry Potter 3 action', 'Harry Potter 3 ending', 'Harry Potter 4 intro', 'Harry Potter 4 soundtrack', 'Harry Potter 4 action', 'Harry Potter 4 ending', 'Harry Potter 5 intro', 'Harry Potter 5 soundtrack', 'Harry Potter 5 action', 'Harry Potter 5 ending', 'Harry Potter 6 intro', 'Harry Potter 6 soundtrack', 'Harry Potter 6 action', 'Harry Potter 6 ending', 'Harry Potter 7 intro', 'Harry Potter 7 soundtrack', 'Harry Potter 7 action', 'Harry Potter 7 ending', 'Harry Potter 8 intro', 'Harry Potter 8 soundtrack', 'Harry Potter 8 action', 'Harry Potter 8 ending', 'Fast and furious 1 intro', 'Fast and furious 1 soundtrack', 'Fast and furious 1 action', 'Fast and furious 1 ending', 'Fast and furious 2 intro', 'Fast and furious 2 soundtrack', 'Fast and furious 2 action', 'Fast and furious 2 ending', 'Fast and furious 3 intro', 'Fast and furious 3 soundtrack', 'Fast and furious 3 action', 'Fast and furious 3 ending', 'Fast and furious 4 intro', 'Fast and furious 4 soundtrack', 'Fast and furious 4 action', 'Fast and furious 4 ending', 'Fast and furious 5 intro', 'Fast and furious 5 soundtrack', 'Fast and furious 5 action', 'Fast and furious 5 ending', 'Fast and furious 6 intro', 'Fast and furious 6 soundtrack', 'Fast and furious 6 action', 'Fast and furious 6 ending', 'Fast and furious 7 intro', 'Fast and furious 7 soundtrack', 'Fast and furious 7 action', 'Fast and furious 7 ending', 'Fast and furious 8 intro', 'Fast and furious 8 soundtrack', 'Fast and furious 8 action', 'Fast and furious 8 ending', 'Avatar 1 intro', 'Avatar 1 soundtrack', 'Avatar 1 action', 'Avatar 1 ending', 'Avatar 2 intro', 'Avatar 2 soundtrack', 'Avatar 2 action', 'Avatar 2 ending', 'Avatar 3 intro', 'Avatar 3 soundtrack', 'Avatar 3 action', 'Avatar 3 ending', 'Avatar 4 intro', 'Avatar 4 soundtrack', 'Avatar 4 action', 'Avatar 4 ending', 'Avatar 5 intro', 'Avatar 5 soundtrack', 'Avatar 5 action', 'Avatar 5 ending', 'Avatar 6 intro', 'Avatar 6 soundtrack', 'Avatar 6 action', 'Avatar 6 ending', 'Avatar 7 intro', 'Avatar 7 soundtrack', 'Avatar 7 action', 'Avatar 7 ending', 'Avatar 8 intro', 'Avatar 8 soundtrack', 'Avatar 8 action', 'Avatar 8 ending', 'Transformers 1 intro', 'Transformers 1 soundtrack', 'Transformers 1 action', 'Transformers 1 ending', 'Transformers 2 intro', 'Transformers 2 soundtrack', 'Transformers 2 action', 'Transformers 2 ending', 'Transformers 3 intro', 'Transformers 3 soundtrack', 'Transformers 3 action', 'Transformers 3 ending', 'Transformers 4 intro', 'Transformers 4 soundtrack', 'Transformers 4 action', 'Transformers 4 ending', 'Transformers 5 intro', 'Transformers 5 soundtrack', 'Transformers 5 action', 'Transformers 5 ending', 'Transformers 6 intro', 'Transformers 6 soundtrack', 'Transformers 6 action', 'Transformers 6 ending', 'Transformers 7 intro', 'Transformers 7 soundtrack', 'Transformers 7 action', 'Transformers 7 ending', 'Transformers 8 intro', 'Transformers 8 soundtrack', 'Transformers 8 action', 'Transformers 8 ending', 'Saw 1 intro', 'Saw 1 soundtrack', 'Saw 1 action', 'Saw 1 ending', 'Saw 2 intro', 'Saw 2 soundtrack', 'Saw 2 action', 'Saw 2 ending', 'Saw 3 intro', 'Saw 3 soundtrack', 'Saw 3 action', 'Saw 3 ending', 'Saw 4 intro', 'Saw 4 soundtrack', 'Saw 4 action', 'Saw 4 ending', 'Saw 5 intro', 'Saw 5 soundtrack', 'Saw 5 action', 'Saw 5 ending', 'Saw 6 intro', 'Saw 6 soundtrack', 'Saw 6 action', 'Saw 6 ending', 'Saw 7 intro', 'Saw 7 soundtrack', 'Saw 7 action', 'Saw 7 ending', 'Saw 8 intro', 'Saw 8 soundtrack', 'Saw 8 action', 'Saw 8 ending', 'Iron man 1 intro', 'Iron man 1 soundtrack', 'Iron man 1 action', 'Iron man 1 ending', 'Iron man 2 intro', 'Iron man 2 soundtrack', 'Iron man 2 action', 'Iron man 2 ending', 'Iron man 3 intro', 'Iron man 3 soundtrack', 'Iron man 3 action', 'Iron man 3 ending', 'Iron man 4 intro', 'Iron man 4 soundtrack', 'Iron man 4 action', 'Iron man 4 ending', 'Iron man 5 intro', 'Iron man 5 soundtrack', 'Iron man 5 action', 'Iron man 5 ending', 'Iron man 6 intro', 'Iron man 6 soundtrack', 'Iron man 6 action', 'Iron man 6 ending', 'Iron man 7 intro', 'Iron man 7 soundtrack', 'Iron man 7 action', 'Iron man 7 ending', 'Iron man 8 intro', 'Iron man 8 soundtrack', 'Iron man 8 action', 'Iron man 8 ending', 'Thor 1 intro', 'Thor 1 soundtrack', 'Thor 1 action', 'Thor 1 ending', 'Thor 2 intro', 'Thor 2 soundtrack', 'Thor 2 action', 'Thor 2 ending', 'Thor 3 intro', 'Thor 3 soundtrack', 'Thor 3 action', 'Thor 3 ending', 'Thor 4 intro', 'Thor 4 soundtrack', 'Thor 4 action', 'Thor 4 ending', 'Thor 5 intro', 'Thor 5 soundtrack', 'Thor 5 action', 'Thor 5 ending', 'Thor 6 intro', 'Thor 6 soundtrack', 'Thor 6 action', 'Thor 6 ending', 'Thor 7 intro', 'Thor 7 soundtrack', 'Thor 7 action', 'Thor 7 ending', 'Thor 8 intro', 'Thor 8 soundtrack', 'Thor 8 action', 'Thor 8 ending', 'Spider man 1 intro', 'Spider man 1 soundtrack', 'Spider man 1 action', 'Spider man 1 ending', 'Spider man 2 intro', 'Spider man 2 soundtrack', 'Spider man 2 action', 'Spider man 2 ending', 'Spider man 3 intro', 'Spider man 3 soundtrack', 'Spider man 3 action', 'Spider man 3 ending', 'Spider man 4 intro', 'Spider man 4 soundtrack', 'Spider man 4 action', 'Spider man 4 ending', 'Spider man 5 intro', 'Spider man 5 soundtrack', 'Spider man 5 action', 'Spider man 5 ending', 'Spider man 6 intro', 'Spider man 6 soundtrack', 'Spider man 6 action', 'Spider man 6 ending', 'Spider man 7 intro', 'Spider man 7 soundtrack', 'Spider man 7 action', 'Spider man 7 ending', 'Spider man 8 intro', 'Spider man 8 soundtrack', 'Spider man 8 action', 'Spider man 8 ending', 'Terminator 1 intro', 'Terminator 1 soundtrack', 'Terminator 1 action', 'Terminator 1 ending', 'Terminator 2 intro', 'Terminator 2 soundtrack', 'Terminator 2 action', 'Terminator 2 ending', 'Terminator 3 intro', 'Terminator 3 soundtrack', 'Terminator 3 action', 'Terminator 3 ending', 'Terminator 4 intro', 'Terminator 4 soundtrack', 'Terminator 4 action', 'Terminator 4 ending', 'Terminator 5 intro', 'Terminator 5 soundtrack', 'Terminator 5 action', 'Terminator 5 ending', 'Terminator 6 intro', 'Terminator 6 soundtrack', 'Terminator 6 action', 'Terminator 6 ending', 'Terminator 7 intro', 'Terminator 7 soundtrack', 'Terminator 7 action', 'Terminator 7 ending', 'Terminator 8 intro', 'Terminator 8 soundtrack', 'Terminator 8 action', 'Terminator 8 ending', 'Star track 1 intro', 'Star track 1 soundtrack', 'Star track 1 action', 'Star track 1 ending', 'Star track 2 intro', 'Star track 2 soundtrack', 'Star track 2 action', 'Star track 2 ending', 'Star track 3 intro', 'Star track 3 soundtrack', 'Star track 3 action', 'Star track 3 ending', 'Star track 4 intro', 'Star track 4 soundtrack', 'Star track 4 action', 'Star track 4 ending', 'Star track 5 intro', 'Star track 5 soundtrack', 'Star track 5 action', 'Star track 5 ending', 'Star track 6 intro', 'Star track 6 soundtrack', 'Star track 6 action', 'Star track 6 ending', 'Star track 7 intro', 'Star track 7 soundtrack', 'Star track 7 action', 'Star track 7 ending', 'Star track 8 intro', 'Star track 8 soundtrack', 'Star track 8 action', 'Star track 8 ending', 'Pirates of Caribbean 1 intro', 'Pirates of Caribbean 1 soundtrack', 'Pirates of Caribbean 1 action', 'Pirates of Caribbean 1 ending', 'Pirates of Caribbean 2 intro', 'Pirates of Caribbean 2 soundtrack', 'Pirates of Caribbean 2 action', 'Pirates of Caribbean 2 ending', 'Pirates of Caribbean 3 intro', 'Pirates of Caribbean 3 soundtrack', 'Pirates of Caribbean 3 action', 'Pirates of Caribbean 3 ending', 'Pirates of Caribbean 4 intro', 'Pirates of Caribbean 4 soundtrack', 'Pirates of Caribbean 4 action', 'Pirates of Caribbean 4 ending', 'Pirates of Caribbean 5 intro', 'Pirates of Caribbean 5 soundtrack', 'Pirates of Caribbean 5 action', 'Pirates of Caribbean 5 ending', 'Pirates of Caribbean 6 intro', 'Pirates of Caribbean 6 soundtrack', 'Pirates of Caribbean 6 action', 'Pirates of Caribbean 6 ending', 'Pirates of Caribbean 7 intro', 'Pirates of Caribbean 7 soundtrack', 'Pirates of Caribbean 7 action', 'Pirates of Caribbean 7 ending', 'Pirates of Caribbean 8 intro', 'Pirates of Caribbean 8 soundtrack', 'Pirates of Caribbean 8 action', 'Pirates of Caribbean 8 ending', 'Avengers 1 intro', 'Avengers 1 soundtrack', 'Avengers 1 action', 'Avengers 1 ending', 'Avengers 2 intro', 'Avengers 2 soundtrack', 'Avengers 2 action', 'Avengers 2 ending', 'Avengers 3 intro', 'Avengers 3 soundtrack', 'Avengers 3 action', 'Avengers 3 ending', 'Avengers 4 intro', 'Avengers 4 soundtrack', 'Avengers 4 action', 'Avengers 4 ending', 'Avengers 5 intro', 'Avengers 5 soundtrack', 'Avengers 5 action', 'Avengers 5 ending', 'Avengers 6 intro', 'Avengers 6 soundtrack', 'Avengers 6 action', 'Avengers 6 ending', 'Avengers 7 intro', 'Avengers 7 soundtrack', 'Avengers 7 action', 'Avengers 7 ending', 'Avengers 8 intro', 'Avengers 8 soundtrack', 'Avengers 8 action', 'Avengers 8 ending', 'Fantastic Beasts 1 intro', 'Fantastic Beasts 1 soundtrack', 'Fantastic Beasts 1 action', 'Fantastic Beasts 1 ending', 'Fantastic Beasts 2 intro', 'Fantastic Beasts 2 soundtrack', 'Fantastic Beasts 2 action', 'Fantastic Beasts 2 ending', 'Fantastic Beasts 3 intro', 'Fantastic Beasts 3 soundtrack', 'Fantastic Beasts 3 action', 'Fantastic Beasts 3 ending', 'Fantastic Beasts 4 intro', 'Fantastic Beasts 4 soundtrack', 'Fantastic Beasts 4 action', 'Fantastic Beasts 4 ending', 'Fantastic Beasts 5 intro', 'Fantastic Beasts 5 soundtrack', 'Fantastic Beasts 5 action', 'Fantastic Beasts 5 ending', 'Fantastic Beasts 6 intro', 'Fantastic Beasts 6 soundtrack', 'Fantastic Beasts 6 action', 'Fantastic Beasts 6 ending', 'Fantastic Beasts 7 intro', 'Fantastic Beasts 7 soundtrack', 'Fantastic Beasts 7 action', 'Fantastic Beasts 7 ending', 'Fantastic Beasts 8 intro', 'Fantastic Beasts 8 soundtrack', 'Fantastic Beasts 8 action', 'Fantastic Beasts 8 ending']
film_awards=['Cannes film festival best film', 'Cannes film festival best action', 'Cannes film festival best story', 'Golden globes best film', 'Golden globes best action', 'Golden globes best story', 'Oscar best film', 'Oscar best action', 'Oscar best story', 'BAFTA best film', 'BAFTA best action', 'BAFTA best story', 'Satellite best film', 'Satellite best action', 'Satellite best story', 'Saturn best film', 'Saturn best action', 'Saturn best story']
music_awards=['Cannes film festival best romantic music', 'Cannes film festival best action music', 'Cannes film festival best horror music', 'Golden globes best romantic music', 'Golden globes best action music', 'Golden globes best horror music', 'Oscar best romantic music', 'Oscar best action music', 'Oscar best horror music', 'BAFTA best romantic music', 'BAFTA best action music', 'BAFTA best horror music', 'Satellite best romantic music', 'Satellite best action music', 'Satellite best horror music', 'Saturn best romantic music', 'Saturn best action music', 'Saturn best horror music']
actor_awards=['Cannes film festival best role of the first plan', 'Cannes film festival best role of the first plan', 'Cannes film festival best action scene', 'Cannes film festival best fight', 'Cannes film festival best hero', 'Cannes film festival best villain', 'Golden globes best role of the first plan', 'Golden globes best role of the first plan', 'Golden globes best action scene', 'Golden globes best fight', 'Golden globes best hero', 'Golden globes best villain', 'Oscar best role of the first plan', 'Oscar best role of the first plan', 'Oscar best action scene', 'Oscar best fight', 'Oscar best hero', 'Oscar best villain', 'BAFTA best role of the first plan', 'BAFTA best role of the first plan', 'BAFTA best action scene', 'BAFTA best fight', 'BAFTA best hero', 'BAFTA best villain', 'Satellite best role of the first plan', 'Satellite best role of the first plan', 'Satellite best action scene', 'Satellite best fight', 'Satellite best hero', 'Satellite best villain', 'Saturn best role of the first plan', 'Saturn best role of the first plan', 'Saturn best action scene', 'Saturn best fight', 'Saturn best hero', 'Saturn best villain']
duration=['4:02', '3:26', '4:32', '4:06', '4:13', '3:52', '4:49', '4:86', '2:56', '4:51', '4:01', '3:04', '4:76', '2:99', '2:48', '2:35', '4:44', '3:43', '3:19', '2:71', '5:16', '4:69', '3:39', '2:31', '3:03', '3:20', '2:61', '3:85', '4:55', '4:95', '2:39', '3:58', '3:22', '5:16', '4:41', '3:49', '2:42', '2:46', '2:48', '4:94', '3:53', '3:17', '4:41', '3:25', '2:58', '3:16', '4:56', '4:98', '4:40', '2:35', '4:74', '2:54', '4:25', '4:64', '4:45', '4:54', '2:66', '2:57', '3:45', '4:96', '5:25', '3:79', '5:11', '4:75', '5:18', '3:99', '3:47', '3:04', '2:58', '4:99', '4:93', '3:87', '2:90', '2:46', '3:22', '5:25', '4:53', '4:62', '4:36', '2:46', '5:02', '5:00', '4:35', '3:51', '3:16', '4:41', '3:63', '4:38', '2:54', '3:94', '3:73', '2:61', '4:03', '5:12', '3:37', '3:89', '3:78', '3:56', '3:05', '3:77', '3:84', '4:71', '5:25', '4:79', '4:46', '5:13', '3:73', '3:70', '3:92', '2:96', '3:99', '3:10', '2:88', '3:46', '3:62', '3:74', '5:06', '4:72', '5:12', '5:00', '4:86', '2:74', '4:42', '4:15', '3:58', '5:05', '2:91', '3:46', '5:15', '2:55', '3:72', '2:43', '4:58', '5:09', '2:95', '4:25', '4:32', '2:62', '4:43', '4:87', '2:75', '3:01', '4:66', '2:46', '3:88', '5:22', '4:99', '4:12', '2:64', '4:30', '4:10', '4:27', '4:74', '4:98', '4:64', '4:25', '5:01', '2:89', '4:89', '4:24', '4:70', '2:99', '2:45', '3:94', '4:16', '3:62', '2:33', '4:40', '3:52', '3:03', '3:01', '2:66', '2:40', '4:11', '2:65', '2:87', '4:40', '4:36', '3:69', '5:22', '3:73', '3:62', '2:89', '2:55', '5:06', '4:91', '3:97', '3:27', '4:46', '3:07', '2:75', '4:89', '3:67', '3:04', '4:61', '2:75', '4:13', '4:01', '3:72', '5:27', '3:57', '3:32', '4:85', '5:02', '3:42', '3:22', '4:18', '2:59', '4:54', '3:45', '3:26', '4:92', '4:00', '3:14', '3:05', '3:29', '3:07', '3:71', '3:79', '3:98', '3:81', '2:58', '2:76', '2:88', '2:60', '3:68', '2:42', '3:47', '3:58', '2:68', '3:37', '5:08', '2:78', '3:33', '3:80', '4:11', '2:52', '5:09', '3:18', '4:16', '4:04', '2:74', '3:21', '4:15', '3:36', '2:68', '4:09', '4:12', '4:19', '4:02', '3:03', '2:54', '3:06', '2:74', '3:10', '3:48', '3:09', '4:84', '3:39', '3:09', '3:66', '4:62', '3:90', '3:68', '5:02', '2:66', '3:08', '2:46', '3:09', '3:35', '4:44', '4:03', '4:15', '5:26', '5:19', '4:23', '3:12', '3:96', '2:87', '4:65', '5:16', '4:76', '4:53', '2:42', '2:99', '3:34', '2:32', '3:84', '2:66', '4:28', '5:01', '4:60', '4:54', '4:02', '4:21', '2:96', '4:35', '3:85', '3:33', '2:74', '5:05', '3:30', '4:26', '2:83', '5:29', '4:82', '4:36', '3:19', '3:27', '3:84', '4:20', '3:83', '2:43', '4:09', '4:05', '5:29', '4:09', '4:81', '4:74', '3:30', '2:96', '4:35', '4:94', '3:15', '4:56', '3:22', '4:90', '4:14', '2:30', '4:87', '3:93', '4:10', '4:09', '2:90', '3:53', '2:73', '2:59', '4:35', '2:48', '4:21', '4:55', '3:13', '4:78', '2:79', '2:94', '2:81', '4:63', '2:53', '4:55', '2:69', '3:96', '4:77', '3:14', '4:80', '3:06', '5:16', '3:61', '3:71', '2:66', '5:17', '3:28', '3:31', '2:32', '5:02', '4:96', '3:75', '4:19', '3:12', '3:50', '4:50', '4:73', '4:42', '2:99', '3:72', '3:07', '4:92', '2:40', '4:44', '4:89', '3:55', '5:10', '2:99', '3:31', '4:82', '4:44', '3:23', '3:08', '3:45', '4:52', '3:87', '2:82', '4:34', '4:63', '4:66', '4:51', '3:56', '3:27', '4:32', '2:68', '2:86', '3:39', '3:98', '3:36', '2:40', '3:49', '3:99', '5:24', '3:90', '5:25', '3:55', '3:14', '2:30', '2:66', '3:71', '3:90', '5:17', '3:43', '4:61', '5:19', '4:01', '2:57', '4:95', '5:26', '3:14', '2:30', '2:38', '2:67', '3:53', '2:98', '3:95', '3:70', '3:36', '5:16', '3:29', '5:00', '2:35', '4:56', '3:91', '5:01', '3:85', '4:81', '2:99', '3:63', '2:83', '5:11', '4:93', '4:83', '4:06', '2:90', '4:98', '3:33', '4:99', '3:54', '3:73', '2:88', '2:35', '4:57', '4:11', '3:50', '5:07', '4:47', '3:68', '2:78', '4:45', '4:81', '2:97', '5:09', '4:56', '3:74', '3:72', '4:51', '3:84', '4:51', '5:01', '2:52', '4:06', '3:02', '4:48', '2:68', '2:79']


from random import randrange
import datetime
from datetime import timedelta

# birthdays=[]
# now = datetime.datetime.now()
# print(now)
# print(datetime.datetime(1970,1,1)-datetime.datetime(2000,1,1))

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    # print(delta)
    # int_delta = delta.days
    # print(int_delta)
    random_second = randrange(delta)
    return start + random_second
# duration=[]
# for i in range(len(music_title)):
#     dur=random_date(230,530)
#     duration.append(str(dur)[0]+':'+str(dur)[1:])
# print(duration)
# for i in range(120):
#     day=random_date(2015,2025)
#     years_films.append(str(day))
# print(years_films)
# mus=['intro','soundtrack','action','ending']
# film_title1=['Star Wars','Lord of the rings', 'Harry Potter', 'Fast and furious','Avatar','Transformers','Saw','Iron man', 'Thor', 'Spider man','Terminator','Star track','Pirates of Caribbean','Avengers','Fantastic Beasts']
# print(len(film_title1))
#
# for i in range(len(film_title1)):
#     for j in range(1,9):
#         s=film_title1[i]
#         s+=' '+str(j)
#         film_title.append(s)
#         for k in mus:
#             s = film_title1[i]
#             s = s + ' ' + str(j)
#             s+=' '+k
#             music_title.append(s)
# print(film_title)
# print(len(film_title))
# print(music_title)
# print(len(music_title))

people=[]
ind=0
for i in range(len(names)):
    for j in range(len(surnames)):
        if ind<40:
            people.append(['director',birthdays[ind],countries[randrange(10)],names[i],surnames[j]])
        elif ind>=40 and ind <80:
            people.append(['composer', birthdays[ind], countries[randrange(10)], names[i], surnames[j]])
        else:
            people.append(['actor', birthdays[ind], countries[randrange(10)], names[i], surnames[j]])
        # print(people[-1])
        ind += 1
# print(ind)
# print(len(birthdays))
# awards_doms=['Cannes film festival','Golden globes','Oscar','BAFTA','Satellite','Saturn']
# flms=['best film','best action','best story']
# msc=['best romantic music','best action music','best horror music']
# acts=['best role of the first plan','best role of the first plan','best action scene','best fight','best hero','best villain']
# for i in awards_doms:
#     for j in flms:
#         film_awards.append(i+' '+j)
#     for j in msc:
#         music_awards.append(i+' '+j)
#     for j in acts:
#         actor_awards.append(i+' '+j)
# print(film_awards)
# print(music_awards)
# print(actor_awards)


films=[]
music=[]
directors=[]
composer=[]
actors=[]
for i in range(len(film_title)):
    films.append([i+1,film_title[i],genres[randrange(13)],years_films[i]])
    # print(films[-1])
    # for j in range(4):
    #     music.append([i*4+j + 1,i+1,randrange(40,79), music_title[i],duration[i*4+j]])
    #     # print(music[-1])
ind=0
for i in range(len(people)):
    if people[i][0]=='director':
        for j in range(3):
            directors.append([i+1,randrange(120),people[i][1],people[i][2],people[i][3],people[i][4]])
    elif people[i][0]=='composer':
        for j in range(3):
            composer.append([i+1, randrange(120), people[i][1], people[i][2], people[i][3], people[i][4]])
    else:
        actors.append([i+1, randrange(120), people[i][1], people[i][2], people[i][3], people[i][4]])
# print(len(directors))
# print(len(composer))
# print(len(films))
for i in range(len(films)):
    directors[i][1]=films[i][0]
    composer[i][1] = films[i][0]

# print(composer)
# print(directors)
# print(composer)
music=[]
for i in range(len(films)):
    comps=[]
    for j in composer:
        if j[1]==i+1:
            comps.append(j[0])
    # print(len(comps))
    for j in range(4):
        ig=random_date(0,len(comps))
        music.append([i*4+j + 1,i+1,comps[ig], music_title[i*4+j],duration[i*4+j]])

# print(music)
film_aw=[]
act_aw=[]
mus_aw=[]
ind=0
for i in range(2015,2026):
    year=[]
    acts=[]
    comps=[]
    dirs=[]

    for j in films:
       if j[-1]==str(i):
           year.append(j[0])
    if len(year)>0:
        ac=random_date(0,len(year))
        # print(ac)
        for j in actors:
           if j[1] ==ac:
               acts.append([j[0],j[1]])
        ac = random_date(0, len(year))
        for j in composer:
           if j[1] ==ac:
               comps.append([j[0],j[1]])
        ac = random_date(0, len(year))
        for j in directors:
           if j[1] ==ac:
               dirs.append([j[0],j[1]])
    # print(len(comps),len(acts),len(dirs))

    for j in actor_awards:
        if len(acts)>0:
            ig=random_date(0,len(acts))
            act_aw.append([acts[ig][0],acts[ig][1],j,i,'winner',len(act_aw)+1])


    for j in film_awards:
        if len(dirs)>0:
            ig=random_date(0,len(dirs))
            film_aw.append([dirs[ig][0],j,i,'winner',dirs[ig][1],len(film_aw)+1])


    for j in music_awards:
        if len(comps)>0:
            ig=random_date(0,len(comps))
            mus_aw.append([comps[ig][0],comps[ig][1],j,i,'winner',len(mus_aw)+1])
    ind+=1
print('--')
print(mus_aw)
# print(directors)
path='C:\\Users\\Евгений\\Documents\\db\\'
with open(path+'film.txt','w') as filmf:
    for i in range(len(films)):
        s='('+str(films[i][0])+', '+'\''+films[i][1]+'\''+', '+'\''+films[i][2]+'\''+', '+films[i][3]+')'+','+'\n'
        # print(s)
        filmf.write(s)
with open(path+'director.txt','w') as dirf:
    for i in range(len(directors)):
        s='('+str(directors[i][0])+', '+str(directors[i][1])+', '+'\''+directors[i][2]+'\''+', '+'\''+directors[i][3]+'\''+', '+'\''+directors[i][4]+'\''+', '+'\''+directors[i][5]+'\''+')'+','+'\n'
        # print(s)
        dirf.write(s)
with open(path+'composer.txt','w') as compf:
    for i in range(len(composer)):
        s='('+'\''+composer[i][2]+'\''+', '+'\''+composer[i][3]+'\''+', '+'\''+composer[i][4]+'\''+', '+'\''+composer[i][5]+'\''+', '+str(composer[i][0])+', '+str(composer[i][1])+')'+','+'\n'
        # print(s)
        compf.write(s)
with open(path+'actor.txt','w') as actf:
    for i in range(len(actors)):
        s='('+str(actors[i][0])+', '+str(actors[i][1])+', '+'\''+actors[i][2]+'\''+', '+'\''+actors[i][3]+'\''+', '+'\''+actors[i][4]+'\''+', '+'\''+actors[i][5]+'\''+')'+','+'\n'
        # print(s)
        actf.write(s)
print(music)
with open(path+'music.txt','w') as musf:
    for i in range(len(music)):
        s='('+str(music[i][0])+', '+str(music[i][1])+', '+str(music[i][2])+', '+'\''+music[i][3]+'\''+', '+'\''+music[i][4]+'\''+')'+','+'\n'
        # print(s)
        musf.write(s)
print(film_aw)
with open(path+'film_aw.txt','w') as film_awf:
    for i in range(len(film_aw)):
        s='('+str(film_aw[i][0])+', '+'\''+film_aw[i][1]+'\''+', '+str(film_aw[i][2])+', '+'\''+film_aw[i][3]+'\''+', '+str(film_aw[i][4])+', '+str(film_aw[i][5])+')'+','+'\n'
        # print(s)
        film_awf.write(s)
with open(path+'mus_aw.txt','w') as mus_awf:
    for i in range(len(mus_aw)):
        s='('+str(mus_aw[i][5])+', '+str(mus_aw[i][1])+', '+'\''+mus_aw[i][2]+'\''+', '+str(mus_aw[i][3])+', '+'\''+mus_aw[i][4]+'\''+')'+','+'\n'
        # print(s)
        mus_awf.write(s)
print(len(act_aw))
with open(path+'act_aw.txt','w') as act_awf:
    for i in range(len(act_aw)):
        s='('+str(act_aw[i][0])+', '+str(act_aw[i][1])+', '+'\''+act_aw[i][2]+'\''+', '+str(act_aw[i][3])+', '+'\''+act_aw[i][4]+'\''+', '+str(act_aw[i][5])+')'+','+'\n'
        # print(s)
        act_awf.write(s)
premiere=[]
start_period=[]
end_period=[0 for i in range(len(years_films))]
# print(datetime.datetime(int(years_films[0]),1,1)+timedelta(31))
for i in years_films:
    start_period.append(datetime.datetime(int(i),1,1))
# print(start_period)
for i in range(10):
    # time = datetime.datetime(int(start_period[j]), 1, 1) +timedelta(31)

    for j in range(len(films)):
        for k in countries:
            num = random_date(1, 10)
            premiere.append([films[j][0],k,start_period[j].strftime("%Y-%m-%d"),num,(start_period[j]+timedelta(31)).strftime("%Y-%m-%d")])
        start_period[j]+=timedelta(31)
with open(path+'prem.txt','w') as premf:
    for i in range(len(premiere)):
        s='('+str(premiere[i][0])+', '+'\''+premiere[i][1]+'\''+', '+'\''+premiere[i][2]+'\''+', '+str(premiere[i][3])+', '+'\''+premiere[i][4]+'\''+')'+','+'\n'
        # print(s)
        premf.write(s)