## Setup

Basically, I made a ChatGPT mirror based on the open source LLM llama.

A couple things to keep in mind:

You probably need an NVidia GPU to run this. If you're using a laptop, keep it plugged in because inference will take too long without your GPU running at full power. You may also need to install CUDA (not 100% sure about this though; I've had it installed for several months before this take home).

I honestly have no idea how this will run on other devices (seeing as it isn't your normal webdev project), so if you run into any issues please don't hesitate to reach out. Worst case I can just do a live demo for you guys.

Right now due to upload issues I'm not able to push the pretrained version of llama that I use. Instead, go to the link below and download the model labelled "llama2_7b_chat_uncensored.ggmlv3.q4_0.bin" and put it in "backend/models/". It's about 4 GB large.

https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/tree/main

### Backend

```bash
cd backend/
source env.sh
python main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```
