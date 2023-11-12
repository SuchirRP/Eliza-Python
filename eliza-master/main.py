import eliza;
import pyttsx3;

# Text to Speech
engine = pyttsx3.init();

def spch2txt(str):
    engine.say(str);
    engine.runAndWait();

#Eliza object creation
eliza = eliza.Eliza();
eliza.load('doctor.txt');

#Inital Line
print(eliza.initial());
spch2txt(eliza.initial());

while True:
    said = input('> ');
    response = eliza.respond(said);
    if response is None:
        break;
    print(response);
    spch2txt(response);

print(eliza.final());
spch2txt(eliza.final());

