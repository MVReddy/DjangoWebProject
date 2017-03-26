<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Account Details</title>
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'content/accounts.css' %}">

</head>
<body>

<h2> Account Details</h2> <br/>
<h2> New Tag</h2>

Account Number: {{account.account_number}} <br/>
Account Name: {{account.account_name}} <br/>
Account Balance: {{account.balance}} <br/>


</body>
</html>
