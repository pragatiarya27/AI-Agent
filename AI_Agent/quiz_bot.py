import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Initialize Pygame mixer
pygame.mixer.init()
WHISPER_SOUND = pygame.mixer.Sound("whisper_reminder.wav")

def show_encouragement_card(mood):
    cards = {
        "happy": "😄 Keep that smile going! Let's ace this!",
        "sad": "💙 It's okay to feel down. You're doing great!",
        "confident": "🚀 You're ready to shine. Let's go!",
        "nervous": "💪 You've got this. Just take it one step at a time!",
    }
    return cards.get(mood.lower(), "🌟 Welcome! Let's start your quiz journey!")

def greet_student(student_id, mood):
    return f"Hello, {student_id}! {show_encouragement_card(mood)}"


# Question bank
QUESTIONS = {
    "easy": {
        "math": [
           
    ("What is 2 + 2?", "4"),
    ("What is 5 - 3?", "2"),
    ("What is 10 / 2?", "5"),
    ("What comes after 6?", "7"),
    ("Is 3 a prime number?", "Yes"),
    ("What is 7 + 3?", "10"),
    ("What is 6 - 4?", "2"),
    ("What is 3 × 2?", "6"),
    ("What is 12 / 4?", "3"),
    ("Is 8 an even number?", "Yes"),
    ("Is 9 an odd number?", "Yes"),
    ("What is 1 more than 10?", "11"),
    ("What is 1 less than 5?", "4"),
    ("What is the result of 2 + 5?", "7"),
    ("How many sides does a triangle have?", "3"),
    ("What is 20 - 5?", "15"),
    ("What is 4 × 1?", "4"),
    ("How many fingers on both hands?", "10"),
    ("What is half of 10?", "5"),
    ("Which is more: 9 or 6?", "9"),
    ("Which is less: 2 or 7?", "2"),
    ("What is the next number after 14?", "15"),
    ("What number comes before 10?", "9"),
    ("What is 5 + 5?", "10"),
    ("What is 0 + 3?", "3"),
    ("What is 2 × 3?", "6"),
    ("What is 4 + 4?", "8"),
    ("What is 6 + 1?", "7"),
    ("What is 9 - 5?", "4"),
    ("How many legs does a spider have?", "8"),
    ("What is 18 - 9?", "9"),
    ("What is 3 + 4?", "7"),
    ("How many hours in a day?", "24"),
    ("What is 2 more than 6?", "8"),
    ("What is 15 - 5?", "10"),
    ("What is 7 - 2?", "5"),
    ("What is 3 + 3?", "6"),
    ("What is 10 × 0?", "0"),
    ("What is 100 - 90?", "10"),
    ("How many months in a year?", "12"),
    ("What is 5 × 1?", "5"),
    ("What is 8 / 4?", "2"),
    ("What is 9 × 1?", "9"),
    ("Which is bigger: 11 or 13?", "13"),
    ("What number comes after 29?", "30"),
    ("What is 14 - 4?", "10"),
    ("What is 7 + 2?", "9"),
    ("What is 5 + 1?", "6"),
    ("What is 3 less than 12?", "9"),
    ("Is 4 an even number?", "Yes"),
    ("What is 6 × 1?", "6"),
    ("What is 1 + 0?", "1"),
    ("How many days in a week?", "7"),
    ("What is 16 / 2?", "8"),
    ("What is 11 - 1?", "10"),
    ("What is 6 more than 3?", "9"),
    ("What is 2 + 7?", "9"),
    ("What is 20 / 5?", "4"),
    ("What is 3 more than 8?", "11"),
    ("What is 13 - 3?", "10"),
    ("What is 6 + 5?", "11"),
    ("What is 1 less than 12?", "11"),
    ("What is 10 / 1?", "10"),
    ("How many toes on both feet?", "10"),
    ("What is 2 × 5?", "10"),
    ("What is 9 / 3?", "3"),
    ("What is 7 - 3?", "4"),
    ("What is 8 + 1?", "9"),
    ("Is 6 an even number?", "Yes"),
    ("What is 3 + 6?", "9"),
    ("How many wheels on a bicycle?", "2"),
    ("What is 4 less than 10?", "6"),
    ("What is 2 + 6?", "8"),
    ("What is 18 / 3?", "6"),
    ("What is 4 + 5?", "9"),
    ("What is 6 - 2?", "4"),
    ("What is 3 × 1?", "3"),
    ("Is 5 an odd number?", "Yes"),
    ("What is 1 + 9?", "10"),
    ("What is 7 / 1?", "7"),
    ("What is 8 - 3?", "5"),
    ("What is 10 + 0?", "10"),
    ("What is 6 / 3?", "2"),
    ("What is 2 × 4?", "8"),
    ("What is 5 less than 15?", "10"),
    ("What is 2 more than 7?", "9"),
    ("What is 1 + 1?", "2"),
    ("What is 0 × 5?", "0"),
    ("What is 2 - 1?", "1"),
    ("What is 4 - 2?", "2"),
    ("What is 9 + 0?", "9"),
    ("What is 3 + 2?", "5"),
    ("What is 7 - 1?", "6"),
    ("What is 12 / 3?", "4"),
    ("What is 8 + 2?", "10"),
    ("What is 3 × 3?", "9"),
    ("What is 2 + 9?", "11"),
    ("What is 10 - 7?", "3"),
    ("What is 6 × 0?", "0"),
    ("How many corners does a square have?", "4"),
    ("What number is double of 4?", "8"),
    ("What is half of 8?", "4"),
    ("What is 4 × 2?", "8")


        ],
    "science": [
    ("What planet do we live on?", "Earth"),
    ("What gas do we need to breathe?", "Oxygen"),
    ("What color is the sky on a clear day?", "Blue"),
    ("Which organ pumps blood in our body?", "Heart"),
    ("Which star gives us light and heat?", "Sun"),
    ("What do plants need to make food?", "Sunlight"),
    ("How many legs does an insect have?", "6"),
    ("What do bees make?", "Honey"),
    ("What do cows drink?", "Water"),
    ("What is frozen water called?", "Ice"),
    ("Which animal barks?", "Dog"),
    ("What do we call a baby cat?", "Kitten"),
    ("How many planets are in our solar system?", "8"),
    ("What is the closest planet to the Sun?", "Mercury"),
    ("Which part of the plant is underground?", "Root"),
    ("What is the main source of energy on Earth?", "Sun"),
    ("Which animal gives us milk?", "Cow"),
    ("How many seasons are there?", "4"),
    ("What do plants give us to breathe?", "Oxygen"),
    ("Which bird cannot fly?", "Ostrich"),
    ("What do fish use to breathe?", "Gills"),
    ("What do you see with?", "Eyes"),
    ("What is the largest land animal?", "Elephant"),
    ("What do you hear with?", "Ears"),
    ("What do you smell with?", "Nose"),
    ("What do you taste with?", "Tongue"),
    ("Which planet is known as the red planet?", "Mars"),
    ("What is the shape of the Earth?", "Round"),
    ("What do birds use to fly?", "Wings"),
    ("What do we call water in the gas form?", "Steam"),
    ("Which planet is famous for its rings?", "Saturn"),
    ("What do we use to measure temperature?", "Thermometer"),
    ("What is a baby dog called?", "Puppy"),
    ("Which animal lives in water and has eight arms?", "Octopus"),
    ("Which organ helps us think?", "Brain"),
    ("How many eyes does a human have?", "2"),
    ("Which planet do astronauts visit with a rocket?", "Moon"),
    ("What do you call the bones in your body?", "Skeleton"),
    ("What is rain made of?", "Water"),
    ("What do you wear to see better?", "Glasses"),
    ("What is the largest planet?", "Jupiter"),
    ("What do plants absorb through their roots?", "Water"),
    ("What do you feel with?", "Skin"),
    ("What color is chlorophyll?", "Green"),
    ("What helps birds fly high in the sky?", "Feathers"),
    ("What is the natural satellite of Earth?", "Moon"),
    ("What is a group of stars called?", "Constellation"),
    ("What do you call melted rock from a volcano?", "Lava"),
    ("What do animals need to survive?", "Food"),
    ("What does a thermometer measure?", "Temperature"),
    ("What do we call the young of a butterfly?", "Caterpillar"),
    ("What do frogs lay?", "Eggs"),
    ("What is the gas plants take in?", "Carbon dioxide"),
    ("What is the color of clouds?", "White"),
    ("What tool helps us see tiny things?", "Microscope"),
    ("What gives plants their green color?", "Chlorophyll"),
    ("What are stars made of?", "Gas"),
    ("Which animal lives in a shell?", "Turtle"),
    ("Which animal is called the king of the jungle?", "Lion"),
    ("What season comes after winter?", "Spring"),
    ("What do trees lose in autumn?", "Leaves"),
    ("What happens when water freezes?", "It turns into ice"),
    ("Which planet is farthest from the Sun?", "Neptune"),
    ("What organ do we use to breathe?", "Lungs"),
    ("What causes day and night?", "Earth's rotation"),
    ("What do you use to brush your teeth?", "Toothbrush"),
    ("Which part of the plant makes seeds?", "Flower"),
    ("What do we call animals that eat plants?", "Herbivores"),
    ("What do we call animals that eat meat?", "Carnivores"),
    ("Which food group gives us energy?", "Carbohydrates"),
    ("Which object orbits the Earth?", "Moon"),
    ("What type of energy comes from the sun?", "Solar energy"),
    ("How many legs does a spider have?", "8"),
    ("What do you call water falling from clouds?", "Rain"),
    ("Which insect glows in the dark?", "Firefly"),
    ("Which is faster: sound or light?", "Light"),
    ("What color are healthy plant leaves?", "Green"),
    ("What do magnets attract?", "Iron"),
    ("Which sense helps you detect flavor?", "Taste"),
    ("What do we call baby frogs?", "Tadpoles"),
    ("What animal has black and white stripes?", "Zebra"),
    ("What do trees absorb from the air?", "Carbon dioxide"),
    ("What do you use to write?", "Pen"),
    ("What color is blood?", "Red"),
    ("What happens when you mix red and yellow?", "Orange"),
    ("Which planet is third from the Sun?", "Earth"),
    ("What do you call a scientist who studies rocks?", "Geologist"),
    ("What shape is a wheel?", "Circle"),
    ("What happens when you boil water?", "It becomes steam"),
    ("What kind of weather has thunder and lightning?", "Storm"),
    ("What do astronauts wear in space?", "Spacesuit"),
    ("What does the Earth revolve around?", "Sun"),
    ("What part of the body helps you move?", "Muscles"),
    ("What is a group of fish called?", "School"),
    ("What is a young plant called?", "Seedling"),
    ("What is the color of the sky at night?", "Black"),
    ("Which organ helps us hear?", "Ears"),
    ("What is found at the center of the Earth?", "Core"),
    ("What makes plants grow tall?", "Sunlight and water"),
    ("What is the name of our galaxy?", "Milky Way"),
    ("Which season is the coldest?", "Winter"),
    ("What can be solid, liquid, or gas?", "Water"),
    ("Which bird is known for its colorful tail?", "Peacock"),
    ("What animal is known for hopping?", "Kangaroo")



        ]
    },
    "medium": {
        "math": [

("What is 12 × 3?", "36"),
("What is 45 ÷ 5?", "9"),
("What is 15% of 100?", "15"),
("What is the square of 7?", "49"),
("What is the cube of 2?", "8"),
("If a box has 4 rows of 6 apples, how many apples are there?", "24"),
("What is 5²?", "25"),
("How many minutes are in 2 hours?", "120"),
("What is 1/2 of 50?", "25"),
("What is 3/4 of 20?", "15"),
("A train travels 60 km in 2 hours. What is the speed?", "30"),
("How many sides does a hexagon have?", "6"),
("What is 100 - 37?", "63"),
("A pack of pens costs ₹60 for 4 pens. What's the cost of 1 pen?", "15"),
("What is 81 ÷ 9?", "9"),
("If you save ₹5 per day, how much after 3 weeks?", "105"),
("What is 36 ÷ 6?", "6"),
("If a pizza is cut into 8 slices and you eat 3, how many remain?", "5"),
("What is 72 ÷ 8?", "9"),
("What is 7 × 7?", "49"),
("Which is greater: 3/5 or 4/7?", "3/5"),
("What is 9 more than 66?", "75"),
("What is 5 less than 100?", "95"),
("If you run 2 km daily, how much in a week?", "14"),
("What is 8²?", "64"),
("If a book has 200 pages and you read 40 pages, what percent is read?", "20"),
("What is 0.5 + 0.25?", "0.75"),
("How many days in 3 weeks?", "21"),
("If 5 pens cost ₹25, how many pens can you buy for ₹50?", "10"),
("What is 3 × 9?", "27"),
("What is 144 ÷ 12?", "12"),
("What is 3³?", "27"),
("How many degrees in a right angle?", "90"),
("If a pack contains 8 chocolates, how many in 5 packs?", "40"),
("What is 25% of 80?", "20"),
("If you multiply any number by 0, the result is?", "0"),
("What is 2/5 of 100?", "40"),
("If a rectangle has sides 5 and 10, what is its area?", "50"),
("What is 5 × 13?", "65"),
("How many hours in 3 days?", "72"),
("What is the average of 5, 10, and 15?", "10"),
("How many millimeters in 1 cm?", "10"),
("What is 60 ÷ 10?", "6"),
("If a triangle has sides 3, 4, and 5, is it right-angled?", "Yes"),
("What is 50% of 200?", "100"),
("What is 0.1 + 0.9?", "1"),
("How many grams in 3 kilograms?", "3000"),
("If it is 9 AM now, what time after 5 hours?", "2 PM"),
("What is 1000 - 250?", "750"),
("What is 6 × 8?", "48"),
("What is 121 ÷ 11?", "11"),
("What is the perimeter of a square with side 5?", "20"),
("What is 0.75 as a fraction?", "3/4"),
("How many 10s in 150?", "15"),
("What is the LCM of 4 and 5?", "20"),
("What is the HCF of 12 and 18?", "6"),
("What is 7/10 + 2/10?", "9/10"),
("How many months have 30 days?", "4"),
("How many inches in a foot?", "12"),
("What is 9 × 11?", "99"),
("If a pen costs ₹7, how much for 8 pens?", "56"),
("What is 0.4 + 0.3?", "0.7"),
("What is 75 ÷ 5?", "15"),
("What is the square of 9?", "81"),
("What is 0.25 × 4?", "1"),
("How many centimeters in 1.5 meters?", "150"),
("If 1 kg = 1000 g, then 3.2 kg = ?", "3200"),
("What is 5³?", "125"),
("If speed = 60 km/h, how far in 2.5 hours?", "150"),
("What is 9²?", "81"),
("What is 6.5 + 3.5?", "10"),
("What is 99 ÷ 11?", "9"),
("If 7 days = 1 week, how many weeks in 28 days?", "4"),
("How many milliliters in 2 liters?", "2000"),
("What is 0.6 × 100?", "60"),
("What is the area of square with side 6?", "36"),
("What is 5/8 as a decimal?", "0.625"),
("How many factors of 12?", "6"),
("What is the sum of angles in triangle?", "180"),
("What is 4.2 + 3.8?", "8"),
("What is the cube of 3?", "27"),
("What is 20% of 150?", "30"),
("What is the volume of cube with side 3?", "27"),
("What is 12 × 12?", "144"),
("What is 2² + 3²?", "13"),
("What is 1.25 × 4?", "5"),
("How many seconds in 5 minutes?", "300"),
("If 1 dozen = 12, what is 3 dozen?", "36"),
("What is 0.2 + 0.8?", "1"),
("If 1 box has 24 items, how many in 6 boxes?", "144"),
("What is the reciprocal of 1/4?", "4"),
("What is 0.5 of 60?", "30"),
("What is 2.5 × 2?", "5"),
("What is the area of rectangle (l=4, b=3)?", "12"),
("What is 16 ÷ 0.5?", "32"),
("If 2 pencils cost ₹10, what is the cost of 1?", "5"),
("What is 3.3 + 1.7?", "5"),
("What is 0.6 + 0.6?", "1.2"),
("What is the square root of 81?", "9"),
("What is the next prime number after 7?", "11")

        ],
        "science": [
           
    ("What part of the plant transports water?", "Xylem"),
    ("What is the main function of the respiratory system?", "Gas exchange"),
    ("Which planet is known for its rings?", "Saturn"),
    ("What do we call animals that give birth to live young?", "Mammals"),
    ("What is the process by which water changes from liquid to gas?", "Evaporation"),
    ("What type of energy is stored in a stretched rubber band?", "Potential energy"),
    ("Which gas is most abundant in Earth’s atmosphere?", "Nitrogen"),
    ("What do we call the remains of ancient organisms?", "Fossils"),
    ("What is the role of chlorophyll in plants?", "Absorbs sunlight for photosynthesis"),
    ("Which force pulls objects toward the center of Earth?", "Gravity"),
    ("What part of the body produces insulin?", "Pancreas"),
    ("What are organisms that make their own food called?", "Producers"),
    ("What is the boiling point of water in Celsius?", "100"),
    ("What is the center of our solar system?", "Sun"),
    ("What are the male parts of a flower called?", "Stamens"),
    ("Which part of the cell controls activities?", "Nucleus"),
    ("What is the process of cell division in body cells?", "Mitosis"),
    ("What is a group of similar cells working together called?", "Tissue"),
    ("What is the smallest unit of matter?", "Atom"),
    ("Which organ system includes the heart and blood vessels?", "Circulatory system"),
    ("What causes day and night on Earth?", "Earth’s rotation"),
    ("What is the energy source for photosynthesis?", "Sunlight"),
    ("What do we call animals that eat both plants and animals?", "Omnivores"),
    ("What are the three states of matter?", "Solid, liquid, gas"),
    ("What is the layer of gases around Earth called?", "Atmosphere"),
    ("Which instrument measures temperature?", "Thermometer"),
    ("What is the term for a push or pull on an object?", "Force"),
    ("What organ removes waste from the blood?", "Kidneys"),
    ("What is a trait that helps an organism survive called?", "Adaptation"),
    ("What do we call the path of an object in orbit?", "Orbit"),
    ("What kind of change is melting?", "Physical change"),
    ("What are the basic needs of living organisms?", "Food, water, air, shelter"),
    ("What are vertebrates?", "Animals with a backbone"),
    ("What is the process of breaking food into small pieces?", "Digestion"),
    ("What is the job of red blood cells?", "Carry oxygen"),
    ("What is friction?", "A force that opposes motion"),
    ("What type of rock forms from lava?", "Igneous rock"),
    ("Which planet is closest to the sun?", "Mercury"),
    ("What is the function of the ozone layer?", "Blocks harmful UV radiation"),
    ("Which simple machine is used in a seesaw?", "Lever"),
    ("What is the basic unit of heredity?", "Gene"),
    ("What do we call water in the solid state?", "Ice"),
    ("What is a food chain?", "A series of organisms each feeding on the next"),
    ("Which part of the digestive system absorbs nutrients?", "Small intestine"),
    ("Which human organ helps regulate body temperature?", "Skin"),
    ("What kind of weather does a high-pressure system usually bring?", "Clear and sunny"),
    ("What do we call the number of protons in an atom?", "Atomic number"),
    ("What is the process of water cycle from leaves to air called?", "Transpiration"),
    ("What are renewable resources?", "Resources that can be replaced naturally"),
    ("What is a comet made of?", "Ice, dust, and gas"),
    ("What is an ecosystem?", "A community of organisms and their environment"),
    ("Which layer of Earth is liquid?", "Outer core"),
    ("What is the name for animals that sleep through winter?", "Hibernators"),
    ("Which planet is known as the 'morning star'?", "Venus"),
    ("Which property of sound determines pitch?", "Frequency"),
    ("What is the function of a root in a plant?", "Anchors plant and absorbs water"),
    ("What is a circuit?", "A complete path for electricity to flow"),
    ("What are genes made of?", "DNA"),
    ("What is the natural satellite of Earth?", "Moon"),
    ("What causes seasons on Earth?", "Tilt of Earth's axis"),
    ("What kind of energy does a moving object have?", "Kinetic energy"),
    ("What is the role of decomposers in an ecosystem?", "Break down dead organisms"),
    ("Which part of the eye controls the amount of light entering?", "Pupil"),
    ("What is a solution?", "A mixture where one substance dissolves into another"),
    ("Which rock is formed by pressure and heat?", "Metamorphic rock"),
    ("What is the function of the liver?", "Detoxifies and produces bile"),
    ("Which tool is used to magnify small objects?", "Microscope"),
    ("What is a chemical change?", "A change that forms a new substance"),
    ("Which element is essential for breathing?", "Oxygen"),
    ("What kind of energy comes from the sun?", "Solar energy"),
    ("What is the freezing point of water in Celsius?", "0"),
    ("What is the unit of electric current?", "Ampere"),
    ("What is the term for species that are no longer living?", "Extinct"),
    ("Which part of the brain is responsible for balance?", "Cerebellum"),
    ("What is weathering?", "Breaking down of rocks into smaller pieces"),
    ("What are nonrenewable resources?", "Resources that cannot be easily replaced"),
    ("What kind of animal is a frog?", "Amphibian"),
    ("Which part of a cell stores water?", "Vacuole"),
    ("What is the outer layer of skin called?", "Epidermis"),
    ("What is the energy stored in food called?", "Chemical energy"),
    ("What is a mixture?", "Two or more substances not chemically combined"),
    ("Which gas is used in fire extinguishers?", "Carbon dioxide"),
    ("What are earthquakes caused by?", "Movement of tectonic plates"),
    ("Which process turns gas into liquid?", "Condensation"),
    ("What is a predator?", "An animal that hunts other animals"),
    ("Which planet has the Great Red Spot?", "Jupiter"),
    ("What is the name for a scientist who studies animals?", "Zoologist"),
    ("Which blood cells fight infections?", "White blood cells"),
    ("What do you call energy stored due to an object’s position?", "Potential energy"),
    ("Which vitamin is made by sunlight?", "Vitamin D"),
    ("What is a food web?", "A system of interconnected food chains"),
    ("What is a lunar eclipse?", "Earth blocks sunlight from reaching the Moon"),
    ("Which part of the ear helps with balance?", "Inner ear"),
    ("What is pollution?", "Introduction of harmful substances into the environment"),
    ("What is a constellation?", "Group of stars forming a pattern"),
    ("Which part of the Earth supports life?", "Biosphere"),
    ("Which nutrient builds body tissues?", "Protein"),
    ("What is the Earth’s primary source of energy?", "Sun"),
    ("What is condensation?", "Gas turning into liquid"),
    ("What is an aquifer?", "Underground layer that holds water")


        ]
    },
    "hard": {
        "math": [
    ("What is the derivative of x^2?", "2x"),
    ("Solve for x: 3x - 7 = 11", "6"),
    ("What is the area of a circle with radius 7?", "153.94"),
    ("What is the square root of 625?", "25"),
    ("What is the value of π (up to 2 decimal places)?", "3.14"),
    ("Solve: 2(x - 3) = 4", "5"),
    ("What is 15% of 200?", "30"),
    ("If a triangle has angles 90°, 45°, what's the third angle?", "45"),
    ("What is the volume of a cube with side 4?", "64"),
    ("What is 13 squared?", "169"),
    ("What is the LCM of 12 and 15?", "60"),
    ("Solve for x: x/5 = 3", "15"),
    ("Simplify: (3x + 2x)", "5x"),
    ("What is the slope of a line between (1,2) and (3,6)?", "2"),
    ("Convert 0.75 to a fraction.", "3/4"),
    ("What is 9 factorial (9!)?", "362880"),
    ("Find the perimeter of a rectangle with length 8 and width 3", "22"),
    ("If 2x + 1 = 9, what is x?", "4"),
    ("What is the cube root of 64?", "4"),
    ("If sinθ = 0.5, what is θ in degrees?", "30"),
    ("What is 20% of 250?", "50"),
    ("What is 7 × 13?", "91"),
    ("Simplify: 4x - 3x + 2", "x + 2"),
    ("Solve: 3x^2 = 27", "3"),
    ("What is the median of [3, 9, 15, 17, 21]?", "15"),
    ("What is the mode of [2, 4, 4, 6, 7]?", "4"),
    ("Solve for x: x^2 - 4 = 0", "2"),
    ("Convert 110% to decimal.", "1.1"),
    ("What is 10^-2?", "0.01"),
    ("Find the area of triangle with base 10 and height 5", "25"),
    ("What is the volume of cylinder: r=3, h=7", "197.82"),
    ("What is the 5th prime number?", "11"),
    ("What is the 10th Fibonacci number?", "55"),
    ("Evaluate: (2^3)^2", "64"),
    ("What is log base 10 of 1000?", "3"),
    ("What is 1/2 + 2/3?", "7/6"),
    ("What is the hypotenuse if sides are 5 and 12?", "13"),
    ("If 2x + 3 = 3x - 5, find x.", "8"),
    ("What is 2.5 × 1.6?", "4"),
    ("What is the discriminant of x^2 - 4x + 4?", "0"),
    ("What is the sum of angles in a pentagon?", "540"),
    ("Simplify: (x^2)^3", "x^6"),
    ("What is 144 ÷ 12?", "12"),
    ("Convert 3/8 to a decimal.", "0.375"),
    ("If x = 3 and y = 2, what is 2x + y?", "8"),
    ("What is 0.2 × 0.5?", "0.1"),
    ("What is the perimeter of a square with side 6?", "24"),
    ("What is 50% of 360?", "180"),
    ("Solve: x^2 = 36", "6"),
    ("What is the sum of first 10 natural numbers?", "55"),
    ("Evaluate: 3^4", "81"),
    ("Simplify: (4x + 3x)/7", "x"),
    ("What is 11% of 600?", "66"),
    ("Solve: 5(x - 2) = 15", "5"),
    ("What is the ratio of 3:12 in simplest form?", "1:4"),
    ("Convert 1.25 to a fraction.", "5/4"),
    ("What is the average of [4, 8, 12, 16]?", "10"),
    ("What is √49?", "7"),
    ("Find the angle in a regular hexagon.", "120"),
    ("Find the 6th term in arithmetic series: a=2, d=3", "17"),
    ("What is the area of a square with diagonal 10?", "50"),
    ("If a/b = 2/3, what is b if a = 8?", "12"),
    ("What is the surface area of cube side 3?", "54"),
    ("Convert 5/4 to decimal.", "1.25"),
    ("Simplify: (3x^2 + 2x) - (x^2 + x)", "2x^2 + x"),
    ("What is 8^2 - 5^2?", "39"),
    ("Evaluate: |−7 + 3|", "4"),
    ("Solve for x: 2x + 4 = 18", "7"),
    ("What is the range of [1, 4, 9, 16]?", "15"),
    ("If x = -2, what is x^2 + 2x + 1?", "1"),
    ("What is 15% of 320?", "48"),
    ("If a = 5, b = 3, find (a^2 - b^2)", "16"),
    ("What is 0.6 of 150?", "90"),
    ("What is the square of 12?", "144"),
    ("What is 8 ÷ 0.5?", "16"),
    ("Solve for y: y/3 + 2 = 6", "12"),
    ("What is the cube of 5?", "125"),
    ("What is 3.5 × 3?", "10.5"),
    ("What is the reciprocal of 2/5?", "5/2"),
    ("What is the value of x: 3x = 21?", "7"),
    ("Solve: x^2 + 6x + 9 = 0", "-3"),
    ("Simplify: (x+2)^2", "x^2 + 4x + 4"),
    ("What is 2% of 500?", "10"),
    ("What is the sum of exterior angles of any polygon?", "360"),
    ("Find area of trapezium with bases 4, 6 and height 5", "25"),
    ("If 4x = 28, find x.", "7"),
    ("Evaluate: (5 + 3)^2", "64"),
    ("If the radius of a circle is doubled, area becomes?", "4 times"),
    ("Convert 0.03 to percent.", "3%"),
    ("What is 2^5?", "32"),
    ("What is the area of rhombus with diagonals 6 and 8?", "24"),
    ("Find the third angle if two angles are 60° and 80°", "40")


        ],
        "science": [
    ("What is the chemical formula for table salt?", "NaCl"),
    ("What is Newton's third law of motion?", "For every action, there is an equal and opposite reaction"),
    ("Which part of the cell contains the genetic material?", "Nucleus"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("What is the acceleration due to gravity on Earth?", "9.8 m/s²"),
    ("Which blood type is known as the universal donor?", "O negative"),
    ("Which element has the atomic number 1?", "Hydrogen"),
    ("Which organelle is responsible for photosynthesis?", "Chloroplast"),
    ("What does DNA stand for?", "Deoxyribonucleic Acid"),
    ("What gas do plants absorb during photosynthesis?", "Carbon dioxide"),
    ("Which planet has the most moons?", "Saturn"),
    ("What is the SI unit of force?", "Newton"),
    ("Which vitamin is produced when sunlight hits the skin?", "Vitamin D"),
    ("What is the process of liquid turning into gas called?", "Evaporation"),
    ("Which gas is responsible for the greenhouse effect?", "Carbon dioxide"),
    ("What part of the brain controls balance?", "Cerebellum"),
    ("What is the pH of pure water?", "7"),
    ("What is the hardest natural substance on Earth?", "Diamond"),
    ("What is the boiling point of water in Celsius?", "100"),
    ("Which organ in the human body produces insulin?", "Pancreas"),
    ("What is the atomic symbol for gold?", "Au"),
    ("What is the main function of red blood cells?", "Transport oxygen"),
    ("Which layer of Earth lies beneath the crust?", "Mantle"),
    ("What causes tides in the ocean?", "Gravitational pull of the moon"),
    ("Which acid is found in the stomach?", "Hydrochloric acid"),
    ("Which gas do humans exhale?", "Carbon dioxide"),
    ("What is the process by which plants make food?", "Photosynthesis"),
    ("What is the smallest unit of life?", "Cell"),
    ("What is the function of white blood cells?", "Fight infection"),
    ("What type of energy is stored in food?", "Chemical energy"),
    ("Which subatomic particle has a positive charge?", "Proton"),
    ("What is the speed of light in vacuum?", "Approximately 3 × 10^8 m/s"),
    ("Which part of the plant conducts water?", "Xylem"),
    ("Which law explains why we wear seatbelts?", "Newton's first law"),
    ("What is an ecosystem?", "A community of organisms and their environment"),
    ("What instrument is used to measure earthquakes?", "Seismograph"),
    ("What is the center of an atom called?", "Nucleus"),
    ("What kind of bond shares electrons?", "Covalent bond"),
    ("What is the most abundant gas in Earth’s atmosphere?", "Nitrogen"),
    ("Which organ filters blood in humans?", "Kidneys"),
    ("What is the name of the protein in red blood cells that carries oxygen?", "Hemoglobin"),
    ("Which vitamin helps in blood clotting?", "Vitamin K"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Which layer of the atmosphere contains the ozone layer?", "Stratosphere"),
    ("What is the term for animals that eat only plants?", "Herbivores"),
    ("What are the three states of matter?", "Solid, liquid, gas"),
    ("What is the charge of a neutron?", "Neutral"),
    ("What happens during nuclear fission?", "An atom splits into smaller parts"),
    ("What process turns sugar into energy in cells?", "Cellular respiration"),
    ("What do we call animals that maintain a constant body temperature?", "Warm-blooded"),
    ("What is the term for a chemical that speeds up a reaction?", "Catalyst"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("Which organ system controls body functions via hormones?", "Endocrine system"),
    ("What metal is liquid at room temperature?", "Mercury"),
    ("What kind of wave is light?", "Electromagnetic wave"),
    ("Which type of blood vessel carries blood away from the heart?", "Arteries"),
    ("What is the main gas used in balloons?", "Helium"),
    ("Which part of the brain is responsible for memory?", "Hippocampus"),
    ("What is a group of stars that forms a pattern called?", "Constellation"),
    ("What is the process of breaking down food called?", "Digestion"),
    ("What is the study of fossils called?", "Paleontology"),
    ("Which device splits white light into a spectrum?", "Prism"),
    ("What is the process of water vapor becoming liquid?", "Condensation"),
    ("What is a black hole?", "A region in space with strong gravity that nothing can escape"),
    ("What is the function of the large intestine?", "Absorb water and form feces"),
    ("Which blood cells help in clotting?", "Platelets"),
    ("What do you call a species no longer in existence?", "Extinct"),
    ("What element is necessary for bones and teeth?", "Calcium"),
    ("What is the chemical symbol for oxygen?", "O"),
    ("What are fungi that decompose material called?", "Decomposers"),
    ("What is the energy in motion called?", "Kinetic energy"),
    ("Which body system includes the skin?", "Integumentary system"),
    ("What is the study of heredity?", "Genetics"),
    ("What are chromosomes made of?", "DNA and protein"),
    ("What is the main component of natural gas?", "Methane"),
    ("What planet is tilted on its side?", "Uranus"),
    ("What is the opposite of endothermic?", "Exothermic"),
    ("What is the function of the liver?", "Detoxify and produce bile"),
    ("What organ is responsible for pumping blood?", "Heart"),
    ("What is a tsunami caused by?", "Underwater earthquake"),
    ("What is the unit of electric current?", "Ampere"),
    ("What’s the scientific name for water?", "H2O"),
    ("What causes seasons on Earth?", "Tilt of Earth's axis"),
    ("What is a renewable energy source?", "Solar energy"),
    ("What is the longest bone in the human body?", "Femur"),
    ("What part of the flower makes pollen?", "Anther"),
    ("What is the main function of the nervous system?", "Transmit signals"),
    ("What is a chemical reaction?", "Process where substances change into others"),
    ("Which field studies living organisms?", "Biology"),
    ("What is the outermost layer of the Earth?", "Crust"),
    ("What type of scientist studies weather?", "Meteorologist"),
    ("Which cell process divides one cell into two identical cells?", "Mitosis"),
    ("Which gas is essential for combustion?", "Oxygen"),
    ("What is the process of changing a solid directly to gas?", "Sublimation"),
    ("What is the function of chlorophyll?", "Absorb light for photosynthesis"),
    ("What causes acid rain?", "Sulfur dioxide and nitrogen oxides"),
    ("What’s the main cause of climate change?", "Greenhouse gases from human activity"),
    ("What is the phase of the moon when it is fully visible?", "Full moon"),
    ("What is a predator?", "An animal that hunts others for food"),
    ("What is the atomic number of carbon?", "6")


        ]
    }

}



class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Quiz with Wellness Break")

        self.student_id = ""
        self.mood = "happy"
        self.current_question = 0
        self.questions = []
        self.incorrect = []
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to the AI Quiz!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.continue_button = tk.Button(self.root, text="Continue", command=self.get_student_info)
        self.continue_button.pack(pady=5)

        self.break_button = tk.Button(self.root, text="Wellness-Break", command=self.start_break)
        self.break_button.pack(pady=5)

    def get_student_info(self):
        self.clear_widgets()

        self.label = tk.Label(self.root, text="Enter Student ID:", font=("Arial", 14))
        self.label.pack(pady=5)

        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack()

        self.label2 = tk.Label(self.root, text="Enter your mood:", font=("Arial", 14))
        self.label2.pack(pady=5)

        self.entry_mood = tk.Entry(self.root)
        self.entry_mood.pack()

        self.submit_info = tk.Button(self.root, text="Submit", command=self.ask_difficulty)
        self.submit_info.pack(pady=10)

    def ask_difficulty(self):
        self.student_id = self.entry_id.get().strip()
        self.mood = self.entry_mood.get().strip().lower()

        if not self.student_id:
            messagebox.showerror("Input Error", "Please enter your student ID.")
            return

        greeting_msg = greet_student(self.student_id, self.mood)
        messagebox.showinfo("Welcome", greeting_msg)

        self.show_topic_and_difficulty_selection()

    def show_topic_and_difficulty_selection(self):
        self.clear_widgets()

        self.label = tk.Label(self.root, text="Choose Subject and Difficulty", font=("Arial", 14))
        self.label.pack(pady=10)

        self.subject_var = tk.StringVar()
        self.difficulty_var = tk.StringVar()

        subject_label = tk.Label(self.root, text="Subject:")
        subject_label.pack()
        subject_menu = tk.OptionMenu(self.root, self.subject_var, "math", "science")
        subject_menu.pack()

        difficulty_label = tk.Label(self.root, text="Difficulty:")
        difficulty_label.pack()
        difficulty_menu = tk.OptionMenu(self.root, self.difficulty_var, "easy", "medium", "hard")
        difficulty_menu.pack()

        start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz)
        start_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.go_back_to_main_menu)
        back_button.pack(pady=5)

    def go_back(self):
     if self.current_question > 0:
        self.current_question -= 1
        self.show_question()
     else:
        messagebox.showinfo("Info", "You're at the previous question.")


        quiz_button = tk.Button(self.root, text="Take New Quiz", command=self.show_topic_and_difficulty_selection)
        quiz_button.pack(pady=5)

        break_button = tk.Button(self.root, text="Wellness Break", command=self.start_break)
        break_button.pack(pady=5)

        exit_button = tk.Button(self.root, text="Exit", command=self.exit_quiz)
        exit_button.pack(pady=5)

    def start_quiz(self):
        subject = self.subject_var.get()
        difficulty = self.difficulty_var.get()

        if not subject or not difficulty:
            messagebox.showerror("Error", "Please select both subject and difficulty!")
            return

        self.topic = subject
        self.difficulty = difficulty
        self.questions = random.sample(QUESTIONS[difficulty][subject], 95)
        self.current_question = 0
        self.score = 0
        self.incorrect = []
        self.show_question()

    def show_question(self):
        pygame.mixer.stop()
        self.clear_widgets()

        if self.current_question >= len(self.questions):
            self.show_score()
            return

        q, a = self.questions[self.current_question]
        self.correct_answer = a

        self.label = tk.Label(self.root, text=f"Q{self.current_question + 1}: {q}", font=("Arial", 14))
        self.label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack(pady=5)

        self.submit_btn = tk.Button(self.root, text="Submit Answer", command=self.check_answer)
        self.submit_btn.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.go_back)
        back_button.pack(pady=5)
        


    def check_answer(self):
        user_ans = self.answer_entry.get().strip().lower()
        correct_ans = self.correct_answer.lower()

        self.clear_widgets()

        if user_ans == correct_ans:
            self.label = tk.Label(self.root, text="✅ Correct!", fg="green", font=("Arial", 14))
            self.score += 1
        else:
            self.label = tk.Label(self.root, text=f"❌ Incorrect. Correct answer: {self.correct_answer}", fg="red", font=("Arial", 14))
            self.incorrect.append(self.questions[self.current_question])
        self.label.pack(pady=10)

        self.continue_btn = tk.Button(self.root, text="Continue", command=self.next_question)
        self.continue_btn.pack(pady=5)

        self.break_btn = tk.Button(self.root, text="Wellness-break", command=self.start_break)
        self.break_btn.pack(pady=5)

        exit_button = tk.Button(self.root, text="Exit", font=("Arial", 12), width=20, command=self.exit_quiz)
        exit_button.pack(pady=5)

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def start_break(self):
        self.clear_widgets()
        self.label = tk.Label(self.root, text="🧘 Taking a 2-minute break...\nPlease relax!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.root.after(2 * 60 * 1000, self.play_whisper)

    def play_whisper(self):
        WHISPER_SOUND.play(loops=-1)

        self.label = tk.Label(self.root, text="⏰ Break Over! Ready to continue?", font=("Arial", 14))
        self.label.pack(pady=10)

        self.continue_btn = tk.Button(self.root, text="Continue Quiz", command=self.show_question)
        self.continue_btn.pack(pady=10)

    def exit_quiz(self):
        self.root.destroy()

    def show_score(self):
        self.clear_widgets()
        msg = f"🎯 You scored {self.score} out of {len(self.questions)}!"
        self.label = tk.Label(self.root, text=msg, font=("Arial", 16))
        self.label.pack(pady=20)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop() 