import gradio as gr
import requests
import folium
from folium.plugins import MarkerCluster
import skops.io as sio

# ------------------------------
# Function: Predict Earthquake Magnitude
# ------------------------------
def predict_eq(lat, lon, depth):
    # Load model safely with trusted types
    untrusted_types = sio.get_untrusted_types(file="earthquake_model.skops")
    model = sio.load("earthquake_model.skops", trusted=untrusted_types)

    pred = model.predict([[lat, lon, depth]])[0]
    return f"🔮 Predicted Magnitude: {pred:.2f}"

# ------------------------------
# Function: Fetch & Show Live Earthquake Data
# ------------------------------
def live_earthquake_map():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response = requests.get(url).json()

    # Create a dark-themed world map
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")
    marker_cluster = MarkerCluster().add_to(m)

    for feature in response["features"]:
        coords = feature["geometry"]["coordinates"]
        lon, lat, depth = coords
        mag = feature["properties"]["mag"]
        place = feature["properties"]["place"]

        # Marker with color depending on magnitude
        folium.CircleMarker(
            location=[lat, lon],
            radius=max(2, (mag if mag else 1) * 1.5),
            color="red" if mag and mag >= 5 else "orange",
            fill=True,
            fill_opacity=0.7,
            popup=f"<b>Magnitude:</b> {mag}<br>"
                  f"<b>Depth:</b> {depth} km<br>"
                  f"<b>Location:</b> {place}"
        ).add_to(marker_cluster)

    return m._repr_html_()  # Return HTML for Gradio

# ------------------------------
# Gradio UI
# ------------------------------
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🌍 Earthquake Prediction & Live Global Data")

    with gr.Tabs():
        # Prediction Tab
        with gr.Tab("🔮 Predictor"):
            with gr.Row():
                lat = gr.Number(label="Latitude")
                lon = gr.Number(label="Longitude")
                depth = gr.Number(label="Depth (km)")
            btn = gr.Button("Predict")
            output = gr.Textbox(label="Result")
            btn.click(predict_eq, inputs=[lat, lon, depth], outputs=output)

        # Live Map Tab
        with gr.Tab("🌐 Live Earthquake Map"):
            gr.Markdown("### Real-time Earthquakes (Last 24 Hours)")
            map_output = gr.HTML()
            refresh_btn = gr.Button("🔄 Refresh Map")
            refresh_btn.click(live_earthquake_map, outputs=map_output)

# ------------------------------
# Launch the App
# ------------------------------
demo.launch()
