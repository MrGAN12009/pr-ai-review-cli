import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import note_cli


class NoteCliTests(unittest.TestCase):
    def test_add_note_saves_text(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Path(directory) / "notes.json"

            note_cli.add_note(store, "Open a pull request")

            notes = json.loads(store.read_text(encoding="utf-8"))
            self.assertEqual(notes, [{"text": "Open a pull request"}])

    def test_list_notes_prints_saved_notes(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Path(directory) / "notes.json"
            store.write_text(
                json.dumps([{"text": "Ask AI for review"}]),
                encoding="utf-8",
            )

            with patch("builtins.print") as print_mock:
                note_cli.list_notes(store)

            print_mock.assert_called_once_with("1. Ask AI for review")

    def test_list_notes_handles_empty_store(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Path(directory) / "notes.json"

            with patch("builtins.print") as print_mock:
                note_cli.list_notes(store)

            print_mock.assert_called_once_with("No notes yet.")


if __name__ == "__main__":
    unittest.main()

