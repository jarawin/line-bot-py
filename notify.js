function sendLineNotify(text) {
  var messages = {
    message: text,
  };
  var url = "https://notify-api.line.me/api/notify";
  var token = ""; // INPUT TOKEN HERE
  var options = {
    method: "post",
    payload: messages,
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  fetch(url, options)
    .then((res) => {
      console.log(res);
      alert("success");
    })
    .catch((e) => {
      console.log(e);
    });
}

// ?? how to get line notify token
// 1. https://notify-bot.line.me/th/
// 2. click เข้าสู่ระบบ และ login ด้วย line ตนเอง
// 3. click ที่ชื่อไลน์ตัวเองมุมขวาบน
// 4. click หน้าของฉัน
// 5. เลื่อนมาข้างล่างสุด ==> กดออกโทเคน
// 6. ใส่ข้อความอะไรก็ได้
// 7. กด รับการแจ้งเตือนแบบตัวต่อตัวจาก LINE Notify
// 8. กด คัดลอก token มาวางในบรรทัดที่ 8

sendLineNotify(text)