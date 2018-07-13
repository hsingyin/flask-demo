// var navli = document.getElementById('navbar').getElementsByTagName('li');
var navli = document.getElementsByTagName('li');
var i,j;

var length = navli.length;

for (let i = 0; i < length; i++) {
    navli[i].onclick = function(){
        for(let j = 0;j<length;j++){
            navli[j].className="";
        }
        this.className+="active";
    }
    
}