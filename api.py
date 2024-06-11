from flask import*
from database import*

api=Blueprint('api',__name__)


@api.route('/logins')
def logins():
	data={}

	u=request.args['username'];
	p=request.args['password'];
	q="select * from login where username='%s' and password='%s'"%(u,p)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return str(data)


@api.route('/ViewUpdateprofile')
def ViewUpdateprofile():
	data={}
	lid=request.args['lid']
	q="select * from student where login_id='%s'"%(lid)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	data['method']="ViewUpdateprofile"
	return str(data)

@api.route('/Updateprofile')
def Updateprofile():
	data={}
	n=request.args['name']
	p=request.args['place']
	ph=request.args['Phone']
	e=request.args['email']
	ln=request.args['lname']
	lid=request.args['login_id']
	q="update student set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(n,ln,p,ph,e,lid)
	update(q)
	
	data['status']='success'
	data['method']="Updateprofile"
	return str(data)

@api.route('/Viewsubject')
def Viewsubject():
	data={}
	q="select * from subject"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"


	
	return str(data)


@api.route('/viewspinner')
def viewspinner():
	data={}
	q="SELECT * FROM `subject`"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
		data['method']="viewspinner"
	
	return str(data)


@api.route('/viewSearchkeyword')
def viewSearchkeyword():
	data={}
	q="SELECT * FROM `keyword` INNER JOIN `farmes` USING (`farme_id`) INNER JOIN `videos` USING (`video_id`)"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
		data['method']="viewSearchkeyword"
	
	return str(data)


@api.route('/Searchkeyword')	
def Searchkeyword():
	data={}
	search=request.args['search']+'%'
	sid=request.args['sid']
	q="SELECT * FROM `keyword` INNER JOIN `farmes` USING (`farme_id`) INNER JOIN `videos` USING (`video_id`) where keyword like '%s'  or subject_id='%s'"%(search,sid)
	res=select(q)
	print(q)
	if res:
		data['status']="success"
		data['data']=res

	else:
		data['status']="failed"
		data['method']="Searchkeyword"
	
	return str(data)


@api.route('/Viewnotes')
def Viewnotes():
	data={}
	q="SELECT * FROM `notes` INNER JOIN `teacher` USING (`teacher_id`) INNER JOIN `subject` USING (`subject_id`)"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
	
	return str(data)


@api.route('/complaint')	
def complaint():
	data={}
	lid=request.args['lid']
	c=request.args['complaint']
	q="insert into `complaint` values(null,(select student_id from student where login_id='%s'),'%s','pending',curdate())"%(lid,c)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="complaint"
	return str(data)

@api.route('/viewcomplaints')
def viewcomplaints():
	data={}
	lid=request.args['lid']
	q="select * from complaint inner join student using (student_id) where login_id='%s'"%(lid)
	res=select(q)
	data['data']=res
	data['status']="success"
	data['method']="viewcomplaints"
	return str(data)

@api.route('/public_view_videos')
def public_view_videos():
	data={}
	vid=request.args['Video_id']
	q="select * from videos where video_id='%s'"%(vid)
	res=select(q)
	print(q)
	data['data']=res
	data['status']="success"
	data['method']="public_view_videos"
	return str(data)

