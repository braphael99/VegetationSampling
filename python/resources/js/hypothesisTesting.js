const form = document.getElementById("hypothTestForm");
const testingResults = document.getElementById("tests");

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const testMean = document.getElementById("hypoMean").value;

    fetch('/hypTest/new', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },

        body: JSON.stringify({ testMean }),

    })
        .then(response => response.json())
        .then(data => {
            testingResults.innerHTML = `
            <div id = "twoTail>
                <div id = "twoTailP">The p-value of our two-tail hypothesis test is ${data.twoTailP}.</div>
                <div id = "twoTail90"> At alpha of 0.1: ${data.twoTailP >= 0.1 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
                <div id = "twoTail95"> At alpha of 0.05: ${data.twoTailP >= 0.05 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
                <div id = "twoTail99"> At alpha of 0.01: ${data.twoTailP >= 0.01 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
            </div>
            <div id = "rightTail">
                <p>The p-value of our right-tail hypothesis test is ${data.rightTailP}.</p>
                <div id = "rtTail90"> At alpha of 0.1: ${data.rightTailP >= 0.1 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
                <div id = "rtTail95"> At alpha of 0.05: ${data.rightTailP >= 0.05 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
                <div id = "rtTail99"> At alpha of 0.01: ${data.rightTailP >= 0.01 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
            </div>
            <div id = "leftTail">
                <p>The p-value of our left-tail hypothesis test is ${data.leftTailP}.</p>
                <div id = "ltTail90"> At alpha of 0.1: ${data.leftTailP >= 0.1 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
                <div id = "ltTail95"> At alpha of 0.05: ${data.leftTailP >= 0.05 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
                <div id = "ltTail99"> At alpha of 0.01: ${data.leftTailP >= 0.01 ? "Fail to reject the null hypothesis." : "Reject the null hypothesis."}</div>
            </div>
            <div id = "90CI">
                <p>Our 90% confidence interval: ${data.ninetyCI}.</p>
            </div>
            <div id = "95CI">
                <p>Our 95% confidence interval: ${data.ninetyFiveCI}.</p>
            <div>
            <div id = "99CI">
                <p>Our 99% confidence interval: ${data.ninetyNineCI}.</p>
            </div>`
        })
        .catch(error => {
            console.error('Error', error);
        });
});