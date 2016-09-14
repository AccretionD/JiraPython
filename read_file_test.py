import csv,sys

class Issue:

    def __init__(self, asignee, name, description, time):
        self.name = name
        self.description = description
        self.time = time
        self.asignee=asignee

class SubTask:

    def __init__(self, issue_parent, issue):
        self.issue_parent = issue_parent
        self.issue = issue

class List:
    def __init__(self,parent):
	self.projectIdentifier = ""
	self.costCenter = ""
        self.parent = parent
        self.subtasks = []
class FileReader:

    def load_content_to_objects(self, fileName, projectIdentifier, costCenterId):
        cr = csv.reader(open(fileName,"rb"))
        superList = List("root")
	superList.projectIdentifier = projectIdentifier
	superList.costCenter = costCenterId
        issueList = List("a")
        for row in cr:
            print row
            assignee = row[0].strip()
            name = row[1].strip()
            description = row[2].strip()
            estimate = row[3].strip()

            if assignee == "" :
                superList.subtasks.append(issueList)
                issueList = List("a")
            else :
                issue = Issue(assignee, name, description, estimate)
              
                if issueList.parent == "a":
                    print "should be changed to issue object"
                    issueList.parent = issue;
                else :
                    issueList.subtasks.append(issue)

            
           # if row[0] == "":
           #     superList.subtasks.append(listIssues)
           # else :
           #     issue = Issue(row[0], row[1], row[2], "")
           #      if row[3] is not "":
           #          issue.time = row[3]
	   # 	    list_exists = False;
	   # 	    try:
	   # 		listIssues
	   # 	    except NameError:
   	   # 		list_exists = False
	   # 	    else:
  	   # 		list_exists = True
	   # 	    if list_exists is False:
	   # 	        listIssues = List(issue)
           # 
	   # 	    else :
	   # 	        listIssues.subtasks.append(issue)
           #      else :
           #          listIssues = List(issue)

        print "how many subtasks are?: "+ str(len(superList.subtasks))
        
        for i in range(0, len(superList.subtasks)):
            listItem = superList.subtasks[i]
            print len(listItem.subtasks)
            self.print_item_content(listItem.parent)
            for item in listItem.subtasks:
                self.print_item_content(item)
        return superList

    def print_item_content(self,item):
        print str(item.name) + " " + str(item.description) + " " + str(item.time) + " " + str(item.asignee)

    def print_file_content(self):
        cr = csv.reader(open("myfile.csv","rb"))
        for row in cr:
            if row[2] is "":
                string = self.print_list_content(row)
            else :
                string = "  "+self.print_list_content(row)
            if row[0] is not "":
                print string

    def print_list_content(self,list):
        string = ""
        for i in list:
            string = string + " " + i
        return string
