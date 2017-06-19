/* globals $, loadFixtures */

import { WelcomeMessage } from '../WelcomeMessage';
import {
  expectRequest,
  requests as mockRequests,
  respondWithJson
} from 'edx-ui-toolkit/js/utils/spec-helpers/ajax-helpers';

describe('Welcome Message factory', () => {
  describe('Ensure button click', () => {
    const endpointUrl = '/course/course_id/dismiss_message/';
    beforeEach(() => {
      loadFixtures('course_experience/fixtures/welcome-message-fragment.html');
      WelcomeMessage(endpointUrl);
    });
    it('When button click is made, ajax call is made and message is hidden.', () => {
      const message = document.querySelector('.welcome-message');
      const requests = mockRequests(this);
      document.querySelector('.dismiss-message button').dispatchEvent(new Event('click'));
      expectRequest(
        requests,
        'POST',
        endpointUrl,
      );
      respondWithJson(requests);
      expect(message.innerHtml).toBe('');
    });
  });
});
