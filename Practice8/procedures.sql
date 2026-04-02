CREATE OR REPLACE PROCEDURE upsert_user(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE first_name = p_name) THEN
        UPDATE PhoneBook
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO PhoneBook(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_insert_users(users JSON)
LANGUAGE plpgsql
AS $$
DECLARE
    u JSON;
    invalid_data JSON := '[]'::json;
BEGIN
    FOR u IN SELECT * FROM json_array_elements(users)
    LOOP
        IF u->>'phone' ~ '^[0-9 -]+$' THEN
            CALL upsert_user(u->>'name', u->>'phone');
        ELSE
            invalid_data := invalid_data || json_build_object(
                'name', u->>'name',
                'phone', u->>'phone'
            );
        END IF;
    END LOOP;
    RAISE NOTICE 'Некорректные данные: %', invalid_data;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_user(
    p_name VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM PhoneBook
    WHERE (p_name IS NOT NULL AND first_name = p_name)
       OR (p_phone IS NOT NULL AND phone = p_phone);
END;
$$;