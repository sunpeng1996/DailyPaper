---
title: 'MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive
  Morphological Alignment'
title_zh: 'MinGram: A Minimalist Unigram Tokenizer with High'
authors:
- Sander Land
arxiv_id: '2606.27019'
url: https://arxiv.org/abs/2606.27019
pdf_url: https://arxiv.org/pdf/2606.27019
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: The Unigram tokenizer uses an elegant representation which makes it straightforward
  to edit voc...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

The Unigram tokenizer uses an elegant representation which makes it straightforward to edit vocabularies, but its training is comparatively heavy and complex. We introduce MinGram (Minimalist Unigram), which keeps the token-list representation but simplifies training using a BPE-derived seed vocabulary, Hard EM on a minimum-token path, and a single flat score-pruning step. This removes the suffix array, the forward-backward pass, and the iterative prune loop, leaving a procedure that requires little beyond tokenizer inference itself. By making token count the primary objective and using a Unigram score only as a tiebreak, MinGram keeps the compression of pure token-count methods while retaining much of the morphological alignment and downstream quality of probabilistic ones. Across six languages, MinGram compresses better than both BPE and standard Unigram, and a compression-oriented variant matches the strongest token-count compressors while retaining substantially higher morphological alignment. In controlled downstream language-model training, Unigram-family tokenizers, with MinGram among the best, consistently beat BPE in bits-per-byte.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
