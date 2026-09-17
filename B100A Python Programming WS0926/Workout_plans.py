# Workout Plans File

class workoutplan:
    # manages workout routines and exercise lists

    def __init__(self, plan_id: str, plan_name: str, difficullty: str ='Beginner'):
        self.plan_id = str(plan_id).strip()
        self.plan_name = str(plan_name).strip()
        self.difficulty = str(difficullty).strip()
        self.exercises = []

    # add an exerice
    def add_exercise(self, exercise_name: str) -> None:
        cleaned = exercise_name.strip()
        if cleaned and cleaned not in self.exercises:
            self.exercises.append(cleaned)

    # remove an exercise
    def remove_exercise(self, exercise_name: str) -> bool:
        if exercise_name in self.exercises:
            self.exercises.remove(exercise_name)
            return True
        return False

    # update difficulty
    def update_diffiulty(self, new_level: str) -> None:
        self.difficulty = new_level.strip().capitalize()
    
    # add it into dictionary
    def to_dict(self) -> dict:
        return {
            'plan_id': self.plan_id,
            'plan_name': self.plan_name,
            'difficulty': self.difficulty,
            'exercises': ';'.join(self.exercises),
        }
