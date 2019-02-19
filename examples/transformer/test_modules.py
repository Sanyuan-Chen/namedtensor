from namedtensor import ntorch
from modules import *

def test_attention():
    query = ntorch.randn(10, 6, 256, names=("batch", "target", "hidden"))
    key = ntorch.randn(10, 5, 256, names=("batch", "src", "hidden"))
    value = ntorch.randn(10, 5, 256, names=("batch", "src", "hidden"))
    mask = ntorch.randint(1, (6, 5), names=("target", "src")).byte()

    mod = Attention(0.5, 0.1).spec("hidden", "src")
    mod(query, key, value, mask)

    mod = MultiHeadedAttention(8, 256, 0).spec("hidden", "src")
    mod(query, key, value, mask)


def test_label():
    vocab = 100
    classes = ntorch.randn(5, vocab, names=("batch", "classes"))
    target = ntorch.randint(vocab, (5,), names=("batch"))
    mod = LabelSmoothing(0.1, vocab, 0).spec("batch", "classes")
    mod(classes, target)


# def test_all():
#     EncoderDecoder()