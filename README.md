# Standalone Build with Python Tests

This repository shows a few Python tests that use the page object model and AltTester® Unity SDK to test the Unity Endless Runner sample:

https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Running the tests on Windows or MacOS
The tests are meant to be run on a Windows or MacOS device.

To start the tests, depending on your OS run:

❗ Starting with version 2.0.0, the AltTester® Desktop must be running on your PC while the tests are running.

1. Install and open AltTester® Desktop:
   - **MacOS/Linux**: Download and install the AltTester® Desktop for MacOS from [here](https://alttester.com/downloads/)
   - **Windows**: Download and install the AltTester® Desktop for Windows from [here](https://alttester.com/downloads/)
2. Instrument the TrashCat application using the latest version of AltTester® Unity SDK - for additional information you can follow [this tutorial](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x)
3. Launch example project game:
   1. Run AltTester® editor in Unity project.
   2. Select platform Editor.
   3. Click Play in Editor.
4. Run `./start_tests.sh` in your terminal:
   - **MacOS/Linux**: Use Terminal
   - **Windows**: Use Git Bash or other unix terminal emulator

This script will:

- start the app on your device
- run the tests
- stop the app after the tests are done

# P.s.

Проблемы, с которыми пришлось столкнуться во время выполнения задания:
1) Установка.
Во время установки необходимо было установить через package manager пакет Editor Coroutins, без него Alt Tester не устанавливался в Unity. Так же были проблемы с запуском проекта через Alt Tester, мешала ошибка NullReferenceException.
Помогло полное удаление Unity и AltTester с ПК, так же заподозрил, что дело могло быть в эмуляторе андроида Bluestacks.

Обязательно необходимо проделать процедуры, описанные по ссылке https://alttester.com/docs/sdk/latest/pages/get-started.html#import-alttester-package-in-unity-editor (внесение дополнений в файл manifest.json).

После решения данных проблем тестовый проект был установлен и запущен, тесты запускались командой ./start_tests.sh через bash терминал в VsCode.

2) Тесты.
В приложенных тестах было три направления тестирования:
- тесты главной страницы;
- тесты стартовой страницы;
- тесты геймплея.

В случае с первыми двумя пунктами проблем нет, ошибки появляются в тестах геймплея:
- тесты на возможность приостановки игры с последующим продолжением либо полной остановкой не проходят. Предположительно
это связано со скоростью анимации срабатывания клавиш "пауза" и "продолжить", не всегда изображение с меню паузы появляется на экране, так быстро это происходит, что возможно программа не успевает захватывать изображение. Лечить пытался стандартными  методами python через time.sleep(), а так же через кастомный метод с циклом while, однако какие бы значения не выставлял, тесты прожимали клавиши молниеносно.

- тесты на избегание препятствий и смерть игрока не могут пройти вообще, тесты на них впадают в бесконечный простой.
Проблема заключается в том, что в момент приближения к первому препястсвию игра останавливается, появляется подсказка "Slide sideway to change lane". Проблема в том, что у меня не вышло интегрировать обход этой проблемы.
Варианты решения проблемы было три:
- заставить игрока сменить линию без каких либо условий в методе avoid_obstacles в game_play_page.py, в том числе используя time.sleep, чтобы точно дождаться момента остановки игры и в самом начале сменить позицию.
- заставить игрока сменить линию при условии обнаружения объектов TutoSlide(объектов туториала) так же в методе avoid_obstacles в game_play_page.py
- создать тест, который мог обойти обучение, так как я заметил, что при определенных манипуляциях если данное сообщение уже выходило, но был перезапуск игры, тесты могут попытаться пройти дальше, пока не уткнутся в такую же подсказку "Slide to jump"

К сожалению, решить эту проблему не удалось.

Так же я написал несколько простых тестов на проверку появляется ли tutorial mode в main menu, появляется ли обратный отсчет и
как раз таки появляется ли подсказка "Slide sideway to change lane" во время первой игры.

P.p.s. Большая часть времени ушла на починку уже существующих тестов.
