 
Script Name: PyRunStatus
========================
Func:It will get the status of a running script in processing huge data. ( percentage,costed Time, Finish Time)

It's tiny , but useful!

 User and CopyRight
========================
user:xu1ji 
email:blueorange4444@gmail.com
CreateTime:	2012-11
EditHistory:	None
CopyRight:You are free to copy and use ,and welcome2 mail me if you have any question.


 UseMethod
========================
 1.import   sys.path.append("--your path--")  
 2.init     tDbg = PyRunStatus.xuRunTime()
 3.setSum   tDbg.setSum(1000)
 4.goStart  gDbg.goStart()
 5.returnTime gDbg.returnTime() or gDbg.returnTime(isSec=False)
 6.addOne    gDbg.addOne()  or gDbg.addOne(4)


