import io.gatling.core.scenario.Simulation
import io.gatling.core.Predef._
import io.gatling.http.Predef._
class Demo  extends Simulation {
  val httpConf = http.baseUrl("http://localhost:8888/work")
//  object Home{
//    val findALL = exec(http("findALL")    //设置请求名称，可随意定义
//      .get("/user/findAll")                 //前端请求地址
//      .check(status.is(200))
//      .check( bodyString.saveAs( "RESPONSE_DATA" ) ))
//      .exec( session => {
//      println("Some Restful Service Response Body:")
//      println(session("RESPONSE_DATA").as[String])
//      session
//    }//判断http status
//    )

//    val findByNameAndTel = exec(http("test_json")   //http 请求name
//      .post("/user/findByNameAndTel")     //post url
//      .headers(Home.headers_json)  //设置body数据格式
//      //将json参数用StringBody包起,并作为参数传递给function body()
//      .body(StringBody("{\"userName\":\"たろう\"},\"userTel\":\"11111111111\"}"))
//      .check( bodyString.saveAs( "RESPONSE_DATA" ) ))

    val headers_json = Map("Content-Type" -> "application/json")
  //}
  val findByNameAndTel = exec(http("findByNameAndTel")   //http 请求name
        .post("/user/findByNameAndTel")     //post url
        .headers(headers_json)  //设置body数据格式
        //将json参数用StringBody包起,并作为参数传递给function body()
        .body(StringBody("{\"userName\":\"たろう\",\"userTel\":\"11111111111\"}"))
        .check( bodyString.saveAs( "RESPONSE_DATA" ) ))
        .exec(session => {
                      println("Some Restful Service Response Body:")
                     println(session("RESPONSE_DATA").as[String])
                      session}
        )

  var userId=1
  var findByID=exec(http("findById")    //设置请求名称，可随意定义
    .get(s"/user/findById?userId=${userId}")                 //前端请求地址
    .check(status.is(200))
    .check( bodyString.saveAs( "RESPONSE_DATA" ) ))
    .exec( session => {
      println("Some Restful Service Response Body:")
      println(session("RESPONSE_DATA").as[String])
      session
    }//判断http status
    )

  val createTelNote = exec(http("createTelNote")   //http 请求name
    .post("/tel/create")     //post url
    .headers(headers_json)  //设置body数据格式
    //将json参数用StringBody包起,并作为参数传递给function body()
    .body(StringBody("{\"sendName\":\"admin\",\"sendTel\":\"12312341234\",\"requestName\":\"たろう\",\"requestTel\":\"111-1111-1111\"}"))
    .check( bodyString.saveAs( "RESPONSE_DATA" ) ))
    .exec(session => {
      println("Some Restful Service Response Body:")
      println(session("RESPONSE_DATA").as[String])
      session}
    )


  val findALLTelNote = exec(http("findALLTelNote")    //设置请求名称，可随意定义
    .get("/tel/findAll")                 //前端请求地址
    .check(status.is(200))
    .check( bodyString.saveAs( "RESPONSE_DATA" ) ))
    .exec( session => {
      println("Some Restful Service Response Body:")
      println(session("RESPONSE_DATA").as[String])
      session }
    )//判断http status


  val scn1 = scenario("test").exec(findByNameAndTel).exec(findByID).exec(createTelNote).exec(findALLTelNote)
  val scn2 = scenario("createTelNote").exec(findALLTelNote)
//        .exec(http("test_json")   //http 请求name
//        .post("/user/findByNameAndTel")     //post url
//        .headers(Home.headers_json)  //设置body数据格式
//        //将json参数用StringBody包起,并作为参数传递给function body()
//        .body(StringBody("{\"userName\":\"たろう\"},\"userTel\":\"11111111111\"}"))
//        .check( bodyString.saveAs( "RESPONSE_DATA" ) ))
//      .exec(session => {
//                println("Some Restful Service Response Body:")
//               println(session("RESPONSE_DATA").as[String])
//                session}
//      )
  setUp(
    scn1.inject(constantUsersPerSec(20) during(10)).protocols(httpConf)
    //scn2.inject(constantUsersPerSec(20) during(10)).protocols(httpConf)
  )
}
