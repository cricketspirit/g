g="{"
m="}"
for i in range(10):
    a=f"""            
            var countDownDate{i} = new Date("April 6, 2022 19:30:00").getTime();
            

            var x{i} = setInterval(function() {g}
            

              var now{i} = new Date().getTime();
            
              // Find the distance between now and the count down date
              var distance{i} = countDownDate{i} - now{i};
            
              // Time calculations for days, hours, minutes and seconds
              var days{i} = Math.floor(distance{i} / (1000 * 60 * 60 * 24));
              var hours{i} = Math.floor((distance{i} % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
              var minutes{i} = Math.floor((distance{i} % (1000 * 60 * 60)) / (1000 * 60));
              var seconds{i} = Math.floor((distance{i} % (1000 * 60)) / 1000);
            
              // Display the result in the element with id="demo"
              document.getElementById("MK").innerHTML = days{i} + "d " + hours{i} + "h "
              + minutes{i} + "m " + seconds{i} + "s ";
            
              // If the count down is finished, write some text
              if (distance{i} < 0) {g}
                clearInterval(x);
                document.getElementById("MK").innerHTML = "STARTED";
                document.getElementById("link_MK").remove()

              {m}
            {m}, 1000);"""
    print(a)
