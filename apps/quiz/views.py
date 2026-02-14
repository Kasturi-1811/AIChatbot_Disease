from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
from django.utils.translation import gettext_lazy as _


# -------------------------------
# Question Bank (Add 50 each)
# -------------------------------

QUIZ_QUESTIONS = {
    

        "nutrition": [

{"question": _("Which vitamin is produced when skin is exposed to sunlight?"),
"options":[
    _("Vitamin A"),
    _("Vitamin D"),
    _("Vitamin C"),
    _("Vitamin K")
],
"correct":1,
"explanation": _("Vitamin D is synthesized through sunlight exposure.")},

{"question": _("Which nutrient is the main source of energy for the body?"),
"options":[
    _("Protein"),
    _("Carbohydrates"),
    _("Vitamins"),
    _("Minerals")
],
"correct":1,
"explanation": _("Carbohydrates are the body's primary energy source.")},

{"question": _("Which mineral is essential for oxygen transport in blood?"),
"options":[
    _("Iron"),
    _("Calcium"),
    _("Magnesium"),
    _("Potassium")
],
"correct":0,
"explanation": _("Iron helps form hemoglobin which carries oxygen.")},

{"question": _("Which food is highest in protein?"),
"options":[
    _("Rice"),
    _("Eggs"),
    _("Butter"),
    _("Sugar")
],
"correct":1,
"explanation": _("Eggs are a rich source of protein.")},

{"question": _("Which vitamin helps with vision?"),
"options":[
    _("Vitamin A"),
    _("Vitamin B12"),
    _("Vitamin C"),
    _("Vitamin E")
],
"correct":0,
"explanation": _("Vitamin A supports healthy vision.")},

{"question": _("Which nutrient helps build muscles?"),
"options":[
    _("Protein"),
    _("Fat"),
    _("Fiber"),
    _("Sugar")
],
"correct":0,
"explanation": _("Protein repairs and builds muscle tissue.")},

{"question": _("Which is a healthy fat source?"),
"options":[
    _("Fried chips"),
    _("Olive oil"),
    _("Butter"),
    _("Processed snacks")
],
"correct":1,
"explanation": _("Olive oil contains healthy monounsaturated fats.")},

{"question": _("Fiber mainly helps in?"),
"options":[
    _("Digestion"),
    _("Breathing"),
    _("Vision"),
    _("Hearing")
],
"correct":0,
"explanation": _("Fiber improves digestion and prevents constipation.")},

{"question": _("Which fruit is rich in Vitamin C?"),
"options":[
    _("Orange"),
    _("Banana"),
    _("Apple"),
    _("Rice")
],
"correct":0,
"explanation": _("Oranges are high in Vitamin C.")},

{"question": _("Too much sugar can lead to?"),
"options":[
    _("Strong bones"),
    _("Diabetes"),
    _("Better sleep"),
    _("More vitamins")
],
"correct":1,
"explanation": _("Excess sugar intake increases diabetes risk.")},

{"question": _("Which mineral strengthens bones?"),
"options":[
    _("Iron"),
    _("Calcium"),
    _("Sodium"),
    _("Zinc")
],
"correct":1,
"explanation": _("Calcium builds strong bones and teeth.")},

{"question": _("Water helps regulate?"),
"options":[
    _("Body temperature"),
    _("Hair color"),
    _("Eye color"),
    _("Height")
],
"correct":0,
"explanation": _("Water regulates body temperature.")},

{"question": _("Balanced diet includes?"),
"options":[
    _("Only protein"),
    _("Only fats"),
    _("All nutrients"),
    _("Only carbs")
],
"correct":2,
"explanation": _("A balanced diet includes all essential nutrients.")},

{"question": _("Which is whole grain?"),
"options":[
    _("White bread"),
    _("Brown rice"),
    _("Candy"),
    _("Soda")
],
"correct":1,
"explanation": _("Brown rice is a whole grain.")},

{"question": _("Which vitamin supports immunity?"),
"options":[
    _("Vitamin C"),
    _("Vitamin K"),
    _("Vitamin D"),
    _("Vitamin B")
],
"correct":0,
"explanation": _("Vitamin C boosts immunity.")},

{"question": _("Overeating can cause?"),
"options":[
    _("Obesity"),
    _("Stronger bones"),
    _("Better vision"),
    _("Hair growth")
],
"correct":0,
"explanation": _("Overeating leads to weight gain and obesity.")},

{"question": _("Which is a dairy product?"),
"options":[
    _("Milk"),
    _("Apple"),
    _("Rice"),
    _("Carrot")
],
"correct":0,
"explanation": _("Milk is a dairy product rich in calcium.")},

{"question": _("Which food is high in fiber?"),
"options":[
    _("Vegetables"),
    _("Candy"),
    _("Butter"),
    _("Oil")
],
"correct":0,
"explanation": _("Vegetables are rich in fiber.")},

{"question": _("Salt mainly contains?"),
"options":[
    _("Sodium"),
    _("Iron"),
    _("Protein"),
    _("Fiber")
],
"correct":0,
"explanation": _("Salt contains sodium.")},

{"question": _("Too much salt causes?"),
"options":[
    _("Low BP"),
    _("High BP"),
    _("Better sleep"),
    _("Strong teeth")
],
"correct":1,
"explanation": _("Excess sodium increases blood pressure.")},



    ],

    "fitness": [

{
"question": _("How many minutes of moderate exercise is recommended per week?"),
"options": [
    _("60 minutes"),
    _("90 minutes"),
    _("150 minutes"),
    _("300 minutes")
],
"correct": 2,
"explanation": _("WHO recommends at least 150 minutes of moderate exercise per week.")
},

{
"question": _("Which exercise mainly improves cardiovascular endurance?"),
"options": [
    _("Weight lifting"),
    _("Running"),
    _("Plank"),
    _("Stretching")
],
"correct": 1,
"explanation": _("Running strengthens the heart and improves stamina.")
},

{
"question": _("Which muscle group is targeted in squats?"),
"options": [
    _("Chest"),
    _("Shoulders"),
    _("Legs"),
    _("Arms")
],
"correct": 2,
"explanation": _("Squats primarily target quadriceps, hamstrings, and glutes.")
},

{
"question": _("What is the main benefit of strength training?"),
"options": [
    _("Flexibility"),
    _("Muscle growth"),
    _("Better eyesight"),
    _("Hair growth")
],
"correct": 1,
"explanation": _("Strength training increases muscle mass and strength.")
},

{
"question": _("Which exercise is best for core strength?"),
"options": [
    _("Push-ups"),
    _("Plank"),
    _("Cycling"),
    _("Walking")
],
"correct": 1,
"explanation": _("Planks engage multiple core muscles.")
},

{
"question": _("How long should you warm up before exercise?"),
"options": [
    _("1 minute"),
    _("5-10 minutes"),
    _("30 minutes"),
    _("No need")
],
"correct": 1,
"explanation": _("A 5–10 minute warm-up prepares muscles and reduces injury risk.")
},

{
"question": _("Which nutrient helps muscle recovery?"),
"options": [
    _("Protein"),
    _("Sugar"),
    _("Salt"),
    _("Fiber")
],
"correct": 0,
"explanation": _("Protein repairs and builds muscle tissue.")
},

{
"question": _("What does BMI stand for?"),
"options": [
    _("Body Mass Index"),
    _("Body Muscle Intake"),
    _("Basic Mass Indicator"),
    _("Body Movement Index")
],
"correct": 0,
"explanation": _("BMI stands for Body Mass Index.")
},

{
"question": _("Which exercise improves flexibility?"),
"options": [
    _("Yoga"),
    _("Deadlift"),
    _("Bench press"),
    _("Sprint")
],
"correct": 0,
"explanation": _("Yoga enhances flexibility and balance.")
},

{
"question": _("Rest days are important because they help:"),
"options": [
    _("Lose weight faster"),
    _("Muscle recovery"),
    _("Sleep less"),
    _("Avoid hydration")
],
"correct": 1,
"explanation": _("Muscles repair and grow during rest.")
},

{
"question": _("What is a common sign of overtraining?"),
"options": [
    _("Improved performance"),
    _("Constant fatigue"),
    _("Better sleep"),
    _("More energy")
],
"correct": 1,
"explanation": _("Overtraining causes fatigue and decreased performance.")
},

{
"question": _("Which exercise strengthens the chest?"),
"options": [
    _("Push-ups"),
    _("Squats"),
    _("Lunges"),
    _("Crunches")
],
"correct": 0,
"explanation": _("Push-ups target chest muscles.")
},

{
"question": _("Hydration during workouts helps to:"),
"options": [
    _("Increase injuries"),
    _("Maintain performance"),
    _("Reduce oxygen"),
    _("Increase cramps")
],
"correct": 1,
"explanation": _("Water prevents dehydration and maintains performance.")
},

{
"question": _("HIIT stands for:"),
"options": [
    _("High Intensity Interval Training"),
    _("Heavy Internal Intense Training"),
    _("Healthy Interval Intensive Training"),
    _("High Internal Integrated Training")
],
"correct": 0,
"explanation": _("HIIT means High Intensity Interval Training.")
},

{
"question": _("Which exercise burns the most calories?"),
"options": [
    _("Sleeping"),
    _("Running"),
    _("Reading"),
    _("Meditation")
],
"correct": 1,
"explanation": _("Running burns high calories compared to resting activities.")
},

{
"question": _("What is the ideal rest between strength sets?"),
"options": [
    _("5 seconds"),
    _("30-90 seconds"),
    _("10 minutes"),
    _("No rest")
],
"correct": 1,
"explanation": _("30–90 seconds rest allows muscle recovery.")
},

{
"question": _("Which is a bodyweight exercise?"),
"options": [
    _("Pull-ups"),
    _("Leg press machine"),
    _("Cable row"),
    _("Treadmill incline")
],
"correct": 0,
"explanation": _("Pull-ups use your own body weight.")
},

{
"question": _("Cardio exercises mainly improve:"),
"options": [
    _("Memory"),
    _("Heart health"),
    _("Hair growth"),
    _("Vision")
],
"correct": 1,
"explanation": _("Cardio strengthens heart and lungs.")
},

{
"question": _("Which vitamin supports muscle function?"),
"options": [
    _("Vitamin D"),
    _("Vitamin C"),
    _("Vitamin A"),
    _("Vitamin K")
],
"correct": 0,
"explanation": _("Vitamin D supports muscle and bone function.")
},

{
"question": _("Which activity improves balance?"),
"options": [
    _("Tai Chi"),
    _("Sleeping"),
    _("Watching TV"),
    _("Driving")
],
"correct": 0,
"explanation": _("Tai Chi improves balance and coordination.")
},

{
"question": _("Which muscle is targeted during bicep curls?"),
"options": [
    _("Triceps"),
    _("Biceps"),
    _("Quadriceps"),
    _("Glutes")
],
"correct": 1,
"explanation": _("Bicep curls target the biceps.")
},

{
"question": _("Which exercise is best for leg strength?"),
"options": [
    _("Lunges"),
    _("Crunches"),
    _("Shoulder press"),
    _("Plank")
],
"correct": 0,
"explanation": _("Lunges strengthen leg muscles.")
},

{
"question": _("How often should beginners exercise weekly?"),
"options": [
    _("1 day"),
    _("3-5 days"),
    _("7 days nonstop"),
    _("None")
],
"correct": 1,
"explanation": _("3–5 days per week is ideal for beginners.")
},

{
"question": _("Stretching after workouts helps:"),
"options": [
    _("Reduce flexibility"),
    _("Prevent soreness"),
    _("Increase stress"),
    _("Burn fat")
],
"correct": 1,
"explanation": _("Stretching reduces stiffness and soreness.")
},

{
"question": _("Which exercise strengthens the back?"),
"options": [
    _("Deadlift"),
    _("Crunches"),
    _("Jump rope"),
    _("Cycling")
],
"correct": 0,
"explanation": _("Deadlifts strengthen lower back and posterior chain.")
},

{
"question": _("Which exercise improves coordination?"),
"options": [
    _("Jump rope"),
    _("Sleeping"),
    _("Reading"),
    _("Watching TV")
],
"correct": 0,
"explanation": _("Jump rope improves coordination and agility.")
},

{
"question": _("Proper posture during exercise prevents:"),
"options": [
    _("Muscle gain"),
    _("Injuries"),
    _("Fat loss"),
    _("Energy use")
],
"correct": 1,
"explanation": _("Correct posture reduces injury risk.")
},

{
"question": _("Which exercise targets abdominal muscles?"),
"options": [
    _("Crunches"),
    _("Squats"),
    _("Bench press"),
    _("Lat pulldown")
],
"correct": 0,
"explanation": _("Crunches focus on abdominal muscles.")
},

{
"question": _("Cool down after workout helps:"),
"options": [
    _("Sudden stop"),
    _("Gradual heart rate decrease"),
    _("Increase stress"),
    _("Injury")
],
"correct": 1,
"explanation": _("Cooling down prevents dizziness and supports recovery.")
},

{
"question": _("Which activity builds endurance?"),
"options": [
    _("Long-distance running"),
    _("Short naps"),
    _("Gaming"),
    _("Reading")
],
"correct": 0,
"explanation": _("Long-distance running improves endurance.")
},

{
"question": _("Muscle soreness after workout is called:"),
"options": [
    _("DOMS"),
    _("BMI"),
    _("HIIT"),
    _("ATP")
],
"correct": 0,
"explanation": _("Delayed Onset Muscle Soreness (DOMS) occurs after exercise.")
},

{
"question": _("Which is anaerobic exercise?"),
"options": [
    _("Sprint"),
    _("Walking"),
    _("Jogging"),
    _("Cycling slowly")
],
"correct": 0,
"explanation": _("Sprinting is short-duration high-intensity anaerobic exercise.")
},

{
"question": _("Which mineral prevents muscle cramps?"),
"options": [
    _("Magnesium"),
    _("Iron"),
    _("Zinc"),
    _("Copper")
],
"correct": 0,
"explanation": _("Magnesium helps prevent muscle cramps.")
},

{
"question": _("Which improves lung capacity?"),
"options": [
    _("Swimming"),
    _("Sleeping"),
    _("Driving"),
    _("Reading")
],
"correct": 0,
"explanation": _("Swimming enhances lung function.")
},

{
"question": _("Push-ups primarily work which body part?"),
"options": [
    _("Chest and arms"),
    _("Legs"),
    _("Back only"),
    _("Neck")
],
"correct": 0,
"explanation": _("Push-ups target chest, shoulders, and triceps.")
},

{
"question": _("How much water is recommended daily?"),
"options": [
    _("1 glass"),
    _("2 liters approx"),
    _("500 ml"),
    _("None")
],
"correct": 1,
"explanation": _("Around 2 liters is generally recommended.")
},

{
"question": _("Which exercise helps lose belly fat?"),
"options": [
    _("Overall cardio"),
    _("Only crunches"),
    _("Sleeping"),
    _("Watching TV")
],
"correct": 0,
"explanation": _("Overall fat loss requires cardio and diet.")
},

{
"question": _("Which exercise strengthens shoulders?"),
"options": [
    _("Shoulder press"),
    _("Squats"),
    _("Lunges"),
    _("Crunches")
],
"correct": 0,
"explanation": _("Shoulder press targets deltoid muscles.")
},

{
"question": _("Exercise improves mental health by:"),
"options": [
    _("Reducing stress"),
    _("Increasing stress"),
    _("Reducing oxygen"),
    _("None")
],
"correct": 0,
"explanation": _("Exercise releases endorphins that reduce stress.")
},

{
"question": _("What is flexibility?"),
"options": [
    _("Ability to stretch muscles"),
    _("Running speed"),
    _("Muscle size"),
    _("Fat percentage")
],
"correct": 0,
"explanation": _("Flexibility is the ability of muscles to stretch.")
},

{
"question": _("Which activity improves agility?"),
"options": [
    _("Ladder drills"),
    _("Sleeping"),
    _("Watching TV"),
    _("Reading")
],
"correct": 0,
"explanation": _("Agility drills improve quick movement.")
},

{
"question": _("Which is a compound exercise?"),
"options": [
    _("Squats"),
    _("Bicep curls"),
    _("Wrist curls"),
    _("Neck rolls")
],
"correct": 0,
"explanation": _("Squats use multiple joints and muscles.")
},

{
"question": _("Exercise reduces risk of:"),
"options": [
    _("Heart disease"),
    _("Fitness"),
    _("Energy"),
    _("Strength")
],
"correct": 0,
"explanation": _("Regular exercise lowers heart disease risk.")
},

{
"question": _("Best time to exercise is:"),
"options": [
    _("When consistent"),
    _("Midnight only"),
    _("Never"),
    _("Random")
],
"correct": 0,
"explanation": _("Consistency matters more than time.")
},

{
"question": _("Which helps build stamina?"),
"options": [
    _("Cycling"),
    _("Sleeping"),
    _("Eating junk"),
    _("Skipping water")
],
"correct": 0,
"explanation": _("Cycling improves stamina.")
},

{
"question": _("Protein shakes are mainly for:"),
"options": [
    _("Muscle recovery"),
    _("Hair growth"),
    _("Vision"),
    _("Sleep")
],
"correct": 0,
"explanation": _("Protein supports muscle repair.")
},

{
"question": _("Which reduces injury risk?"),
"options": [
    _("Proper warm-up"),
    _("Skipping warm-up"),
    _("Overtraining"),
    _("No rest")
],
"correct": 0,
"explanation": _("Warm-up prepares muscles for activity.")
},

{
"question": _("Which improves posture?"),
"options": [
    _("Core strengthening"),
    _("Sleeping poorly"),
    _("Slouching"),
    _("None")
],
"correct": 0,
"explanation": _("Strong core improves posture.")
},

{
"question": _("What does progressive overload mean?"),
"options": [
    _("Gradually increasing workout intensity"),
    _("Stopping exercise"),
    _("Reducing effort"),
    _("Sleeping more")
],
"correct": 0,
"explanation": _("Progressive overload increases muscle strength gradually.")
},

{
"question": _("Exercise helps control:"),
"options": [
    _("Blood sugar"),
    _("Hair color"),
    _("Height"),
    _("Eye color")
],
"correct": 0,
"explanation": _("Exercise helps regulate blood sugar levels.")
}

],


    "mental": [

{
    "question": _("What is mental health?"),
    "options": [
        _("The absence of illness"),
        _("Emotional, psychological, and social well-being"),
        _("Physical strength"),
        _("IQ level")
    ],
    "correct": 1,
    "explanation": _("Mental health includes emotional, psychological, and social well-being.")
},

{
    "question": _("Which hormone is commonly known as the stress hormone?"),
    "options": [
        _("Dopamine"),
        _("Serotonin"),
        _("Cortisol"),
        _("Oxytocin")
    ],
    "correct": 2,
    "explanation": _("Cortisol is released during stress.")
},

{
    "question": _("Which activity helps reduce stress?"),
    "options": [
        _("Meditation"),
        _("Overthinking"),
        _("Skipping sleep"),
        _("Isolation")
    ],
    "correct": 0,
    "explanation": _("Meditation helps calm the mind and reduce stress.")
},

{
    "question": _("How many hours of sleep do adults generally need?"),
    "options": [
        _("4-5"),
        _("7-9"),
        _("10-12"),
        _("5-6")
    ],
    "correct": 1,
    "explanation": _("Adults typically need 7-9 hours of sleep.")
},

{
    "question": _("Which condition involves persistent sadness?"),
    "options": [
        _("Depression"),
        _("Anxiety"),
        _("ADHD"),
        _("Phobia")
    ],
    "correct": 0,
    "explanation": _("Depression is characterized by persistent sadness.")
},

{
    "question": _("Which practice improves emotional awareness?"),
    "options": [
        _("Mindfulness"),
        _("Avoidance"),
        _("Anger"),
        _("Denial")
    ],
    "correct": 0,
    "explanation": _("Mindfulness improves emotional awareness.")
},

{
    "question": _("Which neurotransmitter is linked to happiness?"),
    "options": [
        _("Serotonin"),
        _("Adrenaline"),
        _("Insulin"),
        _("Melatonin")
    ],
    "correct": 0,
    "explanation": _("Serotonin helps regulate mood and happiness.")
},

{
    "question": _("Anxiety mainly affects which part of health?"),
    "options": [
        _("Mental"),
        _("Dental"),
        _("Vision"),
        _("Hearing")
    ],
    "correct": 0,
    "explanation": _("Anxiety affects mental and emotional well-being.")
},

{
    "question": _("Which technique helps control panic attacks?"),
    "options": [
        _("Deep breathing"),
        _("Shouting"),
        _("Skipping meals"),
        _("Isolation")
    ],
    "correct": 0,
    "explanation": _("Deep breathing helps regulate panic symptoms.")
},

{
    "question": _("What is burnout?"),
    "options": [
        _("Extreme physical exercise"),
        _("Chronic workplace stress"),
        _("Sleeping disorder"),
        _("Brain injury")
    ],
    "correct": 1,
    "explanation": _("Burnout results from chronic unmanaged stress.")
},

{
    "question": _("Which habit improves mental health?"),
    "options": [
        _("Regular exercise"),
        _("Overworking"),
        _("Neglecting sleep"),
        _("Isolation")
    ],
    "correct": 0,
    "explanation": _("Exercise releases mood-boosting chemicals.")
},

{
    "question": _("What is cognitive behavioral therapy (CBT)?"),
    "options": [
        _("Medication"),
        _("Talk therapy"),
        _("Surgery"),
        _("Diet plan")
    ],
    "correct": 1,
    "explanation": _("CBT is a form of talk therapy.")
},

{
    "question": _("Which disorder involves excessive fear of social situations?"),
    "options": [
        _("Social anxiety"),
        _("Bipolar disorder"),
        _("Schizophrenia"),
        _("OCD")
    ],
    "correct": 0,
    "explanation": _("Social anxiety disorder involves fear of social situations.")
},

{
    "question": _("What does ADHD stand for?"),
    "options": [
        _("Advanced Health Disorder"),
        _("Attention Deficit Hyperactivity Disorder"),
        _("Anxiety Disorder"),
        _("Adult Depression Habit Disorder")
    ],
    "correct": 1,
    "explanation": _("ADHD stands for Attention Deficit Hyperactivity Disorder.")
},

{
    "question": _("Which practice helps emotional regulation?"),
    "options": [
        _("Journaling"),
        _("Suppressing emotions"),
        _("Avoiding people"),
        _("Anger")
    ],
    "correct": 0,
    "explanation": _("Journaling helps process emotions.")
},

{
    "question": _("Which mental illness includes mood swings between high and low?"),
    "options": [
        _("Bipolar disorder"),
        _("Depression"),
        _("Anxiety"),
        _("Phobia")
    ],
    "correct": 0,
    "explanation": _("Bipolar disorder involves extreme mood swings.")
},

{
    "question": _("Which chemical is known as the 'love hormone'?"),
    "options": [
        _("Oxytocin"),
        _("Cortisol"),
        _("Insulin"),
        _("Adrenaline")
    ],
    "correct": 0,
    "explanation": _("Oxytocin is associated with bonding.")
},

{
    "question": _("What is a common symptom of anxiety?"),
    "options": [
        _("Rapid heartbeat"),
        _("Better memory"),
        _("Improved focus"),
        _("Calmness")
    ],
    "correct": 0,
    "explanation": _("Anxiety often causes rapid heartbeat.")
},

{
    "question": _("Which factor improves mental resilience?"),
    "options": [
        _("Strong support system"),
        _("Isolation"),
        _("Sleep deprivation"),
        _("Stress")
    ],
    "correct": 0,
    "explanation": _("Support systems improve resilience.")
},

{
    "question": _("What is mindfulness?"),
    "options": [
        _("Living in the present moment"),
        _("Overthinking"),
        _("Ignoring feelings"),
        _("Worrying about future")
    ],
    "correct": 0,
    "explanation": _("Mindfulness means focusing on the present.")
},

{
    "question": _("What is insomnia?"),
    "options": [
        _("Sleep disorder"),
        _("Eating disorder"),
        _("Memory issue"),
        _("Vision issue")
    ],
    "correct": 0,
    "explanation": _("Insomnia is difficulty sleeping.")
},

{
    "question": _("Which is a healthy coping mechanism?"),
    "options": [
        _("Talking to friends"),
        _("Substance abuse"),
        _("Isolation"),
        _("Anger")
    ],
    "correct": 0,
    "explanation": _("Talking helps process emotions.")
},

{
    "question": _("Which mental condition involves repetitive behaviors?"),
    "options": [
        _("OCD"),
        _("Depression"),
        _("Phobia"),
        _("Burnout")
    ],
    "correct": 0,
    "explanation": _("OCD involves obsessions and compulsions.")
},

{
    "question": _("Meditation mainly improves?"),
    "options": [
        _("Focus and calmness"),
        _("Anger"),
        _("Stress"),
        _("Fear")
    ],
    "correct": 0,
    "explanation": _("Meditation improves calmness and focus.")
},

{
    "question": _("Which disorder includes hallucinations?"),
    "options": [
        _("Schizophrenia"),
        _("Anxiety"),
        _("Depression"),
        _("Insomnia")
    ],
    "correct": 0,
    "explanation": _("Schizophrenia can involve hallucinations.")
},

{
    "question": _("Which activity releases endorphins?"),
    "options": [
        _("Exercise"),
        _("Skipping sleep"),
        _("Stress"),
        _("Isolation")
    ],
    "correct": 0,
    "explanation": _("Exercise releases endorphins.")
},

{
    "question": _("Emotional intelligence means?"),
    "options": [
        _("Understanding and managing emotions"),
        _("High IQ"),
        _("Physical strength"),
        _("Ignoring emotions")
    ],
    "correct": 0,
    "explanation": _("Emotional intelligence is managing emotions effectively.")
},

{
    "question": _("Chronic stress may lead to?"),
    "options": [
        _("Mental health disorders"),
        _("Better sleep"),
        _("Stronger memory"),
        _("Improved mood")
    ],
    "correct": 0,
    "explanation": _("Chronic stress harms mental health.")
},

{
    "question": _("Which therapy involves group discussion?"),
    "options": [
        _("Group therapy"),
        _("Surgery"),
        _("Medication"),
        _("Diet therapy")
    ],
    "correct": 0,
    "explanation": _("Group therapy involves shared discussions.")
},

{
    "question": _("Which disorder causes intense mood sadness lasting weeks?"),
    "options": [
        _("Major depression"),
        _("Phobia"),
        _("ADHD"),
        _("OCD")
    ],
    "correct": 0,
    "explanation": _("Major depression lasts weeks or longer.")
},

{
    "question": _("Which is a sign of good mental health?"),
    "options": [
        _("Ability to cope with stress"),
        _("Constant anger"),
        _("Isolation"),
        _("Sleep deprivation")
    ],
    "correct": 0,
    "explanation": _("Coping well with stress shows good mental health.")
},

{
    "question": _("Which mental illness affects eating habits?"),
    "options": [
        _("Eating disorders"),
        _("Phobia"),
        _("Burnout"),
        _("Insomnia")
    ],
    "correct": 0,
    "explanation": _("Eating disorders affect food behavior.")
},

{
    "question": _("Self-care includes?"),
    "options": [
        _("Healthy sleep routine"),
        _("Overworking"),
        _("Skipping meals"),
        _("Ignoring stress")
    ],
    "correct": 0,
    "explanation": _("Healthy routines support mental health.")
},

{
    "question": _("Which technique reduces negative thoughts?"),
    "options": [
        _("Cognitive restructuring"),
        _("Isolation"),
        _("Anger"),
        _("Stress")
    ],
    "correct": 0,
    "explanation": _("Cognitive restructuring changes negative thought patterns.")
},

{
    "question": _("Which age group can experience mental health issues?"),
    "options": [
        _("All ages"),
        _("Only adults"),
        _("Only children"),
        _("Only elderly")
    ],
    "correct": 0,
    "explanation": _("Mental health issues can affect all ages.")
},

{
    "question": _("Which practice helps manage anxiety?"),
    "options": [
        _("Deep breathing"),
        _("Skipping meals"),
        _("Overthinking"),
        _("Avoidance")
    ],
    "correct": 0,
    "explanation": _("Breathing exercises calm anxiety.")
},

{
    "question": _("Post-traumatic stress disorder (PTSD) occurs after?"),
    "options": [
        _("Traumatic events"),
        _("Exercise"),
        _("Diet change"),
        _("Vacation")
    ],
    "correct": 0,
    "explanation": _("PTSD follows traumatic events.")
},

{
    "question": _("Positive thinking can?"),
    "options": [
        _("Improve mental well-being"),
        _("Increase stress"),
        _("Cause insomnia"),
        _("Cause anxiety")
    ],
    "correct": 0,
    "explanation": _("Positive thinking supports mental health.")
},

{
    "question": _("Which is a professional mental health provider?"),
    "options": [
        _("Psychologist"),
        _("Chef"),
        _("Driver"),
        _("Engineer")
    ],
    "correct": 0,
    "explanation": _("Psychologists specialize in mental health.")
},

{
    "question": _("What is emotional burnout?"),
    "options": [
        _("Emotional exhaustion"),
        _("Happiness"),
        _("Energy boost"),
        _("Calmness")
    ],
    "correct": 0,
    "explanation": _("Burnout involves emotional exhaustion.")
},

{
    "question": _("Which habit improves focus?"),
    "options": [
        _("Adequate sleep"),
        _("Late-night scrolling"),
        _("Skipping meals"),
        _("Stress")
    ],
    "correct": 0,
    "explanation": _("Sleep improves concentration.")
},

{
    "question": _("Which is NOT a healthy coping strategy?"),
    "options": [
        _("Substance abuse"),
        _("Exercise"),
        _("Meditation"),
        _("Talking")
    ],
    "correct": 0,
    "explanation": _("Substance abuse worsens mental health.")
},

{
    "question": _("Which is a relaxation method?"),
    "options": [
        _("Yoga"),
        _("Anger"),
        _("Isolation"),
        _("Overthinking")
    ],
    "correct": 0,
    "explanation": _("Yoga promotes relaxation.")
},

{
    "question": _("Loneliness can affect?"),
    "options": [
        _("Mental and physical health"),
        _("Only teeth"),
        _("Only vision"),
        _("Only hair")
    ],
    "correct": 0,
    "explanation": _("Loneliness impacts overall health.")
},

{
    "question": _("Which is a symptom of depression?"),
    "options": [
        _("Loss of interest"),
        _("High energy"),
        _("Excitement"),
        _("Confidence boost")
    ],
    "correct": 0,
    "explanation": _("Loss of interest is a depression symptom.")
},

{
    "question": _("Which activity builds self-esteem?"),
    "options": [
        _("Achieving goals"),
        _("Constant criticism"),
        _("Isolation"),
        _("Neglect")
    ],
    "correct": 0,
    "explanation": _("Achievement builds confidence.")
},

{
    "question": _("Mental health awareness helps?"),
    "options": [
        _("Reduce stigma"),
        _("Increase fear"),
        _("Cause stress"),
        _("Promote isolation")
    ],
    "correct": 0,
    "explanation": _("Awareness reduces stigma.")
},

{
    "question": _("Which improves brain function?"),
    "options": [
        _("Regular exercise"),
        _("Sleep deprivation"),
        _("Stress"),
        _("Isolation")
    ],
    "correct": 0,
    "explanation": _("Exercise boosts brain function.")
},

{
    "question": _("Seeking help for mental health is?"),
    "options": [
        _("A sign of strength"),
        _("Weakness"),
        _("Unnecessary"),
        _("Embarrassing")
    ],
    "correct": 0,
    "explanation": _("Seeking help shows strength.")
}

],
"disease_prevention": [

{
"question": _("What is the most effective way to prevent the spread of infectious diseases?"),
"options": [
    _("Wearing perfume"),
    _("Regular handwashing"),
    _("Drinking cold water"),
    _("Sleeping less")
],
"correct": 1,
"explanation": _("Regular handwashing removes germs and prevents transmission.")
},

{
"question": _("Vaccines help prevent diseases by:"),
"options": [
    _("Killing all bacteria"),
    _("Boosting natural immunity"),
    _("Increasing fever"),
    _("Replacing blood cells")
],
"correct": 1,
"explanation": _("Vaccines stimulate the immune system to recognize and fight infections.")
},

{
"question": _("How often should adults get a general health check-up?"),
"options": [
    _("Every 10 years"),
    _("Only when sick"),
    _("Once a year"),
    _("Never")
],
"correct": 2,
"explanation": _("Annual health check-ups help detect diseases early.")
},

{
"question": _("Which of the following helps prevent heart disease?"),
"options": [
    _("Smoking"),
    _("High salt diet"),
    _("Regular exercise"),
    _("Excess sugar intake")
],
"correct": 2,
"explanation": _("Regular physical activity reduces heart disease risk.")
},

{
"question": _("Which vitamin strengthens the immune system?"),
"options": [
    _("Vitamin C"),
    _("Vitamin K"),
    _("Vitamin B12"),
    _("Vitamin A")
],
"correct": 0,
"explanation": _("Vitamin C supports immune defense.")
},

{
"question": _("Using mosquito nets helps prevent:"),
"options": [
    _("Diabetes"),
    _("Malaria"),
    _("Asthma"),
    _("Arthritis")
],
"correct": 1,
"explanation": _("Mosquito nets prevent malaria transmission.")
},

{
"question": _("Which disease can be prevented by HPV vaccination?"),
"options": [
    _("Lung cancer"),
    _("Cervical cancer"),
    _("Diabetes"),
    _("Tuberculosis")
],
"correct": 1,
"explanation": _("HPV vaccine helps prevent cervical cancer.")
},

{
"question": _("Quitting smoking reduces risk of:"),
"options": [
    _("Lung cancer"),
    _("Flu"),
    _("Fractures"),
    _("Migraine")
],
"correct": 0,
"explanation": _("Smoking is a major cause of lung cancer.")
},

{
"question": _("Safe drinking water prevents:"),
"options": [
    _("Malaria"),
    _("Cholera"),
    _("Cancer"),
    _("Arthritis")
],
"correct": 1,
"explanation": _("Contaminated water spreads cholera.")
},

{
"question": _("Which test helps in early detection of breast cancer?"),
"options": [
    _("ECG"),
    _("Mammogram"),
    _("X-ray"),
    _("Blood sugar test")
],
"correct": 1,
"explanation": _("Mammograms detect early breast cancer.")
},

{
"question": _("Maintaining healthy weight prevents:"),
"options": [
    _("Obesity-related diseases"),
    _("Infections"),
    _("Cold"),
    _("Fractures")
],
"correct": 0,
"explanation": _("Healthy weight reduces diabetes and heart risk.")
},

{
"question": _("Using sunscreen prevents:"),
"options": [
    _("Skin cancer"),
    _("Cold"),
    _("Flu"),
    _("Asthma")
],
"correct": 0,
"explanation": _("Sunscreen protects against harmful UV rays.")
},

{
"question": _("Which disease spreads through airborne droplets?"),
"options": [
    _("Tuberculosis"),
    _("Diabetes"),
    _("Hypertension"),
    _("Arthritis")
],
"correct": 0,
"explanation": _("TB spreads through air.")
},

{
"question": _("Brushing teeth daily prevents:"),
"options": [
    _("Tooth decay"),
    _("Diabetes"),
    _("Asthma"),
    _("Heart attack")
],
"correct": 0,
"explanation": _("Oral hygiene prevents cavities.")
},

{
"question": _("Which screening detects colon cancer early?"),
"options": [
    _("Colonoscopy"),
    _("MRI"),
    _("CT scan"),
    _("ECG")
],
"correct": 0,
"explanation": _("Colonoscopy detects early colon cancer.")
},

{
"question": _("Physical activity reduces risk of:"),
"options": [
    _("Type 2 diabetes"),
    _("Cold"),
    _("Fracture"),
    _("Injury")
],
"correct": 0,
"explanation": _("Exercise improves insulin sensitivity.")
},

{
"question": _("Balanced diet helps prevent:"),
"options": [
    _("Malnutrition"),
    _("Fractures"),
    _("Injury"),
    _("Burns")
],
"correct": 0,
"explanation": _("Balanced diet provides essential nutrients.")
},

{
"question": _("Wearing masks helps prevent:"),
"options": [
    _("COVID-19"),
    _("Diabetes"),
    _("Cancer"),
    _("Hypertension")
],
"correct": 0,
"explanation": _("Masks reduce virus transmission.")
},

{
"question": _("High blood pressure can be prevented by:"),
"options": [
    _("Reducing salt intake"),
    _("Eating junk food"),
    _("Smoking"),
    _("Stress")
],
"correct": 0,
"explanation": _("Low salt diet controls blood pressure.")
},

{
"question": _("Which vaccine prevents tuberculosis?"),
"options": [
    _("BCG"),
    _("MMR"),
    _("Polio"),
    _("Hepatitis B")
],
"correct": 0,
"explanation": _("BCG vaccine protects against TB.")
},

{
"question": _("Proper sanitation prevents:"),
"options": [
    _("Diarrheal diseases"),
    _("Asthma"),
    _("Fractures"),
    _("Cancer")
],
"correct": 0,
"explanation": _("Sanitation reduces infection spread.")
},

{
"question": _("Regular eye checkups help prevent:"),
"options": [
    _("Vision loss"),
    _("Flu"),
    _("Asthma"),
    _("Diabetes")
],
"correct": 0,
"explanation": _("Early detection prevents vision damage.")
},

{
"question": _("Which disease is prevented by insulin control?"),
"options": [
    _("Diabetes complications"),
    _("Cold"),
    _("Flu"),
    _("Migraine")
],
"correct": 0,
"explanation": _("Blood sugar control prevents complications.")
},

{
"question": _("Hepatitis B spreads through:"),
"options": [
    _("Blood contact"),
    _("Air"),
    _("Sweat"),
    _("Sound")
],
"correct": 0,
"explanation": _("Hepatitis B spreads through infected blood.")
},

{
"question": _("Avoiding junk food reduces risk of:"),
"options": [
    _("Obesity"),
    _("Cold"),
    _("Injury"),
    _("Burns")
],
"correct": 0,
"explanation": _("Junk food increases obesity risk.")
},

{
"question": _("Which test checks blood sugar?"),
"options": [
    _("Glucose test"),
    _("ECG"),
    _("MRI"),
    _("X-ray")
],
"correct": 0,
"explanation": _("Glucose test measures blood sugar levels.")
},

{
"question": _("Early cancer detection improves:"),
"options": [
    _("Survival rate"),
    _("Infection rate"),
    _("Pain"),
    _("Fever")
],
"correct": 0,
"explanation": _("Early detection increases survival.")
},

{
"question": _("Which habit prevents liver disease?"),
"options": [
    _("Limiting alcohol"),
    _("Smoking"),
    _("Skipping meals"),
    _("Sleeping less")
],
"correct": 0,
"explanation": _("Alcohol damages liver.")
},

{
"question": _("Flu vaccine should be taken:"),
"options": [
    _("Yearly"),
    _("Once in lifetime"),
    _("Never"),
    _("Every month")
],
"correct": 0,
"explanation": _("Flu strains change yearly.")
},

{
"question": _("Safe sex practices prevent:"),
"options": [
    _("STDs"),
    _("Cold"),
    _("Migraine"),
    _("Asthma")
],
"correct": 0,
"explanation": _("Protection reduces STD transmission.")
},

{
"question": _("Drinking adequate water prevents:"),
"options": [
    _("Dehydration"),
    _("Cold"),
    _("Cancer"),
    _("TB")
],
"correct": 0,
"explanation": _("Water maintains hydration.")
},

{
"question": _("Stress management helps prevent:"),
"options": [
    _("Heart disease"),
    _("Fracture"),
    _("Burns"),
    _("Cold")
],
"correct": 0,
"explanation": _("Chronic stress affects heart health.")
},

{
"question": _("Avoiding smoking prevents:"),
"options": [
    _("COPD"),
    _("Cold"),
    _("Fever"),
    _("Migraine")
],
"correct": 0,
"explanation": _("Smoking causes lung diseases.")
},

{
"question": _("Which test detects cervical cancer?"),
"options": [
    _("Pap smear"),
    _("MRI"),
    _("CT"),
    _("ECG")
],
"correct": 0,
"explanation": _("Pap smear detects abnormal cervical cells.")
},

{
"question": _("Healthy sleep prevents:"),
"options": [
    _("Weakened immunity"),
    _("Cold"),
    _("Injury"),
    _("Burns")
],
"correct": 0,
"explanation": _("Sleep boosts immunity.")
},

{
"question": _("Regular dental visits prevent:"),
"options": [
    _("Gum disease"),
    _("Diabetes"),
    _("Cancer"),
    _("Cold")
],
"correct": 0,
"explanation": _("Dentists detect oral problems early.")
},

{
"question": _("Which disease is prevented by measles vaccine?"),
"options": [
    _("Measles"),
    _("TB"),
    _("Cancer"),
    _("Asthma")
],
"correct": 0,
"explanation": _("MMR vaccine protects from measles.")
},

{
"question": _("Avoiding contaminated food prevents:"),
"options": [
    _("Food poisoning"),
    _("Diabetes"),
    _("Asthma"),
    _("Fracture")
],
"correct": 0,
"explanation": _("Contaminated food spreads infection.")
},

{
"question": _("Routine blood pressure checks prevent:"),
"options": [
    _("Stroke"),
    _("Cold"),
    _("Migraine"),
    _("Burns")
],
"correct": 0,
"explanation": _("High BP leads to stroke.")
},

{
"question": _("Which helps prevent osteoporosis?"),
"options": [
    _("Calcium intake"),
    _("Smoking"),
    _("Alcohol"),
    _("Junk food")
],
"correct": 0,
"explanation": _("Calcium strengthens bones.")
},

{
"question": _("Regular physical checkups help in:"),
"options": [
    _("Early diagnosis"),
    _("Late detection"),
    _("Infection spread"),
    _("Weight gain")
],
"correct": 0,
"explanation": _("Early detection improves treatment.")
},

{
"question": _("Hand sanitizers should contain at least:"),
"options": [
    _("60% alcohol"),
    _("10% sugar"),
    _("5% salt"),
    _("1% water")
],
"correct": 0,
"explanation": _("60% alcohol kills germs effectively.")
},

{
"question": _("Which disease spreads via contaminated needles?"),
"options": [
    _("HIV"),
    _("Cold"),
    _("Asthma"),
    _("Fracture")
],
"correct": 0,
"explanation": _("HIV spreads through infected blood.")
},

{
"question": _("Healthy cholesterol levels prevent:"),
"options": [
    _("Heart attack"),
    _("Cold"),
    _("Burns"),
    _("Fracture")
],
"correct": 0,
"explanation": _("High cholesterol causes heart disease.")
},

{
"question": _("Proper ventilation reduces:"),
"options": [
    _("Airborne infection"),
    _("Diabetes"),
    _("Hypertension"),
    _("Fractures")
],
"correct": 0,
"explanation": _("Fresh air reduces germ concentration.")
},

{
"question": _("Avoiding processed sugar reduces risk of:"),
"options": [
    _("Diabetes"),
    _("Cold"),
    _("Asthma"),
    _("Injury")
],
"correct": 0,
"explanation": _("Sugar increases insulin resistance.")
},

{
"question": _("Regular exercise improves:"),
"options": [
    _("Immune function"),
    _("Virus growth"),
    _("Stress level"),
    _("Fatigue")
],
"correct": 0,
"explanation": _("Exercise strengthens immunity.")
},

{
"question": _("Early HIV detection improves:"),
"options": [
    _("Treatment success"),
    _("Infection rate"),
    _("Pain"),
    _("Cold")
],
"correct": 0,
"explanation": _("Early treatment improves life expectancy.")
},

{
"question": _("Which disease is prevented by polio vaccine?"),
"options": [
    _("Polio"),
    _("Cancer"),
    _("TB"),
    _("Diabetes")
],
"correct": 0,
"explanation": _("Polio vaccine protects against paralysis.")
},

{
"question": _("Maintaining hygiene prevents:"),
"options": [
    _("Many infections"),
    _("Bone fracture"),
    _("Burns"),
    _("Migraine")
],
"correct": 0,
"explanation": _("Good hygiene blocks infection spread.")
}

],
"general": [

{"question": _("How many hours of sleep do adults need daily?"),
"options": [
    _("4-5"),
    _("5-6"),
    _("7-9"),
    _("10-12")
],
"correct": 2,
"explanation": _("Adults need 7-9 hours of sleep for proper health.")},

{"question": _("Drinking enough water helps to:"),
"options": [
    _("Cause fatigue"),
    _("Improve digestion"),
    _("Reduce oxygen"),
    _("Increase stress")
],
"correct": 1,
"explanation": _("Hydration improves digestion and overall health.")},

{"question": _("Which organ pumps blood through the body?"),
"options": [
    _("Lungs"),
    _("Brain"),
    _("Heart"),
    _("Kidney")
],
"correct": 2,
"explanation": _("The heart pumps blood throughout the body.")},

{"question": _("What is a normal body temperature?"),
"options": [
    _("35°C"),
    _("37°C"),
    _("40°C"),
    _("39°C")
],
"correct": 1,
"explanation": _("Normal body temperature is approximately 37°C.")},

{"question": _("Which nutrient helps build muscles?"),
"options": [
    _("Protein"),
    _("Sugar"),
    _("Salt"),
    _("Fat")
],
"correct": 0,
"explanation": _("Protein helps in muscle repair and growth.")},

{"question": _("BMI stands for:"),
"options": [
    _("Body Mass Index"),
    _("Body Muscle Indicator"),
    _("Basic Metabolic Intake"),
    _("Blood Measure Index")
],
"correct": 0,
"explanation": _("BMI means Body Mass Index.")},

{"question": _("Regular exercise helps reduce:"),
"options": [
    _("Energy"),
    _("Stress"),
    _("Sleep"),
    _("Immunity")
],
"correct": 1,
"explanation": _("Exercise reduces stress levels.")},

{"question": _("Which vitamin improves vision?"),
"options": [
    _("Vitamin A"),
    _("Vitamin B"),
    _("Vitamin C"),
    _("Vitamin D")
],
"correct": 0,
"explanation": _("Vitamin A supports eye health.")},

{"question": _("Smoking mainly damages which organ?"),
"options": [
    _("Heart"),
    _("Liver"),
    _("Lungs"),
    _("Brain")
],
"correct": 2,
"explanation": _("Smoking primarily damages the lungs.")},

{"question": _("A balanced diet includes:"),
"options": [
    _("Only carbohydrates"),
    _("Only proteins"),
    _("All nutrients"),
    _("Only fats")
],
"correct": 2,
"explanation": _("A balanced diet includes all essential nutrients.")},

{"question": _("Which test measures blood sugar?"),
"options": [
    _("ECG"),
    _("Blood Glucose Test"),
    _("X-ray"),
    _("MRI")
],
"correct": 1,
"explanation": _("Blood glucose test measures sugar levels.")},

{"question": _("Hypertension means:"),
"options": [
    _("Low sugar"),
    _("High blood pressure"),
    _("Low BP"),
    _("High sugar")
],
"correct": 1,
"explanation": _("Hypertension means high blood pressure.")},

{"question": _("Which mineral prevents anemia?"),
"options": [
    _("Iron"),
    _("Calcium"),
    _("Sodium"),
    _("Zinc")
],
"correct": 0,
"explanation": _("Iron deficiency causes anemia.")},

{"question": _("Excess sugar intake may lead to:"),
"options": [
    _("Diabetes"),
    _("Improved vision"),
    _("Stronger bones"),
    _("Better sleep")
],
"correct": 0,
"explanation": _("Too much sugar increases diabetes risk.")},

{"question": _("Which habit improves mental health?"),
"options": [
    _("Meditation"),
    _("Smoking"),
    _("Overeating"),
    _("Alcohol abuse")
],
"correct": 0,
"explanation": _("Meditation improves mental wellness.")},

{"question": _("Cholesterol mainly affects:"),
"options": [
    _("Bones"),
    _("Heart"),
    _("Hair"),
    _("Skin")
],
"correct": 1,
"explanation": _("High cholesterol affects heart health.")},

{"question": _("Vaccines help by:"),
"options": [
    _("Causing disease"),
    _("Preventing disease"),
    _("Reducing sleep"),
    _("Lowering oxygen")
],
"correct": 1,
"explanation": _("Vaccines prevent diseases.")},

{"question": _("Hand washing prevents:"),
"options": [
    _("Infections"),
    _("Sleep"),
    _("Hunger"),
    _("Stress")
],
"correct": 0,
"explanation": _("Hand washing reduces infection risk.")},

{"question": _("Stress can affect:"),
"options": [
    _("Only brain"),
    _("Only heart"),
    _("Whole body"),
    _("Nothing")
],
"correct": 2,
"explanation": _("Stress impacts the whole body.")},

{"question": _("Fiber helps in:"),
"options": [
    _("Digestion"),
    _("Breathing"),
    _("Hearing"),
    _("Vision")
],
"correct": 0,
"explanation": _("Fiber improves digestion.")},

{"question": _("Obesity increases risk of:"),
"options": [
    _("Heart disease"),
    _("Stronger immunity"),
    _("Better sleep"),
    _("Improved vision")
],
"correct": 0,
"explanation": _("Obesity increases heart disease risk.")},

{"question": _("Which is good for heart health?"),
"options": [
    _("Fried food"),
    _("Exercise"),
    _("Smoking"),
    _("Sugary drinks")
],
"correct": 1,
"explanation": _("Exercise strengthens the heart.")},

{"question": _("Water makes up about what % of body?"),
"options": [
    _("20%"),
    _("40%"),
    _("60%"),
    _("90%")
],
"correct": 2,
"explanation": _("About 60% of the body is water.")},

{"question": _("Which habit boosts immunity?"),
"options": [
    _("Proper sleep"),
    _("Smoking"),
    _("Alcohol abuse"),
    _("Skipping meals")
],
"correct": 0,
"explanation": _("Good sleep strengthens immunity.")},

{"question": _("Which organ filters blood?"),
"options": [
    _("Heart"),
    _("Kidney"),
    _("Lung"),
    _("Brain")
],
"correct": 1,
"explanation": _("Kidneys filter waste from blood.")},

{"question": _("Regular health checkups help to:"),
"options": [
    _("Detect diseases early"),
    _("Cause disease"),
    _("Reduce height"),
    _("Increase stress")
],
"correct": 0,
"explanation": _("Early detection improves treatment.")},

{"question": _("Too much salt may cause:"),
"options": [
    _("Low BP"),
    _("High BP"),
    _("Low sugar"),
    _("Anemia")
],
"correct": 1,
"explanation": _("High salt increases blood pressure.")},

{"question": _("Sun exposure gives:"),
"options": [
    _("Vitamin D"),
    _("Vitamin C"),
    _("Iron"),
    _("Calcium")
],
"correct": 0,
"explanation": _("Sunlight helps produce Vitamin D.")},

{"question": _("Which activity improves lung capacity?"),
"options": [
    _("Smoking"),
    _("Deep breathing"),
    _("Skipping water"),
    _("Overeating")
],
"correct": 1,
"explanation": _("Breathing exercises improve lung function.")},

{"question": _("Alcohol mainly affects:"),
"options": [
    _("Liver"),
    _("Eyes"),
    _("Hair"),
    _("Teeth")
],
"correct": 0,
"explanation": _("Alcohol damages the liver.")},

{"question": _("Healthy weight reduces risk of:"),
"options": [
    _("Diabetes"),
    _("Height growth"),
    _("Better hair"),
    _("Eye color change")
],
"correct": 0,
"explanation": _("Healthy weight lowers disease risk.")},

{"question": _("Daily physical activity should be at least:"),
"options": [
    _("10 min"),
    _("30 min"),
    _("2 hrs"),
    _("5 hrs")
],
"correct": 1,
"explanation": _("At least 30 minutes daily.")},

{"question": _("Which vitamin boosts immunity?"),
"options": [
    _("Vitamin C"),
    _("Vitamin K"),
    _("Vitamin B12"),
    _("Vitamin E")
],
"correct": 0,
"explanation": _("Vitamin C supports immunity.")},

{"question": _("Dehydration can cause:"),
"options": [
    _("Headache"),
    _("Strength"),
    _("Energy boost"),
    _("Better sleep")
],
"correct": 0,
"explanation": _("Lack of water causes headaches.")},

{"question": _("Balanced meals should include:"),
"options": [
    _("Protein, carbs, fats"),
    _("Only carbs"),
    _("Only sugar"),
    _("Only fats")
],
"correct": 0,
"explanation": _("All macronutrients are needed.")},

{"question": _("Good posture prevents:"),
"options": [
    _("Back pain"),
    _("Vision"),
    _("Cold"),
    _("Flu")
],
"correct": 0,
"explanation": _("Proper posture prevents back pain.")},

{"question": _("Walking improves:"),
"options": [
    _("Heart health"),
    _("Stress"),
    _("Fatigue"),
    _("Weakness")
],
"correct": 0,
"explanation": _("Walking improves heart health.")},

{"question": _("Which is a healthy snack?"),
"options": [
    _("Fruits"),
    _("Chips"),
    _("Soda"),
    _("Candy")
],
"correct": 0,
"explanation": _("Fruits are healthy snacks.")},

{"question": _("Meditation helps with:"),
"options": [
    _("Stress reduction"),
    _("Height growth"),
    _("Hair color"),
    _("Vision")
],
"correct": 0,
"explanation": _("Meditation reduces stress.")},

{"question": _("Which reduces infection risk?"),
"options": [
    _("Hand sanitizer"),
    _("Sharing bottles"),
    _("Skipping bath"),
    _("Not washing hands")
],
"correct": 0,
"explanation": _("Sanitizer reduces germs.")},

],
"firstaid": [

{"question": _("What should you do first in an emergency?"),
"options": [
    _("Panic"),
    _("Ensure safety"),
    _("Run away"),
    _("Ignore")
],
"correct": 1,
"explanation": _("Always ensure scene safety first.")},

{"question": _("For minor burns, use:"),
"options": [
    _("Ice directly"),
    _("Cold running water"),
    _("Oil"),
    _("Toothpaste")
],
"correct": 1,
"explanation": _("Cool running water soothes burns.")},

{"question": _("CPR stands for:"),
"options": [
    _("Cardio Pulmonary Resuscitation"),
    _("Cardiac Pressure Response"),
    _("Chest Pump Rescue"),
    _("Critical Pulse Recovery")
],
"correct": 0,
"explanation": _("CPR means Cardio Pulmonary Resuscitation.")},

{"question": _("For nosebleed, you should:"),
"options": [
    _("Tilt head back"),
    _("Lean forward"),
    _("Lie down"),
    _("Ignore")
],
"correct": 1,
"explanation": _("Lean forward to avoid swallowing blood.")},

{"question": _("If someone is choking, perform:"),
"options": [
    _("Heimlich maneuver"),
    _("CPR immediately"),
    _("Water therapy"),
    _("Massage")
],
"correct": 0,
"explanation": _("Heimlich maneuver helps remove obstruction.")},

{"question": _("For cuts, first step:"),
"options": [
    _("Wash with clean water"),
    _("Apply mud"),
    _("Ignore"),
    _("Use dirty cloth")
],
"correct": 0,
"explanation": _("Clean wound with water.")},

{"question": _("If someone faints, you should:"),
"options": [
    _("Lay them flat"),
    _("Shake violently"),
    _("Throw water"),
    _("Ignore")
],
"correct": 0,
"explanation": _("Lay flat and elevate legs.")},

{"question": _("For sprain, use:"),
"options": [
    _("RICE method"),
    _("Heat immediately"),
    _("Ignore"),
    _("Massage hard")
],
"correct": 0,
"explanation": _("Rest, Ice, Compression, Elevation.")},

{"question": _("Emergency number in India is:"),
"options": [
    _("100"),
    _("108"),
    _("101"),
    _("112")
],
"correct": 3,
"explanation": _("112 is national emergency helpline.")},

{"question": _("If electric shock occurs:"),
"options": [
    _("Touch directly"),
    _("Switch off power first"),
    _("Pour water"),
    _("Ignore")
],
"correct": 1,
"explanation": _("Turn off power before touching victim.")},

{"question": _("For snake bite, you should:"),
"options": [
    _("Suck venom"),
    _("Keep person calm"),
    _("Cut wound"),
    _("Apply ice")
],
"correct": 1,
"explanation": _("Keep calm and seek medical help.")},

{"question": _("For eye injury, you should:"),
"options": [
    _("Rub eye"),
    _("Rinse gently"),
    _("Ignore"),
    _("Apply oil")
],
"correct": 1,
"explanation": _("Rinse gently with clean water.")},

{"question": _("If fracture suspected:"),
"options": [
    _("Move limb"),
    _("Immobilize"),
    _("Massage"),
    _("Ignore")
],
"correct": 1,
"explanation": _("Keep limb still and supported.")},

{"question": _("For heat stroke:"),
"options": [
    _("Cool the person"),
    _("Give alcohol"),
    _("Ignore"),
    _("Wrap blanket")
],
"correct": 0,
"explanation": _("Cool body immediately.")},

{"question": _("For poisoning:"),
"options": [
    _("Induce vomiting always"),
    _("Call emergency"),
    _("Ignore"),
    _("Give soda")
],
"correct": 1,
"explanation": _("Call emergency services immediately.")},

]



    # Add other categories similarly
}


@login_required
def quiz(request):
    category = request.GET.get("category")

    selected_questions = []

    if category and category in QUIZ_QUESTIONS:
        all_questions = QUIZ_QUESTIONS[category]

        # Randomly select 10 (or less if not 50 yet)
        selected_questions = random.sample(
            all_questions,
            min(10, len(all_questions))
        )
    

    return render(request, 'quiz/quiz.html', {
        "questions": selected_questions,
        "selected_category": category
    })