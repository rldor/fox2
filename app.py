from flask import Flask, request, render_template


app = Flask(__name__)
import random
from rand import cards

@app.route('/')
def hello():

    return render_template("index.html")#,i=f'{words[0]} ({words[1][1:]})')#"s.html")


@app.route('/bio')
def biology():
    from rand import s_bio, m
    s1=cards(s_bio)
    words=random.choice(s1).split(':')
    current_mode=random.choice(m)
    return render_template("s1.html", i=f'{words[0]} ({words[1][1:]})', j=current_mode, subb='Biology!')


@app.route('/bot')
def botany():
    from rand import s_bot, m
    s1 = cards(s_bot)
    words = random.choice(s1).split(':')
    current_mode = random.choice(m)
    return render_template("s1.html", i=f'{words[0]} ({words[1][1:]})', j=current_mode, subb='Botany!')


@app.route('/bh')
def biochem():
    from rand import s_bh, m
    s1 = cards(s_bh)
    words = random.choice(s1).split(':')
    current_mode = random.choice(m)
    return render_template("s1.html", i=f'{words[0]} ({words[1][1:]})', j=current_mode, subb='Biochemistry!')


@app.route('/chem')
def chemistry():
    from rand import s_chem_easy, s_chem_hard, m
    s1 = cards(s_chem_easy)
    s2 = cards(s_chem_hard)
    current_mode = random.choice(m)
    words1 = random.choice(s1).split(':')
    words2 = random.choice(s2).split(':')
    return render_template("s1_chem.html", i1=f'{words1[0]} ({words1[1][1:]})', i2=f'{words2[0]} ({words2[1][1:]})', j=current_mode, subb='Chemistry!')

#if __name__ == '__main__':
#    app.run()
