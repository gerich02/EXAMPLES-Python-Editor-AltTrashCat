open App/TrashCatMac/TrashCat.app
sleep 3
pip install -r requirements.txt

echo "Create allure-report folder..."
allure generate

pytest TestsPython/tests/main_menu_page_test.py --alluredir=allure-report/
pytest TestsPython/tests/game_play_test.py --alluredir=allure-report/
pytest TestsPython/tests/start_page_test.py --alluredir=allure-report/

echo "Generate Allure report..."
allure generate -c allure-report -o allure-results-html

echo "Combine Allure report..."
allure-combine ./allure-results-html

killall TrashCat