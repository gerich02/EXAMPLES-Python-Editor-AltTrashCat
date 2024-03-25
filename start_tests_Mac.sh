open App/TrashCatMac/TrashCat.app
sleep 3
pip install -r requirements.txt

pytest TestsPython/tests/main_menu_page_test.py
pytest TestsPython/tests/game_play_test.py
pytest TestsPython/tests/start_page_test.py

killall TrashCat