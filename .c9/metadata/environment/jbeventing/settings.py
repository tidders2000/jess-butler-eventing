{"filter":false,"title":"settings.py","tooltip":"/jbeventing/settings.py","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":73}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":22},"action":"insert","lines":["#import env","import dj_database_url"],"id":74}],[{"start":{"row":85,"column":5},"end":{"row":86,"column":0},"action":"insert","lines":["",""],"id":75},{"start":{"row":86,"column":0},"end":{"row":86,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":86,"column":4},"end":{"row":86,"column":82},"action":"insert","lines":["DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"],"id":76}],[{"start":{"row":86,"column":2},"end":{"row":86,"column":82},"action":"remove","lines":["  DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"],"id":77}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":80},"action":"insert","lines":["  DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"],"id":78}],[{"start":{"row":81,"column":0},"end":{"row":81,"column":1},"action":"insert","lines":["#"],"id":79}],[{"start":{"row":82,"column":0},"end":{"row":82,"column":1},"action":"insert","lines":["#"],"id":80}],[{"start":{"row":83,"column":1},"end":{"row":83,"column":2},"action":"insert","lines":["#"],"id":81}],[{"start":{"row":84,"column":1},"end":{"row":84,"column":2},"action":"insert","lines":["#"],"id":82}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":1},"action":"insert","lines":["#"],"id":83}],[{"start":{"row":87,"column":0},"end":{"row":87,"column":1},"action":"insert","lines":["#"],"id":84}],[{"start":{"row":89,"column":1},"end":{"row":89,"column":2},"action":"remove","lines":[" "],"id":85},{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":78,"column":0},"end":{"row":89,"column":78},"action":"remove","lines":["# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","#DATABASES = {","#    'default': {"," #       'ENGINE': 'django.db.backends.sqlite3',"," #       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#    }","  ","#}","","DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"],"id":86},{"start":{"row":78,"column":0},"end":{"row":88,"column":0},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","       DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database url not found using sql instead\")","    DATABASES = {","     'default': {","        'ENGINE': 'django.db.backends.sqlite3',","       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}",""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["#"],"id":87}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["£"],"id":88}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["£"],"id":89}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":90}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":1},"end":{"row":13,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1569182797394,"hash":"44152e4e5849c5ae4630ac8a534888388bbc3eab"}