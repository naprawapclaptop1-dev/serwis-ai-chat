src/index.js
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Strona główna
    if (request.method === "GET" && url.pathname === "/") {
      return new Response(`<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Serwis AI - Naprawa komputerów i laptopów</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #f4f6f8;
      color: #222;
    }

    .container {
      max-width: 900px;
      margin: 40px auto;
      padding: 20px;
    }

    .header {
      background: #111827;
      color: white;
      padding: 25px;
      border-radius: 16px 16px 0 0;
      text-align: center;
    }

    .header h1 {
      margin: 0 0 10px;
      font-size: 28px;
    }

    .header p {
      margin: 0;
      color: #d1d5db;
    }

    .chat {
      background: white;
      border-radius: 0 0 16px 16px;
      padding: 20px;
      box-shadow: 0 8px 30px rgba(0,0,0,.08);
    }

    #messages {
      min-height: 400px;
      max-height: 550px;
      overflow-y: auto;
      padding: 10px;
    }

    .message {
      padding: 12px 16px;
      margin: 10px 0;
      border-radius: 12px;
      line-height: 1.5;
      white-space: pre-wrap;
    }

    .user {
      background: #e0f2fe;
      margin-left: 15%;
    }

    .ai {
      background: #f3f4f6;
      margin-right: 15%;
    }

    .input-area {
      display: flex;
      gap: 10px;
      margin-top: 15px;
    }

    #question {
      flex: 1;
      padding: 15px;
      border: 1px solid #d1d5db;
      border-radius: 10px;
      font-size: 16px;
    }

    button {
      border: 0;
      border-radius: 10px;
      padding: 0 22px;
      background: #2563eb;
      color: white;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      background: #1d4ed8;
    }

    button:disabled {
      background: #9ca3af;
      cursor: not-allowed;
    }

    .info {
      margin-top: 20px;
      text-align: center;
      font-size: 14px;
      color: #666;
    }

    @media (max-width: 600px) {
      .container {
        margin: 0;
        padding: 0;
      }

      .input-area {
        flex-direction: column;
      }

      button {
        height: 50px;
      }

      .user,
      .ai {
        margin-left: 0;
        margin-right: 0;
      }
    }
  </style>
</head>

<body>

<div class="container">

  <div class="header">
    <h1>🤖 Serwis AI</h1>
    <p>Pomoc w naprawie komputerów i laptopów</p>
  </div>

  <div class="chat">

    <div id="messages">
      <div class="message ai">
        Witam! Jestem asystentem serwisu komputerowego. 
        Opisz problem z komputerem lub laptopem, a postaram się pomóc.
      </div>
    </div>

    <div class="input-area">
      <input
        id="question"
        type="text"
        placeholder="Np. komputer nie uruchamia się..."
        autocomplete="off"
      >

      <button id="send">Wyślij</button>
    </div>

    <div class="info">
      Naprawa komputerów i laptopów • Serwis • Pogotowie
    </div>

  </div>
</div>

<script>
const question = document.getElementById("question");
const send = document.getElementById("send");
const messages = document.getElementById("messages");

function addMessage(text, type) {
  const div = document.createElement("div");
  div.className = "message " + type;
  div.textContent = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage() {
  const text = question.value.trim();

  if (!text) return;

  addMessage(text, "user");

  question.value = "";
  send.disabled = true;
  send.textContent = "Czekaj...";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: text
      })
    });

    const data = await response.json();

    if (data.answer) {
      addMessage(data.answer, "ai");
    } else {
      addMessage("Nie udało się uzyskać odpowiedzi.", "ai");
    }

  } catch (error) {
    addMessage(
      "Wystąpił błąd połączenia z asystentem.",
      "ai"
    );
  }

  send.disabled = false;
  send.textContent = "Wyślij";
  question.focus();
}

send.addEventListener("click", sendMessage);

question.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});
</script>

</body>
</html>`, {
        headers: {
          "content-type": "text/html; charset=UTF-8"
        }
      });
    }

    // API czatu
    if (
      request.method === "POST" &&
      url.pathname === "/api/chat"
    ) {
      try {
        const body = await request.json();
        const message = body.message;

        if (!message) {
          return Response.json({
            answer: "Napisz proszę, jaki masz problem z komputerem lub laptopem."
          });
        }

        if (!env.AI) {
          return Response.json({
            answer:
              "Asystent AI nie jest jeszcze podłączony do Cloudflare Workers AI. Trzeba dodać binding AI w konfiguracji Workera."
          });
        }

        const result = await env.AI.run(
          "@cf/meta/llama-3.1-8b-instruct",
          {
            messages: [
              {
                role: "system",
                content:
                  "Jesteś pomocnym asystentem polskiego serwisu komputerowego. Pomagasz diagnozować problemy z komputerami stacjonarnymi i laptopami. Odpowiadasz po polsku, jasno i konkretnie. Nie udawaj, że fizycznie naprawiłeś urządzenie. Jeżeli problem wymaga rozebrania komputera, pomiarów lub specjalistycznej naprawy, poinformuj użytkownika, że powinien skontaktować się z serwisem."
              },
              {
                role: "user",
                content: message
              }
            ]
          }
        );

        return Response.json({
          answer:
            result.response ||
            "Nie udało mi się przygotować odpowiedzi."
        });

      } catch (error) {
        return Response.json({
          answer:
            "Wystąpił błąd asystenta AI. Spróbuj ponownie za chwilę."
        });
      }
    }

    return new Response("Nie znaleziono strony.", {
      status: 404
    });
  }
};
