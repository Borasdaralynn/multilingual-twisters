import argparse, json, os, datetime, epitran

p = argparse.ArgumentParser()
p.add_argument("--lang", default="eng-Latn", help="Epitran code, e.g., spa-Latn, fra-Latn")
args = p.parse_args()

epi = epitran.Epitran(args.lang)
out_path = os.path.join("outputs", f"{args.lang}.json")
os.makedirs("outputs", exist_ok=True)

print(f"Language: {args.lang}")
print("Type a tongue twister (blank line or :q to quit).")
while True:
    t = input("> ").strip()
    if not t or t == ":q" or t == ":quit":
        break
    try:
        ipa = epi.transliterate(t)
    except Exception as e:
        print("\nError during transliteration:", e, "\n")
        continue
    rec = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "lang": args.lang,
        "text": t,
        "ipa": ipa
    }
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(ipa)
print(f"\nSaved to {out_path}")
