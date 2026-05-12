const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

exports.handler = async (event) => {
  // Responde ao preflight CORS
  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 204, headers: CORS_HEADERS, body: "" };
  }

  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      headers: CORS_HEADERS,
      body: JSON.stringify({ error: "Method Not Allowed" }),
    };
  }

  const apiKey = process.env.BLACKCAT_API_KEY;
  if (!apiKey) {
    return {
      statusCode: 500,
      headers: CORS_HEADERS,
      body: JSON.stringify({ error: "BLACKCAT_API_KEY não configurada no Netlify" }),
    };
  }

  let body;
  try {
    body = JSON.parse(event.body);
  } catch {
    return {
      statusCode: 400,
      headers: CORS_HEADERS,
      body: JSON.stringify({ error: "Body inválido" }),
    };
  }

  const { amount, customerName, customerEmail, customerCpf, customerPhone } = body;

  if (!amount || amount < 100) {
    return {
      statusCode: 400,
      headers: CORS_HEADERS,
      body: JSON.stringify({ error: "Valor mínimo é R$ 1,00 (100 centavos)" }),
    };
  }
  if (!customerName || !customerEmail || !customerCpf) {
    return {
      statusCode: 400,
      headers: CORS_HEADERS,
      body: JSON.stringify({ error: "Dados do cliente incompletos" }),
    };
  }

  const siteUrl = process.env.URL || process.env.DEPLOY_URL || "";

  const payload = {
    amount,
    paymentMethod: "PIX",
    items: [
      {
        title: "Produto",
        quantity: 1,
        unitPrice: amount,
      },
    ],
    customer: {
      name: customerName,
      email: customerEmail,
      document: {
        type: "cpf",
        number: customerCpf,
      },
      ...(customerPhone && { phone: customerPhone }),
    },
    ...(siteUrl && { postbackUrl: `${siteUrl}/.netlify/functions/webhook` }),
  };

  try {
    const response = await fetch("https://api.blackcatpay.com.br/api/sales/create-sale", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": apiKey,
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
      return {
        statusCode: response.status,
        headers: { "Content-Type": "application/json", ...CORS_HEADERS },
        body: JSON.stringify({ error: data.message || "Erro na Black Cat API", detail: data }),
      };
    }

    return {
      statusCode: 200,
      headers: { "Content-Type": "application/json", ...CORS_HEADERS },
      body: JSON.stringify(data),
    };
  } catch (err) {
    return {
      statusCode: 500,
      headers: CORS_HEADERS,
      body: JSON.stringify({ error: "Erro interno: " + err.message }),
    };
  }
};
