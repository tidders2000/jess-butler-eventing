 function initMap() {
            var map = new google.maps.Map(document.getElementById("map"), {
                zoom: 10,
                center: {
                    lat: 53.070251,
                    lng: -0.809587
                }
            });
            var labels = "Jess Butler Eventing";
            var locations = [{
                
                lat:  53.106958,
                lng: -0.728639
            }];
            var markers = locations.map(function(location, i) {
                return new google.maps.Marker({
                    position: location,
                    label: labels
                });
            });
            var markerCluster = new MarkerClusterer(map, markers, {
                imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
            });
        }