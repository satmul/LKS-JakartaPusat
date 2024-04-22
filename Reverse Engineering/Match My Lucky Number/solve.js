

Java.perform(function() {
    var it = setInterval(function(){
      try{
        let MainActivity = Java.use("id.blackbear.lksctf.MainActivity");
        MainActivity["generateNumber"].implementation = function () {
            console.log('generateNumber is called');
            let ret = this.generateNumber();
            console.log('generateNumber ret value is ' + ret);
            return 1;
        };
      } catch(e) {
        console.log("failed!");
      }
    },200); // runs every 200milisecods
  });