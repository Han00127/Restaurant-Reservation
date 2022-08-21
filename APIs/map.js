      //code inspired from The Coding Train youtube channel
      const mymap = L.map('issMap').setView([0, 0], 1);
      const attribution =
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
      const tileUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
      const tiles = L.tileLayer(tileUrl, { attribution });
      tiles.addTo(mymap);
      const issIcon = L.icon({
        iconUrl: 'arrow.png',
        iconSize: [50, 32],
        iconAnchor: [25, 16]
      });
      const marker = L.marker([0, 0], { icon: issIcon }).addTo(mymap);
      var code_name;
      var lat;
      var log;
      var latitude;
      var longitude;
      var is_valid;
      async function logi(){
          var country = document.getElementById("ok").value;
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
      const resp1 = await fetch("https://api.myjson.com/bins/gcbc8");
      const data = await resp1.json();
      for(var i =0; i< data.length; i++){
          if(data[i].country_code == code_name){
              lat = data[i].latlng[0];
              log = data[i].latlng[1];
          }
      }
      update_location();
    }
      let firstTime = true;
      async function update_location() {
     
         const latitude = lat;
         const longitude = log;
         var newLatLng = new L.LatLng(latitude, longitude);

        mymap.setView([lat, log], 4);
        marker.setLatLng(newLatLng); 
        firstTime = false;
  
      }
