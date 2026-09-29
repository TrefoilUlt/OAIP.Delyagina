from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name" : "Дмитров Дмитрий",
        "group_name" : "ИСП-324п",
        "grade" : 4,
    },
]

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route("/api/students", methods=['POST'])
def add_student():
    data = request.get_json()

    if not data or "name" not in data or "group_name" not in data:
        return jsonify({"error" : "Необходимо указать имя и группу студента"}), 400

    new_student = {
        "id": max([student["id"] for student in students]) + 1,
        "name" : data["name"],
        "group_name" : data["group_name"],
        "grade" : data["grade"],
    }

    students.append(new_student)

    return jsonify(new_student), 201

@app.route('/api/students/edit_grade/<int:id>', methods=['PUT'])
def edit_grade(id):
    student = next(
        (student for student in students if student["id"] == id),
        None
    )

    if student is None:
        return jsonify({"error": "Студент не найден"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Тело запроса отсутствует"}), 400

    return jsonify({
        "message": "Оценка изменена",
        "grade": data["grade"]
    }), 300


@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = next(
        (student for student in students if student["id"] == id),
        None
    )

    if student is None:
        return jsonify({"error": "Студент не найден"}), 404


    students.remove(student)

    return jsonify({
        "message" : "Студент удалён",
        "student" : student
    }), 200


if __name__ == '__main__':
    app.run(debug=True)