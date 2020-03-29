const express = require("express");
const app = express();
const mysql = require("mysql");
const cors = require("cors")

// TODO: make proper useful select queries
// TODO: tt should show free slots 
// TODO: tt text should not wrap
// TODO: full tt from mon-sun should be shown
// TODO: notification of next class should be given
// TODO: notification of attendace marked should be given
// TODO: status of atttendance should be shown

let time_slot_dict =
{
  nine_to_ten: '09:15 - 10:10',
  ten_to_eleven: '10:15 - 11:10',
  eleven_to_twelve: '11:15 - 12:10',
  twelve_to_thirteen: '12:15 - 13:10',
  thiteen_to_fourteen: '13:15 - 14:10',
  fourteen_to_fifteen: '14:15 - 15:10',
  fifteen_to_sixteen: '15:15 - 16:10',
  sixteen_to_seventeen: '16:15 - 17:10',
  seventeen_to_eighteen: '17:10 - 18:10'
}


const createConnection = () => {
  var connection = mysql.createConnection({
    host: 'localhost',
    user: 'manik',
    password: 'sweetbread',
    database: 'amizone'
  });

  return connection

}


const fetchTimeTable = (connection) => {

  const promise = new Promise((resolve, reject) => {
    connection.connect();
    query = 'SELECT class_time, course_name, class_loc, `date` FROM homepage_tt '
    connection.query(query, function (error, results, fields) {
      if (error) { return reject(err) }
      // for(const result of results){
      //   console.log(result.course_name)
      // }
      const refinedResults = results.map((result) => {
        return {
          courseName: result.course_name,
          courseTime: result.class_time,
          classLoc: result.class_loc,
          classDate: result.date
        }
      });
      refinedResults.forEach(element => {
        if (element.class_time == time_slot_dict.nine_to_ten) {
          period = element.class_name;
        }
      });
      connection.end();
      return resolve(refinedResults)
    })

  })
  return promise

}

app.use(cors())

app.get('/', (req, res) => {
  res.send(("<h1>hello world</h1>"));
});

app.get('/api/timetable', async (req, res) => {
  // TODO: fetch timetable from db
  // TODO: compose into proper response JSON object
  // TODO: respond with json object
  const connection = createConnection()
  const results = await fetchTimeTable(connection)
  res.json(results)

});

const port = process.env.PORT || 3000
app.listen(port, () => console.log(`listening on port ${port}`))