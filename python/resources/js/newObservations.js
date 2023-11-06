document.getElementById("newObservation").addEventListener("click", () => {
    const CBH = document.getElementById("CBH").value;
    const height = document.getElementById("height").value;
    const DBH = document.getElementById("DBH").value;
    const BA = document.getElementById("BA").value;
    const dead = document.getElementById("dead").value;

    const newObservation = {
        CBH: CBH,
        height: height,
        DBH: DBH,
        BA: BA,
        dead: dead
    };

    const response = fetch("/newObservations/new", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(newObservation) 
    });
    confirm("Observation Posted!")
});

