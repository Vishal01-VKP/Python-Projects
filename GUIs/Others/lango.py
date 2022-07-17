import googletrans as GT

text = "me"

translator = GT.Translator()
raw_trans = translator.translate(text, dest="hi", src="en")
translation = raw_trans.text

print(f"Translation : {translation}")

with open("lango.txt", "a", encoding="utf-8") as writer:
    info = f"{text} (English) : (Hindi) {translation}"
    writer.write(info)
    writer.write("\n\n")

with open("lango.txt", "r", encoding="utf-8") as reader:
    correct_info = reader.read()
    print(correct_info)