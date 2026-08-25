import pytest

from playwright.sync_api import sync_playwright
from utilities.constants import BASE_URL
from utilities.data_reader import load_json
from pathlib import Path


ROOT = Path(__file__).parent
SCREENSHOTS = ROOT / "screenshots"
VIDEOS = ROOT / "videos"
TRACES = ROOT / "traces"


@pytest.fixture
def page(request):
    test_name = request.node.name
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    VIDEOS.mkdir(parents=True, exist_ok=True)
    TRACES.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,args=["--start-maximized"])
        context = browser.new_context(
            no_viewport=True,
            record_video_dir=str(VIDEOS),
            record_video_size ={"width" : 1024, "height":768}
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto(BASE_URL)
        try:
            yield page
        finally:
            trace_path = TRACES / f"{test_name}.zip"
            context.tracing.stop(path=str(trace_path))
            video = page.video
            context.close()
            if video:
                video_path = video.path()
                print(f"Video saved: {video_path}")
            browser.close()


@pytest.fixture
def register_data():
    return load_json("data/register.json")


@pytest.fixture
def login_data():
    return load_json("data/login.json")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("page")
        if report.failed and page:
            SCREENSHOTS.mkdir(parents=True, exist_ok=True)
            screenshot_path = SCREENSHOTS / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"Failure screenshot saved: {screenshot_path}")
            
@pytest.fixture
def screenshot(page):
    def take_screenshot(name):
        SCREENSHOTS.mkdir(parents=True, exist_ok=True)
        screenshot_path = SCREENSHOTS / f"{name}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        print(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    return take_screenshot


