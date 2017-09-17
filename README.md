# linode user enumeration

## how does this work?
`python3 main.py <valid username> <invalid username> <usernames to check>`

this is just PoC, adopt to fit real situation

## why does this work?
i think linode sends the password reset email during your script execution, severely delaying the return of the generated page

interesting idea regardless, considering that linode takes the precaution of ambiguous error messages

`— Instructions for completing the password reset *may* have been emailed to you. —`

when whether or not it was mailed is pretty obvious
