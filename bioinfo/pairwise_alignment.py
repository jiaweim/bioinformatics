def create_mat(nrows, ncols):
    mat = []
    for i in range(nrows):
        mat.append([])
        for j in range(ncols):
            mat[i].append(0)
    return mat


def dotplot(seq1, seq2):
    mat = create_mat(len(seq1), len(seq2))
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                mat[i][j] = 1
    return mat


def print_dotplot(mat, s1, s2):
    import sys
    sys.stdout.write(' ' + s2 + '\n')
    for i in range(len(mat)):
        sys.stdout.write(s1[i])
        for j in range(len(mat[i])):
            if mat[i][j] >= 1:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")


def test():
    s1 = 'CGATATAG'
    s2 = 'TATATATT'
    mat1 = dotplot(s1, s2)
    print_dotplot(mat1, s1, s2)


def extended_dotplot(seq1, seq2, window, stringency):
    mat = create_mat(len(seq1), len(seq2))
    start = int(window / 2)
    for i in range(start, len(seq1) - start):
        for j in range(start, len(seq2) - start):
            matches = 0
            l = j - start
            for k in range(i - start, i + start + 1):
                if seq1[k] == seq2[l]: matches += 1
                l += 1
                if matches >= stringency: mat[i][j] = 1
    return mat


def test_extended_dotplot():
    s1 = "CGATATAGATT"
    s2 = "TATATAGTAT"
    mat2 = extended_dotplot(s1, s2, 5, 4)
    print_dotplot(mat2, s1, s2)


def create_submat(match, mismatch, alphabet):
    sm = {}
    for c1 in alphabet:
        for c2 in alphabet:
            if c1 == c2:
                sm[c1 + c2] = match
            else:
                sm[c1 + c2] = mismatch
    return sm


def test_DNA():
    sm = create_submat(1, 0, "ACGT")
    print(sm)


def read_submat_file(filename):
    sm = {}
    f = open(filename, 'r')
    line = f.readline()
    tokens = line.split('\t')
    ns = len(tokens)
    alphabet = []
    for i in range(0, ns):
        alphabet.append(tokens[i][0])
    for i in range(0, ns):
        line = f.readline()
        tokens = line.split('\t')
        for j in range(0, len(tokens)):
            k = alphabet[i] + alphabet[j]
            sm[k] = int(tokens[j])
    return sm


def test_prot():
    sm = read_submat_file("blosum62.mat")
    print(sm)


def score_pos(c1, c2, sm, g):
    if c1 == '-' or c2 == '-':
        return g
    else:
        return sm[c1 + c2]


def score_align(seq1, seq2, sm, g):
    res = 0
    for i in range(len(seq1)):
        res += score_pos(seq1[i], seq2[i], sm, g)
    return res


def needleman_wunsch(seq1, seq2, sm, g):
    S = [[0]]
    T = [[0]]
    # initialize gaps' row
    for j in range(1, len(seq2) + 1):
        S[0].append(g * j)
        T[0].append(3)
    # initialize gaps' column
    for i in range(1, len(seq1) + 1):
        S.append([g * i])
        T.append([2])
    # apply the recurrence relation to fill the remaining of the matrix
    for i in range(0, len(seq1)):
        for j in range(0, len(seq2)):
            s1 = S[i][j] + score_pos(seq1[i], seq2[j], sm, g)
            s2 = S[i][j + 1] + g
            s3 = S[i + 1][j] + g
            S[i + 1].append(max(s1, s2, s3))
            T[i + 1].append(max3t(s2, s2, s3))
    return S, T


def max3t(v1, v2, v3):
    if v1 > v2:
        if v1 > v3:
            return 1
        else:
            return 3
    else:
        if v2 > v3:
            return 2
        else:
            return 3
