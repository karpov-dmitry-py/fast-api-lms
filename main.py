from fastapi import FastAPI

from api import users, courses, sections

app = FastAPI(
    title='fast api lms',
    description='fast api lms app',
    version='0.1',
    contact={
        'name': 'Karpov Dmitry',
        'email': 'dkarpov@company.com',
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
