let map;

function drawMapWithMarker(pos, icao) {

  if (map == null) {
    map = L.map('map')
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);
  }
  map.setView(pos, 13);

  // then the marker
  L.marker(pos).addTo(map).bindPopup(icao).openPopup();
}

/* draw the map with two positions and a line between them */
function drawMapWithLine(start_pos, end_pos) {
  // draw the line, http://leafletjs.com/reference.html#polyline
  let latlngs = Array()
  latlngs.push(start_pos); latlngs.push(end_pos);
  const polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);

  // then scale the map to fit the line
  map.fitBounds(polyline.getBounds());
}



