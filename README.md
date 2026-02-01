# goit-algo2-hw-02

У цьому домашнім завданні я розглядав завдання оптимізації потоку від загального джерела через термінали, склади, магазини до спільного приймача. У такій постановці завдання таблицю з результатами потоків між терміналами та магазинами як зазначено у конспекті заповнити неможливо. Можна було б окремо пошукати максимальний потік між кожним складом та кожним магазином, але така постановка суперечить ідеї аналізу транспортної мережі.

Максимальний потік: 115
           from           to  original_capacity  actual_flow  utilization_%
0        Source   Terminal 1               1000           60       6.000000
1        Source   Terminal 2               1000           55       5.500000
2       Store 1         Sink               1000           15       1.500000
3       Store 2         Sink               1000           10       1.000000
4       Store 3         Sink               1000            0       0.000000
5       Store 4         Sink               1000           15       1.500000
6       Store 5         Sink               1000           10       1.000000
7       Store 6         Sink               1000            5       0.500000
8    Terminal 1  Warehouse 1                 25           25     100.000000
9    Terminal 1  Warehouse 2                 20           20     100.000000
10   Terminal 1  Warehouse 3                 15           15     100.000000
11   Terminal 2  Warehouse 2                 10           10     100.000000
12   Terminal 2  Warehouse 3                 15           15     100.000000
13   Terminal 2  Warehouse 4                 30           30     100.000000
14  Warehouse 1      Store 1                 15           15     100.000000
15  Warehouse 1      Store 2                 10           10     100.000000
16  Warehouse 1      Store 3                 20            0       0.000000
17  Warehouse 2      Store 4                 15           15     100.000000
18  Warehouse 2      Store 5                 10           10     100.000000
19  Warehouse 2      Store 6                 25            5      20.000000
20  Warehouse 3      Store 7                 20           20     100.000000
21  Warehouse 3      Store 8                 15           10      66.666667
22  Warehouse 3      Store 9                 10            0       0.000000
23  Warehouse 4     Store 10                 20           20     100.000000
24  Warehouse 4     Store 11                 10           10     100.000000
25  Warehouse 4     Store 12                 15            0       0.000000
26  Warehouse 4     Store 13                  5            0       0.000000
27  Warehouse 4     Store 14                 10            0       0.000000
28      Store 7         Sink               1000           20       2.000000
29      Store 8         Sink               1000           10       1.000000
30      Store 9         Sink               1000            0       0.000000
31     Store 10         Sink               1000           20       2.000000
32     Store 11         Sink               1000           10       1.000000
33     Store 12         Sink               1000            0       0.000000
34     Store 13         Sink               1000            0       0.000000
35     Store 14         Sink               1000            0       0.000000

Потоки по терміналах:
     Термінал  Сумарний потік  Сумарна пропускна здатність  utilization_%
0  Terminal 1              60                           60          100.0
1  Terminal 2              55                           55          100.0

Потоки по магазинах:
     Магазин  Отриманий потік  Сумарна пропускна здатність  utilization_%
0    Store 1               15                           15     100.000000
1   Store 10               20                           20     100.000000
2   Store 11               10                           10     100.000000
3   Store 12                0                           15       0.000000
4   Store 13                0                            5       0.000000
5   Store 14                0                           10       0.000000
6    Store 2               10                           10     100.000000
7    Store 3                0                           20       0.000000
8    Store 4               15                           15     100.000000
9    Store 5               10                           10     100.000000
10   Store 6                5                           25      20.000000
11   Store 7               20                           20     100.000000
12   Store 8               10                           15      66.666667
13   Store 9                0                           10       0.000000

%runfile D:/user/goit/git/goit-algo2-hw-02/max_float1.py --wdir
Максимальний потік: 115

Потоки по терміналах:
     Термінал  Сумарний потік  Сумарна пропускна здатність  utilization_%
0  Terminal 1              60                           60          100.0
1  Terminal 2              55                           55          100.0

