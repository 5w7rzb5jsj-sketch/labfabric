import test_detector


def main():
    test_detector.test_error_event_is_anomaly()
    test_detector.test_info_event_is_not_anomaly()
    print("detector tests passed")


if __name__ == "__main__":
    main()
