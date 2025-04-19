-- Создаём или заменяем процедуру delete_user
-- Принимает два параметра: имя или номер
CREATE OR REPLACE PROCEDURE delete_user(p_username TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Удаляем пользователя, если имя или номер совпадают
    DELETE FROM PhoneBook
    WHERE username = p_username OR phone = p_phone;
END;
$$;
    