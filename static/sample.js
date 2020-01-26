let options = {
    type: "radar",
    data: {
        labels: ["嬉しい", "悲しい", "嫌悪", "怒り", "怖い", "驚き"],
        datasets: [{
            label: "感情",
            data: [2.0, 3.9, 7.9, 4.2, 5.5, 2.4],
            pointHitRadius: 25,
            backgroundColor: "rgba(255, 255, 0, 0.8)"
        }]
    },
    options: {
        dragData: true,
        dragDataStart: (e) => {
            console.log(e);
        },
        onDrag: (e, datasetIndex, index, value) => {},
        onDragEnd: (e, datasetIndex, index, value) => {
            console.log(datasetIndex, index, value);
        },
        scale: {
            ticks: {
                max: 10,
                min: 0,
                stepSize: 1,
                backdropColor: "rgba(255, 255, 255, 0.25)"
            },
            gridLines: {
                color: "rgba(0, 0, 0, 0.4)",
                lineWidth: 1.5
            },
            pointLabels: {
                fontColor: ["green", "blue", "black", "red", "white", "orange"],
                fontSize: 15
            }
        }
    }
};
let context = document.getElementById("chart").getContext("2d");
let chart = null;
window.onload = () => {
    if (!chart) {
        chart = new Chart(context, options);
    } else {
        // alert("chart is already created");
    }
}

function beforeSubmit() {
    document.form.happy.value = options.data.datasets[0].data[0];
    document.form.sad.value = options.data.datasets[0].data[1];
    document.form.disgust.value = options.data.datasets[0].data[2];
    document.form.anger.value = options.data.datasets[0].data[3];
    document.form.fear.value = options.data.datasets[0].data[4];
    document.form.surprise.value = options.data.datasets[0].data[5];
}
