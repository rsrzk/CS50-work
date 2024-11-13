SELECT title FROM movies
    JOIN
    (
        SELECT movie_id
        FROM stars
        JOIN people
        ON stars.person_id = people.id
        WHERE name IN ('Jennifer Lawrence', 'Bradley Cooper')
        GROUP BY movie_id
        HAVING COUNT(DISTINCT name) = 2
    ) AS filter
    ON movies.id = filter.movie_id;

-- reference: https://stackoverflow.com/questions/43394975/sqlite-select-row-with-multiple-condition-from-other-table


