$.ajax({
  url: "/rest/",
  type: "GET",
  dataType: "json",
  success: (data) => {
    console.log(data);
    $.each(data, function (index, element) {
      $("#tb_sch").append(
        "<tr>" +
          "<td>" +
          (index + 1) +
          "</td>" +
          "<td>" +
          element.schedule_name +
          "</td>" +
          "<td>" +
          element.schedule_time +
          "</td>" +
          "<td>" +
          "<button type='button' class='btn btn-danger btn-sm ms-1'>Delete</button>" +
          "<button type='button' class='btn btn-success btn-sm ms-1'>Update</button>" +
          "</td>" +
          "</tr>"
      );
    });
  },
  error: (error) => {
    console.log(error);
  },
});
