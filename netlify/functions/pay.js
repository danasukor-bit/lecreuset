const BC_KEY = process.env.BC_KEY;
const BC_URL = 'https://api.blackcatpay.com.br/api/sales/create-sale';

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Content-Type': 'application/json',
};

exports.handler = async function(event) {
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers: CORS, body: '' };
  }
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers: CORS, body: JSON.stringify({ error: 'Method Not Allowed' }) };
  }

  let payload;
  try {
    payload = JSON.parse(event.body);
  } catch(e) {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: 'Invalid JSON' }) };
  }

  // Garante que cada item tenha unitPrice (obrigatório pela Black Cat Pay)
  if (Array.isArray(payload.items)) {
    const totalCents = payload.amount || 0;
    const totalItems = payload.items.reduce(function(sum, i) { return sum + (i.quantity || 1); }, 0);
    const pricePerItem = totalItems > 0 ? Math.round(totalCents / totalItems) : totalCents;
    payload.items = payload.items.map(function(item) {
      if (!item.unitPrice) {
        return Object.assign({}, item, { unitPrice: pricePerItem * (item.quantity || 1) });
      }
      return item;
    });
  }

  try {
    const response = await fetch(BC_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': BC_KEY,
      },
      body: JSON.stringify(payload),
    });

    const text = await response.text();
    console.log('BlackCat status:', response.status);
    console.log('BlackCat response:', text.substring(0, 800));

    let data;
    try { data = JSON.parse(text); } catch(e) { data = { raw: text }; }

    // Normaliza erros: garante que qualquer resposta de erro vire { success: false, error: ... }
    if (!response.ok) {
      return {
        statusCode: response.status,
        headers: CORS,
        body: JSON.stringify({
          success: false,
          error: data.message || data.error || data.raw || 'Erro na API Black Cat Pay',
          detail: data,
        }),
      };
    }

    return {
      statusCode: 200,
      headers: CORS,
      body: JSON.stringify(data),
    };
  } catch(err) {
    console.error('pay.js fetch error:', err.message);
    return {
      statusCode: 500,
      headers: CORS,
      body: JSON.stringify({ success: false, error: 'Erro interno: ' + err.message }),
    };
  }
};
