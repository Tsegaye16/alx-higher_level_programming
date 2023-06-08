#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_directory = dir(hidden_4)
    for k in range(0, len(all_directory)):
        if "__" != all_directory[k][:2]:
            print(all_directory[k])
