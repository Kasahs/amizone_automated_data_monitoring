window.addEventListener("load", async () => {
  await main()
})

const main = async () => {
  // put all stuff here

  //   const res = await fetch("http://localhost:3000/api/timetable")
  //   const data = await res.json()
  //   console.dir(data)

  //   el.innerHTML = data.map(d => `<li>${d.courseName}</li>`).join(",<br>")
  const timeTable = {
    monday: {
      slot1: { courseName: "math" },
      slot3: { courseName: "science" }
    },

    tuesday: {
      slot2: { courseName: "math" },
      slot5: { courseName: "science" }
    }
  }

  const slots = [
    { name: "slot1", startTime: "", endTime: "" },
    { name: "slot2", startTime: "", endTime: "" },
    { name: "slot3", startTime: "", endTime: "" },
    { name: "slot4", startTime: "", endTime: "" },
    { name: "slot5", startTime: "", endTime: "" }
  ]

  const days = ["monday", "tuesday", "wednesday"]
  const el = document.getElementById("el")
  renderTimeTable(el, timeTable, days, slots)
}

const arrayToRowItems = items => {
  return `${items.map(item => `<td>${item}</td>`).join("\n")}`
}

const arrayToTableRow = items => {
  return `<tr>${arrayToRowItems(items)}</tr>`
}
const arrayToTableHead = items => {
  return `<thead>${arrayToRowItems(items)}</thead>`
}

const timetableRows = (timetable, days, slots) => {
  const rows = []
  days.forEach(day => {
    const row = [day]
    slots.forEach(slot => {
      row.push(timetable[day][slot] || "")
    })
    rows.push(row)
  })
  return rows
}

const timeTableToHtml = (timetable, days, slots) => {
  const dataInRows = timetableRows(timetable, days, slots)
  const tableContentHtml = ""
  tableContentHtml += arrayToTableHead(["day/time", ...slots])

  const rowsHtml = dataInRows.map(row => arrayToTableRow).join("\n")
  tableContentHtml += rowsHtml
  return `<table>${tableContentHtml}</table>`
}

const renderHtml = (el, html) => {
  el.innerHTML = html
  return el
}

const renderTimeTable = (el, timetable, days, slots) => {
  return renderHtml(el, timeTableToHtml(timetable, days, slots))
}
