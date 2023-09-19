def count_substring(st, s):
    count = 0
    for i in range(len(st)):
        if st.startswith(s, i):
            count += 1
    return count