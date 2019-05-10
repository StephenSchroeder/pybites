"""
You are presented with workout_schedule with keys: days and values: workouts. Complete get_workout_motd that receives a day string, title case it so the function can receive case insensitive days, look it up in the dict and do two things:

If the day (key) is not in the dictionary, raise a KeyError, we don't want this function to continue, the caller needs to catch this exception,
If the key is in the dictionary, return chill or go_train depending if it's a Rest day or not. The latter you will need to string-interpolate using format.
"""

workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
       if day.title() in workout_schedule:
              if workout_schedule[day.title()] == 'Rest':
                     return chill

              else:
                     return go_train.format(workout_schedule[day.title()])

       else:
              raise KeyError('That is not a day')

print(get_workout_motd("wednesday"))

