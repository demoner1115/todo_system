import argparse
import todo

def main():
    parser = argparse.ArgumentParser(description="할 일 관리 CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add")
    p_add.add_argument("name")

    sub.add_parser("list")

    p_done = sub.add_parser("done")
    p_done.add_argument("number", type=int)

    p_delete = sub.add_parser("delete")
    p_delete.add_argument("number", type=int)

    args = parser.parse_args()

    if args.command == "add":
        todo.add(args.name)
    elif args.command == "list":
        todo.list_json()
    # done, delete 분기는 직접 채워라
    elif args.command == "done":
        todo.done(args.number)
    elif args.command == "delete":
        todo.delete(args.number)

if __name__ == "__main__":
    main()