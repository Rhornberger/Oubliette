var Register = {
    template:     
        `
        {% load crispy_forms_tags %}
        <div class="content-section">
            <form method="POST" >
                {% csrf_token %}
                <fieldset class="form-group">
                    <legend class="border-bottom mb-4">Let the Adventure begin</legend>
                    {{ form|crispy }}
                </fieldset>
                <div class="form-group">
                    <button class="btn btn-outline-info" type="submit" >Let's Drop into the Theater of the Mind!</button>
                </div>
            </form>
            <div class="border-top pt-3">
                <small class="text-muted">Already an adventurer?<a class="ml-2" href="{% url 'login' %}">Sign In</a></small>
            </div>
        </div>`
}