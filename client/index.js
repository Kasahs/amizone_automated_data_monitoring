window.addEventListener("load", async () => {
  await main()
})

const main = async () => {
  // put all stuff here

  //   const res = await fetch("http://localhost:3000/api/timetable")
  //   const data = await res.json()
  //   console.dir(data)

  //   el.innerHTML = data.map(d => `<li>${d.courseName}</li>`).join(",<br>")

  const data = {
    monday: {
      "1": "math",
      "3": "science"
    },

    tuesday: {
      "2": "english",
      "5": "history"
    }
  }

  const slots = ["1", "2", "3", "4", "5"]

  const days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
  ]
  const el = document.getElementById("el")
  const renderTable = Table(days, slots, "day/slot")
  renderTable(el, data)
}

const Table = (vLabels, hLabels, pivot) => {
  const _arrayToRowItems = items => {
    const html = `${items.map(item => `<td>${item}</td>`).join("\n")}`
    return html
  }

  const _arrayToTableRow = items => {
    return `<tr>${_arrayToRowItems(items)}</tr>`
  }

  const _arrayToTableHead = items => {
    return `<thead>${_arrayToRowItems(items)}</thead>`
  }

  const _dataAsRows = (data, vLabels, hLabels) => {
    const rows = []
    vLabels.forEach(vLabel => {
      const row = [vLabel]
      hLabels.forEach(hLabel => {
        row.push(
          data[vLabel] ? (data[vLabel][hLabel] ? data[vLabel][hLabel] : "") : ""
        )
      })
      rows.push(row)
    })
    return rows
  }

  const _dataToHtmlTable = (data, vLabels, hLabels, pivot) => {
    const dataInRows = _dataAsRows(data, vLabels, hLabels)
    let tableContentHtml = ""
    tableContentHtml += _arrayToTableHead([pivot, ...hLabels])

    const rowsHtml = dataInRows.map(row => _arrayToTableRow(row)).join("\n")
    tableContentHtml += rowsHtml
    return `<table>${tableContentHtml}</table>`
  }

  const _renderHtml = (el, html) => {
    el.innerHTML = html
    return el
  }

  const renderTable = (el, data) => {
    return _renderHtml(el, _dataToHtmlTable(data, vLabels, hLabels, pivot))
  }

  return renderTable
}
