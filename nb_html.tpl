{%- extends 'full.tpl' -%}


{%- block html_head -%}
{{ super() }}

<!-- base css for whole site -->
<link rel="stylesheet" href="{{ resources.path_to_pages_root }}pages.css">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.css">

<link rel="stylesheet" type="text/css" href="https://rawgit.com/ipython-contrib/jupyter_contrib_nbextensions/master/src/jupyter_contrib_nbextensions/nbextensions/toc2/main.css">

<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.9.1/jquery-ui.min.js"></script>

<script src="https://rawgit.com/ipython-contrib/jupyter_contrib_nbextensions/master/src/jupyter_contrib_nbextensions/nbextensions/toc2/toc2.js"></script>

<script>
$( document ).ready(function(){
           var cfg = {{ nb.get('metadata', {}).get('toc', {})|tojson|safe }};
           // fire the main function with these parameters
           require(['nbextensions/toc2/toc2'], function (toc2) {
               toc2.table_of_contents(cfg);
           });
   });
</script>

{%- endblock html_head -%}
