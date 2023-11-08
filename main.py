import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

url = 'https://camsys.mmu.edu.my/psp/csprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_CART_GBL&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=CO_EMPLOYEE_SELF_SERVICE&EOPP.SCLabel=Enrollment&EOPP.SCFName=HCCC_ENROLLMENT&EOPP.SCSecondary=true&EOPP.SCPTfname=HCCC_ENROLLMENT&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.N_NEW_ACADEMICS.N_NEW_CRSENRL.HCCC_ENROLLMENT.HC_SSR_SSENRL_CART_GBL&IsFolder=false'

payload = {
    'cmd' : 'login',
    'languageCd' : 'ENG',
    'timezoneOffset' : '-480',
    'userid' : '1211104786',
    'pwd' : 'Tanzhixuan_1217'
}

r = requests.post(url = url, headers = headers, data=payload)
r.encoding = 'utf-8'

print(r.text)
print(r)
print(r.url)