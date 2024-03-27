start "" "App\TrashCatWindows\TrashCat.exe"
sleep 3
pip install -r requirements.txt
echo "Create allure-report folder..."
allure generate
echo "Execute tests..."

python -m pytest TestsPython\\tests\\main_menu_page_test.py --alluredir=allure-report/
python -m pytest TestsPython\\tests\\game_play_test.py --alluredir=allure-report/
python -m pytest TestsPython\\tests\\start_page_test.py --alluredir=allure-report/

echo "Generate Allure report..."
allure generate -c allure-report -o allure-results-html

echo "Combine Allure report..."
allure-combine ./allure-results-html
echo "Kill Trashcat..."
tskill TrashCat