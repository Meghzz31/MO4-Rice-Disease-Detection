from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import random

# Example data for remedies, precautions, and overviews. You can replace this with actual data retrieval logic, e.g., from a database or API.
disease_data = {
    "blast": {
        "overview": "Rice blast is a serious fungal disease caused by the fungus Pyricularia oryzae. It affects rice plants at all growth stages, causing lesions on leaves, necks, and grains.",
        "precautions": [
            "Use resistant varieties of rice.",
            "Ensure proper water management and drainage.",
            "Avoid excessive nitrogen fertilizer application.",
            "Remove infected plant debris."
        ],
        "remedies": [
            "Apply fungicides like Tricyclazole or Carbendazim.",
            "Spray with copper-based fungicides to control fungal growth.",
            "Use resistant rice varieties."
        ]
    },
    "bacterial blight": {
        "overview": "Bacterial blight is caused by the bacterium Xanthomonas oryzae. It leads to water-soaked lesions on leaves, which eventually dry out and turn yellow.",
        "precautions": [
            "Use certified disease-free seeds.",
            "Implement crop rotation and avoid growing rice in the same field every year.",
            "Use resistant varieties of rice."
        ],
        "remedies": [
            "Apply copper-based bactericides.",
            "Remove infected plants and dispose of them properly.",
            "Avoid over-irrigation to reduce the spread of bacteria."
        ]
    },
    "sheath blight": {
        "overview": "Sheath blight is caused by the fungus Rhizoctonia solani. It affects the rice plant's leaf sheaths and leads to the formation of lesions, reducing yields.",
        "precautions": [
            "Avoid over-crowding of plants and ensure proper spacing.",
            "Implement proper irrigation and drainage to prevent waterlogging.",
            "Use resistant rice varieties."
        ],
        "remedies": [
            "Apply fungicides like Validamycin or Propiconazole.",
            "Ensure proper nitrogen management.",
            "Use resistant rice varieties to reduce disease severity."
        ]
    },
    "brown planthopper": {
        "overview": "Brown planthopper (Nilaparvata lugens) is a major insect pest of rice. It damages the rice plants by sucking sap and transmitting viruses.",
        "precautions": [
            "Use resistant rice varieties.",
            "Control weeds that serve as hosts for the pest.",
            "Apply insecticides if necessary and monitor regularly."
        ],
        "remedies": [
            "Use neem-based insecticides or synthetic insecticides like Imidacloprid.",
            "Encourage natural predators of the planthopper like spiders and dragonflies.",
            "Apply biocontrol agents like Beauveria bassiana."
        ]
    },
    "false smut": {
        "overview": "False smut, caused by Ustilaginoidea virens, is a fungal disease that infects rice, particularly affecting the panicle, causing the formation of spore balls.",
        "precautions": [
            "Avoid over-fertilization, especially with nitrogen.",
            "Use certified disease-free seeds.",
            "Maintain proper water management."
        ],
        "remedies": [
            "Apply fungicides like Tricyclazole or Carbendazim.",
            "Ensure proper drainage and aeration to reduce moisture around the plants.",
            "Remove and destroy infected plants."
        ]
    },
    "leaf blast": {
        "overview": "Leaf blast is caused by the fungus Pyricularia oryzae, and it results in lesions on the leaves, causing them to brown and die, ultimately affecting yield.",
        "precautions": [
            "Use resistant rice varieties.",
            "Properly manage irrigation to avoid excessive moisture.",
            "Control weeds that may harbor the pathogen."
        ],
        "remedies": [
            "Apply fungicides like Tricyclazole or Propiconazole.",
            "Remove and destroy infected plant material.",
            "Use crop rotation to break disease cycles."
        ]
    },
    "bacterial leaf blight": {
        "overview": "Bacterial leaf blight is caused by Xanthomonas oryzae pv. oryzae, leading to the formation of water-soaked lesions on the rice plant leaves, which eventually turn yellow and die.",
        "precautions": [
            "Use disease-free seeds.",
            "Implement proper water management to avoid excess moisture.",
            "Avoid mechanical injury to plants."
        ],
        "remedies": [
            "Apply copper-based bactericides.",
            "Remove and destroy infected leaves.",
            "Use resistant rice varieties."
        ]
    },
    "stem rot": {
        "overview": "Stem rot is caused by Rhizoctonia solani and results in the rotting of rice plant stems, leading to lodging and reduced yields.",
        "precautions": [
            "Avoid over-watering, as it promotes fungal growth.",
            "Use well-drained soils.",
            "Maintain proper plant spacing to improve airflow."
        ],
        "remedies": [
            "Apply fungicides like Benomyl or Propiconazole.",
            "Remove infected plants and crop debris.",
            "Use resistant rice varieties."
        ]
    },
    "rice tungro": {
        "overview": "Rice tungro is a viral disease transmitted by the green leafhopper. It causes yellowing and stunting of the rice plant, leading to severe yield loss.",
        "precautions": [
            "Control leafhopper populations using insecticides.",
            "Use resistant rice varieties.",
            "Ensure proper field management to minimize vector transmission."
        ],
        "remedies": [
            "Use systemic insecticides like Imidacloprid.",
            "Remove and destroy infected plants.",
            "Control weed hosts that harbor the virus."
        ]
    },
    "downy mildew": {
        "overview": "Downy mildew is caused by the fungus Peronosclerospora, leading to yellowing of the rice plant leaves, often accompanied by a white fungal growth on the underside of the leaves.",
        "precautions": [
            "Avoid over-fertilization with nitrogen.",
            "Use resistant varieties of rice.",
            "Control weed growth and maintain proper irrigation."
        ],
        "remedies": [
            "Apply fungicides like Metalaxyl or Mancozeb.",
            "Improve soil drainage.",
            "Destroy infected plant material."
        ]
    },
    "white tip": {
        "overview": "White tip disease is caused by the rice white tip virus, which results in white lesions on rice leaves and can affect overall yield.",
        "precautions": [
            "Use certified virus-free seeds.",
            "Control leafhopper populations that spread the virus.",
            "Practice proper crop rotation and spacing."
        ],
        "remedies": [
            "Apply insecticides to control leafhopper populations.",
            "Remove and destroy infected plants.",
            "Use resistant rice varieties where available."
        ]
    },
    "rice yellow mottle virus": {
        "overview": "Rice yellow mottle virus (RYMV) causes yellowing and mottling on rice leaves, leading to reduced rice yield and quality.",
        "precautions": [
            "Use virus-free seeds.",
            "Control weed hosts of the virus.",
            "Control leafhopper populations that can spread the virus."
        ],
        "remedies": [
            "Use insecticides to control vector transmission.",
            "Remove and destroy infected plants.",
            "Practice crop rotation and use resistant varieties."
        ]
    },
    "rice blight": {
        "overview": "Rice blight, caused by various fungal pathogens, leads to the formation of lesions on rice leaves, causing wilting and yellowing. It severely affects rice growth and yields.",
        "precautions": [
            "Use resistant rice varieties.",
            "Implement crop rotation and avoid rice monoculture.",
            "Ensure proper water management to avoid excess moisture."
        ],
        "remedies": [
            "Apply fungicides like Tricyclazole or Propiconazole.",
            "Remove and destroy infected plant material.",
            "Ensure proper spacing between plants to improve airflow."
        ]
    },
    "sheath rot": {
        "overview": "Sheath rot is caused by the fungus Sarocladium oryzae and affects the leaf sheaths of rice plants, leading to lesions and decay, which significantly reduces yield.",
        "precautions": [
            "Avoid over-watering and ensure good drainage to prevent waterlogging.",
            "Use well-drained soils and ensure proper field sanitation.",
            "Use resistant rice varieties."
        ],
        "remedies": [
            "Apply fungicides like Validamycin or Carbendazim.",
            "Remove infected plant debris and avoid mechanical injury.",
            "Ensure proper nitrogen management to prevent disease spread."
        ]
    },
    "paddy rust": {
            "overview": "Paddy rust is a fungal disease caused by the fungus *Puccinia oryzae*. It affects rice plants, particularly during the flowering and grain-filling stages, leading to rust-colored lesions on leaves and stems, causing yield loss.",
            "precautions": [
                "Use resistant rice varieties.",
                "Avoid excessive nitrogen application, as it promotes fungal growth.",
                "Implement crop rotation to break the disease cycle.",
                "Remove infected plant material and debris."
            ],
            "remedies": [
                "Apply fungicides like Tricyclazole or Propiconazole to control fungal growth.",
                "Ensure proper spacing between plants to reduce humidity around the crop.",
                "Use resistant rice varieties to reduce disease severity."
            ]
    },
    "fungal infection": {
        "overview": "Fungal infections in rice plants are caused by a variety of fungi, leading to a wide range of symptoms such as lesions, discoloration, and decay of plant tissues. Common fungal diseases include rice blast, sheath blight, and false smut.",
        "precautions": [
            "Use resistant rice varieties to reduce the risk of fungal infections.",
            "Ensure proper water management to prevent waterlogging and excessive moisture.",
            "Implement crop rotation to break the fungal life cycle.",
            "Avoid overcrowding plants to improve air circulation and reduce humidity.",
            "Remove and destroy infected plant debris to reduce inoculum buildup."
        ],
        "remedies": [
            "Apply fungicides like Tricyclazole, Carbendazim, or Propiconazole to control fungal growth.",
            "Improve drainage in fields to prevent excessive moisture accumulation.",
            "Use copper-based fungicides to control a wide range of fungal pathogens.",
            "Incorporate organic matter to improve soil health and reduce fungal proliferation."
        ]
    },
    "paddy wilting": {
        "overview": "Paddy wilting is a condition where rice plants show signs of drooping, yellowing, and dying, usually due to water stress, root diseases, or environmental factors. It can also result from fungal infections like Fusarium wilt or from bacterial wilt.",
        "precautions": [
            "Ensure proper water management and irrigation to avoid both drought and waterlogging.",
            "Plant rice in well-drained soils to prevent root rot and wilting.",
            "Use disease-resistant rice varieties where available.",
            "Avoid planting rice in areas with a history of root diseases.",
            "Implement crop rotation to reduce the risk of soil-borne pathogens."
        ],
        "remedies": [
            "Apply fungicides like Carbendazim or Benomyl to control fungal infections affecting roots.",
            "Use systemic insecticides if insect pests are contributing to wilting.",
            "Improve soil aeration and drainage to reduce the impact of waterlogging.",
            "Remove and destroy infected plant material to prevent the spread of disease."
        ]
    }

    # Add more diseases here...
}


