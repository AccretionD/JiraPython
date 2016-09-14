#coding: utf8 
from jira.client import JIRA,GreenHopper
import sys, getopt, ConfigParser, os
from read_file_test import FileReader


class Jira_committer:
    def __init__(self, user, pwd):
        self.options = {
            'server': 'https://meridian.atlassian.net'
        } 
        self.authed_jira = GreenHopper(options=self.options,basic_auth=(user,pwd))
        #self.authed_green = GreenHopper(options=self.options,basic_auth=('camilo.soto','19055573'))


    def add_worklog(self,issue, time, comment):
        print 'issue time', issue, time, comment
        worklog = self.authed_jira.add_worklog(issue, time)
        worklog.update(comment=comment, timeSpent=worklog.timeSpent)

    def svn_command (self,command):
        os.system(command)

    def create_issue_with_fields(self, project, summary, description, environment, assignee, issuetype, priority, time):

        fields_issue = {'project': {'key': project},
                'summary':summary,
                'description':description,
                'environment':environment,
                'assignee':{'name':assignee},
                'issuetype':{'name':issuetype},
                'customfield_10800':{'id':'10415'},
                'priority':{'name':priority}}
        issue=self.authed_jira.create_issue(fields=fields_issue)
        print 'issue.....', issue

    def create_issue_with_fields_subtask(self, project, subtask_id,summary, description, environment, assignee, priority, time):

        fields_issue = {'project': {'key': project},
                'parent':{'key': subtask_id},
                'summary':summary,
                'description':description,
                'environment':environment,
                'assignee':{'name':assignee},
                'issuetype':{'id':'7'},
                'customfield_10800':{'id':'10415'},
                'priority':{'name':priority},
                'timetracking':{'originalEstimate':time,'remainingEstimate':time}}
        issue=self.authed_jira.create_issue(fields=fields_issue)
        print 'issue.....', issue

    def create_android(self):
        descriptions= [{'Seguimiento':'Lograr deteccion de Peajes, POIs, etc y generar una notificacion del sistema'},{'Notificaciones':'A partide de notificacion del sistema mostrar el detalle de notificacion'},{'Configuracion de ruta':'ventana de configuracion de ruta (Cilindraje, Vehiculo, combustible)'},{'Ruta famoso':'si se detecta condiciones se muestra la ventana de ruta de famoso'}, {'Seleccion tipo de ruta':'seleccionar el tipo de ruta: normal, famoso, gastronomica, etc'}, {'Formulario de ruta':'tener un formulario con parametros adicionales (checklist, costo)'}, {'Detalle de ruta':'ver el detalle de ruta con los cambios para fase 2'}, {'Edicion puntos intermedios':'tener la posibilidad de editar los puntos intermedios en una ventana flotante'}, {'Detalles de costos de ruta':'poder ver los detalles del costo de una ruta. (peajes, costo total, etc)'}, {'Guardar ruta':'poder guardar una ruta con formulario fase 2'},{'Menu de ruta':'tener una ventana para poder lanzas las distintas subsecciones de rutas'},{'Radar fase 2':'tener un radar con los items de fase 2 (famosos, peajes, barra ruta, botones)'}, {'Filtro famosos':'Tener un nuevo filtro q prenda y apague ruta personalizada'}, {'Subsecciones perfil':'Cambios de elementos graficos en perfil'}]
        jira_android= [{'Seguimiento':[{'time':'1h','name':'Reunion seguimiento'},{'time':'13h','name':'Algoritmos de deteccion'},{'time':'3h','name':'Notificaciones desde movil'},{'time':'8h','name':'Offline (storage minimo y completo)'}]}, {'Notificaciones':[{'time':'1h','name':'Discucion campos cambiantes y nuevos'},{'time':'9h','name':'Fragmento contenedor principal'},{'time':'6h','name':'Configuracion de notificaciones'}]}, {'Configuracion de ruta':[{'time':'3h','name':'Discucion protocolo'},{'time':'10h','name':'Montaje y funcionalidad ventana'}]},{'Ruta famoso':[{'time':'9h','name':'Deteccion de ruta'},{'time':'10h','name':'Ventana de famoso'}]},{'Seleccion tipo de ruta':[{'time':'10h','name':'Modificacion esquema actual'},{'time':'12h','name':'Ventana de seleccion'}]}, {'Formulario de ruta':[{'time':'9h','name':'Adicion de parametros'}]}, {'Detalle de ruta':[{'time':'9h','name':'seccion vista puntos intermedios'},{'time':'5h','name':'seccion costo de ruta'},{'time':'3h','name':'seccion descripcion de ruta tematica'},{'time':'5h','name':'adecuacion detalle fase1'}]}, {'Edicion puntos intermedios':[{'time':'11h','name':'migracion a ventana flotante'},{'time':'6h','name':'adecuación punto A y B fase 1'}]},{'Detalles de costos de ruta':[{'time':'2h','name':'Discucion protocolos'},{'time':'26h','name':'implementacion ventana de detalle'}]}, {'Guardar ruta':[{'time':'7h','name':'Adecuacion fase 1'}]}, {'Menu de ruta':[{'time':'10h','name':'Montaje ventana'},{'time':'10h','name':'Conexion subsecciones'}]}, {'Radar fase 2':[{'time':'10h','name':'Adicion item famosos'},{'time':'7h','name':'Implementacion burbuja peajes'},{'time':'21h','name':'Distencion item pequeno y mediano'},{'time':'6h','name':'Barra en modo ruta'},{'time':'31h','name':'Voltear el radar'},{'time':'13h','name':'Botones flotantes'}]}, {'Filtro famosos':[{'time':'8h','name':'Validacion libreria adicion-eliminacion'},{'time':'8h','name':'Implementacion filtro'}]}, {'Subsecciones perfil':[{'time':'5h','name':'Cambios menu lateral y conexiones'}]}]
        for j in range(0, len(jira_android)):
            desc_obj=descriptions[j];
            todo_obj=jira_android[j]
            key =todo_obj.keys()[0]
            sub_task_array=todo_obj[key]
            desc=desc_obj[key]
            issue = self.create_issue_with_fields_iphone(key,desc)

            for i in range(0, len(sub_task_array)):
                sub_task_obj = sub_task_array[i]
                time = sub_task_obj['time']
                name = sub_task_obj['name']
                self.create_issue_with_fields_subtask_iphone(issue.key, name, name, time)




    def create_all(self):
        descriptions= [{'Seguimiento':'Lograr deteccion de Peajes, POIs, etc y generar una notificacion del sistema'},{'Notificaciones':'A partide de notificacion del sistema mostrar el detalle de notificacion'},{'Detalle sitio recomendado':'mostrar detalles de sitios recomendados y famosos'},{'Configuracion de ruta':'ventana de configuracion de ruta (Cilindraje, Vehiculo, combustible)'},{'Ruta famoso':'si se detecta condiciones se muestra la ventana de ruta de famoso'}, {'Seleccion tipo de ruta':'seleccionar el tipo de ruta: normal, famoso, gastronomica, etc'}, {'Formulario de ruta':'tener un formulario con parametros adicionales (checklist, costo)'}, {'Detalle de ruta':'ver el detalle de ruta con los cambios para fase 2'}, {'Edicion puntos intermedios':'tener la posibilidad de editar los puntos intermedios en una ventana flotante'}, {'Detalles de costos de ruta':'poder ver los detalles del costo de una ruta. (peajes, costo total, etc)'}, {'Guardar ruta':'poder guardar una ruta con formulario fase 2'},{'Menu de ruta':'tener una ventana para poder lanzas las distintas subsecciones de rutas'},{'Radar fase 2':'tener un radar con los items de fase 2 (famosos, peajes, barra ruta, botones)'}, {'Filtro famosos':'Tener un nuevo filtro q prenda y apague ruta personalizada'}, {'Subsecciones perfil':''}]

        todo_iphone= [{'Edicion puntos intermedios':[{'time':'8h','name':'migracion a ventana flotante'},{'time':'8h','name':'adecuacion punto A y B fase 1'}]},{'Detalles de costos de ruta':[{'time':'5h','name':'Discucion protocolos'},{'time':'10h','name':'implementacion ventana de detalle'}]},{'Guardar ruta':[{'time':'9h','name':'Adecuacion fase 1'}]},{'Menu de ruta':[{'time':'4h','name':'Montaje ventana'},{'time':'2h','name':'Conexion subsecciones'}]},{'Radar fase 2':[{'time':'10h','name':'Adicion item famosos'},{'time':'6h','name':'Implementacion burbuja peajes'},{'time':'19h','name':'Distencion item pequeno y mediano'},{'time':'6h','name':'Barra en modo ruta'},{'time':'10h','name':'Botones flotantes'}]},{'Filtro famosos':[{'time':'6h','name':'Validacion libreria adicion-eliminacion'},{'time':'16h','name':'Implementacion filtro'}]},{'Subsecciones perfil':[{'time':'8h','name':'Cambios menu lateral y conexiones'}]}]
        for j in range(0, len(todo_iphone)):
            desc_obj=descriptions[j+8];
            todo_obj=todo_iphone[j]
            key =todo_obj.keys()[0]
            sub_task_array=todo_obj[key]
            desc=desc_obj[key]
            issue = self.create_issue_with_fields_iphone(key,desc, asignee)

            for i in range(0, len(sub_task_array)):
                sub_task_obj = sub_task_array[i]
                time = sub_task_obj['time']
                name = sub_task_obj['name']
                self.create_issue_with_fields_subtask_iphone(issue.key, name, name, time,asignee)
    
    def createAllFromFile(self):

        fileReader= FileReader()
        superList = fileReader.load_content_to_objects()
        for i in range(0, len(superList.subtasks)):
            listItem = superList.subtasks[i]
            fileReader.print_item_content(listItem.parent)
            issue = self.create_issue_with_fields_iphone(listItem.parent.name,listItem.parent.description, listItem.parent.asignee)
            for item in listItem.subtasks:
                fileReader.print_item_content(item)
                self.create_issue_with_fields_subtask_iphone(issue.key, item.name, item.description, item.time,item.asignee)
 
    def update_issues_iphone(self, issue_key,times):
        #stories=self.authed_jira.search_issues('project=PIPHONE and created>="2014/07/14" and issuetype=Story')
        #for issue_story in stories:
        subtasks= authed_jira.search_issues('parent='+issue_key)


    
    def list_issues_and_stories(self, assignee):
        stories=self.authed_jira.search_issues('project=CT and assignee='+assignee+' and issuetype=Story and Sprint=539')
        for issue in stories:
            print 'STORY issue: ',issue.key, issue.fields.summary
            subtasks= self.authed_jira.search_issues('parent='+issue.key)
            for subtask in subtasks:
                print '     SUB-TASK issue ', subtask.key, subtask.fields.summary
        #for task in subtasks:
        #    fields_issue = {'timetracking':{'originalEstimate':time,'remainingEstimate':time}}
        #    issue = self.authed_jira.issue(task.key)
        #    issue.update(fields=fields_issue)

    def add_worklog_time(self, issue_id, time, comment):
        issue = self.authed_jira.issue(issue_id)
        rem_estimate = issue.fields.timetracking.remainingEstimate
        print 'issue:', issue.fields.summary,'remaining time', rem_estimate
        worklogs = self.authed_jira.worklogs(issue_id)
        print 'worklog status'
        for worklog in worklogs:
            print 'author', worklog.author.name,'timespent', worklog.timeSpent,'comment',(worklog.comment if hasattr(worklog, 'comment') else 'NA')
        worklog = self.authed_jira.add_worklog(issue_id, timeSpent=time,comment=comment)

    def create_issue_with_fields_subtask_android(self, subtask_id,summary, description, time):

        fields_issue = {'project': {'key': 'PAP'},
                'parent':{'key': subtask_id},
                'summary':summary,
                'description':description,
                'environment':'android',
                'assignee':{'name':'antonio.vanegas'},
                'issuetype':{'id':'7'},
                'customfield_10800':{'id':'10415'},
                'priority':{'name':'Major'},
                'timetracking':{'originalEstimate':time,'remainingEstimate':time}}
        issue=self.authed_jira.create_issue(fields=fields_issue)
        print 'issue.....', issue

    def create_issue_with_fields_android(self, summary, description):

        fields_issue = {'project': {'key': 'PAP'},
                'summary':summary,
                'description':description,
                'environment':'android',
                'assignee':{'name':'antonio.vanegas'},
                'issuetype':{'name':'Story'},
                'customfield_10800':{'id':'10415'},
                'priority':{'name':'Major'}}
        issue=self.authed_jira.create_issue(fields=fields_issue)
        print 'issue.....', issue
        return issue


    def create_issue_with_fields_subtask_iphone(self, subtask_id,summary, description, time, asignee):

        fields_issue = {'project': {'key': 'AN'},
                'parent':{'key': subtask_id},
                'summary':summary,
                'description':description,
                'environment':'iphone-ipad',
                'assignee':{'name':asignee},
                'issuetype':{'id':'7'},
                'components': [{'name':"iPhone"}],
                'customfield_10800':{'id':'11003'},
                'priority':{'name':'Major'},
                'timetracking':{'originalEstimate':time,'remainingEstimate':time}}
        issue=self.authed_jira.create_issue(fields=fields_issue)
        print 'issue.....', issue

    def create_issue_with_fields_iphone(self, summary, description, asignee):

        fields_issue = {'project': {'key': 'AN'},
                'summary':summary,
                'description':description,
                'environment':'ios-ipad',
                'assignee':{'name':asignee},
                'components': [{'name':"iPhone"}],
                'issuetype':{'name':'Story'},
                'customfield_10800':{'id':'11003'},
                'priority':{'name':'Major'}}
        issue=self.authed_jira.create_issue(fields=fields_issue)
        print 'issue.....', issue
        return issue





