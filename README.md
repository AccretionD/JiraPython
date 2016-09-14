Jira Python 
There are many commands for upload tickets to jira.
It use a lot of them to create tickets, create stories and its tickets.

You can create a csv to upload the tickets.
The sytaxis of the file is:

``` text
jira.user, Ticket title, description of ticket, time
,,,

```
- jira.user = The workmate who will be assigned to do the task

If you want create a story and its tickets, the syntax of the file should be:

``` text
jira.user, story title, description of story,
jira.user, Ticket title, description of ticket, time
,,,

```
Every time that you create a ticket or an story, and the ticket isn't related to a story, or you finish to list the tickets of one story, you should use ',,,' in a new line to create a new task or a new story.


