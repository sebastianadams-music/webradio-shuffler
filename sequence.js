randomStation()
loopRandomStation()  


function loopRandomStation() {
    var min = 0,
      max = 7;
    var rand = Math.floor(Math.random() * (max - min + 1) + min); //Generate Random number between 5 - 10
    console.log("rand", rand)
    randomStation()
    setTimeout(loopRandomStation, rand * 1000);
  }
  

