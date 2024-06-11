from flask import*
from database import*

public=Blueprint('public',__name__)


@public.route('/')
def public_home():
    return render_template('public_home.html')


@public.route('/public_login',methods=['post','get'])
def public_login():
    if "login" in request.form:
        u=request.form['uname']
        p=request.form['pwd']
        q="select * from login where username='%s' and password='%s'"%(u,p)
        res=select(q)
        if res:
            session['login_id']=res[0]['login_id']
            lid=session['login_id']
            if res[0]['usertype']=="admin":
                return redirect(url_for('admin.admin_home'))
            elif res[0]['usertype']=="teacher":
                q="select * from teacher inner join login using (login_id) where login_id='%s'"%(lid)
                res=select(q)
                if res:
                    session['teacher_id']=res[0]['teacher_id']
                    tid=session['teacher_id']
                return redirect(url_for('teacher.teacher_home'))
    return render_template('public_login.html')



@public.route('/teacher_registration',methods=['post','get'])
def teacher_registration():
  

    
    if "teacher" in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        pho=request.form['pho']
        email=request.form['email']
        uname=request.form['uname']
        pwd=request.form['pwd']
        q="insert into login values(null,'%s','%s','teacher')"%(uname,pwd)
        id=insert(q)
        q="insert into teacher values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,pho,email)
        insert(q)
        flash('successfully')
        return redirect(url_for('public.teacher_registration'))
    
    
    
    
    
    return render_template('teacher_registration.html')


@public.route('/student_registration',methods=['post','get'])
def student_registration():

                
    
    if "student" in request.form:
        number=request.form['number']
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        pho=request.form['pho']
        email=request.form['email']
        uname=request.form['uname']
        pwd=request.form['pwd']
        q="insert into login values(null,'%s','%s','Student')"%(uname,pwd)
        id=insert(q)
        q="insert into student values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,pho,email,number)
        insert(q)
        flash('successfully')
        return redirect(url_for('public.student_registration'))
    
    return render_template('student_registration.html')



              
              
              
    