import argparse
import json
from pathlib import Path


DEFAULT_STORE = Path(".notes.json")


def load_notes(path):
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_notes(path, notes):
    with path.open("w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2)
        file.write("\n")


def add_note(path, text):
    notes = load_notes(path)
    notes.append({"text": text})
    save_notes(path, notes)
    print(f"Added note: {text}")


def list_notes(path):
    notes = load_notes(path)

    if not notes:
        print("No notes yet.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note['text']}")


def clear_notes(path):
    save_notes(path, [])
    print("All notes cleared.")


def export_notes(path, output):
    notes = load_notes(path)
    lines = ["# Notes", ""]

    if notes:
        for index, note in enumerate(notes, start=1):
            lines.append(f"{index}. {note['text']}")
    else:
        lines.append("No notes yet.")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Exported notes to {output}")


def build_parser():
    parser = argparse.ArgumentParser(description="A tiny CLI notes app.")
    parser.add_argument(
        "--store",
        type=Path,
        default=DEFAULT_STORE,
        help="Path to the JSON notes file.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new note.")
    add_parser.add_argument("text", help="Text of the note.")

    export_parser = subparsers.add_parser("export", help="Export notes to Markdown.")
    export_parser.add_argument("output", type=Path, help="Markdown output path.")

    subparsers.add_parser("list", help="List notes.")
    subparsers.add_parser("clear", help="Clear all notes.")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_note(args.store, args.text)
    elif args.command == "export":
        export_notes(args.store, args.output)
    elif args.command == "list":
        list_notes(args.store)
    elif args.command == "clear":
        clear_notes(args.store)


if __name__ == "__main__":
    main()
