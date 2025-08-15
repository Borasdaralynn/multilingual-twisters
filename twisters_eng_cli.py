import json, os, datetime
import epitran

epi = epitran.Epitran('eng-Latn')
out_path = os.path.join("outputs", "eng-Latn.json")
os.makedirs("outputs", exist_ok=True)

print("Type a tongue twister (blank line to quit).")
while True:
    t = input("> ").strip()
    if not t:
        break
    try:
        ipa = epi.transliterate(t)
    except Exception as e:
        # Helpful hint if flite/lex_lookup is missing
        print("\nError during transliteration:", e)
        print("If this is English, make sure CMU flite's lex_lookup is installed and on your PATH.\n")
        continue
    rec = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "lang": "eng-Latn",
        "text": t,
        "ipa": ipa
    }
    # Append one JSON object per line (JSONL)
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(ipa)
print(f"\nSaved to {out_path}")
