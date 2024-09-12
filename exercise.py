import requests
import json

slack_url = 'https://hooks.slack.com/services/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'

def send_slack_message(url, message):
    payload = {
        "text": message
    }
    response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    return response

'''
import requests

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'



@router.post('/', response_model=BubbleUserCreate)
async def create_user(user: BubbleUserCreate):
    create_user_task.delay(user.json())
    return user


@celery_application.task(bind=True, max_retries=3, acks_late=True)
def create_user_task(self, json_user):
    async def call(user_create):
        async with session_manager() as session:
            new_user = BubbleUser(
                first_name=user_create.firstName,
                last_name=user_create.lastName,
                birth_date=user_create.birthDate,
                gender=user_create.gender,
                email=user_create.email,
                bubble_id=user_create.bubbleId,
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

     try:
        event_loop = asyncio.get_event_loop()
        user_create = BubbleUserCreate.parse_raw(json_user)
        coro = call(user_create)
        new_user = event_loop.run_until_complete(coro)
        if self.request.retries == 0:
            upsert_klaviyo_user_task.delay(new_user.to_json())
    except Exception as exc:
        slack_message = f"Error creating user in create_user_task: {exc}"
        send_slack_message(SLACK_WEBHOOK_URL, slack_message)

        if self.request.retries == self.max_retries:
            logger.exception(f'Error creating user! {exc}')
            raise Reject(requeue=False)
        self.retry(exc=exc, countdown=5)
'''
