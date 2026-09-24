from flask import Flask,render_template,request,redirect,url_for,flash,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
from datetime import datetime,date

app=Flask(__name__)
app.config["SECRET_KEY"]="change-this-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

DEVELOPER_NAME="MD.Atiqul Islam (Atik)"
DEVELOPER_EMAIL="atik.cmttiu1001@gmail.com"

class Admin(db.Model):
 id=db.Column(db.Integer,primary_key=True); username=db.Column(db.String(100),unique=True,nullable=False)
 password_hash=db.Column(db.String(255),nullable=False); full_name=db.Column(db.String(150),nullable=False)
 email=db.Column(db.String(150)); created_at=db.Column(db.DateTime,default=datetime.utcnow)
 def set_password(self,p): self.password_hash=generate_password_hash(p)
 def check_password(self,p): return check_password_hash(self.password_hash,p)

class Teacher(db.Model):
 id=db.Column(db.Integer,primary_key=True); teacher_id=db.Column(db.String(50),unique=True,nullable=False)
 name=db.Column(db.String(150),nullable=False); subject=db.Column(db.String(100)); phone=db.Column(db.String(30))
 email=db.Column(db.String(150)); qualification=db.Column(db.String(200)); experience=db.Column(db.String(100))
 status=db.Column(db.String(30),default="Active"); created_at=db.Column(db.DateTime,default=datetime.utcnow)

class Batch(db.Model):
 id=db.Column(db.Integer,primary_key=True); batch_code=db.Column(db.String(50),unique=True,nullable=False)
 name=db.Column(db.String(150),nullable=False); subject=db.Column(db.String(100)); teacher_id=db.Column(db.Integer,db.ForeignKey("teacher.id"))
 schedule=db.Column(db.String(200)); room=db.Column(db.String(100)); capacity=db.Column(db.Integer,default=30)
 status=db.Column(db.String(30),default="Active"); teacher=db.relationship("Teacher",backref="batches")

class Student(db.Model):
 id=db.Column(db.Integer,primary_key=True); student_id=db.Column(db.String(50),unique=True,nullable=False)
 name=db.Column(db.String(150),nullable=False); phone=db.Column(db.String(30)); email=db.Column(db.String(150))
 guardian_name=db.Column(db.String(150)); guardian_phone=db.Column(db.String(30)); address=db.Column(db.Text)
 gender=db.Column(db.String(30)); date_of_birth=db.Column(db.String(30)); status=db.Column(db.String(30),default="Pending")
 admission_date=db.Column(db.Date,default=date.today); batch_id=db.Column(db.Integer,db.ForeignKey("batch.id")); created_at=db.Column(db.DateTime,default=datetime.utcnow)

class Attendance(db.Model):
 id=db.Column(db.Integer,primary_key=True); student_id=db.Column(db.Integer,db.ForeignKey("student.id"),nullable=False)
 batch_id=db.Column(db.Integer,db.ForeignKey("batch.id"),nullable=False); attendance_date=db.Column(db.Date,default=date.today)
 status=db.Column(db.String(30),default="Present"); student=db.relationship("Student",backref="attendance_records")
 batch=db.relationship("Batch",backref="attendance_records")

class Fee(db.Model):
 id=db.Column(db.Integer,primary_key=True); student_id=db.Column(db.Integer,db.ForeignKey("student.id"),nullable=False)
 amount=db.Column(db.Float,nullable=False); month=db.Column(db.String(50)); payment_date=db.Column(db.Date,default=date.today)
 status=db.Column(db.String(30),default="Paid"); note=db.Column(db.Text); student=db.relationship("Student",backref="fees")

class Notice(db.Model):
 id=db.Column(db.Integer,primary_key=True); title=db.Column(db.String(200),nullable=False); content=db.Column(db.Text,nullable=False)
 notice_type=db.Column(db.String(50),default="General"); published=db.Column(db.Boolean,default=True); created_at=db.Column(db.DateTime,default=datetime.utcnow)

def login_required(fn):
 @wraps(fn)
 def w(*a,**kw):
  if "admin_id" not in session: flash("Please login as administrator.","warning"); return redirect(url_for("login"))
  return fn(*a,**kw)
 return w

