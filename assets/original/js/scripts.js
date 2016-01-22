$(document).ready(function(){
    var map,
        location_circles;
    var init = function() {
        map = L.map('map-canvas').setView([21.1610714, 79.0024694], 5);

        L.tileLayer('https://api.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.emerald',
            accessToken: 'pk.eyJ1IjoiYmliaGFzZG4iLCJhIjoiY2lqbmMyaWd2MDAzeHYxbHh6cGFtOHVhNCJ9.CVZicsB8IMNsLE5AtiRgeQ'
        }).addTo(map);

        location_circles = [];
    };

    var circle_color = function(aqi) {
        if (aqi >= 0 && aqi <= 50) {
            return '#096';
        } else if (aqi >= 51 && aqi <= 100) {
            return '#ffde33';
        } else if (aqi >= 101 && aqi <= 150) {
            return '#f93';
        } else if (aqi >= 151 && aqi <= 200) {
            return '#c03';
        } else if (aqi >= 201 && aqi <= 300) {
            return '#609';
        } else if (aqi >= 301) {
            return '#7e0023';
        }
    }

    var circle_radius = function(zoom) {
        return Math.abs(zoom-20);
    }

    var fetch_location_list = function() {
        $.getJSON('/api/locations/', function(data) {
            $.each(data, function(idx, val) {
                var row = '<tr><td>';
                row += '<a href="/location/' + val.id + '">' + val.name + '</a>';
                row += '</td><td>'
                row += val.current_condition.aqi;
                row += '</td><td>'
                row += val.current_condition.pm25;
                row += '</td><td>'
                row += val.current_condition.pm10;
                row += '</td><td>'
                row += moment(val.current_condition.created_at).fromNow();
                row += '</td></tr>'
                $(row).appendTo('#table_locations');

                var circ = L.circleMarker([val.latitude, val.longitude], {
                    color: circle_color(val.current_condition.aqi),
                    fillColor: circle_color(val.current_condition.aqi),
                    fillOpacity: 0.2
                }).setRadius(
                    circle_radius(map.getZoom())
                ).bindPopup(vsprintf(
                    "<h4>%s</h4><br />" +
                    "<span>AQI: %s</span>",
                    [val.name, val.current_condition.aqi]
                )).addTo(map);
                location_circles.push(circ)
            });
        })
    }

    init();
    fetch_location_list();

    // map events
    map.on('zoomend', function(e) {
        // resize circles
        for (var i = location_circles.length - 1; i >= 0; i--) {
            var circ = location_circles[i];
            circ.setRadius(circle_radius(map.getZoom()));
        };
    })
});