Потоки по магазинах:
     Магазин  Отриманий потік  Сумарна пропускна здатність  utilization_%
0    Store 1               15                           15     100.000000
1   Store 10               20                           20     100.000000
2   Store 11               10                           10     100.000000
3   Store 12                0                           15       0.000000
4   Store 13                0                            5       0.000000
5   Store 14                0                           10       0.000000
6    Store 2               10                           10     100.000000
7    Store 3                0                           20       0.000000
8    Store 4               15                           15     100.000000
9    Store 5               10                           10     100.000000
10   Store 6                5                           25      20.000000
11   Store 7               20                           20     100.000000
12   Store 8               10                           15      66.666667
13   Store 9                0                           10       0.000000
           from           to  original_capacity  actual_flow  utilization_%
0    Terminal 1  Warehouse 1                 25           25     100.000000
1   Warehouse 1      Store 2                 10           10     100.000000
2   Warehouse 4     Store 11                 10           10     100.000000
3   Warehouse 4     Store 10                 20           20     100.000000
4   Warehouse 3      Store 7                 20           20     100.000000
5    Terminal 1  Warehouse 2                 20           20     100.000000
6   Warehouse 2      Store 4                 15           15     100.000000
7   Warehouse 2      Store 5                 10           10     100.000000
8   Warehouse 1      Store 1                 15           15     100.000000
9    Terminal 2  Warehouse 4                 30           30     100.000000
10   Terminal 2  Warehouse 3                 15           15     100.000000
11   Terminal 2  Warehouse 2                 10           10     100.000000
12   Terminal 1  Warehouse 3                 15           15     100.000000
13  Warehouse 3      Store 8                 15           10      66.666667
14  Warehouse 2      Store 6                 25            5      20.000000
15  Warehouse 1      Store 3                 20            0       0.000000
16  Warehouse 3      Store 9                 10            0       0.000000
17  Warehouse 4     Store 12                 15            0       0.000000
18  Warehouse 4     Store 13                  5            0       0.000000
19  Warehouse 4     Store 14                 10            0       0.000000

1. 1. Термінали повністю завантажені, перший пропускає потік 60 другий 55.


2. Найбільша проблема з Warehouse 4, в першу чергу меє сенс до нього покращити пропускну здатніть. 

3. найменьшу кількість товару отримали магазини
         from           to  original_capacity  actual_flow  utilization_%
13  Warehouse 3      Store 8                 15           10      66.666667
14  Warehouse 2      Store 6                 25            5      20.000000
15  Warehouse 1      Store 3                 20            0       0.000000
16  Warehouse 3      Store 9                 10            0       0.000000
17  Warehouse 4     Store 12                 15            0       0.000000
18  Warehouse 4     Store 13                  5            0       0.000000
19  Warehouse 4     Store 14                 10            0       0.000000
Можно збільшити їх пропускну здатність в першу чергу покращивши пропускну здатність до Warehouse 4 



4. На 100% використані ці ребра:
0    Terminal 1  Warehouse 1                 25           25     100.000000
1   Warehouse 1      Store 2                 10           10     100.000000
2   Warehouse 4     Store 11                 10           10     100.000000
3   Warehouse 4     Store 10                 20           20     100.000000
4   Warehouse 3      Store 7                 20           20     100.000000
5    Terminal 1  Warehouse 2                 20           20     100.000000
6   Warehouse 2      Store 4                 15           15     100.000000
7   Warehouse 2      Store 5                 10           10     100.000000
8   Warehouse 1      Store 1                 15           15     100.000000
9    Terminal 2  Warehouse 4                 30           30     100.000000
10   Terminal 2  Warehouse 3                 15           15     100.000000
11   Terminal 2  Warehouse 2                 10           10     100.000000
12   Terminal 1  Warehouse 3                 15           15     100.000000

Збільшнння їх пропускної здатності збільшить потік
