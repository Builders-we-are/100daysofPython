import 'cesium/Build/Cesium/Widgets/widgets.css';
import Cesium from 'cesium/Build/Cesium/Cesium';

const viewer = new Cesium.Viewer('cesiumContainer', {
    animation: false,
    baseLayerPicker: false,
    fullscreenButton: false,
    vrButton: false,
    geocoder: false,
    homeButton: false,
    infoBox: false,
    sceneModePicker: false,
    selectionIndicator: false,
    timeline: false,
    navigationHelpButton: false
});

// Load and display your CZML file
const czmlPath = 'czml/your.czml';
Cesium.CzmlDataSource.load(czmlPath).then(dataSource => {
    viewer.dataSources.add(dataSource);
    viewer.zoomTo(dataSource);
});
