"""
1.根据 requirements.txt 安装环境
2.注意修改 PYTHONPATH 环境变量,将工作目录加入到 PYTHONPATH 环境变量中
  PYTHONPATH=. python examples/demo.py
"""

from keyphrasetransformer import KeyPhraseTransformer

kp = KeyPhraseTransformer()

if __name__ == '__main__':
    
    import time
    text = "Well, if you found this video, you probably use some vocal fillers when you present, like um uh you know, and a whole long list of other ones, we're going to look at, four tips to get rid of them coming up.Hello again, Friends, I'm Alex Line and this channel communication Coach is here to help you increase your impact, so you can leave the teams around you to higher levels of excellence, and it's gonna be very hard to inspire people if you're using lots of vocal fillers when you present. I used to use, kinda and sorta quite a bit, but maybe it's and so, you know, like, and again, the list is endless. this can be a big distraction. And if you can get rid of these, then people can focus on your message and not count how many homes or do you use. So let's. Look at four tips to get rid of them that I have personally used. And I've seen these tips work for many people over the years. The first tip is a mindset tip and that is you have to get comfortable with silence. A lot of the times we fill in the silence, what could be pauses with ums and UHS and you knows, because we feel like, oh if we're silent, it sounds like well, lost our place or we don't know what we're talking about. But I think really the opposite is true. I think those little beats of silence, those pauses help listeners consider our last idea, let it sink in and then they're ready for the next one when you don't have any pauses and it's all one long sound, you never give that moment for people to reflect and accept your message. So get comfortable with pauses. Step number two, you have to develop a new habit to replace the old one. A lot of times we don't even realize we're saying. Um and unless someone brings it to our attention, so one of the ways you can realize you're doing it is by practicing in private a little bit louder than you normally would. And when you practice louder, your arms and your legs come out a little louder and you can hear them. And once you're aware of them, you can get rid of them. Step number three instead of saying an um or whatever your favorite filler is, replace it with the word period or pause. And I literally want you to practice this out loud. That's what I recommend. So today we're going to change the brakes on our car periodwhen you say it out loud, it really starts to emphasize the idea that yeah, I should be ending my sentence there and giving a nice pause and then after you practice a few times out loud like that all the way through a presentation, then begin just to say the word period or pause in your head and it sounds like this. Today, we're gonna learn how to change the brakes in your car.It sounds very confident, very composed, like you meant it to be there and gives your idea a chance to sink into your listeners minds. And then the fourth tip is to breathe again instead of saying an um or whatever your filler is. If you take a nice breath, it gives a nice pause to your listeners ears, but it also helps you relax and helps you come across as much more composed. So those are my four tips, but enough about what I think, What are your vocal fillers and what do you recommend you do and other people do to get rid of them. I would love to hear your feedback in that section below. So thanks, God bless and I will see you in the next video."
    print("{} words".format(len(text.split(" "))))
    start = time.time()
    result = kp.get_key_phrases(text, 512)
    print("\nElapsed Time: {:.3f} seconds\n".format((time.time() - start)/10))
    print(f"result:{result}")

