const API_URL = "https://canteen-chapter-chosen.ngrok-free.dev";

const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const result = document.getElementById("result");
const predictBtn = document.getElementById("predictBtn");

imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];

    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";
    result.innerHTML = "";
});

predictBtn.addEventListener("click", async () => {
    const file = imageInput.files[0];

    if (!file) {
        alert("Please upload an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    result.innerHTML = `<p>🔄 Analyzing Banana...</p>`;

    const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    result.innerHTML = `
        <div class="result-card">

            <h2>🍌 Prediction Result</h2>

            <p><strong>Prediction:</strong> ${data.prediction}</p>

            <p><strong>Confidence:</strong> ${data.confidence}%</p>

            <div class="progress">
                <div
                    class="progress-bar"
                    style="width:${data.confidence}%">
                </div>
            </div>

            <br>

            <p><strong>Shelf Life:</strong> ${data.shelf_life}</p>

            <p><strong>Recommendation:</strong> ${data.recommendation}</p>

        </div>
    `;
});