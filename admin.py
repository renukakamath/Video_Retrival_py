from flask import*
from database import*

admin=Blueprint('admin',__name__)


@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')


@admin.route('/admin_managesubject',methods=['post','get'])
def admin_managesubject():
    data={}
    q="select * from subject"
    res=select(q)
    data['viewsubject']=res
    
    if "action" in request.args:
        action=request.args['action']
        sid=request.args['sid']
        
        if action=='delete':
            q="delete from subject where subject_id='%s'"%(sid)
            delete(q)
            flash('successfully')
            return redirect(url_for('admin.admin_managesubject'))
        if action=='update':
            q="select * from subject where subject_id='%s'"%(sid)
            res=select(q)
            data['updatesubject']=res
            
            
            if "update" in request.form:
                sub=request.form['sub']
                q="update subject set subject='%s' where subject_id='%s'"%(sub,sid)
                update(q)
                flash('successfully')
                return redirect(url_for('admin.admin_managesubject'))
            
            
    
    if "subject" in request.form:
        sub=request.form['sub']
        q="insert into subject values(null,'%s')"%(sub)
        insert(q)
        flash('successfully')
        return redirect(url_for('admin.admin_managesubject'))
    
    return render_template('admin_managesubject.html',data=data)


@admin.route('/admin_viewsubject',methods=['post','get'])
def admin_viewsubject():
    data={}
    q="select * from subject"
    res=select(q)
    data['viewsubject']=res

    
    return render_template('admin_viewsubject.html',data=data)


@admin.route('/admin_manageteacher',methods=['post','get'])
def admin_manageteacher():
    data={}
    q="select * from teacher"
    res=select(q)
    data['viewteacher']=res
    
    
    
    if "action" in request.args:
        action=request.args['action']
        
        uid=request.args['uid']
        
    else:
        action=None
        
        
    if action=='delete':
        q="delete from teacher where teacher_id='%s'"%(uid)
        delete(q)
        return redirect(url_for('admin.admin_manageteacher'))

    
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
        return redirect(url_for('admin.admin_manageteacher'))
    
    
    
    
    
    return render_template('admin_manageteacher.html',data=data)
@admin.route('/admin_viewvideos')
def admin_viewvideos():
    data={}
    q="select * from videos inner join teacher using (teacher_id) inner join subject using (subject_id)"
    res=select(q)
    data['videoview']=res

    return render_template('admin_viewvideos.html',data=data)

@admin.route('/admin_viewkeywords')
def admin_viewkeywords():
    data={}
    q="select * from keyword inner join `farmes` using (farme_id) inner join `videos` using (video_id)"
    res=select(q)
    data['keywordview']=res
    return render_template('admin_viewkeywords.html',data=data)


@admin.route('/admin_viewcomplaints')
def admin_viewcomplaints():
    data={}
    q="select * from complaint inner join student using (student_id)"
    res=select(q)
    data['comp']=res
    return render_template('admin_viewcomplaints.html',data=data)


@admin.route('/sendreply',methods=['get','post'])
def sendreply():
    if "sendreply" in request.form:
        rep=request.form['rep']
        cid=request.args['cid']
        q="update complaint set reply='%s' where complaint_id='%s'"%(rep,cid)
        update(q)
        flash('successfully')
        return redirect(url_for('admin.admin_viewcomplaints'))

    return render_template('sendreply.html')


@admin.route('/admin_assignsubject',methods=['post','get'])
def admin_assignsubject():
    data={}
    q="select * from subject"
    res=select(q)
    data['subdrop']=res
    if "subjectadd" in request.form:
        sub=request.form['sub']
        tid=request.args['tid']
        q="insert into assignsubject values(null,'%s','%s')"%(sub,tid)
        insert(q)
        flash('successfully')

        return redirect(url_for('admin.admin_assignsubject'))
    return render_template('admin_assignsubject.html',data=data)
