// Initialize and add the map
let map;

const compas_map_marker = document.createElement('img');
compas_map_marker.src = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';

async function initMap() {
  // The location
  const position = { lat: latitude, lng: longitude }; // 36.766467, 34.534685
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered
  map = new Map(document.getElementById("map"), {
    zoom: 11,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    content: compas_map_marker,
    title: "Локация",
  });
}

initMap();