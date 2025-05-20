import pandas as pd


def main():
    df = pd.read_csv("notes.csv")

    
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
            print(df[df["tags"].str.contains(item, case=False)])

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
