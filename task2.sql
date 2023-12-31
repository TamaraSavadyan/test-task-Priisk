/*task 1*/
SELECT
    Абоненты.ФИО,
    Звонки.время_разговора
FROM
    Звонки
JOIN
    Абоненты ON Звонки.номер_телефона = Абоненты.телефон
WHERE
    Звонки.дата_разговора BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '1 DAY';

/*task 2*/
SELECT
    номер_телефона,
    дата_разговора,
    время_разговора
FROM
    Звонки
WHERE
    дата_разговора BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '1 DAY'
    AND время_разговора > 5;

/*task 3*/
SELECT
    з1.номер_телефона,
    з1.дата_разговора,
    з1.время_разговора
FROM
    Звонки з1
LEFT JOIN
    Звонки з2 ON з1.номер_телефона = з2.номер_телефона
    AND з1.дата_разговора > з2.дата_разговора
    AND з1.дата_разговора - з2.дата_разговора <= INTERVAL '5 MINUTE';

/*task 4*/
SELECT
    А.ФИО AS Абонент,
    COUNT(З.номер_телефона) AS Количество_звонков,
    AVG(З.время_разговора) AS Средняя_длительность,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY З.время_разговора) AS Медиана,
    MAX(З.время_разговора) - MIN(З.время_разговора) AS Размах
FROM
    Звонки З
JOIN
    Абоненты А ON З.номер_телефона = А.телефон
GROUP BY
    А.ФИО;

