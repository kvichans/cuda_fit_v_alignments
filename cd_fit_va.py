''' Plugin for CudaText editor
Authors:
    Andrey Kvichansky    (kvichans on github.com)
Version:
    '0.9.0 2015-11-26'
ToDo: (see end of file)
'''

import  re, os
import  cudatext        as app
from    cudatext    import ed
import  cudax_lib       as apx
from    .cd_plug_lib    import *
_   = get_translation(__file__) # I18N

pass;                           # Logging
pass;                           from pprint import pformat
pass;                           pfrm15=lambda d:pformat(d,width=15)
pass;                           pfrm150=lambda d:pformat(d,width=150)
pass;                           LOG = (-2==-2)  # Do or dont logging.

class Command:
    def dlg_valign_consts(self):
        pass;                   LOG and log('ok')
        DLG_W,  \
        DLG_H   = 310, 310
        vals    = dict(
#                  _sp1=top_plus_for_os('check'         , 'label')
#                 ,_sp2=top_plus_for_os('edit'          , 'label')
#                 ,_sp3=top_plus_for_os('button'        , 'label')
#                 ,_sp4=top_plus_for_os('combo_ro'      , 'label')
#                 ,_sp5=top_plus_for_os('combo'         , 'label')
#                 ,_sp6=top_plus_for_os('checkbutton'   , 'label')
#                 ,_sp7=top_plus_for_os('linklabel'     , 'label')
#                 ,_sp8=top_plus_for_os('spinedit'      , 'label')
                   _sp1=fit_top_by_env('check')
                  ,_sp2=fit_top_by_env('edit')
                  ,_sp3=fit_top_by_env('button')
                  ,_sp4=fit_top_by_env('combo_ro')
                  ,_sp5=fit_top_by_env('combo')
                  ,_sp6=fit_top_by_env('checkbutton')
                  ,_sp7=fit_top_by_env('linklabel')
                  ,_sp8=fit_top_by_env('spinedit')
                  ,ch1 =False
                  ,ed2 ='====fit'
                  ,cbo4=0
                  ,cb5 ='====fit'
                  ,chb6=0
                  ,sp8 =4444444
                  )
        focused = '_sp1'
        while True:
            aid, vals, chds = dlg_wrapper(_('V-Alignment Fitting: env='+get_desktop_environment())   ,DLG_W, DLG_H, 
                [dict(cid='_sp1'    ,tp='sp-ed' ,t=  5              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb1'     ,tp='lb'    ,t=  5              ,l=60   ,w=100  ,cap='base:=========='  )
                ,dict(cid='ch1'     ,tp='ch'    ,t=  5+vals['_sp1'] ,l=170  ,w=100  ,cap='====fit'          )
                
                ,dict(cid='_sp2'    ,tp='sp-ed' ,t= 35              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb2'     ,tp='lb'    ,t= 35              ,l=60   ,w=100  ,cap='base:=========='  )
                ,dict(cid='ed2'     ,tp='ed'    ,t= 35+vals['_sp2'] ,l=170  ,w=100                          )
                
                ,dict(cid='_sp3'    ,tp='sp-ed' ,t= 65              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb3'     ,tp='lb'    ,t= 65              ,l=60   ,w=100  ,cap='base:=========='  )
                ,dict(cid='bt3'     ,tp='bt'    ,t= 65+vals['_sp3'] ,l=170  ,w=100  ,cap='========fit'      )
                
                ,dict(cid='_sp4'    ,tp='sp-ed' ,t= 95              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb4'     ,tp='lb'    ,t= 95              ,l=60   ,w=100  ,cap='base:=========='  )
                ,dict(cid='cbo4'    ,tp='cb-ro' ,t= 95+vals['_sp4'] ,l=170  ,w=100  ,items=['====fit']      )
                
                ,dict(cid='_sp5'    ,tp='sp-ed' ,t=125              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb5'     ,tp='lb'    ,t=125              ,l=60   ,w=100  ,cap='base:=========='  )
                ,dict(cid='cb5'     ,tp='cb'    ,t=125+vals['_sp5'] ,l=170  ,w=100  ,items=['====fit']      )
                
                ,dict(cid='_sp6'    ,tp='sp-ed' ,t=155              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb6'     ,tp='lb'    ,t=155              ,l=60   ,w=100  ,cap='base:=========='  )
                ,dict(cid='chb6'    ,tp='ch-bt' ,t=155+vals['_sp6'] ,l=170  ,w=100  ,cap='========fit'      )
                
                ,dict(cid='_sp7'    ,tp='sp-ed' ,t=185              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb7'     ,tp='lb'    ,t=185              ,l=60   ,w=100  ,cap='base:=========='  )
                ,dict(cid='chb7'    ,tp='ln-lb' ,t=185+vals['_sp7'] ,l=170  ,w=100  ,cap='========fit',props='ya.ru')
                
                ,dict(cid='_sp8'    ,tp='sp-ed' ,t=215              ,l=5    ,w=40   ,props='10,-10,-1'      )
                ,dict(cid='lb8'     ,tp='lb'    ,t=215              ,l=60   ,w=100  ,cap='base:44444444444' )
                ,dict(cid='sp8'     ,tp='sp-ed' ,t=215+vals['_sp8'] ,l=170  ,w=100  ,props='0,4444444,1'    )
                
                ,dict(cid='apply'   ,tp='bt'    ,t=DLG_H-60         ,l=5    ,w=80   ,cap=_('Re&Align') ,props='1'
                                                                                    ,hint=_('Apply fittings to controls of this dialog'))
                ,dict(cid='rprt'    ,tp='bt'    ,t=DLG_H-30         ,l=5    ,w=80   ,cap=_('&Report')
                                                                                    ,hint=_('Show data to change default fittings'))
                ,dict(cid='save'    ,tp='bt'    ,t=DLG_H-30     ,l=DLG_W-170,w=80   ,cap=_('&Save')
                                                                                    ,hint=_('Apply fittings to controls of all dialogs'))
                ,dict(cid='-'       ,tp='bt'    ,t=DLG_H-30     ,l=DLG_W-85 ,w=80   ,cap=_('Cancel')    )
                ], vals, focus_cid=focused)
            if aid is None or aid=='-':    return#while True
            focused = chds[0] if 1==len(chds) else focused
            if aid=='save':
                ctrls   = ['check'
                          ,'edit'
                          ,'button'   
                          ,'combo_ro' 
                          ,'combo'    
                          ,'checkbutton'
                          ,'linklabel'
                          ,'spinedit'
                          ]
                for ic, nc in enumerate(ctrls):
                    fit = vals['_sp'+str(1+ic)]
                    if fit==fit_top_by_env(nc): continue#for ic, nc
                    apx.set_opt('dlg_wrapper_fit_va_for_'+nc, fit)
                   #for ic, nc
                fit_top_by_env__clear()
#               app.msg_box(_('Need restart CudaText to use saved values'))
            
            if aid=='rprt':
                rpt = 'env:'+get_desktop_environment()
                rpt+= c13+'check:'+str(vals['_sp1'])
                rpt+= c13+'edit:'+str(vals['_sp2'])
                rpt+= c13+'button:'+str(vals['_sp3'])
                rpt+= c13+'combo_ro:'+str(vals['_sp4'])
                rpt+= c13+'combo:'+str(vals['_sp5'])
                rpt+= c13+'checkbutton:'+str(vals['_sp6'])
                rpt+= c13+'linklabel:'+str(vals['_sp7'])
                rpt+= c13+'spinedit:'+str(vals['_sp8'])
                aid_r, vals_r, chds_r = dlg_wrapper(_('Report'), 210,290,     #NOTE: dlg-hlp
                     [dict(cid='rprt',tp='me'    ,t=5   ,l=5 ,h=200 ,w=200)
                     ,dict(           tp='lb'    ,t=215 ,l=5        ,w=200, cap=_('Send the report to addres'))
                     ,dict(cid='mail',tp='ed'    ,t=235 ,l=5        ,w=200)
                     ,dict(cid='-'   ,tp='bt'    ,t=260 ,l=205-80   ,w=80   ,cap=_('Close'))
                     ], dict(rprt=rpt
                            ,mail='kvichans@mail.ru'), focus_cid='rprt')
#               if aid_r is None or btn_hlp=='-': break#while_hlp
       #def dlg_halign_consts

   #class Command

'''
ToDo
'''