@app.context_processor
def globals_():
 return {"developer_name":DEVELOPER_NAME,"developer_email":DEVELOPER_EMAIL,"today":date.today()}

@app.route("/")
def home(): return redirect(url_for("dashboard" if "admin_id" in session else "login"))

@app.route("/login",methods=["GET","POST"])
def login():
 if request.method=="POST":
  a=Admin.query.filter_by(username=request.form.get("username")).first()
  if a and a.check_password(request.form.get("password","")):
   session["admin_id"]=a.id; session["admin_name"]=a.full_name; flash("Welcome to Shikkha Coaching Centre!","success"); return redirect(url_for("dashboard"))
  flash("Invalid username or password.","danger")
 return render_template("login.html")

@app.route("/logout")
def logout(): session.clear(); flash("You have been logged out.","info"); return redirect(url_for("login"))

@app.route("/dashboard")
@login_required
def dashboard():
 return render_template("dashboard.html",total_students=Student.query.count(),pending_students=Student.query.filter_by(status="Pending").count(),
 approved_students=Student.query.filter_by(status="Approved").count(),total_teachers=Teacher.query.count(),
 active_teachers=Teacher.query.filter_by(status="Active").count(),total_batches=Batch.query.count(),
 active_batches=Batch.query.filter_by(status="Active").count(),total_fees=db.session.query(db.func.sum(Fee.amount)).scalar() or 0,
 recent_students=Student.query.order_by(Student.created_at.desc()).limit(5).all(),
 notices=Notice.query.filter_by(published=True).order_by(Notice.created_at.desc()).limit(5).all())

@app.route("/students")
@login_required
def students():
 q=request.args.get("search",""); st=request.args.get("status",""); query=Student.query
 if q: query=query.filter(db.or_(Student.name.ilike(f"%{q}%"),Student.student_id.ilike(f"%{q}%"),Student.phone.ilike(f"%{q}%")))
 if st: query=query.filter_by(status=st)
 return render_template("students.html",students=query.order_by(Student.created_at.desc()).all(),batches=Batch.query.filter_by(status="Active").all(),search=q,status=st)

@app.route("/students/add",methods=["GET","POST"])
@login_required
def add_student():
 if request.method=="POST":
  if Student.query.filter_by(student_id=request.form["student_id"]).first(): flash("Student ID already exists.","danger"); return redirect(url_for("add_student"))
  s=Student(student_id=request.form["student_id"],name=request.form["name"],phone=request.form.get("phone"),email=request.form.get("email"),
   guardian_name=request.form.get("guardian_name"),guardian_phone=request.form.get("guardian_phone"),address=request.form.get("address"),
   gender=request.form.get("gender"),date_of_birth=request.form.get("date_of_birth"),status=request.form.get("status","Pending"),batch_id=request.form.get("batch_id") or None)
  db.session.add(s); db.session.commit(); flash("Student added successfully.","success"); return redirect(url_for("students"))
 return render_template("student_form.html",student=None,batches=Batch.query.filter_by(status="Active").all())

@app.route("/students/edit/<int:id>",methods=["GET","POST"])
@login_required
def edit_student(id):
 s=Student.query.get_or_404(id)
 if request.method=="POST":
  for f in ["name","phone","email","guardian_name","guardian_phone","address","gender","date_of_birth","status"]: setattr(s,f,request.form.get(f))
  s.batch_id=request.form.get("batch_id") or None; db.session.commit(); flash("Student updated.","success"); return redirect(url_for("students"))
 return render_template("student_form.html",student=s,batches=Batch.query.filter_by(status="Active").all())

@app.route("/students/approve/<int:id>")
@login_required
def approve_student(id): s=Student.query.get_or_404(id); s.status="Approved"; db.session.commit(); flash("Student approved.","success"); return redirect(url_for("students"))

@app.route("/students/reject/<int:id>")
@login_required
def reject_student(id): s=Student.query.get_or_404(id); s.status="Rejected"; db.session.commit(); flash("Student rejected.","warning"); return redirect(url_for("students"))

@app.route("/students/delete/<int:id>")
@login_required
def delete_student(id):
 s=Student.query.get_or_404(id); Attendance.query.filter_by(student_id=id).delete(); Fee.query.filter_by(student_id=id).delete(); db.session.delete(s); db.session.commit(); flash("Student deleted.","success"); return redirect(url_for("students"))

