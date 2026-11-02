#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Local childcare work log viewer/editor using Tkinter and XML."""
from __future__ import annotations
from datetime import date, datetime
import os
from pathlib import Path
import shutil
import tempfile
import tkinter as tk
from tkinter import messagebox, ttk
import xml.etree.ElementTree as ET

DATA = Path(__file__).resolve().parent / "work.xml"
PEOPLE = ("Bobby", "Sam", "Sarah")

def read_entries(path: Path = DATA) -> list[dict[str, str]]:
    root = ET.parse(path).getroot()
    return [{"person": child.tag, "date": child.get("date", ""),
             "hours": child.get("hours", ""), "added": child.get("added", "")}
            for child in root if child.tag in PEOPLE]

def add_entry(path: Path, person: str, day: str, hours: str, notes: str) -> None:
    if person not in PEOPLE:
        raise ValueError("Unknown person")
    try:
        date.fromisoformat(day)
        amount = float(hours)
    except ValueError as exc:
        raise ValueError("Use ISO date YYYY-MM-DD and numeric hours") from exc
    if not 0 < amount <= 24 or not amount < float("inf"):
        raise ValueError("Hours must be greater than zero and at most 24")
    if len(notes) > 500:
        raise ValueError("Notes are too long")
    tree = ET.parse(path)
    root = tree.getroot()
    ET.SubElement(root, person, {"date": day, "hours": str(amount), "added": notes})
    backup = path.with_name(path.name + "." + datetime.now().strftime("%Y%m%d%H%M%S%f") + ".bak")
    shutil.copy2(path, backup)
    fd, tmpname = tempfile.mkstemp(prefix=".childcare-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            tree.write(stream, encoding="utf-8", xml_declaration=True)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmpname, path)
    finally:
        Path(tmpname).unlink(missing_ok=True)

def main() -> None:
    root = tk.Tk()
    root.title("Childcare Time")
    root.geometry("760x540")
    frame = ttk.Frame(root, padding=14)
    frame.pack(fill="both", expand=True)
    table = ttk.Treeview(frame, columns=("person", "date", "hours", "notes"), show="headings")
    for key, title in (("person", "Person"), ("date", "Date"), ("hours", "Hours"), ("notes", "Notes")):
        table.heading(key, text=title)
    table.pack(fill="both", expand=True)
    form = ttk.Frame(frame)
    form.pack(fill="x", pady=12)
    person = tk.StringVar(value=PEOPLE[0])
    day = tk.StringVar(value=date.today().isoformat())
    hours = tk.StringVar(value="1")
    notes = tk.StringVar()
    for column, (label, widget) in enumerate((
        ("Person", ttk.Combobox(form, textvariable=person, values=PEOPLE, state="readonly", width=10)),
        ("Date", ttk.Entry(form, textvariable=day, width=13)),
        ("Hours", ttk.Entry(form, textvariable=hours, width=7)),
        ("Notes", ttk.Entry(form, textvariable=notes, width=24)),
    )):
        ttk.Label(form, text=label).grid(row=0, column=column, padx=5)
        widget.grid(row=1, column=column, padx=5)
    def refresh() -> None:
        for item in table.get_children():
            table.delete(item)
        for item in read_entries():
            table.insert("", "end", values=(item["person"], item["date"], item["hours"], item["added"]))
    def save() -> None:
        try:
            add_entry(DATA, person.get(), day.get(), hours.get(), notes.get())
            refresh()
        except (OSError, ValueError, ET.ParseError) as exc:
            messagebox.showerror("Could not save", str(exc), parent=root)
    ttk.Button(frame, text="Add entry (creates backup)", command=save).pack(pady=5)
    try:
        refresh()
    except (OSError, ET.ParseError) as exc:
        messagebox.showerror("Could not read work.xml", str(exc), parent=root)
    root.mainloop()

if __name__ == "__main__":
    main()
