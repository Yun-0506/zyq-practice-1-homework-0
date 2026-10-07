from pathlib import Path
import torch
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from transformers import AutoImageProcessor, ResNetForImageClassification
from tqdm import tqdm

torch.manual_seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
checkpoint = "microsoft/resnet-50"
processor = AutoImageProcessor.from_pretrained(checkpoint)
model = ResNetForImageClassification.from_pretrained(
    checkpoint, num_labels=10, ignore_mismatched_sizes=True,
    id2label={i: str(i) for i in range(10)},
    label2id={str(i): i for i in range(10)},
).to(device).eval()

dataset = MNIST(root="data", train=False, download=True)
loader = DataLoader(dataset, batch_size=16,
                    collate_fn=lambda batch: tuple(zip(*batch)))
correct = total = 0
with torch.inference_mode():
    for images, labels in tqdm(loader):
        images = [image.convert("RGB") for image in images]
        inputs = processor(
            images=images, do_resize=True, return_tensors="pt"
        ).to(device)
        predictions = model(**inputs).logits.argmax(dim=1)
        targets = torch.tensor(labels, device=device)
        correct += (predictions == targets).sum().item()
        total += targets.numel()

result = f"MNIST test accuracy={correct / total:.2%} ({correct}/{total})"
print(result)
Path("accuracy.txt").write_text(result + "\n", encoding="utf-8")