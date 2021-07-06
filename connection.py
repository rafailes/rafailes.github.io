import cgi
import cgitb


html = """
<!DOCTYPE html>
<head>
    <p>voici la chat room</p>
</head>
<body>
    
    
    <form method="post" action =envoie.py>
        <p><input type="text" name="message">
        <input type="submit" value="envoyer"></p>
    </form>
        
        <p>
</body>



"""
print(html)

