import pandas as pd


def main():
    df = pd.read_csv("notes.csv")

    def format(title, note, tags):
        title_length = len(title)
        print(f"#" * title_length)
        print(f"# {title} #")

        print(f"#" * 25)
        print(f"# {note} #")
        print(f"#" * 25)

        tag_length = len(tags)
        print(f"# {tags} #")
        print(f"#" * tag_length)

    
    while True:
        choice = input("what do you want to do: ").strip().lower()
    
        if choice == "write":
            title = input("title:")
            note = input("note:")
            tags = input("tags")
            newline = [[title, note, tags]]
            df2 = pd.DataFrame(newline)
            df2.to_csv("notes.csv", index=False, mode="a", header=False)

        elif choice == "search":
            item = input("search: ")
            cpdf = df[df["tags"].str.contains(item, case=False) | df["title"].str.contains(item, case=False) | df["note"].str.contains(item, case=False)]
            format(cpdf.iloc[0,0], cpdf.iloc[0,1], cpdf.iloc[0,2])

            i = len(cpdf) - 1

            while i > 0:
                format(cpdf.iloc[i,0], cpdf.iloc[i,1], cpdf.iloc[i,2])
                i = i - 1

        elif choice == "tags":
            print(df.loc[:, "tags"])

        elif choice == "options":
            print("write, search, tags, options, exit")

        elif choice == "exit":
            break

        else:
            print("incorrect input, for help type options")


if __name__ == "__main__":
    main()
