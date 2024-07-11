A common response format when writing an API is JSON. It’s easy to get started writing such an API with Flask. If you return a dict from a view, it will be converted to a JSON response.

@app.route("/me")
def me_api():
        user = get_current_user()
            return {
                            "username": user.username,
                                    "theme": user.theme,
                                            "image": url_for("user_image", filename=user.image),
                                                }
            Depending on your API design, you may want to create JSON responses for types other than dict. In that case, use the jsonify() function, which will serialize any supported JSON data type. Or look into Flask community extensions that support more complex applications.

            @app.route("/users")
            def users_api():
                    users = get_all_users()
                        return jsonify([user.to_json() for user in users])
