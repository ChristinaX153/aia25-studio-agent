from server.config import *


def classify_input(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        Your task is to classify if the user message is related to architecture, spatial organization, or furniture arrangement.
                        Output only the classification string.
                        If it is related, output "Related", if not, output "Refuse to answer".

                        # Example #
                        User message: "How do I bake cookies?"
                        Output: "Refuse to answer"

                        User message: "Where should I place the desk to get better daylight?"
                        Output: "Related"
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def generate_concept(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are a visionary intern at a leading architecture firm.
                        Craft a short, poetic, and evocative spatial concept for how furniture could be positioned within a space given the environmental conditions.
                        Use sensory and spatial language. Keep it to one paragraph.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        What is the concept for this building? 
                        Initial information: {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def extract_attributes(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """

                        # Instructions #    
                        You are a keyword extraction assistant for interior architecture.
                        Your task is to read a given text and extract keywords into three categories: furniture, comfort, and placement.

                        {
                          "furniture": "keyword1, keyword2",
                          "comfort": "keyword3, keyword4",
                          "placement": "keyword5, keyword6"
                        }

                        # Rules #
                         If a category has no keywords, write "None".
                         Use only concise, meaningful keywords.
                         Do not include explanations, markdown, or formatting.
                         Do not output anything other than the valid JSON.

                        # Category guidelines #
                        Furniture: Specific items mentioned (e.g., sofa, desk, bed, chair, cabinet).
                        Comfort: Terms related to comfort/environment (e.g., daylight, glare, temperature, PMV, privacy).
                        Placement: Spatial clues or zones (e.g., near window, center, corner, away from door, next to wall).
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        # GIVEN TEXT # 
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def create_question(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        # Instruction #
                        You are a thoughtful research assistant specializing in interior architecture and spatial optimization.
                        Your task is to create an open-ended question based on the given text.
                        The question should explore ideas about how furniture placement can respond to environmental conditions such as daylight, comfort, and spatial layout.
                        Imagine the question will be answered using design research, precedents, or architectural strategies.
                        The question should feel exploratory and intellectually curious.
                        Output only the question, without any extra text.

                        # Examples #
                        - How can furniture placement strategies enhance thermal and visual comfort in small living spaces?
                        - What are spatial techniques for optimizing desk placement in naturally lit interiors?
                        - How do architects balance privacy and daylight access when arranging bedroom furniture?
                        - In what ways can furniture arrangement respond to passive environmental conditions?
                        - Which design approaches use flexible furniture zones to adapt to varying environmental conditions?

                        # Important #
                        Keep the question open-ended, encouraging exploration, examples, or speculative design approaches.
                        Ensure the question connects naturally to the core themes present in the input text.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content
