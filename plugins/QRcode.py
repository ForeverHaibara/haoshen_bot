# -*- coding: utf-8 -*-
"""
@author: zyckk4  https://github.com/zyckk4
"""
from utils.utils import Listen,send
from mirai import Plain,Image
import qrcode

@Listen.all_mesg()
async def make_QRcode(event):
    if str(event.message_chain).startswith('/二维码'):
        if event.message_chain.count(Image)>0:
               await send(event,"当前不支持二维码内添加图片！",True)
               return
        x=str(event.message_chain.get(Plain)[0]).replace('/二维码','',1)
        if x.startswith(' '):
            x=x.replace(' ','',1)
        img=ez_make_QRcode(x)
        await send(event,[],PIL_image=img)

def ez_make_QRcode(content):
    img=qrcode.make(content)
    return img