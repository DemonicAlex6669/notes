import csv


def main():
    ...
    if choice == "write":
        title = input("title:")
        note = input("note:")
        tags = input("tags")
        with open("notes.csv") as csvfile:
            note = csv.writer(csvfile)
            note.writerrow([title, note, tags])
    elif choice == "search":
        item = input("search")
        with open("notes.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if item in row["tags"]:
                    print(f"{row['title']}/n {row['note]} /n tags: {row['tags]}")
    elif choice == "tags":
        with open("notes.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row["tags"])
    elif choice == "options":
        print("write, search, tags, options")
    else:
        print("incorrect input, for help type options")


if __name__ == "__main__":
    main()
