let sessionId = null;
let txnId = null;

async function getCaptcha() {
  const res = await fetch('/get-captcha');
  const data = await res.json();
  if (data?.captcha_image && data?.session_id) {
    sessionId = data.session_id;
    document.getElementById('captchaImg').src = 'data:image/png;base64,' + data.captcha_image;
    document.getElementById('captchaBox').style.display = 'block';
  } else {
    alert('Failed to get captcha.');
  }
}

async function generateOTP() {
  const aadhaar = document.getElementById('aadhaar').value.trim();
  const captcha = document.getElementById('captcha').value.trim();

  const res = await fetch('/generate-otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ aadhaar_number: aadhaar, captcha, session_id: sessionId })
  });

  const data = await res.json();
  document.getElementById('result').textContent = JSON.stringify(data, null, 2);

  if (data.txn_id) {
    txnId = data.txn_id;
    document.getElementById('otpSection').style.display = 'block';
  } else {
    alert('OTP generation failed.');
  }
}

async function verifyOTP() {
  const otp = document.getElementById('otp').value.trim();

  const res = await fetch('/verify-otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      otp,
      txn_id: txnId,
      client_id: 'YOUR_CLIENT_ID' // Optional: if API requires it separately in body
    })
  });

  const data = await res.json();
  document.getElementById('result').textContent = JSON.stringify(data, null, 2);
}
