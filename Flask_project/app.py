from flask import Flask, request, render_template 
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       f = request.form.get("fname")
       # getting input with name = lname in HTML form 
       if f[0] == 'a' or f[0] == 'A' :
         result = " You are looking to hone your skills and bring a fresh innovative eye to your work, as the hard-working Virgo moon links up with originality-craving Uranus. Elsewhere, messenger Mercury locks eyes with aspirational Jupiter. This pairing helps you think and dream big when it comes to goal-setting, but it may also increase expectations beyond a realistic standard."
         return render_template("form.html",result = result)
       elif f[0] == 'b' or f[0] == 'B':
         result = " Your mind is about to open up a little further. You'll be seeing things differently for a while, and it might give you a whole new direction in life.Don't take any risks right now. In the long run, short cuts will only get you lost."
         return render_template("form.html",result = result)
       elif f[0] == 'c' or f[0] == 'C':
         result = " You need to stop thinking so much and just get busy with whatever it is that's been itching lately. Even if it doesn't work at first, keep at it: less talk, more rock.Taking things to a deeper level takes time; don't rush someone who isn't ready yet."
         return render_template("form.html",result = result)
       elif f[0] == 'd' or f[0] == 'D':
         result = " Don't skimp when it comes to taking care of your physical health, Aries. In an effort to save money, you may not bother getting dental checkups, or you could opt for the least expensive doctor in the book. Nothing is more important than your health. Treat your body with the honor and respect it deserves. You may have no trouble doing for others what you know you should be doing for yourself."
         return render_template("form.html",result = result)
       elif f[0] == 'e' or f[0] == 'E':
         result = " Sometimes it's necessary for our personal growth to let the pendulum swing all the way to one side. The more you can let go and accept that everything isn't going to always be peaceful and harmonious, the better able you will be to deal with the sudden emotional turmoil that is bound to arise."
         return render_template("form.html",result = result)
       elif f[0] == 'f' or f[0] == 'F':
         result = "  Your upbeat spirit will be more welcome than usual due to the drama around you. Be careful of falling into the role that you know others want you to play. It's easy to take on the role that's in front of you, but this doesn't always help the situation. Read from your own script, not someone else's."
         return render_template("form.html",result = result)
       elif f[0] == 'g' or f[0] == 'H':
         result = " Your tendency is to assume things before you have all the facts. You may assume the worst, making you more stressed about the situation than you need to be. Don't worry about things you don't know to be true."
         return render_template("form.html",result = result)
       elif f[0] == 'h' or f[0] == 'H':
         result = " You may feel very opinionated about a certain issue, but you know that expressing yourself is likely to cause someone else to feel threatened or upset. But if you keep these thoughts to yourself, you're going to feel resentful and perhaps even used. You're better off expressing yourself honestly."
         return render_template("form.html",result = result)
       elif f[0] == 'i' or f[0] == 'I':
         result = " Seek comfort in sitting by a body of water where you can let your emotions flow. Tension builds as the storm draws near. Once it has passed, however, there is calm as the sunshine pierces the clouds. This time of peace and serenity may seem far off, but it's closer than you think."
         return render_template("form.html",result = result)
       elif f[0] == 'j' or f[0] == 'J':
         result = " Be prepared to deal with the expected. The key is not to overreact. The calmer and more stable you can stay, the better off you'll be. Dealing with the situation in a reactive outburst will only turn the scene into an explosive rage. Count to ten or sit by yourself for a while before you deal with the problem."
         return render_template("form.html",result = result)
       elif f[0] == 'k' or f[0] == 'K':
         result = " Perhaps it's your emotions that you want to distance yourself from, or it feels like someone is smothering you. On the one hand, you long for company and intimacy to fill an inner void. On the other, you resent having to be so needy. Make sure you're whole before you sink too deeply into a relationship."
         return render_template("form.html",result = result)
       elif f[0] == 'l' or f[0] == 'L':
         result = " Gridlock could be making you feel uncomfortable. Your solution to the problem is to put on a happy face and divert attention from the difficulty by telling some jokes. Realize that this technique will delay having to face a particular situation for a while, but it certainly won't keep you from ever having to deal with it."
         return render_template("form.html",result = result)
       elif f[0] == 'm' or f[0] == 'M':
         result = " There's momentum building within that you shouldn't ignore or suppress. Perhaps you feel that what you have to say isn't appropriate for the situation. More than likely, it will do more harm than good to ignore these feelings rather than get them out, even when it seems disruptive to do so."
         return render_template("form.html",result = result)
       elif f[0] == 'n' or f[0] == 'N':
         result = " If you're frustrated, angry, or hurt, address the issue openly. Don't feel like you have to be the one who cheers up everyone else. Let someone else have a turn for a change. You're only harming yourself by pretending that everything is OK when it isn't."
         return render_template("form.html",result = result)
       elif f[0] == 'o' or f[0] == 'O':
         result = "Sometimes you can be very set in the way you look at something. You tend to form an opinion quickly, and once you've made up your mind, nothing can convince you otherwise! Today you might want to reconsider a judgment that you have made. More information and insight could be coming to light. Perhaps this involves a loved one."
         return render_template("form.html",result = result)
       elif f[0] == 'p' or f[0] == 'P':
         result = " Your intuition is quite high right now, enabling you to tune in with great accuracy on the hopes and dreams of others. This can be a bit tricky in a social situation, however. Someone could be saying one thing when you know full well they are thinking something else entirely! Don't dwell on other people's thoughts too much."
         return render_template("form.html",result = result)
       elif f[0] == 'q' or f[0] == 'Q':
         result = " Your boss could express a firm opinion about something. His or her attitude might shock you! Or a coworker could confess the truth about something. People will be inspired to speak from the heart today, and they won't be in the mood to edit themselves. This could make for a dramatic day, but if you pay attention, you'll learn something!"
         return render_template("form.html",result = result)
       elif f[0] == 'r' or f[0] == 'R':
         result = " You have a certain tendency to over-analyze things. People have surely told you this often. What they don't realize is that you analyze yourself even more than you do others! You think that you understand who you are, but do you really? With today's planetary energy, you will be asked to take a risk and let your intellect take a back seat to your emotions. You might be surprised by what you discover."
         return render_template("form.html",result = result) 
       elif f[0] == 's' or f[0] == 'S':
         result = "The world is truly a small place. Today you could discover this to be true in your personal life. In an improbable circumstance, you could find yourself bumping into someone that you rarely see. This could be a relative, an old college buddy, or a client from another state. Coincidences like this can bring you a special opportunity to connect with someone, so take some time to reach out to them."
         return render_template("form.html",result = result)                                 
       elif f[0] == 't' or f[0] == 'T':
         result = "Generally you are a very sociable person, and today you aren't likely to slow down any. Invitations to all kinds of parties, from intimate coffee klatches to big neighborhood bashes continue to come in. There may be too many for you to handle, so you might find yourself having to turn some of them down - which goes against your nature!"
         return render_template("form.html",result = result)
       elif f[0] == 'u' or f[0] == 'U':
         result = " You could find yourself very busy today. It might be a good day to sit down and make a list of all the things you need to get done. Scheduling the organization of specific tasks or engagements can make a big difference in the amount of stress you'll feel."
         return render_template("form.html",result = result)  
       elif f[0] == 'v' or f[0] == 'V':
         result = " Today you might be in doubt as to exactly how much money you might be getting from a business transaction of some kind. If you can, verify this before starting anything. There is something you're not being told. Personal relationships, particularly love and romance, should be stable and rewarding at this time, though today you might not have that much time to spend with those you care for. Hang in there!"
         return render_template("form.html",result = result)  
       elif f[0] == 'w' or f[0] == 'W':
         result = " What's happening in your community today that attracts crowds? A parade? A festival of some kind? Some friends may want you to go there with them. You might think you're too busy, but an hour or two away from your chores certainly won't hurt. Take some time out - this is a time for having fun! If you want to, go! You could meet some interesting people."
         return render_template("form.html",result = result) 
       elif f[0] == 'x' or f[0] == 'X':
         result = " You took off like a bullet a few days ago, making great progress in a short amount of time. But now you are grappling with doubts that are undermining all your energy. Reflecting on the events of the past few days, it is obvious to you that you were somewhat reckless in your headlong pursuit of your goals. Don't give up, just rethink your strategy."
         return render_template("form.html",result = result)  
       elif f[0] == 'y' or f[0] == 'Y':
         result = " Are you feeling the urge to redecorate your home? You might find yourself feeling a little closed in, and decide that the only way to escape this feeling is to recreate your surroundings. This is a good day to do it, as your sense of aestheticism is especially acute right now. A little paint, some fresh curtains, a few new knickknacks and throw pillows, and it'll almost be as if you had a new place. Enjoy it!"
         return render_template("form.html",result = result)  
       elif f[0] == 'z' or f[0] == 'Z':
         result = " If you dream of a promotion, this is YOUR week to show off your talents and skills. The Sun and Venus want you to shine and to show people exactly what you are capable of. Some good financial news will put a smile on your face this weekend."
         return render_template("form.html",result = result) 
       else:
         result="Enter a valid Name"  
         return render_template("form.html",result = result) 


    return render_template("form.html")
  
if __name__=='__main__':
   app.run(debug=True)