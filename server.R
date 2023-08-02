server <- function(){
  while(TRUE){
    writeLines("Listening...")
    con <- socketConnection(host="localhost", port = 6011, blocking=TRUE, server=TRUE, open="r+", timeout=2678400)
    data = try(readLines(con, 1))

    if(nchar(data) > 0) {
      print(data)
      response <- toupper(data) 
      writeLines(response, con) 
    }

    close(con)
  }
}

server()
