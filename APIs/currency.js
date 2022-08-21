          var code_set;
          var currency_key;
          var code_name ;
          var name_set;
          var is_valid;
          var symbol;
       async function mycur() {
         document.getElementById("curr").innerHTML = "";
         document.getElementById("curr").className = "well"
         var country = document.querySelector('#ok').value;
         country = country.toLowerCase();
          const res01 = await fetch("https://api.myjson.com/bins/17q5jg");
            const data02 = await res01.json(); 
              let keys01 = Object.keys(data02);
              let vals01 =  Object.values(data02);
               for(var i = 0; i < vals01.length; i++){
                   if(country==keys01[i]){
                       country = vals01[i];
                    }
               }
         const res1 = await fetch("https://api.myjson.com/bins/17mzvs");
         const data2 = await res1.json(); 
         let keys = Object.keys(data2);
            let vals = Object.values(data2);
            is_valid = false;
            for(var i = 0; i < vals.length; i++){
              if (vals[i].toLowerCase() == country.toLowerCase()){
                code_name = keys[i];
                is_valid = true;
              }
            }
            if(is_valid == false){
              return;
            }
          const res2 = await fetch ("https://api.myjson.com/bins/ujgko");
          const data1 = await res2.json();
          let keys1 = Object.keys(data1);
            let vals1 = Object.values(data1);
            for(var i = 0; i < vals1.length; i++){
              if (keys1[i] == code_name){
                currency_key = vals1[i];
              }
            }
          const res3 = await fetch("https://api.myjson.com/bins/z8ed4");
          const data3 = await res3.json();
          let keys3 = Object.keys(data3);
          let vals3 = Object.values(data3);
          for(var i =0; i < vals3.length; i++){
            if(keys3[i] == currency_key){
              symbol = vals3[i].symbol;
            }
          }
          const api_url = "http://www.apilayer.net/api/live?access_key=00cf3976617c79146b38d2619eeeceb8&currencies="+currency_key+"&source=USD&format=1";
            const res = await fetch(api_url);
            const data = await res.json();
            let result = Object.values(data.quotes);
            let num =parseFloat(result[0])
            num =num.toFixed(2);
            document.getElementById("curr").innerHTML = "<h5>Currency based on US Dollar</h5><p>" + "$1 is " + symbol + " " + num+ "<p>";
            
        }
