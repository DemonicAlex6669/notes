import pandas as pd


def main():
    df = pd.read_csv("notes.csv")
    choice = input("what do you want to do").strip().lower()
    if choice == "write":
        title = input("title:")
        note = input("note:")
        tags = input("tags")
        newline = [[title, note, tag]]
        df2 = pandas.DataFrame(newline)
        df2.to_csv("notes.csv", index=false, mode="a", headers=false)
    elif choice == "search":
        print(df.loc[choice in df["tags"]])
    elif choice == "tags":
        print(df.loc[:, "tags"])
    elif choice == "options":
        print("write, search, tags, options")
    else:
        print("incorrect input, for help type options")


if __name__ == "__main__":
    main()
