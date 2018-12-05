from flask import Flask, render_template, request, redirect, url_for , flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Company, MobilePhones

app = Flask(__name__)

engine = create_engine('sqlite:///mobilephones.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home/')
def showCompanies():
    company = session.query(Company).all()

    return render_template('companies.html', company=company)

@app.route('/company/new/', methods = ['GET','POST'])
def newCompany():
    if request.method == 'POST':
        newCompany = Company(name = request.form['name'] )
        session.add(newCompany)
        session.commit()
        flash('New Company Created!')
        return redirect(url_for('showCompanies'))
    else:
        return render_template('newCompany.html')

@app.route('/company/<int:company_id>/edit/' , methods = ['GET','POST'])
def editCompanies(company_id):
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

@app.route('/company/<int:company_id>/delete/', methods = ['GET','POST'])
def deleteCompanies(company_id):
    deleteCompany = session.query(Company).filter_by(id=company_id).one()
    if request.method == 'POST':
        session.delete(deleteCompany)
        session.commit()
        flash("%s has been deleted"% deleteCompany.name)
        return redirect(url_for('showCompanies'))
    else:
        return render_template('deleteCompany.html', company=deleteCompany)

@app.route('/company/<int:company_id>/')
@app.route('/company/<int:company_id>/mobilePhones/')
def showMobilePhones(company_id):
    company = session.query(Company).filter_by(id = company_id).first()
    mobilePhones = session.query(MobilePhones).filter_by(company_id = company_id)
    return render_template("mobilePhones.html", company = company, company_id = company_id , mobilePhones=mobilePhones)

@app.route('/company/<int:company_id>/mobilePhones/new', methods = ['GET','POST'])
def newMobilePhone(company_id):
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

@app.route('/company/<int:company_id>/mobilePhones/<int:mobile_id>/edit', methods=['GET','POST'])
def editMobilePhone(company_id , mobile_id):
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

@app.route('/company/<int:company_id>/mobilePhones/<int:mobile_id>/delete', methods=['GET','POST'])
def deleteMobilePhone(company_id, mobile_id):
    deleteMobile = session.query(MobilePhones).filter_by(id=mobile_id).one()
    if request.method == 'POST':
        session.delete(deleteMobile)
        session.commit()
        flash("%s has been Deleted"% deleteMobile.name)
        return redirect(url_for('showMobilePhones', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMobilePhone.html',phone=deleteMobile)

@app.route('/home/JSON')
def companiesJSON():
    company = session.query(Company).all()
    return jsonify(Company=[i.serialize for i in company])

@app.route('/company/<int:company_id>/mobilePhones/JSON')
def mobilePhonesJSON(company_id):
    company = session.query(Company).filter_by(id=company_id).one()
    mobilePhone = session.query(MobilePhones).filter_by(
        company_id=company_id).all()
    return jsonify(MobilePhones=[i.serialize for i in mobilePhone])

@app.route('/company/<int:company_id>/mobilePhones/<int:mobile_id>/JSON')
def mobileJSON(company_id, mobile_id):
    mobile = session.query(MobilePhones).filter_by(id=mobile_id).one()
    return jsonify(MobilePhones=mobile.serialize)


if __name__ == '__main__':
    app.secret_key ='super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)