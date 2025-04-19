DROP FUNCTION IF EXISTS get_paginated_users(INT, INT);

CREATE OR REPLACE FUNCTION get_paginated_users(p_limit INT, p_offset INT)
RETURNS TABLE(user_id INT, username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT PhoneBook.id, PhoneBook.username, PhoneBook.phone
    FROM PhoneBook
    ORDER BY PhoneBook.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
