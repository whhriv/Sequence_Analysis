from app import app, db
from app.models import User, SequenceForm
from app.forms import LoginForm, RegisterForm, SequenceForm, SingleSequenceForm
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_required, UserMixin, login_user, logout_user, LoginManager, current_user
from app.DNAfunctions import *

app.secret_key = 'you-will-never-guess'
@app.route('/')
def index():

    # if current_user.is_autheexport FLASK_APP=microblog.py_for('dashboard'))
    # SELECT * FROM post ORDER BY date_created DESC;
    # sequence = db.session.execute(db.select(Sequence).order_by(db.desc(Sequence.date_created))).scalars().all()
    # return render_template('index.html', sequence=sequence)
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.data.get('username')
        password = form.data.get('password')
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('dashboard'))
    return render_template('register.html', title='Register', form=form)

    
@app.route('/login', methods=[ 'GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.data)
        username = form.data.get('username')
        password = form.data.get('password')
        remember_me = form.data.get('remember_me')

        user = db.session.execute(db.select(User).where(User.username == username)).scalar()

        flash("You have logged in.")
        login_user(user, remember=remember_me)
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)
    
@app.route('/dashboard', methods=["GET", "POST"])
# @login_required
def dashboard():
    form = SingleSequenceForm()
    if form.validate_on_submit():
        # sequenceDNA = form.data.get('sequenceDNA')
        # if isSequenceValid(FASTAConverter(form.sequenceDNA.data)[1]):
        session['sequenceDNA'] = form.sequenceDNA.data
        return redirect('/results')
        # else:
            # flash(repr(FASTAConverter(form.sequenceDNA.data)))
    # sequences = db.session.execute(db.select(Sequence).where(Sequence.user_id == current_user.user_id).order_by(db.asc(Sequence.isolate))).scalars().all()
    # else:
        # flash('invalid entry')
    # return render_template('index.html' )
    return render_template('dashboard.html', form=form)
    
@app.route('/results', methods=["GET","POST"])
def sequenceResults():
    geneTitle = FASTAConverter(session['sequenceDNA'])[0]
    sequence = FASTAConverter(session['sequenceDNA'])[1]
    _composition = composition(sequence)
    contentGC = int(percentGC(sequence))
    fusionTemp = tempPCR(sequence)
    RNAseq = DNA_to_RNA(sequence)
    proteinSeq = translation(RNAseq)
    length = len(sequence)
    print(proteinSeq)

    return render_template('results.html', fusionTemp=fusionTemp, length=length, geneTitle=geneTitle, sequence=sequence, _composition=_composition, contentGC=contentGC, RNAseq=RNAseq, proteinSeq=proteinSeq )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged OUT')
    return redirect(url_for('index'))


