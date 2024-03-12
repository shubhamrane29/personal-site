document.addEventListener("DOMContentLoaded", function() {
    const body = document.body;

    for (let i = 0; i < 500; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        setRandomPosition(star, body);
        body.appendChild(star);
    }
});

function setRandomPosition(element, container) {
    const containerRect = container.getBoundingClientRect();
    const randomTop = Math.random() * containerRect.height;
    const randomLeft = Math.random() * containerRect.width;

    element.style.top = randomTop + 'px';
    element.style.left = randomLeft + 'px';
}

// JavaScript for handling tabs
var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

function opentab(tabname, clickedEvent) {
    for (var i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active-link");
    }

    for (var i = 0; i < tabcontents.length; i++) {
        tabcontents[i].classList.remove("active-tab");
    }

    clickedEvent.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
}

// JavaScript for handling side menu
var sidemenu = document.getElementById("sidemenu");

function openmenu() {
    sidemenu.style.right = "0";
}

function closemenu() {
    sidemenu.style.right = "-250px";
}

// Form entry
$(document).ready(function(){
    $(".form").on('submit', function(e){
        e.preventDefault();
        var name = $(".name").val();
        var email = $(".email").val();
        $.post("https://script.google.com/macros/s/AKfycbx4F6WaEuAJQ2s_MUqGvXHbY7mM4hAiyHvjyZIDZXqG0aqzWLdNY6uK_69p05PVHDcB/exec", {Name: name, Email: email}, function(res) {
            if(res == 1) {
                alert("Done");
            } else {
                alert("Error");
            }
        });
    });
});

