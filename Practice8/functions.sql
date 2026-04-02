CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
RETURNS TABLE(first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.first_name, pb.phone
    FROM PhoneBook pb
    WHERE pb.first_name ILIKE '%' || p_pattern || '%'
       OR pb.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_phonebook_page(p_offset INT, p_limit INT)
RETURNS TABLE(first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.first_name, pb.phone
    FROM PhoneBook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;