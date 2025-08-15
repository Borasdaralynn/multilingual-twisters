import epitran
import panphon
from phonemizer import phonemize

# Example: English tongue twister
text = "She sells sea shells by the sea shore"
lang_code = "eng-Latn"

ipa = ""
if lang_code == "eng-Latn":
    # Use phonemizer for English to avoid flite/lex_lookup issues
    ipa = phonemize(text, language='en-us', backend='espeak', strip=True)
else:
    epi = epitran.Epitran(lang_code)
    ipa = epi.transliterate(text)

# If Epitran doesn't support the language, fallback to phonemizer
if not ipa:
    ipa = phonemize(text, language='en-us', backend='espeak', strip=True)

print("IPA:", ipa)

# Extract phonological features
ft = panphon.FeatureTable()
features = ft.word_fts(ipa)
print("Features:", features)
import epitran
import panphon
from phonemizer import phonemize

# Example: English tongue twister
text = "She sells sea shells by the sea shore"
lang_code = "eng-Latn"

ipa = ""
if lang_code == "eng-Latn":
    # Use phonemizer for English to avoid flite/lex_lookup issues
    ipa = phonemize(text, language='en-us', backend='espeak', strip=True)
else:
    epi = epitran.Epitran(lang_code)
    ipa = epi.transliterate(text)

# If Epitran doesn't support the language, fallback to phonemizer
if not ipa:
    ipa = phonemize(text, language='en-us', backend='espeak', strip=True)

print("IPA:", ipa)

# Extract phonological features
ft = panphon.FeatureTable()
features = ft.word_fts(ipa)
print("Features:", features)
