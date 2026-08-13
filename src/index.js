export class ChatRoom {
  constructor(state, env) {
    this.state = state;
    this.env = env;
  }

  async fetch(request) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type"
        }
      });
    }

    if (request.method === "GET") {
      const messages = (await this.state.storage.get("messages")) || [];

      return new Response(JSON.stringify(messages), {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }

    if (request.method === "POST") {
      try {
        const body = await request.json();
        const message = String(body.message || "").trim();

        if (!message) {
          return new Response(
            JSON.stringify({ error: "Brak wiadomości" }),
            {
              status: 400,
              headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
              }
            }
          );
        }

        const messages = (await this.state.storage.get("messages")) || [];

        messages.push({
          role: "user",
          content: message,
          time: new Date().toISOString()
        });

        let answer = "Nie udało się uzyskać odpowiedzi AI.";

        if (this.env.AI) {
          const result = await this.env.AI.run(
            "@cf/meta/llama-3.1-8b-instruct",
            {
              messages: [
                {
                  role: "system",
                  content:
                    "Jesteś pomocnym asystentem serwisu Naprawa Komputerów i Laptopów. Pomagasz klientom w sprawach dotyczących komputerów, laptopów, Windows, sprzętu, diagnostyki i napraw. Odpowiadaj po polsku, konkretnie i zrozumiale."
                },
                ...messages.slice(-10).map((m) => ({
                  role: m.role,
                  content: m.content
                }))
              ]
            }
          );

          answer =
            result?.response ||
            result?.result ||
            "Nie otrzymałem odpowiedzi od modelu AI.";
        }

        messages.push({
          role: "assistant",
          content: answer,
          time: new Date().toISOString()
        });

        await this.state.storage.put("messages", messages.slice(-50));

        return new Response(
          JSON.stringify({
            answer,
            messages: messages.slice(-50)
          }),
          {
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*"
            }
          }
        );
      } catch (error) {
        return new Response(
          JSON.stringify({
            error: "Błąd serwera",
            details: error?.message || String(error)
          }),
          {
            status: 500,
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*"
            }
          }
        );
      }
    }

    return new Response("Not found", { status: 404 });
  }
}


export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/") {
      return new Response(`<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
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
  padding: 20px;
  min-height: 450px;
  border-radius: 0 0 16px 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,.08);
}

.messages {
  height: 350px;
  overflow-y: auto;
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 15px;
  background: #fafafa;
}

.message {
  padding: 12px;
  margin-bottom: 10px;
  border-radius: 10px;
  white-space: pre-wrap;
}

.user {
  background: #e0ecff;
  text-align: right;
}

.assistant {
  background: #eeeeee;
}

.form {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

input {
  flex: 1;
  padding: 14px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 16px;
}

button {
  padding: 14px 22px;
  border: 0;
  border-radius: 10px;
  background: #2563eb;
  color: white;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background: #1d4ed8;
}

.info {
  text-align: center;
  margin-top: 15px;
  font-size: 14px;
  color: #666;
}

@media(max-width:600px) {
  .container {
    margin: 10px auto;
    padding: 10px;
  }

  .form {
    flex-direction: column;
  }

  button {
    width: 100%;
  }
}
</style>
</head>

<body>

<div class="container">

  <div class="header">
    <h1>Serwis AI</h1>
    <p>Naprawa komputerów i laptopów</p>
  </div>

  <div class="chat">

    <div id="messages" class="messages">
      <div class="message assistant">
        Witam! Jestem asystentem serwisu komputerowego.
        W czym mogę pomóc?
      </div>
    </div>

    <div class="form">
      <input
        id="input"
        type="text"
        placeholder="Napisz, co dzieje się z komputerem lub laptopem..."
        autocomplete="off"
      >

      <button id="send">Wyślij</button>
    </div>

    <div class="info">
      Naprawa komputerów i laptopów • Warszawa
    </div>

  </div>
</div>

<script>
const input = document.getElementById("input");
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
  const text = input.value.trim();

  if (!text) return;

  addMessage(text, "user");
  input.value = "";
  send.disabled = true;
  send.textContent = "Piszę...";

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
      addMessage(data.answer, "assistant");
    } else {
      addMessage(
        "Wystąpił błąd: " + (data.error || "brak odpowiedzi"),
        "assistant"
      );
    }

  } catch (error) {
    addMessage(
      "Nie udało się połączyć z serwerem.",
      "assistant"
    );
  }

  send.disabled = false;
  send.textContent = "Wyślij";
  input.focus();
}

send.addEventListener("click", sendMessage);

input.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});
</script>

</body>
</html>`);
    }

    if (url.pathname === "/api/chat" && request.method === "POST") {
      const id = env.CHATROOM.idFromName("glowny-chat");
      const room = env.CHATROOM.get(id);

      return room.fetch(request);
    }

    return new Response("Nie znaleziono strony", {
      status: 404
    });
  }
};
