    # several arguments
        # starts with '--' means option, can be anywhere
        # pattern always before file names, one pattern only
        # hidden or not
        # can be no pattern
        # can be no file name --> current directory
        # (given directory: /tmp/guest-cmiet0/Documents/)
        # recursive search: sub dirs
# print file name in green

#for directory in directories:
#    print(os.path.join(root, directory))
# print(file_path.read())


def find_pattern_in_file(file_path, pattern, option):
    with open(file_path) as target_file:
        count_lines = 0
        contents = dict()
        for line in target_file:
            count_lines += 1
            contents[count_lines] = [line.strip('\n')]
    for order, line in contents.items():  # scan each line for the pattern
        if option == '--case-sensitive':
            if pattern in line[0]:  # because type(line) is list
                lines_w_pattern[order] = ':' + line[0]
        elif option == '':
            if pattern.lower() in line[0].lower():  # type(line) is list
                lines_w_pattern[order] = ':' + line[0]
    return lines_w_pattern  # for later use in color function


def print_in_colors(lines_w_pattern, pattern, option):
    if lines_w_pattern != {}:
        print('\033[1;32m' + file_path.replace(os.getcwd(), '') + '\033[0m')
        if option == '--case-sensitive':
            for order, line in sorted(lines_w_pattern.items()):
                start_i = line.find(pattern)  # line[0:2] = '1:'
                end_i = start_i + len(pattern)
                colored_pattern = '\033[30;43m' + pattern + '\033[0m'
                colored_order = '\033[1;33m' + str(order) + '\033[0m'
                print(colored_order + line.replace(pattern, colored_pattern))
        elif option == '':  # case-insensitive
            for order, line in sorted(lines_w_pattern.items()):
                matched_ps = []
                colored_ps = []
                for i in range(len(line)):
                    start_i = line[i:].lower().find(pattern.lower())
                    if start_i < 0:
                        break
                    end_i = start_i + len(pattern)
                    if end_i > len(line[i:]):
                        break
                    matched_ps.append(line[i:][start_i:end_i])
                matched_ps = list(set(matched_ps))
                for matched_p in matched_ps:
                    colored_ps.append('\033[30;43m' + matched_p + '\033[0m')
                colored_order = '\033[1;33m' + str(order) + '\033[0m'
                pre_output = line
                for i in range(len(colored_ps)):
                    pre_output = pre_output.replace(matched_ps[i], colored_ps[i])
                print(colored_order + pre_output)


import os
import sys
lines_w_pattern = dict()  # global
file_paths = []  # global
subdirs_n_files = []  # global
option = ''
option_hid = ''

current_dirs_n_files = os.listdir(os.getcwd())  # list
inputs = sys.argv[1:]
for input in inputs:
    if input == '--case-sensitive':
        option = input
        inputs.remove(input)
    elif input == '--hidden':
        option_hid = input
        inputs.remove(input)
    if input not in current_dirs_n_files:
        pattern = input
    elif input in current_dirs_n_files:
        subdirs_n_files.append(input)

if subdirs_n_files != []:
    if option_hid == '--hidden':
        for subdir_n_file in subdirs_n_files:
            for root, dirs, files in os.walk(subdir_n_file):
                if files != []:
                    for file in files:
                        file_paths.append(os.path.join(root,file))
                elif files == []:
                    file_paths.append(os.path.join(subdir_n_file))
    elif option_hid == '':
        for subdir_n_file in subdirs_n_files:
            for root, dirs, files in os.walk(subdir_n_file):
                if files != []:
                    for file in files:
                        if file[0] != '.':
                            file_paths.append(os.path.join(root,file))
                elif files == []:
                    if subdir_n_file[0] != '.':
                        file_paths.append(os.path.join(subdir_n_file))
else:
    if option_hid == '--hidden':
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                file_paths.append(os.path.join(root,file))
    elif option_hid == '':
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if file[0] != '.':
                    file_paths.append(os.path.join(root,file))

for file_path in file_paths:  # first and foremost
    find_pattern_in_file(file_path, pattern, option)
    print_in_colors(lines_w_pattern, pattern, option)
