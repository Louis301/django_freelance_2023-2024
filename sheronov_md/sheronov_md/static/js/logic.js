let canvas = document.getElementById("canvas");
const w = canvas.width;
const h = canvas.height;
const mouse = { x : 0, y : 0 };

let context = canvas.getContext("2d");
// let pen_color = "black"
// let pen_width = 1
let draw = false;


function setDefaultPen(color, width) {
    pen_color = color
    pen_width = width
}

function setPenColor(element) { 
    pen_color = element.id
}

function setPenWidth(element) { 
    pen_width = element.id 
}


canvas.addEventListener("mousedown", function(e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop; 
    draw = true;
    context.beginPath();
    context.moveTo(mouse.x, mouse.y);
});


canvas.addEventListener("mousemove", function(e) {   
    if(draw) {
        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
        context.lineTo(mouse.x, mouse.y);
        context.strokeStyle = pen_color;
        context.lineWidth = pen_width;
        context.stroke();
    }
});


canvas.addEventListener("mouseup", function(e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
    context.lineTo(mouse.x, mouse.y);
    context.stroke();
    context.closePath();
    draw = false;
});





// let canvas = document.getElementById('canvas');
// let context = canvas.getContext('2d');

// canvas.width = w;
// canvas.height = h;

// const wrapText = function(context, text, x, y, maxWidth, lineHeight) {
//     var words = text.split(' ');
//     var line = '';
//     let testLine = '';
//     let wordArray = [];
//     let totalLineHeight = 0;
//     for(var n = 0; n < words.length; n++) {
//         testLine += `${words[n]} `;
//         var metrics = context.measureText(testLine);
//         var testWidth = metrics.width;
//         if (testWidth > maxWidth && n > 0) {
//             wordArray.push([line, x, y]);
//             y += lineHeight;
//             totalLineHeight += lineHeight;
//             line = `${words[n]} `;
//             testLine = `${words[n]} `;
//         }
//         else {
//             line += `${words[n]} `;
//         }
//         if(n === words.length - 1) {
//             wordArray.push([line, x, y]);
//         }
//     }
//     return [ wordArray, totalLineHeight ];
// }

// // Add gradient
// let grd = context.createLinearGradient(0, 853, 1352, 0);
// grd.addColorStop(0, '#00a0ff');
// grd.addColorStop(1, '#12cba6');
// context.fillStyle = grd;
// context.fillRect(0, 0, 1342, 853);

// // Write text
// context.fillStyle = 'white';
// context.font = '95px Inter';
// context.fillText('👍', 85, 700);

// // More text
// context.font = '700 95px Inter';
// context.fillStyle = 'white';
// let wrappedText = wrapText(context, "Download this Canvas", 85, 753, 1200, 100);
// wrappedText[0].forEach(function(item) {
//     context.fillText(item[0], item[1], item[2] - wrappedText[1] - (200)); // 200 is height of emoji
// })

// // And more
// context.font = '200 50px Inter';
// context.fillStyle = 'rgba(255,255,255,0.8)';
// context.fillText("HTML", 85, 553 - wrappedText[1] - 100); // 853 - 200 for emoji, -100 for line height of 1