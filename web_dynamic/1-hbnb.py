<!DOCTYPE html>
<HTML lang="en">
  <HEAD>

    <!-- HEAD -->

    <META charset="utf-8">
    <META name="viewport" content="width=device-width">
    <TITLE>HolbertonBnB</TITLE>

    <!-- FAVICON -->

    <LINK rel="shortcut icon" href="{{ url_for('static', filename='images/icon.png') + '?' + cache_id }}">

    <!-- **********************
	 CSS styles
	 ********************** -->

    <LINK rel="stylesheet" href="{{ url_for('static', filename='styles/4-common.css') + '?' + cache_id }}">
    <LINK rel="stylesheet" href="{{ url_for('static', filename='styles/3-header.css') + '?' + cache_id }}">
    <LINK rel="stylesheet" href="{{ url_for('static', filename='styles/3-footer.css') + '?' + cache_id }}">
    <LINK rel="stylesheet" href="{{ url_for('static', filename='styles/6-filters.css') + '?' + cache_id }}">
    <LINK rel="stylesheet" href="{{ url_for('static', filename='styles/8-places.css') + '?' + cache_id }}">
    <LINK rel="stylesheet" href="{{ url_for('static', filename='styles/font-awesome.css') + '?' + cache_id }}">

    <!-- jQUERY -->
    <SCRIPT src="https://code.jquery.com/jquery-3.2.1.min.js"></SCRIPT>
    <SCRIPT src="{{ url_for('static', filename='scripts/1-hbnb.js') + '?' + cache_id }}"></SCRIPT>
  </HEAD>

  <!-- **********************
       BODY
       ********************** -->

  <BODY>

    <!-- **********************
	 HEADER
	 ********************** -->

    <HEADER>
    </HEADER>
    <MAIN>
      <DIV class="container">

	<!-- **********************
	     FILTERS
	     ********************** -->

	<SECTION class="filters">

	  <!-- **********************
	       LOCATIONS
	       ********************** -->

	  <DIV class="locations">
	    <H3>States</H3>
	    <H4>&nbsp;</H4>
	    <UL class="popover">
	      {% for state in states|dictsort %}
	      <H2>{{ state[0] }}</H2>
	      <UL>
		    {% for city in state[1].cities|sort(attribute='name') %}
		      <LI>{{ city.name }}</LI>
		    {% endfor %}
	      </UL>
	      {% endfor %}
	    </UL>
	  </DIV>

	  <!-- **********************
	       AMENITIES
	       ********************** -->

	  <DIV class="amenities">
	    <H3>Amenities</H3>
	    <H4>&nbsp;</H4>
	    <UL class="popover">
	      {% for amenity in amens|sort(attribute='name') %}
	      <LI>
          <INPUT type="checkbox" data-id="{{ amenity.id }}" data-name="{{ amenity.name }}">
            {{ amenity.name }}
          </INPUT>
        </LI>
	      {% endfor %}
	    </UL>
	  </DIV>

	  <!-- **********************
	       SEARCH BUTTON
	       ********************** -->

	  <BUTTON>Search</BUTTON>
	</SECTION>

	<SECTION class="places">
	  <H1>Places</H1>

	<!-- **********************
	     BEGIN 1 PLACE
	     ********************** -->

	  {% for place in places|sort(attribute='name') %}

	  <ARTICLE>

	    <DIV class="title">

	      <H2>{{ place.name }}</H2>

	      <DIV class="price_by_night">

		{{ place.price_by_night }}

	      </DIV>
	    </DIV>
	    <DIV class="information">
	      <DIV class="max_guest">
		<I class="fa fa-users fa-3x" aria-hidden="true"></I>

		<BR />

		{{ place.max_guest }} Guests

	      </DIV>
	      <DIV class="number_rooms">
		<I class="fa fa-bed fa-3x" aria-hidden="true"></I>

		<BR />

		{{ place.number_rooms }} Bedrooms
	      </DIV>
	      <DIV class="number_bathrooms">
		<I class="fa fa-bath fa-3x" aria-hidden="true"></I>

		<BR />

		{{ place.number_bathrooms }} Bathroom

	      </DIV>
	    </DIV>

	    <!-- **********************
		 USER
		 **********************  -->

	    <DIV class="user">

	      <STRONG>Owner: {{ users[place.user_id] }}</STRONG>

	    </DIV>
	    <DIV class="description">

	      {{ place.description }}

	    </DIV>

	  </ARTICLE> <!-- End 1 PLACE Article -->

	  {% endfor %}

	</SECTION>
      </DIV>
    </MAIN>

    <!-- FOOTER -->

    <FOOTER>
      Holberton School
    </FOOTER>
  </BODY>
</HTML>
