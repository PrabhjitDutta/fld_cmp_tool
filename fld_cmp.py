def same(path1, path2):

    """
        Compare directories for similar files/folders.

        :argument path1: Address of first directory.

        :argument path2: Address of second directory.

        :return: list of similar files/folders.

    """

    import os

    count = 0
    file_list1 = os.listdir(path1)
    file_list2 = os.listdir(path2)
    return_list = []

    for i in file_list1:
        for j in file_list2:
            if i == j:
                return_list.append(i)
                file_list2.pop(file_list2.index(j))
                count += 1
                continue

    return return_list


def diff(path1, path2):

    """
        Compare directories for different files/folders.

        :argument path1: Address of first directory.

        :argument path2: Address of second directory.

        :return: list of different files/folders.

    """

    import os

    count = 0
    temp = 0
    return_list = []
    file_list1 = os.listdir(path1)
    file_list2 = os.listdir(path2)

    for i in file_list1:
        for j in file_list2:
            if i == j:
                count += 1
                file_list2.pop(file_list2.index(j))
        if count == 0:
            return_list.append(i)
            temp += 1
    for i in file_list2:
        return_list.append(i)
        temp += 1

    return return_list


def sync(path1, path2):

    """
        Syncs two directories.

        :argument path1: Address of first directory.

        :argument path2: Address of second directory.

    """

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
