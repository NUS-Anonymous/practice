from file import File

def read_file(index):
    directory = "final_round_2019.in/"
    file_name = ["a_example.in", "b_narrow.in", "c_urgent.in", "d_typical.in", "e_intriguing.in", "f_big.in"]
    file_path = directory + file_name[index]
    files = {}
    targets = {}
    with open(file_path) as fp:
        # 6 files, 3 targets, 2 servers
        [num_of_file, num_of_target, num_of_server] = fp.readline().split()
        print("-----------------------------------")
        print("files {} targets {} server {}".format(num_of_file, num_of_target, num_of_server))
        for i in range(int(num_of_file)):
            [name, compile_time, replicate_time] = fp.readline().strip().split()
            dependency_data = fp.readline().strip().split()
            dependency_files = []
            for j in range(int(dependency_data[0])):
                dependency_files.append(dependency_data[j+1])
            files[name] = (File(name, int(compile_time), int(replicate_time), dependency_files))
        for i in range(int(num_of_target)):
            [name, deadline, point] = fp.readline().strip().split()
            targets[name] = (int(deadline), int(point))
    return files, targets, num_of_server


def get_min_compile_time(target_file, files):
    time_list = []
    dfs(target_file, 0, time_list, files)
    return max(time_list)


def dfs(file, time, time_list, files):
    time += file.compile_time
    if not file.dependency:
        time_list.append(time)
    else:
        for f in file.dependency:
            dfs(files[f], time, time_list, files)


def main():
    print("This is Main")
    files, targets, num_of_server = read_file(0)
    for file_name, (deadline, point) in list(targets.items()):
        min_compile_time = get_min_compile_time(files[file_name], files)
        if min_compile_time > deadline:
            targets.pop(file_name)

    print(targets.items())


if __name__ == "__main__":
    main()



