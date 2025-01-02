# qase-pytest

This is an example repository with tests in the `tests/examples/` directory. To run the tests :

1. Clone the repository with `git clone https://github.com/cskmnrpt/qase-pytest.git`.
   To clone a different branch, other than `main`, use this command - <br> `git clone --single-branch --branch <branch-name> https://github.com/cskmnrpt/qase-pytest.git`

2. Create a virtual environment with `virtualenv venv`, and activate it with `source venv/bin/activate`.

3. Run `pip install -r requirements.txt` from the root of this repository to install dependencies.

4. Install browsers, if you are using the `playwright` library: `playwright install`.

5. Create a `qase.config.json` in the root of the repository, and add your token, and project code.

6. Run `pytest`.
