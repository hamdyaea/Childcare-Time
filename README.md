# Childcare Time

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A Python 3/Tkinter application for browsing and adding entries to the repository's local `work.xml` childcare work log. The legacy XML is read without modifying old records, even if they contain historically invalid date strings. New records require ISO dates and validated hours. Every write creates a timestamped backup and uses atomic replacement.

```sh
python3 ChildcareTime.py
python3 -m unittest discover -s tests -v
```

**Privacy:** The XML file may contain personal scheduling information. Do not publish real personal entries in a public repository. Back up `work.xml` before use. The GUI makes no network requests.

Original EasyGUI version: [old branch](https://github.com/hamdyaea/Childcare-Time/tree/old).
