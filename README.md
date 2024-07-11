# Mouse Jiggler

Mouse Jiggler is a script to move the cursor randomly to prevent idle detection. This can be useful in scenarios where you want to prevent your computer from going to sleep or appearing idle.

## Installation

To install the Mouse Jiggler, you need to have Python and pip installed on your system. Follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/hurryingauto3/mouse_jiggler.git
    cd mouse_jiggler
    ```

2. Install the package:

    ```sh
    pip install .
    ```

## Usage

After installation, you can use the `jiggler` command to run the script. Here are the available options:

```sh
jiggler --min-delay 10 --max-delay 120 --min-steps 50 --max-steps 150 -s 600 -m 70 -i 5 -w 90 -tz "America/New_York" -sh 8 -eh 18
