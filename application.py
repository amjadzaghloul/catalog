from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Company, MobilePhones, User

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# GConnect CLIENT_ID
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

# Connect to Database and create database session
engine = create_engine('sqlite:///mobilephones.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template("login.html", STATE=state)

# GConnect
@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;' \
            'height: 300px;' \
            'border-radius: 150px;' \
            '-webkit-border-radius: 150px;' \
            '-moz-border-radius: 150px;"> '

    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Show all companies
@app.route('/')
@app.route('/company/')
def showCompanies():
    company = session.query(Company).order_by(asc(Company.name))
    if 'username' not in login_session:
        return render_template('publicCompanies.html' , company=company)
    else:
        return render_template('companies.html', company=company)

# Create a new Company
@app.route('/company/new/', methods = ['GET','POST'])
def newCompany():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCompany = Company(name = request.form['name'] )
        session.add(newCompany)
        session.commit()
        flash('New Company Created!')
        return redirect(url_for('showCompanies'))
    else:
        return render_template('newCompany.html')

# Edit a company
@app.route('/company/<int:company_id>/edit/' , methods = ['GET','POST'])
def editCompanies(company_id):
    if 'username' not in login_session:
        return redirect('/login')
    editCompany = session.query(Company).filter_by(id=company_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editCompany.name = request.form['name']
        session.add(editCompany)
        session.commit()
        flash("%s has been edited"% editCompany.name)
        return redirect(url_for('showCompanies'))
    else:
        return render_template('editCompany.html', company_id = company_id, editCompany = editCompany)

# Delete a company
@app.route('/company/<int:company_id>/delete/', methods = ['GET','POST'])
def deleteCompanies(company_id):
    if 'username' not in login_session:
        return redirect('/login')
    deleteCompany = session.query(Company).filter_by(id=company_id).one()
    if request.method == 'POST':
        session.delete(deleteCompany)
        session.commit()
        flash("%s has been deleted"% deleteCompany.name)
        return redirect(url_for('showCompanies'))
    else:
        return render_template('deleteCompany.html', company=deleteCompany)

# Show a mobilePhones
@app.route('/company/<int:company_id>/')
@app.route('/company/<int:company_id>/mobilephones/')
def showMobilePhones(company_id):
    company = session.query(Company).filter_by(id = company_id).one()
    mobilePhones = session.query(MobilePhones).filter_by(company_id = company_id).all()
    if 'username' not in login_session:
        return render_template('publicMobilePhones.html', company=company , company_id=company_id , mobilePhones=mobilePhones)
    else:
        return render_template("mobilePhones.html", company = company, company_id = company_id , mobilePhones=mobilePhones)

# Create a new mobile phone
@app.route('/company/<int:company_id>/mobilephones/new', methods = ['GET','POST'])
def newMobilePhone(company_id):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newMobile = MobilePhones(name = request.form['name'],
                           Specifications = request.form['Specifications'],
                           price = request.form['price'],
                           company_id = company_id)
        session.add(newMobile)
        session.commit()
        flash('New Mobile Phone Created!')
        return redirect(url_for('showMobilePhones', company_id=company_id))
    else:
        return render_template('newMobilePhone.html',company_id = company_id)

# Edit a mobile phone
@app.route('/company/<int:company_id>/mobilephones/<int:mobile_id>/edit', methods=['GET','POST'])
def editMobilePhone(company_id , mobile_id):
    if 'username' not in login_session:
        return redirect('/login')
    editMobile = session.query(MobilePhones).filter_by(id=mobile_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editMobile.name = request.form['name']
            editMobile.Specifications = request.form['Specifications']
            editMobile.price = request.form['price']
        session.add(editMobile)
        session.commit()
        flash("%s has been edited"% editMobile.name)
        return redirect(url_for('showMobilePhones', company_id=company_id ))
    else:
        return render_template('editMobilePhone.html', company_id=company_id , mobile_id= mobile_id , editMobile=editMobile)

# Delete a mobile phone
@app.route('/company/<int:company_id>/mobilephones/<int:mobile_id>/delete', methods=['GET','POST'])
def deleteMobilePhone(company_id, mobile_id):
    if 'username' not in login_session:
        return redirect('/login')
    deleteMobile = session.query(MobilePhones).filter_by(id=mobile_id).one()
    if request.method == 'POST':
        session.delete(deleteMobile)
        session.commit()
        flash("%s has been Deleted"% deleteMobile.name)
        return redirect(url_for('showMobilePhones', company_id=company_id))
    else:
        return render_template('deleteMobilePhone.html',phone=deleteMobile)

# JSON APIs to view Company Information
@app.route('/company/JSON')
def companiesJSON():
    company = session.query(Company).all()
    return jsonify(Company=[i.serialize for i in company])

@app.route('/company/<int:company_id>/mobilephones/JSON')
def mobilePhonesJSON(company_id):
    company = session.query(Company).filter_by(id=company_id).one()
    mobilePhone = session.query(MobilePhones).filter_by(
        company_id=company_id).all()
    return jsonify(MobilePhones=[i.serialize for i in mobilePhone])

@app.route('/company/<int:company_id>/mobilephones/<int:mobile_id>/JSON')
def mobileJSON(company_id, mobile_id):
    mobile = session.query(MobilePhones).filter_by(id=mobile_id).one()
    return jsonify(MobilePhones=mobile.serialize)


if __name__ == '__main__':
    app.secret_key ='super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)