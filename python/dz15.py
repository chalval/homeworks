import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

# Класс модели
class DialogModel(nn.Module):
    def __init__(self, tokenizer):
        super().__init__()

        # BERT Encoder
        self.encoder = BertModel.from_pretrained('bert-base-cased')
        self.proj = nn.Linear(768, 512)

        # Transformer Decoder
        self.decoder = nn.TransformerDecoder(
            nn.TransformerDecoderLayer(d_model=512, nhead=8),
            num_layers=6
        )
        self.attention = nn.MultiheadAttention(512, 8)

        # Декодер токенов для генерации текста
        self.out = nn.Linear(512, tokenizer.vocab_size)

    def generate(self, x):
        # Декодируем токены
        out_tokens = self.out(x).argmax(-1)

        # Преобразуем токены в текст
        return tokenizer.decode(out_tokens)

    def forward(self, input_ids, attention_mask):
        x = self.encoder(input_ids, attention_mask)[0]
        x = self.proj(x)
        x = self.attention(x, x, x)[0]
        x = self.decoder(x, x)

        return self.generate(x) # генерация ответа

# Создаем токенайзер
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

# Инициализируем модель
model = DialogModel(tokenizer)

text = "Hello!"
inputs = tokenizer(text, return_tensors="pt")
output = model(inputs["input_ids"], inputs["attention_mask"])

print(output)

