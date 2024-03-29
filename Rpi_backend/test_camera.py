from src import camera as camera_module
import time

if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 30

    camera = camera_module.Camera({
        "show_preview": True
    })
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        camera.capture()
        print(camera.image_array)

        time.sleep(max(0, 1/sample_hz -
                       (time.time() - start_time)))
