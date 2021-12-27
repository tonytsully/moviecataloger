From the Readme doc:

Movie Cataloger
This project allows users to catalog DVD, Blu-Ray and 4k UHD titles in a readable web UI db configuration.
*(UI not implemented at this time)
API Reference Table
Movies endpoints:
Del:Delete method
{{ _.base_url }}/moives/23
23 denotes the movie ID

Show: Get method
{{ _.base_url }}/movies/19
19 denotes the movie ID

Index:Get method
{{ _.base_url }}/movies

User Account endpoints:
Index:Get method
{{ _.base_url }}/user_account

Update: Put/Patch method
{{ _.base_url }}/user_account/491
491 denotes user_account ID
Header Info
Content-Type: application/json
JSON object example
{
    "username": "example_name",
    "password": "example_pw"
}

Show: Get method
{{ _.base_url }}/user_account/501
501 denotes user_account ID

Create: Post method
{{ _.base_url }}/user_account
eader Info
Content-Type: application/json
JSON object example
{
    "username": "example_name",
    "password": "example_pw"
}

Del: Delete method
{{ _.base_url }}/users_account/452
452 denotes the user_account ID

Retrospective answering of the following questions:
How did the project's design evolve over time?
This was a very challenging project with a lot of unknowns.
I had to continue to change what I thougt I knew to what actually worked
and made sense to use for the project.
From what I originally designed to what I implemented changed as I
understood more of the flask app and SQL implementation.
I will continue to use this project and a model and build onto it
as I learn more about flask, backend and SQL design and development.

Did you choose to use an ORM or raw SQL? Why?
Yes I choose to use an ORM because my research has shown that a large majority
of team utilize ORM's in their projects. This makes this skill a high in demand
skill set to have. I also will continue to learn implementing raw SQL in my projects as
well.

What future improvements are in store, if any?
I will continue to work on this project implementing the Genre workflow and possibly
implementing other cataloging categories for this project. I can see implementing the
ability to catalog household items as well. An example would to to catalog appliances,
or furniture so that the user can use this info for shopping and or insurance information
if needed. There are tons of things user can catalog and exploring those options will
make this a long expanded learning opportunity.