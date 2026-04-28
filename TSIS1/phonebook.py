import json
from connect import get_connection

# ---------------- DB ----------------
def fetch(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or ())
    data = cur.fetchall()
    conn.close()
    return data

def run(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or ())
    conn.commit()
    conn.close()

# ---------------- ADD CONTACT ----------------
def add_contact(name, email, birthday, group, phone, ptype):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES (%s,%s,%s,(SELECT id FROM groups WHERE name=%s))
        RETURNING id
    """, (name,email,birthday,group))

    cid = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO phones(contact_id,phone,type)
        VALUES (%s,%s,%s)
    """, (cid,phone,ptype))

    conn.commit()
    conn.close()

# ---------------- DELETE ----------------
def delete_contact(name):
    run("DELETE FROM contacts WHERE name=%s", (name,))
    print("Deleted")

# ---------------- VIEW ALL ----------------
def view_all():
    return fetch("""
        SELECT c.name,c.email,p.phone,p.type,g.name
        FROM contacts c
        LEFT JOIN phones p ON c.id=p.contact_id
        LEFT JOIN groups g ON c.group_id=g.id
        ORDER BY c.name
    """)

# ---------------- SEARCH ----------------
def search(q):
    return fetch("SELECT * FROM search_contacts(%s)", (q,))

# ---------------- FILTER ----------------
def by_group(g):
    return fetch("""
        SELECT c.name,c.email,p.phone,p.type,g.name
        FROM contacts c
        LEFT JOIN phones p ON c.id=p.contact_id
        JOIN groups g ON c.group_id=g.id
        WHERE g.name=%s
    """, (g,))

# ---------------- EMAIL SEARCH ----------------
def email_search(e):
    return fetch("""
        SELECT c.name,c.email,g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        WHERE c.email ILIKE %s
    """, (f"%{e}%",))

# ---------------- SORT ----------------
def sort_contacts(f):
    col = {
        "name":"c.name",
        "birthday":"c.birthday",
        "date":"c.created_at"
    }.get(f,"c.name")

    return fetch(f"""
        SELECT c.name,c.email,c.birthday,g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        ORDER BY {col}
    """)

# ---------------- PAGINATION ----------------
def paginate(page,size=5):
    off = (page-1)*size
    return fetch("""
        SELECT c.name,c.email,c.birthday,g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        ORDER BY c.name
        LIMIT %s OFFSET %s
    """,(size,off))

# ---------------- JSON EXPORT ----------------
def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id,name,email,birthday FROM contacts")
    data = cur.fetchall()

    result = []

    for c in data:
        cur.execute("SELECT phone,type FROM phones WHERE contact_id=%s",(c[0],))
        phones = cur.fetchall()

        result.append({
            "name":c[1],
            "email":c[2],
            "birthday":str(c[3]),
            "phones":[{"phone":p[0],"type":p[1]} for p in phones]
        })

    conn.close()

    with open("contacts.json","w") as f:
        json.dump(result,f,indent=4)

# ---------------- IMPORT JSON ----------------
def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    for c in data:
        exists = fetch("SELECT id FROM contacts WHERE name=%s",(c["name"],))

        if exists:
            choice = input(f"{c['name']} exists skip/overwrite: ")
            if choice=="skip":
                continue
            run("DELETE FROM contacts WHERE name=%s",(c["name"],))

        # create contact (default group Other)
        add_contact(
            c["name"],
            c["email"],
            c["birthday"],
            "Other",
            c["phones"][0]["phone"],
            c["phones"][0]["type"]
        )

# ---------------- MENU ----------------
def menu():
    page=1

    while True:
        print("""
1 Add
2 Search
3 Group
4 Email
5 Sort
6 View All
7 Next Page
8 Export JSON
9 Import JSON
10 Delete
11 Quit
""")

        cmd=input("> ")

        if cmd=="1":
            add_contact(
                input("name:"),
                input("email:"),
                input("birthday:"),
                input("group:"),
                input("phone:"),
                input("type:")
            )

        elif cmd=="2":
            print(search(input("query:")))

        elif cmd=="3":
            print(by_group(input("group:")))

        elif cmd=="4":
            print(email_search(input("email:")))

        elif cmd=="5":
            print(sort_contacts(input("name/birthday/date:")))

        elif cmd=="6":
            print(view_all())

        elif cmd=="7":
            print(paginate(page))
            act=input("next/prev/quit:")
            if act=="next": page+=1
            elif act=="prev": page=max(1,page-1)

        elif cmd=="8":
            export_json()

        elif cmd=="9":
            import_json()

        elif cmd=="10":
            delete_contact(input("name:"))

        elif cmd=="11":
            break

if __name__=="__main__":
    menu()