# Ollama python irc local ai bot

Hi over there! this is ale. and i'm going to guido you in this tutorial. here we are going to learn how to make an irc bot powered with the open source project "ollama".

### Why to do this?

I'm part of the pesterchum IRC community, and, the idea of an ai autoresponder is related to our fandom (not explaining because of spoilers). so, when a friend started a testing irc, i asked if i could use it to develop this tiny app and said that was okey.

### How to read this.

This part is devided in sections marked on the python code that i'm going to explain so, easily you can jump to the part you want.

> [!WARNING]  
> As ollama has only linux and mac support, this can only be used on linux and/or mac, for windows use WSL or another kind of virtualization like docker(that runs over WSL too).

## Section 0
### Setup

first of all we have to install some things. python 3 is one of this. right now, this tutorial wont teach you how to install python, you can google that and or probably already have it installed and updated.

we need the ollama python library so we run:
```pip install ollama```

but, we also need ollama. lets install ollama! this is kinda easy and i could just paste the code here but. i will not keep this updated, so i recommend you to go here: 

https://ollama.ai/download/linux

now that we have ollama, we have to run the service. to do that you can run:
```
ollama serve
```
this will start ollama server. don't close that terminal! 

after installing, and running the server, you have also to install a model. in this particular case we are using tinydolphin. because can run even on an android device, or a raspberry py.

```
ollama run tinydolphin
```

after a big big instalation time, we have all set up to run our bot!