@app.route("/teachers")
@login_required
def teachers(): return render_template("teachers.html",teachers=Teacher.query.order_by(Teacher.created_at.desc()).all())

@app.route("/teachers/add",methods=["GET","POST"])
@login_required
def add_teacher():
 if request.method=="POST":
  if Teacher.query.filter_by(teacher_id=request.form["teacher_id"]).first(): flash("Teacher ID already exists.","danger"); return redirect(url_for("add_teacher"))
  t=Teacher(teacher_id=request.form["teacher_id"],name=request.form["name"],subject=request.form.get("subject"),phone=request.form.get("phone"),
   email=request.form.get("email"),qualification=request.form.get("qualification"),experience=request.form.get("experience"),status=request.form.get("status","Active"))
  db.session.add(t); db.session.commit(); flash("Teacher added.","success"); return redirect(url_for("teachers"))
 return render_template("teacher_form.html",teacher=None)

@app.route("/teachers/edit/<int:id>",methods=["GET","POST"])
@login_required
def edit_teacher(id):
 t=Teacher.query.get_or_404(id)
 if request.method=="POST":
  for f in ["name","subject","phone","email","qualification","experience","status"]: setattr(t,f,request.form.get(f))
  db.session.commit(); flash("Teacher updated.","success"); return redirect(url_for("teachers"))
 return render_template("teacher_form.html",teacher=t)

@app.route("/teachers/delete/<int:id>")
@login_required
def delete_teacher(id):
 t=Teacher.query.get_or_404(id)
 for b in t.batches: b.teacher_id=None
 db.session.delete(t); db.session.commit(); flash("Teacher deleted.","success"); return redirect(url_for("teachers"))

@app.route("/batches")
@login_required
def batches(): return render_template("batches.html",batches=Batch.query.order_by(Batch.id.desc()).all())

@app.route("/batches/add",methods=["GET","POST"])
@login_required
def add_batch():
 if request.method=="POST":
  if Batch.query.filter_by(batch_code=request.form["batch_code"]).first(): flash("Batch code already exists.","danger"); return redirect(url_for("add_batch"))
  b=Batch(batch_code=request.form["batch_code"],name=request.form["name"],subject=request.form.get("subject"),teacher_id=request.form.get("teacher_id") or None,
   schedule=request.form.get("schedule"),room=request.form.get("room"),capacity=int(request.form.get("capacity",30)),status=request.form.get("status","Active"))
  db.session.add(b); db.session.commit(); flash("Batch created.","success"); return redirect(url_for("batches"))
 return render_template("batch_form.html",batch=None,teachers=Teacher.query.filter_by(status="Active").all())

@app.route("/batches/edit/<int:id>",methods=["GET","POST"])
@login_required
def edit_batch(id):
 b=Batch.query.get_or_404(id)
 if request.method=="POST":
  for f in ["name","subject","schedule","room","status"]: setattr(b,f,request.form.get(f))
  b.teacher_id=request.form.get("teacher_id") or None; b.capacity=int(request.form.get("capacity",30)); db.session.commit(); flash("Batch updated.","success"); return redirect(url_for("batches"))
 return render_template("batch_form.html",batch=b,teachers=Teacher.query.filter_by(status="Active").all())

@app.route("/batches/delete/<int:id>")
@login_required
def delete_batch(id):
 b=Batch.query.get_or_404(id); Student.query.filter_by(batch_id=id).update({"batch_id":None}); Attendance.query.filter_by(batch_id=id).delete(); db.session.delete(b); db.session.commit(); flash("Batch deleted.","success"); return redirect(url_for("batches"))

