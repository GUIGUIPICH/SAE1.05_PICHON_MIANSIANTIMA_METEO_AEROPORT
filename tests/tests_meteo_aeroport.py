def genere_page_web(nom_fichier, titre_page, corps):
    f = open(nom_fichier,'w',encoding='utf-8')
    HTML_INDEX = """ <!DOCTYPE html>
    <html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"fr\" lang=\"fr\" dir=\"ltr\">
    <style>
        table, th, td {
        border:1px solid black;
        }
    </style>
    <head>
    <title> Mon titre </title>
    <p> Partie du test SAE traitement dfe donée </p>
    <table>
       <tr>
         <td>Mois</td>
         <td>Age</td>
    <tr>
    <tr>
         <td>Mars</td>
         <td>18</td>
    <tr>
     </table>
    
         
       
    </head>
    <body>
    Bonjour HTML
    </body>
    </html>
    """
    f.write(HTML_INDEX)
    f.close()

def main():
    corps = """ <h1> Titre </h1>
            """
    genere_page_web("../html/index.html", "mon titre", corps)

if __name__ == "__main__":
    main()




