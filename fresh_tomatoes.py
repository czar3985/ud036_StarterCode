import webbrowser
import os
import re


def create_movie_tiles_content(movies):
    # A single movie entry html template
    movie_tile_content = '''
    <div class="col-sm-6 col-md-6 col-lg-4 movie-tile text-center"
            data-title="{movie_title}"
            data-storyline="{storyline}"
            data-trailer-youtube-id="{trailer_youtube_id}"
            data-toggle="modal"
            data-target="#trailer">
        <img src="{poster_image_url}" width="220" height="342">
        <h2>{movie_title}</h2>
    </div>
    '''

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Styles, scripting and page layout for the page
    base_file = open('base_page.html', 'r')
    main_page_content = base_file.read()
    base_file.close()

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
