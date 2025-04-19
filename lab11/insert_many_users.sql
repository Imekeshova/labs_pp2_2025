-- Создаём или заменяем процедуру insert_many_users
CREATE OR REPLACE PROCEDURE insert_many_users(usernames TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;  -- Индекс для перебора элементов массива
    incorrect_data TEXT[] := '{}';  -- Список для хранения некорректных данных
BEGIN
    FOR i IN 1..array_length(usernames, 1) LOOP
        -- Проверка: номер телефона должен содержать только цифры
        IF phones[i] ~ '^\d+$' THEN
            -- Если пользователь уже существует — обновляем номер
            IF EXISTS (SELECT 1 FROM PhoneBook WHERE username = usernames[i]) THEN
                UPDATE PhoneBook SET phone = phones[i] WHERE username = usernames[i];
            ELSE
                -- Иначе вставляем нового пользователя
                INSERT INTO PhoneBook(username, phone) VALUES (usernames[i], phones[i]);
            END IF;
        ELSE
            -- Если номер некорректный — добавляем в список ошибок
            incorrect_data := array_append(incorrect_data, usernames[i] || ' -> ' || phones[i]);
        END IF;
    END LOOP;

    -- Показываем список ошибок, если есть
    RAISE NOTICE 'Некорректные данные: %', incorrect_data;
END;
$$;
