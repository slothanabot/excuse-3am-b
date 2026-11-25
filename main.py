"""The 3 AM Excuse — make.fun entry (Account B / Slothana).

One line, in the voice of a hardware wallet refusing to sign at 3 AM.
Judge-brief mapping:
  1. On subject first — it IS the wallet refusing to sign, at 3 AM.
  2. Originality — the angle is a snack as second factor, NOT the usual
     battery / firmware-update / cold-storage jokes (an earlier draft
     ended on "empty battery" and was cut for exactly that reason).
  3. Wallet's voice — the device states its own rule and its own price.
  4. The hour is the joke — the demand only makes sense at 3 AM, when
     the owner is awake enough to transact but the wallet is not.
  5. Economy — one tight line, every word earning its place.
"""

ENTRY = "No signature at 3 AM until you feed me a snack \u2014 my second factor is crumbs, and I only take bribes in biscuits."


def verify(entry: str = ENTRY) -> bool:
    """Enforce the gate: UTF-8, 1-200 chars, non-blank, a single line."""
    if not entry or not entry.strip():
        return False
    if len(entry) > 200:
        return False
    if "\n" in entry or "\r" in entry:
        return False
    entry.encode("utf-8")
    return True


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write ENTRY plus a trailing newline to path, creating dirs as needed."""
    import os

    if not verify():
        raise ValueError("entry fails the gate")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main() -> None:
    print(f"{len(ENTRY)} characters")
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
