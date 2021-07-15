# Inspired by https://stackoverflow.com/questions/25782727/keep-alive-the-object-for-using-them-in-another-program-in-python
import fasttext
model = fasttext.load_model("/Users/alex/result/cc.en.300.bin")

try:
    import traceback
    import script

    while True:
        raw_input()

        try:
            reload(script)
            script.main(model)
        except:
            print(traceback.print_exc())

except KeyboardInterrupt:
    print('exit launcher')