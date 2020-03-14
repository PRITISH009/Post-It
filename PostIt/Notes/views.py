from django.shortcuts import render

context = {
    'title' : 'My Wall',
    'posts' : [
        {
            'task' : 'Task 1',
            'description' : 'Description of Task 1'
        },
        {
            'task' : 'Task 2',
            'description' : 'Description of Task 2'
        },
        {
            'task' : 'Task 3',
            'description' : 'Description of Task 3'
        },
        {
            'task' : 'Task 4',
            'description' : 'Description of Task 4'
        },
        {
            'task' : 'Task 5',
            'description' : 'Description of Task 5'
        },
        {
            'task' : 'Task 6',
            'description' : 'Description of Task 6' 
        }
    ]
}


# Create your views here.
def home(req):
    return render(req, 'Notes/wall.html', context)

def  about(req):
    return render(req, 'Notes/about.html', {'title' : 'About Page'})