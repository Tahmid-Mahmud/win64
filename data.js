// document.body.onloadedmetadata = function() {
//     window.scrollTo({ top: 0, behavior: 'smooth' });
//   };

academics = [[11, 7, 9], [0, 7, 9], [11, 8, 8], [6, 7, 7], [0, 0, 8], [5, 7, 3]]


aca = document.getElementsByClassName('aca');


function view() {
    year = document.getElementById('year').value;
    document.getElementsByClassName('template')[0].style.display='block';
    index = parseInt(year) - 2020
    i = 0;
    academics[index].forEach(pos => {
        aca[i].innerHTML = pos;
        i++;
    });
}