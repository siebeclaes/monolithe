<!DOCTYPE html>
<html lang="en">
<head>
    <title>VSD API Reference</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/style.css">
</head>

<body data-spy="scroll" data-target="#navbarmain">

    <nav class="navbar navbar-default navbar-fixed-top" id="navbarmain">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="index.html">VSD API Documentation</a>

            </div>
            <div class="collapse navbar-collapse" id="navbar">
                <ul class="nav navbar-nav">
                    <li><a href="usage.html">API Usage</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Components <span class="caret"></span></a>
                        <ul class="dropdown-menu" role="menu">
                            {% for package_name, model_names in packages|dictsort %}
                            <li class="divider"></li>
                            <li><a data-id="section-{{package_name| replace(" ", "_")}}" href="#section-{{package_name | replace(" ", "_")}}">{{package_name}}</a></li>
                            {% endfor %}
                        </ul>
                    </li>
                </ul>
                <form class="navbar-form navbar-right" role="search">
                    <div class="form-group dropdown">
                        <input type="text" class="form-control" placeholder="Search" id="searchfield">
                        <ul class="dropdown-menu dropdown-menu-left" role="menu" id="searchresult" style="display: none"></ul>
                    </div>
                </form>
            </div>
        </div>
    </nav>

    <div class="container" id="content">

        {% for package_name, model_names in packages|dictsort %}
        <section id="section-{{package_name | replace(" ", "_")}}">
            <h3>{{package_name}}</h3>
                {% for model_name in model_names|sort %}
                {% set model = models[model_name] %}
                <div class="row">
                    <div class="col-xs-12" style="padding: 10px; border-top: 1px solid #E7E7E7">
                        <a class="filterable"
                            data-filter-keyword="{{model.resource_name}}" id="{{model.resource_name}}" href="{{model.remote_name}}.html"
                            title="API reference for {{model.name}}">{{model.resource_name}}</a>
                    </div>
                </div>
                {% endfor %}
                <tr><td></td></tr>
            </table>
        </section>
        {% endfor %}

    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/search.js"></script>

    <script>
        $(document).ready(function() {
            initialize_search("");
            initialize_scrollspy();
        });
    </script>

</body>
</html>