@app.route("/attendance",methods=["GET","POST"])
@login_required
def attendance():
 bs=Batch.query.filter_by(status="Active").all(); bid=request.args.get("batch_id",""); d=request.args.get("date",str(date.today()))
 ss=Student.query.filter_by(batch_id=int(bid),status="Approved").all() if bid else []
 if request.method=="POST":
  bid=int(request.form["batch_id"]); d=datetime.strptime(request.form["attendance_date"],"%Y-%m-%d").date()
  for s in Student.query.filter_by(batch_id=bid,status="Approved").all():
   st=request.form.get(f"attendance_{s.id}","Absent"); r=Attendance.query.filter_by(student_id=s.id,batch_id=bid,attendance_date=d).first()
   if r:r.status=st
   else:db.session.add(Attendance(student_id=s.id,batch_id=bid,attendance_date=d,status=st))
  db.session.commit(); flash("Attendance saved.","success"); return redirect(url_for("attendance",batch_id=bid,date=d))
 ex={}
 if bid:
  for r in Attendance.query.filter_by(batch_id=int(bid),attendance_date=datetime.strptime(d,"%Y-%m-%d").date()).all(): ex[r.student_id]=r.status
 return render_template("attendance.html",batches=bs,students=ss,selected_batch=bid,selected_date=d,existing_attendance=ex)

@app.route("/fees",methods=["GET","POST"])
@login_required
def fees():
 if request.method=="POST":
  db.session.add(Fee(student_id=int(request.form["student_id"]),amount=float(request.form["amount"]),month=request.form.get("month"),
   payment_date=datetime.strptime(request.form["payment_date"],"%Y-%m-%d").date(),status=request.form.get("status","Paid"),note=request.form.get("note")))
  db.session.commit(); flash("Payment recorded.","success"); return redirect(url_for("fees"))
 return render_template("fees.html",fees=Fee.query.order_by(Fee.payment_date.desc()).all(),students=Student.query.filter_by(status="Approved").all(),
  total_paid=db.session.query(db.func.sum(Fee.amount)).filter(Fee.status=="Paid").scalar() or 0)

@app.route("/fees/delete/<int:id>")
@login_required
def delete_fee(id): f=Fee.query.get_or_404(id); db.session.delete(f); db.session.commit(); flash("Payment deleted.","success"); return redirect(url_for("fees"))

@app.route("/notices")
@login_required
def notices(): return render_template("notices.html",notices=Notice.query.order_by(Notice.created_at.desc()).all())

@app.route("/notices/add",methods=["GET","POST"])
@login_required
def add_notice():
 if request.method=="POST":
  db.session.add(Notice(title=request.form["title"],content=request.form["content"],notice_type=request.form.get("notice_type","General"))); db.session.commit(); flash("Notice published.","success"); return redirect(url_for("notices"))
 return render_template("notice_form.html",notice=None)

@app.route("/notices/edit/<int:id>",methods=["GET","POST"])
@login_required
def edit_notice(id):
 n=Notice.query.get_or_404(id)
 if request.method=="POST":
  n.title=request.form["title"]; n.content=request.form["content"]; n.notice_type=request.form.get("notice_type","General"); n.published=request.form.get("published")=="on"; db.session.commit(); flash("Notice updated.","success"); return redirect(url_for("notices"))
 return render_template("notice_form.html",notice=n)

@app.route("/notices/delete/<int:id>")
@login_required
def delete_notice(id): n=Notice.query.get_or_404(id); db.session.delete(n); db.session.commit(); flash("Notice deleted.","success"); return redirect(url_for("notices"))

@app.route("/settings",methods=["GET","POST"])
@login_required
def settings():
 a=Admin.query.get(session["admin_id"])
 if request.method=="POST":
  a.full_name=request.form["full_name"]; a.email=request.form.get("email"); np=request.form.get("new_password")
  if np:
   if not a.check_password(request.form.get("current_password","")): flash("Current password is incorrect.","danger"); return redirect(url_for("settings"))
   if len(np)<6: flash("New password must contain at least 6 characters.","danger"); return redirect(url_for("settings"))
   a.set_password(np)
  db.session.commit(); session["admin_name"]=a.full_name; flash("Admin settings updated.","success"); return redirect(url_for("settings"))
 return render_template("settings.html",admin=a)

def seed():
 if not Admin.query.filter_by(username="admin").first():
  a=Admin(username="admin",full_name="Shikkha Centre Administrator",email=DEVELOPER_EMAIL); a.set_password("Admin@123"); db.session.add(a); db.session.commit()
with app.app_context(): db.create_all(); seed()
if __name__=="__main__": app.run(debug=True,host="127.0.0.1",port=5000)
