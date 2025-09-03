$(document).ready(function () {

    $('#detectDiseaseForm').submit(function (event) {
        event.preventDefault();
        var formData = new FormData(this);
        showConfirmation("Are you sure you want to detect the disease?",
            () => {
                DetectDisease(formData);
            });
    });

    $('#image').change(function () {
        $('#disease_name').text('');
        $('#details-block').empty();
        $('.info-block').hide()
        displayImage(this);
    });


});


const displayImage = (input) => {
    var previewImage = $('#previewImage')[0];

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            previewImage.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
    }
}


const DetectDisease = (formData) => {
    showProcessingAlert("Please wait....", false);
    PostRequest(detectDiseaseApiUrl, formData,
        (response) => {
            closeProcessingAlert();
            if (response.status) {
                console.log(response.data);
                const data = response.data;

                $('#disease_name').text(data.name);

                // Building precautions list
                let precautionsList = "";
                if (data.precautions) {
                    data.precautions.forEach(element => {
                        precautionsList += `<li>${element}</li>`;
                    });
                }

                // Building remedies list
                let remediesList = "";
                if (data.remedies) {
                    data.remedies.forEach(element => {
                        remediesList += `<li>${element}</li>`;
                    });
                }

                // Constructing the details block
                let details = `
                <h3>Precautions:</h3>
                <ul>
                    ${precautionsList}
                </ul>
                <h3 class="pt-3">Remedies:</h3>
                <ul>
                    ${remediesList}
                </ul>`;

                // Updating the HTML content
                $('#details-block').html(details);
            } else {
                showError(response.message);
            }
        }, true
    );
}
