INPUT_PATH=$(pwd) OUTPUT_PATH=$(pwd)/play_output docker run \
-w="/tmp/input" \
--entrypoint="manim" \
-v="$(pwd):/tmp/input" \
eulertour/manim:latest \
$@
