document.getElementById('close-btn').addEventListener('click', () => {
    document.querySelector('.chat-container').style.display = 'none';
});

function addQuestion() {
    let question = document.getElementById("message-input").value;
    
    let chatBoxEl=document.getElementById("chat-add");
    
    let msgEl=document.createElement("p");
    msgEl.innerText = question;
    chatBoxEl.appendChild(msgEl);
    msgEl.classList.add("chat-msg");
    msgEl.classList.add("chat-msg-quest");
    
    fetch('http://localhost:8000/'+question, {method: 'POST'})
    .then(response => {
        return response.json();
    })
    .then(data => {
        answerEl.innerText = data;
    });

    let answerEl=document.createElement("p");
    answerEl.innerText = "...";
    chatBoxEl.appendChild(answerEl);
    answerEl.classList.add("chat-msg");
    answerEl.classList.add("chat-msg-answer");
    // Clear the input box after processing the question
    document.getElementById("message-input").value = '';
    }

    document.addEventListener("DOMContentLoaded", function() {
  var chatContainer = document.querySelector('.chat-container');
  var closeBtn = document.getElementById('close-btn');
  var messageInput = document.getElementById('message-input');
  var scrollTimeout;

  window.addEventListener('scroll', function() {
    clearTimeout(scrollTimeout); // Clear previous timeout if exists
    scrollTimeout = setTimeout(function() {
        if (window.scrollY > 50) { // Adjust this value as needed
            chatContainer.style.display = 'block';
        } else {
            chatContainer.style.display = 'none';
        }
    }, 1000); // Adjust the delay (in milliseconds) as needed
});

  closeBtn.addEventListener('click', function() {
    chatContainer.style.display = 'none';
  });

  // // Function to handle asking a question
  // function addQuestion() {
  //   var message = messageInput.value;
  //   if (message.trim() !== '') {
  //     var chatMessages = document.getElementById('chat-messages');
  //     var messageElement = document.createElement('div');
  //     messageElement.classList.add('message');
  //     messageElement.textContent = message;
  //     chatMessages.appendChild(messageElement);
  //     messageInput.value = '';
  //   }
  // }
});
