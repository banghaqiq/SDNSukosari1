var ctx = document.getElementById("static");
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["2018", "2019", "2020", "2021", "2022", "2023"],
        datasets: [{
            label: 'laki laki',
            data: [8, 12, 1, 9, 8, 0],
            backgroundColor: [
                'rgba(54, 162, 235, 1.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        },{
            label: 'perempuan',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 1.2)',
            ],
            borderColor: [
                'rgba(255,99,132,1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
    });