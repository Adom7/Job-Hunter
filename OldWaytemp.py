
   try:
        apply_button = driver.find_element_by_css_selector(
            '.jobs-apply-button')
        apply_button.click()
        time.sleep(1)
        phone_input = driver.find_element_by_css_selector(
            '.fb-single-line-text__input')
        phone_input.clear()
        phone_input.send_keys(Phone_Number)
        next_button = driver.find_element_by_css_selector('footer button')
        time.sleep(1)
        next_button.click()
        verify_button = driver.find_element_by_css_selector(
            'footer .artdeco-button--primary')
        verify_button.click()
        time.sleep(1)
        tick_box = driver.find_element_by_css_selector(
            'footer .ember-checkbox')
        tick_box.click()
        verify_button = driver.find_element_by_css_selector(
            'footer .artdeco-button--primary')
        if verify_button.get_attribute("data-control-name") == "continue unify":
            close_button = driver.find_elements_by_class_name(
                "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(1)
            discard_button = driver.find_elements_by_class_name(
                "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print('Candidature complexe , annuler')
            continue
        else:
            tick_box = driver.find_element_by_css_selector(
                'footer .ember-checkbox')
            tick_box.click()
            verify_button.click()
            time.sleep(2)
            submit_button = driver.find_element_by_class_name()
    except NoSuchElementException:
        print("Pas de Button candidature , passer")
        continue
