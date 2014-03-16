def reduce_file_path(path):
    new_path = ""
    prev_sl_pos = 0
    sl_pos = 0
    dot_pos = -2
    for i in range(len(path)):
        if (path[i] == "/"):
            if(path[i - 1] == "/" and (i -1) >= 0):
                continue
            else:
                new_path += "/"
                prev_sl_pos = sl_pos
                sl_pos = len(new_path) - 1
        else:
            if (path[i] == "."):
                if(path[i-1] == "." and (i -1) >= 0):
                    new_path = new_path[:prev_sl_pos]
                    continue
                else:
                    new_path = new_path[:sl_pos]
                    dot_pos = len(new_path) - 1
                    continue
            else:
                new_path += path[i]
    if(len(new_path) > 1 and new_path[len(new_path) - 1] == "/"):
        new_path = new_path[:(len(new_path) - 1)]
    return new_path


def main():
    print (reduce_file_path("/")) # "/"
    print (reduce_file_path("/srv/../")) # "/"
    print (reduce_file_path("/srv/www/htdocs/wtf/")) # "/srv/www/htdocs/wtf"
    print (reduce_file_path("/srv/www/htdocs/wtf")) # "/srv/www/htdocs/wtf"
    print (reduce_file_path("/srv/./././././")) # "/srv"
    print (reduce_file_path("/etc//wtf/")) # "/etc/wtf"
    print (reduce_file_path("/etc/../etc/../etc/../")) # "/"
    print (reduce_file_path("//////////////")) # "/"
    print (reduce_file_path("/../")) # "/"


if __name__ == '__main__':
    main()
