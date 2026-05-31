# Conceptualizing Synthetic Data Generation
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.datasets.demo import download_demo

# 1. Selection: Load your real (but small) Gold Price dataset
real_data, metadata = download_demo(modality='single_table', dataset_name='fake_hotel_guests')

# 2. Mining/Transformation: Train the Generative Model
synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(real_data)

# 3. Generation: Create 1,000 new 'synthetic' observations
synthetic_data = synthesizer.sample(num_rows=1000)

# Now you have a massive dataset for your 'Gold Bot' to train on!
print(synthetic_data.head())