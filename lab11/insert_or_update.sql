CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE username = p_name) THEN
        UPDATE PhoneBook SET phone = p_phone WHERE username = p_name;
    ELSE
        INSERT INTO PhoneBook(username, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
