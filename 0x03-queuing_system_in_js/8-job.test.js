const { describe, it, before, after, afterEach,} = require('mocha');
const { expect } = require('chai');
const { createQueue } = require('kue')
const  createPushNotificationsJobs = require('./8-job.js');

const queue = createQueue();

describe('Test createPushNotificatinsJobs function', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('job', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('Test whether jobs are created', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
