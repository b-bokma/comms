# table overview, used for the main page table
table_overview = '''
SELECT id,subject, status, deadline
FROM (SELECT 
        questions.id, 
        status.status, 
        questions.subject, 
        journalists.first_name || ' ' || journalists.middle_name || ' ' || journalists.last_name AS journalist, 
        media.name AS media, 
        spokespersons.first_name || ' ' || spokespersons.middle_name || ' ' || spokespersons.last_name AS spokesperson, 
        questions.created_on,
        questions.deadline
        FROM
        questions
        JOIN status ON status.id = questions.status_id
        JOIN spokespersons ON spokespersons.id = questions.spokesperson_id
        JOIN questionjournalistmap ON questionjournalistmap.question_id = questions.id
        JOIN journalists ON questionjournalistmap.journalist_id = journalists.id
        JOIN journalistmediamap ON journalistmediamap.journalist_id = journalists.id
        JOIN media ON journalistmediamap.media_id = media.id
        )
        GROUP BY ID;
        '''

question_page = '''
SELECT 
        questions.id, 
        questions.subject,
        questions.question,
        questions.created_on,
        questions.deadline,
        status.status, 
        journalists.first_name || ' ' || journalists.middle_name || ' ' || journalists.last_name AS journalist, 
        media.name AS media, 
        spokespersons.first_name || ' ' || spokespersons.middle_name || ' ' || spokespersons.last_name AS spokesperson, 
        users.username
    FROM
        questions
        LEFT JOIN status ON status.id = questions.status_id
        LEFT JOIN spokespersons ON spokespersons.id = questions.spokesperson_id
        LEFT JOIN users ON users.id = questions.created_by
        
        LEFT JOIN questionjournalistmap ON questionjournalistmap.question_id = questions.id
        LEFT JOIN questiondossiermap ON questiondossiermap.question_id = questions.id
        LEFT JOIN journalists ON questionjournalistmap.journalist_id = journalists.id

        LEFT JOIN journalistmediamap ON journalistmediamap.journalist_id = journalists.id
        LEFT JOIN media ON journalistmediamap.media_id = media.id
;
'''
