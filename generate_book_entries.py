#this array creates the various html files and overwrites the previous versions with new headers
#this structure is repeated in the "End" section to append the footer and end of html to all the files
shelf_array_count = 0  #counter counts up through array positions
shelf_array = ["Fiction", "Non-Fiction", "Art-Design", "Art-Film", "Art-Instruction", "Mythology", "Poetry-Plays-Essays", "Comics-Manga-Visual"]
while shelf_array_count < 8:
  shelf_file = ((shelf_array[shelf_array_count])+".html")

  
  #write the start of the html
  #to open/create a new html file in the write mode 
  # w overwrites file, a adds to existing contents
  f = open((shelf_file), 'w') 
  
  # the html code which will go in the file
  html_template = """
    <!DOCTYPE html>
    <head>
    <meta charset="UTF-8"> 
    
    <Title>Books | """+(shelf_array[shelf_array_count])+"""</Title>

        <!--Bootstrap Links-->
            <!-- Latest compiled and minified CSS -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
            <!-- Optional theme -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
            <!-- Latest compiled and minified JavaScript -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

            
          <!--I THINK these are for the drop-down buttons-->
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.min.js" integrity="sha384-VQqxDN0EQCkWoxt/0vsQvZswzTHUVOImccYmSyhJTp7kGtPed0Qcx8rK9h9YEgx+" crossorigin="anonymous"></script>

            <!-- jQuery (required for Bootstrap's JavaScript plugins) -->
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

            <!-- Popper.js (required for Bootstrap dropdowns) -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.6/umd/popper.min.js"></script>
            
            
  <style>
  body {
    background-color: rgb(226, 209, 185);
  }

  button {
    background-color: gray;
    color: white;
    width: 100%;
  }
  </style>
        
    </head>

    <body>
  <h1><b>Library Catalog | Fiction</b></h1>
  <h3><a href="Fiction.html">Fiction</a> | <a href="Non-Fiction.html">Non-Fiction</a> | <a href="Art-Design.html">Art-Design</a> | <a href="Art-Film.html">Art-Film</a> | <a href="Art-Instruction.html">Art-Instruction</a> | <a href="Mythology.html">Mythology</a> | <a href="Poetry-Plays-Essays.html">Poetry-Plays-Essays</a> | <a href="Comics-Manga-Visual.html">Comics-Manga-Visual</a></h3>
  <br>
            


  """
  
  # writing the code into the file 
  f.write(html_template) 
  
  # close the file 
  f.close()

  #end top loop createing files and headers
  shelf_array_count +=1


#read spreadsheet
  #pip install xlrd
  #pip install pandas
  #pip install openpyxl
  #https://pythonbasics.org/read-excel/
import pandas as pd

#load spreadsheet into a data frame
df = pd.read_excel('book_library.xlsx')

#current row
current_row = 0
book_select = df.loc[(current_row)]

#loop starts
while (book_select)[0] != "end":
  print(current_row)


  #book (row) selection
  book_select = df.loc[(current_row)]
  print(book_select)

  #establish loop

  # Set variables
  book_shelf = (book_select)[0] 
  book_id = (book_select)[1]
  book_author = (book_select)[2]
  shelf_file = ((book_shelf)+".html")
#book
  if book_author == "book":
    book_series = (book_select)[3]
    book_entry = str((book_select)[4])
    book_title = (book_select)[5]
    book_subtitle = ((book_select)[6])
    book_year = str((book_select)[7])
    book_isbn = str((book_select)[8])
    book_pages = str((book_select)[9])
    book_cover = (book_select)[10]
    book_wiki = (book_select)[11]
    book_goodreads = (book_select)[12]
    book_description = (book_select)[13]
    #write the end of the html
    # to open/create a new html file in the write mode 
    # w overwrites file, a adds to existing contents
    f = open((shelf_file), 'a') 
  
    # the html code which will go in the file GFG.html 
    html_template = """
    <div class="col-xs-12 col-sm-12 col-md-4 col-lg-3">  <!--book Entry-->
      <br>
    <div class="row"> <!--Top Section-->
    <!--"""+(book_title)+"""-->
    <div class="col-xs-4 col-sm-4 col-md-6 col-lg-6"> <!--cover-->
        <img src="""+(book_cover)+""" width="100%">
    </div>  <!-- end of cover-->

          <div class="col-xs-8 col-sm-8 col-md-6 col-lg-6"> <!--info-->
              <b>"""+(book_series)+"""  """+(book_entry)+"""</b>  <!--series and entry number-->
              <h2>"""+(book_title)+"""</h2> <!--book Title-->
              <p><i>"""+(book_subtitle)+"""</i></p> <!--subtitle-->
              <h4>"""+(book_year)+""" | """+(book_pages)+"""pg</h4> <!--year and page count-->
              <h5>ISBN: """+(book_isbn)+"""</h5> <!--isbn number-->
              <b><a href="""+(book_wiki)+""">Wikipedia</a> | <a href="""+(book_goodreads)+""">Goodreads</a></b><!--wikipedia and goodreads--> 
          </div>  <!-- end of right text side--> 
    </div>
    <!-- Button -->
    <p class="d-inline-flex gap-1">
      <button class="btn" type="button" data-bs-toggle="collapse" data-bs-target=#"""+(book_id)+""" aria-expanded="false" aria-controls="""+(book_id)+""">
          Description &#9660
      </button>
    </p>
    <div class="collapse" id="""+(book_id)+""">
      <div class="card card-body">
      <p>"""+(book_description)+"""</p> <!--book Description-->  
      </div>
    </div> 
    </div> <!--end of book entry-->     

    """
    # writing the code into the file 
    f.write(html_template) 
  
    # close the file 
    f.close()
#end
  elif book_author == "end":
    end_shelf_count = 0
    while end_shelf_count < 8:
      shelf_file = ((shelf_array[end_shelf_count])+".html")
      # to open/create a new html file in the write mode 
      # w overwrites file, a adds to existing contents
      f = open((shelf_file), 'a') 
  
      # the html code which will go in the file GFG.html 
      html_template = """
    
      <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <hr>
        <h3><a href="Fiction.html">Fiction</a> | <a href="Non-Fiction.html">Non-Fiction</a> | <a href="Art-Design.html">Art-Design</a> | <a href="Art-Film.html">Art-Film</a> | <a href="Art-Instruction.html">Art-Instruction</a> | <a href="Mythology.html">Mythology</a> | <a href="Poetry-Plays-Essays.html">Poetry-Plays-Essays</a> | <a href="Comics-Manga-Visual.html">Comics-Manga-Visual</a></h3>
      </div>
      </body>
      </html>    

      """
      # writing the code into the file 
      f.write(html_template) 
  
      # close the file 
      f.close()

      end_shelf_count += 1
#author    
  else:
    # to open/create a new html file in the write mode 
    # w overwrites file, a adds to existing contents
    f = open((shelf_file), 'a') 
  
    # the html code which will go in the file GFG.html 
    html_template = """

    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
    <!--author  """+(book_author)+"""-->
    <hr>
    <h2>"""+(book_author)+"""</h2>
    </div>     

    """
    # writing the code into the file 
    f.write(html_template) 
  
    # close the file 
    f.close()


  #loop ends
  #increase row count
  current_row += 1

