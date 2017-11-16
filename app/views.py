import json
from steem import Steem

from django.views.generic import TemplateView


papapepper_entries = [
    {
        'permlink': 'the-daily-steemit-selfie-challenge-an-elimination-contest-from-papa-pepper-50-sbd-starting-prize-pool',
        'challenge': 'REGISTRATION DAY',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-1-60-sbd-prize-pool-and-growing',
        'challenge': 'DAY 1: PLANT',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-2-75-sbd-prize-pool-and-growing',
        'challenge': 'DAY 2: ANIMAL',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-3-1oo-sbd-prize-pool-and-growing',
        'challenge': 'DAY 3: FIRE',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-4-111-sbd-prize-pool-and-growing',
        'challenge': 'DAY 4: REFLECTIONS',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-5-125-sbd-prize-pool-and-growing',
        'challenge': 'DAY 5: FOOD',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-6-140-sbd-prize-pool-and-growing',
        'challenge': 'DAY 6: SKY',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-7-150-sbd-prize-pool-and-growing',
        'challenge': 'DAY 7: PERFECT SELFIE SMILE LIFEHACK ATTACK!',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-8-160-sbd-prize-pool-and-growing',
        'challenge': 'DAY 8: I GOTTA HAND IT TO YOU',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-9-175-sbd-prize-pool-and-growing',
        'challenge': 'DAY 9: CUTTING IT CLOSE',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-10-185-sbd-prize-pool-and-growing-21-hour-round',
        'challenge': 'DAY 10: WATER YOU TALKING ABOUT?',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-11-200-sbd-prize-pool-and-growing',
        'challenge': 'DAY 11: VEHICLE',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-12-215-sbd-prize-pool-and-growing',
        'challenge': 'DAY 12: THE MONEY SHOT',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-13-230-sbd-prize-pool-and-growing',
        'challenge': 'DAY 13: FOUR MORE',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-14-250-sbd-prize-pool-and-growing',
        'challenge': 'DAY 14: FIRE & WATER',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-15-265-sbd-prize-pool-and-growing',
        'challenge': 'DAY 15: THE "SEAL" OF APPROVAL',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-16-275-sbd-prize-pool-and-growing',
        'challenge': 'DAY 16: LOOK WHAT I FOUND!',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-17-290-sbd-prize-pool-and-growing',
        'challenge': "DAY 17: YOU WOULDN'T LIKE ME WHEN I AM ANGRY",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-18-300-sbd-prize-pool-and-growing',
        'challenge': 'DAY 18: BUSTED!',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-19-315-sbd-prize-pool-and-growing',
        'challenge': 'DAY 19: JUGGLE',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-20-325-sbd-prize-pool-and-growing',
        'challenge': 'DAY 20: BLACK EYE',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-21-340-sbd-prize-pool-and-growing',
        'challenge': 'DAY 21: PEEKING',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-22-350-sbd-prize-pool-and-growing',
        'challenge': 'DAY 22: THIS LITTLE PIGGY',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-23-365-sbd-prize-pool-and-growing-shortened-round',
        'challenge': 'DAY 23: WATER ON THE HEAD',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-24-375-sbd-prize-pool-and-growing',
        'challenge': 'DAY 24: TURN THE WORLD UPSIDEDOWN!',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-25-385-sbd-prize-pool-and-growing',
        'challenge': 'DAY 25: POWDER POWER!',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-26-400-sbd-prize-pool-and-growing',
        'challenge': 'DAY 26: THE FLAMINGO SHOE TELEPHONE!',
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-27-415-sbd-prize-pool-and-growing',
        'challenge': "DAY 27: revved up like a deuce - Who's ready to get blinded by the light?",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-28-425-sbd-prize-pool-and-growing',
        'challenge': "DAY 28: THREE-HEADED BEAST!",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-29-435-sbd-prize-pool-and-growing',
        'challenge': "DAY 29 - BACKWARDS PERFECT SMILE",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-30-444-sbd-prize-pool-and-growing-warning-short-round',
        'challenge': "DAY 30 - YOU ARE WHAT YOU EAT LITTLE MAN!",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-31-450-sbd-prize-pool-and-growing',
        'challenge': "DAY 31 - PLECOCTOMUS - DO YOU KNOW WHAT THAT FISH DOES?",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-32-460-sbd-prize-pool-and-growing',
        'challenge': "DAY 32 - SUSPENDERS - THE SUSPENDS IS KILLING ME!",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-33-475-sbd-prize-pool-and-growing',
        'challenge': "DAY 33 - HAPPY CHIN FACE",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-34-485-sbd-prize-pool-and-growing',
        'challenge': "DAY 34 - BED HEAD",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-35-500-sbd-prize-pool-and-growing',
        'challenge': "DAY 35 - FEEL THE BURN!",
    },
    {
        'permlink': 'the-daily-steemit-selfie-challenge-day-36-515-sbd-prize-pool-and-growing',
        'challenge': "DAY 36 - DON’T HURT YOURSELF",
    },
]


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        s = Steem()

        dearjyoce_selfies = []

        for entry_dict in papapepper_entries:
            entry_comments = s.get_content_replies(
                author='papa-pepper',
                permlink=entry_dict['permlink'],
            )

            selfie_dict = {
                'challenge': entry_dict['challenge'],
                'permlink': entry_dict['permlink'],
            }

            for comment in entry_comments:
                author = comment['author']

                if author == 'bien':
                    json_metadata = json.loads(comment['json_metadata'])
                    image_list = json_metadata.get('image')

                    if image_list:
                        image = image_list[0]
                        selfie_dict['image'] = image

                        break

            dearjyoce_selfies.append(selfie_dict)

        return self.render_to_response(
            self.get_context_data(
                dearjyoce_selfies=dearjyoce_selfies
            )
        )


class NotFoundView(TemplateView):
    template_name = '404.html'
