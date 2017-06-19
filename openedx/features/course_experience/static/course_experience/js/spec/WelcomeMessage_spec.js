/* globals $, loadFixtures */

import { AjaxHelpers } from 'edx-ui-toolkit/js/utils/spec-helpers/ajax-helpers';
import { WelcomeMessage } from '../WelcomeMessage';

describe('Welcome Message factory', () => {
  describe('Ensure button click', () => {
    const endpointUrl = '/course/course_id/dismiss_message/';
    beforeEach(() => {
      loadFixtures('course_experience/fixtures/welcome-message-fragment.html');
      WelcomeMessage(endpointUrl);
    });
    it('When button click is made, ajax call is made and message is hidden.', () => {
      const message = document.querySelector('.welcome-message');
      document.querySelector('.dismiss-message button').dispatchEvent(new Event('click'));
      const requests = AjaxHelpers.requests(this);
      AjaxHelpers.expectRequest(
        requests,
        'POST',
        endpointUrl,
      );
      AjaxHelpers.respondWithJson(requests);
      expect(message.innerHtml).toBe('');
    });
  });
});
