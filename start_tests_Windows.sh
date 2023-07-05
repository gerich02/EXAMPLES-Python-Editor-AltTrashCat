start "" "App\TrashCatWindows\TrashCat.exe"
sleep 3
pip install -r requirements.txt

python -m pytest TestsPython\\tests\\main_menu_page_test.py
python -m pytest TestsPython\\tests\\game_play_test.py
python -m pytest TestsPython\\tests\\start_page_test.py

tskill TrashCat