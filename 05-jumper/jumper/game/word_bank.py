import random
class WordBank():
    """
    Randomly selects a word from a list of words
    """
    def __init__(self):
        self.words = random.choice(['deception', 'snowman', 'closet', 'complete', 'kingpin', 'options', 'python', 'basketball', 'elephant', 'xylophone',
        'mother', 'cashew', 'mountain', 'toothbrush', 'tarantula', 'salesman', 'cobbler', 'chocolate', 'security', 'poltergeist',
        'hibernation', 'infant', 'bipolar', 'gucci', 'quaker', 'crystal', 'ibuprofen', 'arrangement', 'recycle', 'frosted',
        'sombrero', 'pocket', 'kindergarden', 'anaconda', 'pillar', 'water', 'sweating', 'arrowhead', 'cupcake', 'attachment',
        'empire', 'squid', 'switch', 'haunting', 'cactus', 'circle', 'dimension', 'grandma', 'electric', 'dazzle', 'francium',
        'igneous', 'garlic', 'castle', 'coconut', 'nightmare', 'inside', 'horror', 'camping', 'pride', 'gluttony', 'organs',
        'waffle', 'funniest', 'monster', 'blizzard', 'bright', 'flower', 'religion', 'explore', 'figure', 'remember', 'mannequin',
        'capitol', 'principle', 'bedrock', 'iconic', 'mystery', 'mission', 'honeycomb', 'tampered', 'listen', 'banchie',
        'pumpkin', 'gorilla', 'english', 'machine', 'outfit', 'eternals', 'salty', 'eight', 'cookie', 'roasted', 'nutrition', 
        'backpack', 'heater', 'sloth', 'jalapeno', 'anxious', 'computer', 'sweater', 'marriage', 'formula', 'signal', 'unholy',
        'pizza', 'kangaroo', 'storage', 'pioneer', 'christmas', 'freshness', 'resist', 'borrow', 'monkey', 'spring', 'signature',
        'magazine', 'deposit', 'heaven', 'exorcism', 'cardinal', 'principal', 'garden', 'baseball', 'minute', 'enormous', 
        'racket', 'potato', 'terminate', 'bewildered', 'temporary', 'torment', 'inviting', 'guessing', 'kettle', 'climb', 'thing',
        'hidden', 'assassination', 'literature', 'liberate', 'locked', 'nothing', 'everything', 'painting', 'movement', 'watching',
        'picture', 'camera', 'chihuahua', 'programming', 'trapped', 'graveyard', 'zombie', 'chicken', 'citrus', 'relative', 'asphalt',
        'shingle', 'physics', 'omega', 'diaper', 'domination', 'zipper', 'running', 'strange', 'alcohol', 'poisoning', 'floating',
        'escaped', 'rainbow', 'brass', 'comedy', 'cheese', 'calories', 'vinegar', 'quote', 'together', 'shining', 'valve', 
        'ballerina', 'astray', 'entity', 'darkness', 'fragrant', 'similar', 'growth', 'producer', 'impressed', 'memories',
        'archer', 'split', 'cargo', 'leadership', 'bridge', 'punched', 'indigo', 'fishing', 'village', 'monument', 'piano', 'orange',
        'mouse', 'almond', 'cholesterol', 'dinosaur', 'enrages', 'drinking', 'stolen', 'exclamation', 'umbrella', 'chimney', 'scared', 
        'present', 'projection', 'complementary', 'perfection', 'lightbulb', 'refreshing', 'turtle', 'botched', 'quarterback',
        'captain', 'igloo', 'towering', 'friendship', 'unworthy', 'overalls', 'grabbed', 'wrapping', 'hurry', 'gasoline', 'fossil',
        'galaxy', 'cooperate', 'bulldog', 'sodium', 'shrimp', 'lonely', 'shadow', 'sewers', 'birthday', 'criminal', 'angry', 
        'promise', 'burning', 'quickly', 'foxtrot', 'laziness', 'puppeteer', 'retirement', 'controller', 'remote', 'weekend',
        'shield', 'vigilant', 'disarray', 'microscopic', 'buzzsaw', 'whiskey', 'stairs', 'salmon', 'bucket', 'hoarders', 
        'khakis', 'apology', 'knocking', 'reaper', 'humidifier', 'discrimination', 'sponge', 'sedimentary', 'rhetoric', 'hurting',
        'undertake', 'surfing', 'crispy', 'slender', 'arrival', 'effective', 'mankind', 'widget', 'screwdriver', 'extras', 
        'furnace', 'gloves', 'quarter', 'daylight', 'hydraulics', 'calling', 'hallucination', 'routine', 'coincidence', 'ocean',
        'oatmeal', 'casually', 'pentagon', 'symbol', 'doorknob', 'violin', 'hunter', 'season', 'pretty', 'false', 'flamingo',
        'vacumn', 'flashlight', 'vengeful', 'huckleberry', 'adventures', 'overdrive', 'rewind', 'rambling', 'radiation', 'helium',
        'wallpaper', 'pancake', 'bathtub', 'corridor', 'fantastic', 'danger', 'country', 'decades', 'distance', 'dominate', 'princess',
        'creation', 'millennial', 'generator', 'battery', 'providence', 'crusade', 'amazing', 'suction', 'skeleton', 'allocation',
        'jewel', 'healthy', 'flight', 'narcissist', 'manuel', 'walking', 'designated', 'trombone', 'ethernet', 'omware', 'transmition'])   