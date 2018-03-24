def same_files(path1, path2):
    import os

    count = 0
    file_list1 = os.listdir(path1)
    file_list2 = os.listdir(path2)

    for i in file_list1:
        for j in file_list2:
            if i == j:
                print(i)
                file_list2.pop(file_list2.index(j))
                count += 1
                continue
    print("\n{} Similar files/folder Found".format(count))


def diff_files(path1, path2):
    import os

    count = 0
    temp = 0
    file_list1 = os.listdir(path1)
    file_list2 = os.listdir(path2)

    for i in file_list1:
        for j in file_list2:
            if i == j:
                count += 1
                file_list2.pop(file_list2.index(j))
        if count == 0:
            print(i)
            temp += 1
    for i in file_list2:
        print(i)
        temp += 1
    print("\n{} Different files/folders Found".format(temp))


def sync_files(path1, path2):
    import os

    count = 0
    temp = 0
    sync_list1 = []
    sync_list2 = []
    file_list1 = os.listdir(path1)
    file_list2 = os.listdir(path2)

    for i in file_list1:
        for j in file_list2:
            if i == j:
                count += 1
                file_list2.pop(file_list2.index(j))
        if count == 0:
            sync_list1.append(i)
            temp += 1
    for i in file_list2:
        sync_list2.append(i)
        temp += 1

    for i in sync_list1:
        os.system(f'copy "{path1}\\{i}" "{path2}"')
    for i in sync_list2:
        os.system(f'copy "{path2}\\{i}" "{path1}"')