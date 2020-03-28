window.addEventListener('load', async () => {
    await main()
})

const main = async () => {
    // put all stuff here

    const el = document.getElementById("el")

    const res = await fetch("http://localhost:3000/api/timetable")
    const data = await res.json()
    console.dir(data)

    el.innerHTML = data.map(d => `<li>${d.courseName}</li>`).join(",<br>")
}


const slots = [
    { name: "slot1", startTime: "", endTime: "" },
    { name: "slot2", startTime: "", endTime: "" },
    { name: "slot3", startTime: "", endTime: "" },
    { name: "slot4", startTime: "", endTime: "" },
    { name: "slot5", startTime: "", endTime: "" },
]

const days = ["monday", "tuesday", "wednesday"]

const timetable = {
    "monday": {
        "slot1": { courseName: "math" },
        "slot3": { courseName: "science" }
    },


    "tuesday": {
        "slot2": { courseName: "math" },
        "slot5": { courseName: "science" }
    },
}

const renderTimeTable = (timetable, days, slots) => {

    days.forEach(day => {

    });
}
