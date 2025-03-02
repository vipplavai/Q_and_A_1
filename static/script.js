function fetchContent() {
    let contentID = $("#contentID").val();
    $.get(`/content/${contentID}`, function(response) {
        if (response.status === "success") {
            $("#contentSection").show();
            $("#contentText").val(response.content);  // Load content in large textbox
            $("#questionList").empty();
            response.questions.forEach(q => {
                $("#questionList").append(
                    `<li>${q.question} (${q.difficulty})
                    <button onclick="editQuestion('${q.question}', '${q.difficulty}')">Edit</button></li>`
                );
            });
        } else {
            alert(response.message);
        }
    });
}

function addQuestion() {
    let contentID = $("#contentID").val();
    let question = $("#newQuestion").val();
    let difficulty = $("#difficulty").val();
    $.post("/add-question", JSON.stringify({ content_id: contentID, question: question, difficulty: difficulty }), function(response) {
        alert(response.message);
        fetchContent();
    }, "json");
}

function editQuestion(oldQuestion, oldDifficulty) {
    let newQuestion = prompt("Edit Question:", oldQuestion);
    let newDifficulty = prompt("Edit Difficulty (easy, medium, hard):", oldDifficulty);
    let contentID = $("#contentID").val();

    $.ajax({
        url: "/edit-question",
        type: "PUT",
        contentType: "application/json",
        data: JSON.stringify({ content_id: contentID, old_question: oldQuestion, new_question: newQuestion, new_difficulty: newDifficulty }),
        success: function(response) {
            alert(response.message);
            fetchContent();
        }
    });
}