class ActionAskDiseaseOverview(Action):
    def name(self):
        return "action_provide_disease_overview"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.get_slot("disease")

        if disease in disease_data:
            overview = disease_data[disease]["overview"]
            # dispatcher.utter_message(text=f"Overview of {disease}: {overview}")
            dispatcher.utter_message(response="utter_disease_overview", **{"disease": disease,"info": overview})
        else:
            dispatcher.utter_message(response="utter_no_info", **{"disease": disease})

        return []

class ActionAskDiseasePrecautions(Action):
    def name(self):
        return "action_provide_disease_precautions"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.get_slot("disease")

        if disease in disease_data:
            precautions = disease_data[disease]["precautions"]
            precaution_text = "\n- ".join(precautions)
            # dispatcher.utter_message(text=f"Precautions for {disease}:\n- {precaution_text}")
            dispatcher.utter_message(response="utter_disease_precautions", **{"disease": disease,"info": precaution_text})

        else:
            dispatcher.utter_message(response="utter_no_info", **{"disease": disease})

        return []

class ActionAskDiseaseRemedies(Action):
    def name(self):
        return "action_provide_disease_remedies"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.get_slot("disease")

        if disease in disease_data:
            remedies = disease_data[disease]["remedies"]
            remedy_text = "\n- ".join(remedies)
            # dispatcher.utter_message(text=f"Remedies for {disease}:\n- {remedy_text}")
            dispatcher.utter_message(response="utter_disease_remedies", **{"disease": disease,"info": remedy_text})
        else:
            dispatcher.utter_message(response="utter_no_info", **{"disease": disease})

        return []
