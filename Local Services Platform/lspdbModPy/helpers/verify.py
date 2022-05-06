from config.config import connect

# Returns an empty list if no users are found. E.j.:"if not veriyfyUser(...)" evaluates to True if no user is found.
def verifyUser(cursor, u_id):
    # Check list of users to see if they are registered
    test_query = "\
    select U_Id \
    from users \
    where U_Id = %s"
    cursor.execute(test_query, (u_id,))

    return cursor.fetchone()


# Returns an empty list if no posts are found. E.j.:"if not veriyfyPost(...)" evaluates to True if no post is found.
def verifyPost(cursor, c_id):
    # Checking if post exists
    test_query = "select c_id from chirps where c_id = %s;"
    cursor.execute(test_query, (c_id,))

    return cursor.fetchone()