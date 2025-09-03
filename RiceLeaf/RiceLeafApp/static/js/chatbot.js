let inputRequest = $('#chat_input');
let submitButton = $('#send_button');
let voice_input = $('#voice_input');
let fileInput = $('#fileInput');
let counseling = $('#counseling');
let requestCount = 0;
let is_upgraded = false;
let imageUrl = null;

$(document).ready(function () {
    imageUrl = $('#profile').val();
    if (inputRequest.val().length == 0) {
        submitButton.prop("disabled", true);
    }

    inputRequest.on("input", function () {
        $.trim($(this).val()) != "" ? submitButton.prop("disabled", false) : submitButton.prop("disabled", true);
    });

    $('#chatForm').submit(function (event) {
        event.preventDefault();
        var chatData = new FormData(this);
        chatbot(chatData, requestCount);
        requestCount++;
    });

    inputRequest.on("keypress", function (event) {
        // Check if the pressed key is Enter (key code 13)
        if (event.which === 13) {
            if (inputRequest.val().length > 0) {
                $("#chatForm").submit();
                event.preventDefault();
            }
        }
    });

    // $("#voice_input").on("click", function () {
    //     inputRequest.val(null);
    //     submitButton.prop("disabled", true)
    //     navigator.mediaDevices.getUserMedia({ audio: true })
    //         .then(function (stream) {
    //             const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    //             recognition.lang = 'en-US';
    //             recognition.start();
    //             inputRequest.attr('placeholder', 'Recognizing ...');

    //             recognition.onresult = function (event) {
    //                 inputRequest.attr('placeholder', 'Message ...');
    //                 const transcript = event.results[0][0].transcript;
    //                 inputRequest.val(transcript);
    //                 $.trim(transcript) != "" ? submitButton.prop("disabled", false) : submitButton.prop("disabled", true);

    //             };

    //             recognition.onend = function () {
    //                 inputRequest.attr('placeholder', 'Message ...');
    //                 stream.getTracks().forEach(track => track.stop()); // Stop the microphone stream
    //             };
    //         })
    //         .catch(function (error) {
    //             console.error('Error accessing microphone:', error);
    //             alert('Please grant microphone permissions to use this feature.');
    //         });
    // });

    $('#new_chat').click(() => window.location.reload());

    $("#file_button").click(function () {
        $("#fileInput").click();
    });

    $("#fileInput").change(function (event) {
        $("#chatForm").submit();
        event.preventDefault();
    });
});


const chatbot = (chatData, index) => {
    let chat = Object.fromEntries(chatData);
    var request = requestDiv(chat);
    var response = responseDiv(index);
    var inputValue = $.trim(chat.chat_input);

    if (inputValue != "") {
        delete chat.fileInput;
    }
    if (inputValue != "" || chat.fileInput.size > 0) {
        $('.chat-block').append(request);
        $('#chat_input').val("");
        $('#send_button').prop("disabled", true);
        $('.chat-block').append(response);
        sendRequest(chat, index, false);
        scrollToBottom();
    }


}


const sendRequest = (formData, index) => {
    PostRequest("/chatbot/", formData,
        (response) => {
            console.log(response);

            const texts = response.map(item => item.text);
            const combinedText = texts.join('\n');
            typeText(".response .response-text-" + index + "", combinedText, 0, 20);
            $(`.response-text-${index} .spinner-grow`).remove();
        }
    );
}
const requestDiv = (chatData, view_chat = false) => {

    var content; // Variable to store the content (image or text)
    if (view_chat) {
        content = chatData;
    } else {
        content = chatData.chat_input;
    }

    // Create the request HTML
    var request = `
    <div class="d-flex justify-content-end mb-3">
        <div class="bg-primary-subtle p-3 rounded-3 border shadow-sm w-75 max-width-80">
            <span class="fw-bold text-primary">User :</span><br/>
            <span>${content}</span>
        </div>
    </div>
`;
    return request;

}


const responseDiv = (index) => {
    var response = `
    <div class="d-flex justify-content-start mb-3 response">
        <div class="bg-body-tertiary p-3 rounded-3 border shadow-sm w-75 max-width-80">
            <span class="fw-bold text-dark">Bot :</span>
            <div class="response-text-${index} w-100 text-wrap" style="word-wrap: break-word;"> 
                <span class="spinner-grow spinner-grow-sm text-dark" role="status">
                    <span class="visually-hidden">Loading...</span>
                </span> 
            </div>
        </div>
    </div>
    `;
    return response;
}


// Function to simulate typing effect
const typeText = (element, text, index = 0, speed = 50) => {
    const lines = text.split("\n");
    let currentLineIndex = 0;
    let currentCharIndex = index;
    const typeNextChar = () => {
        const currentLine = lines[currentLineIndex];
        if (currentLine) {
            const char = currentLine[currentCharIndex] === " " ? " " : currentLine[currentCharIndex];
            $(element).append(char);
            currentCharIndex++;
            if (currentCharIndex === currentLine.length) {
                if (lines[currentLineIndex + 1] && (lines[currentLineIndex + 1].startsWith("-") || lines[currentLineIndex + 1] === "")) {
                    $(element).append("<br>"); // Add a break after the current line
                }
                currentLineIndex++;
                currentCharIndex = 0;
            }
            setTimeout(typeNextChar, speed);
        }
        scrollToBottom();
    };

    // Start the typing process
    typeNextChar();
};



const scrollToBottom = () => {
    var container = $(".scroll");
    container.scrollTop(container.prop("scrollHeight"));
}


function openFileInput() {
    document.getElementById('fileInput').click();
}

function handleFileSelect(input) {
    // Handle the selected file here
    // You can access the selected file using input.files[0]
    console.log("Selected file:", input.files[0].name);
}

