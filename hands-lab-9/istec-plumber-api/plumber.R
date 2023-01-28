#* @apiTitle ISTEC - Software Engineering API
#* @apiDescription API to demonstrate the use of a REST API to ISTEC - Software Engineering Class
#* @apiTOS  https://www.linkedin.com/in/joao-carlos-caldeira/
#* @apiContact list(name = "API Support", url = " https://www.linkedin.com/in/joao-carlos-caldeira/", email = "joaocarlos.caldeira@my.istec.pt")
#* @apiLicense list(name = "Apache 2.0", url = "https://www.apache.org/licenses/LICENSE-2.0.html")
#* @apiVersion 1.0.0
#* @apiTag security Security Operations
#* @apiTag management Management operations
#* @apiTag execution Executing operations


#* Echo back success to access the API 
#* @get /
function() {
  return("SUCCESS: You are accessing the ISTEC - Software Engineering API v1.0 (Using R)")
}

#* Echo back the API version
#* @tag management
# @param msg The message to echo
#* @get /version
function() {
  return("API Version 1.0.0")
}

#* Authenticates the client
#* @tag security
# @param username The Username 
# @param password The Password 
#* @post /login
function( req ) {
 library(jsonlite) 
 library(openssl)

 body <- as.data.frame(lapply(fromJSON(req$postBody), unlist))

 token <- paste0(sha256(paste0(body$username,body$password)))
  
 response <- list( status = "SUCCESS", code = "200", body = data.frame("token"= token )  )
  
 return ( response )
  
}

#* Return a normal distribution of size "n"
#* @tag execution
#* @get /normal/<n>
function( n = 1 ) {
  rand <- rnorm( n )
}

#* Return a normal distribution of size "n"
#* @tag execution
#* @serializer pdf
#* @get /plot/normal/<n>
function( n = 1 ) {
  rand <- rnorm( n )
  hist (rand)
}

#* Return a normal distribution of size "n"
#* @tag execution
#* @get /crypto/<token>/<n>
function( token, n = 1 ) {
  
  if (token == "BTC") { values <- rnorm(n, mean=17400, sd=200) }
  if (token == "ETH")  { values <- rnorm(n, mean=1320, sd=50) }
  if (token != "BTC" && token != "ETH")  { values <- rnorm(n, mean=0.33, sd=0.03); token <- "XRP"; }

  days <- as.Date(rev(seq(Sys.Date()-1, Sys.Date() - as.difftime(n, unit="days"), by = "-1 day" )))

  response <- list( status = "SUCCESS", code = "200", token = list( ticker = token,  date = days, values = values ) ) 
  
  return ( response )
}


#* Return a normal distribution of size "n"
#* @tag execution
#* @serializer pdf
#* @get /plot/crypto/<token>/<n>
function( token, n = 1 ) {

if (token == "BTC") { values <- rnorm(n, mean=17400, sd=200) }
if (token == "ETH")  { values <- rnorm(n, mean=1320, sd=50) }
if (token != "BTC" && token != "ETH")  { values <- rnorm(n, mean=0.33, sd=0.03); token <- "XRP"; }

days <- as.Date(rev(seq(Sys.Date()-1, Sys.Date() - as.difftime(n, unit="days"), by = "-1 day" )))
df <- data.frame(day=days, value=values)

plot(values ~ day, df, xaxt = "n", type = "l", xlab="Days", ylab="Values", main = paste0(token, " Evolution per day") )
axis(1, df$day, format(df$day, "%Y %b %d"), cex.axis = .7)

}



#* Return an exponential distribution of size "n"
#* @tag execution
#* @get /exponential/<n>
function( n = 1 ) {
  rand <- rexp( n )
}

#* Return an exponential distribution of size "n"
#* @tag execution
#* @serializer pdf
#* @get /plot/exponential/<n>
function( n = 1 ) {
  rand <- rexp( n )
  hist (rand)
}

#* Print Query String parameters
#* @tag execution
#* @get /test_query_string
function (req, param1 = "", param2 = "") {
  msgParam1 = paste0("The value of param1 is: '", param1, "'")
  msgParam2 = paste0("The value of param2 is: '", param2, "'")

  return (list(msgParam1, msgParam2))
}

#* Print URL Path
#* @tag execution
#* @get /test_url_path/<param>
function (req, param = "") {
  msgParam = paste0("The value of param is: '", param, "'")

  return (list(msgParam))
}

#* Print Image PNG Serialization
#* @tag execution
#* @serializer png
#* @get /image_png_serialization/<n>
function (req, n = 1) {
  rand <- rexp( n )
  hist (rand)
}