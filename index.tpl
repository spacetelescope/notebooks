<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8>
<title>Notebooks Index</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
</head>
<body>
  <h2 style="margin: 1em; border-bottom: 1px solid #eaecef;
    padding-bottom: .3em; font-size: 1.5em">Notebooks Index</h2>

<ul class="list-group list-group-flush" style="width: fit-content; margin: .5em">
{% for group in page_groups %}
  <li>
    <ul class="list-group list-group-flush" style="width: fit-content; margin: .5em">
      {{ group[0]['output_file_path'].split("/")[1] }}
      {% for page in group %}
        {% set pre = page['output_file_path'].split("/")[2] + " | " if "_" not in page['output_file_path'].split("/")[2] else "" %}
        <li class="list-group-item"><a href="{{ page['output_file_path'] }}">{{ pre + page['name'] + "   |    " + page['title'] }}</a></li>
      {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>

</body>
</html>
