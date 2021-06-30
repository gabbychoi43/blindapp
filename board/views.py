from datetime import datetime
from board.models import boardcontent, reply, rereply, user, board
from django.shortcuts import render
from django.http import HttpResponse
import django.utils.crypto as crypt
import bcrypt
from django.utils import timezone

# Create your views here.

def index(request) :
    '''
    for i in range(10) :
        d=user(id=i+1,userid='A'*i,pw=bcrypt.hashpw(('BS'*i).encode('utf-8'),salt=bcrypt.gensalt()),name='C'*i,dept='육군',expiredate=timezone.datetime.now(),signdate=timezone.datetime.now(),auth='가입대기')
        d.save()
        
    d=board(1,'게시판1',timezone.datetime.now())
    d.save()
    d=boardcontent(cre_date=timezone.datetime.now(),hit=0,isnotice=True,content=,boardid_id=1,userid_id=5)

    d.save()
    
    d=reply(cre_date=timezone.datetime.now(),reply=, boardcontentid_id=4,userid_id=1)
    

    '''

    d=rereply(replyid_id=1,cre_date=timezone.datetime.now(),rereply='''대댓글입니다3''',userid_id=6)
    d.save()
    return HttpResponse('오류가 안뜨면 저장이 완료된것')