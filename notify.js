function sendLineNotify(text, image) {
  var messages = {
    message: text,
    imageThumbnail: image,
    imageFullsize: image,
  };
  var url = "https://notify-api.line.me/api/notify";
  var token = "p9KEHl2DpVLfRgN0QH4q36ZfF8Ku7xgU5lpm3GbrVrD";
  var options = {
    method: "post",
    payload: messages,
    headers: {
      Authorization: "Bearer " + token,
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



export { sendLineNotify };
