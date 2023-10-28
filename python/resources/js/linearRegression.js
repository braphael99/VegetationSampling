fetch('/linearRegress')
.then(response => response.json())
.then(data => {
    const correlation = data.correlation;
// Manipulate the HTML to display the JSON data
    document.getElementById('diamHolder').innerText = `The Correlation Coefficient is: ${correlation}`

})
.catch(error => {
    console.error('Error fetching data:', error);
});