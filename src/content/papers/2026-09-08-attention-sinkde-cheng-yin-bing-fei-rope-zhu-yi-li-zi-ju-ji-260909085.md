---
title: 'It''s Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing
  in Attention'
title_zh: Attention Sink的成因并非RoPE：注意力自聚集与Value不混合的作用
authors:
- Raito Kiya
- Satoki Ohashi
- Kosuke Sato
- Go Kamoda
- Ryosuke Takahashi
- Yuji Yamamoto
- Daiki Shiono
- Keisuke Sakaguchi
- Goro Kobayashi
affiliations:
- Tohoku University
- SOKENDAI
- NINJAL
- MBZUAI
- RIKEN
arxiv_id: '2609.09085'
url: https://arxiv.org/abs/2609.09085
pdf_url: https://arxiv.org/pdf/2609.09085
published: '2026-09-08'
collected: '2026-09-09'
category: LLM
direction: 大语言模型 · 注意力机制优化
tags:
- Attention Sink
- RoPE
- Value Mixing
- Quantization
- KV cache
one_liner: 揭示Attention Sink与大规模激活的核心成因是注意力自聚集与Value不混合，否定RoPE的主导作用
practical_value: '- 电商Agent、生成式推荐的LLM部署优化时，无需针对RoPE修改缓解Attention Sink，重点关注初始位置的Value不混合问题即可

  - 低比特量化（如端侧推荐Agent模型压缩）可针对性优化初始位置的Massive Activations，而非全量调整激活范围，提升量化精度

  - 长上下文LLM推理的KV cache优化（如用户长行为序列生成推荐）可利用自聚集位置的稳定性，简化缓存策略降低显存占用

  - 训练垂直领域电商LLM时，可在早期层添加微小注意力扰动破坏Value不混合状态，从根源降低Attention Sink强度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM普遍存在序列初始位置的Attention Sink（AS）与伴随的Massive Activations（MAs），MAs会严重阻碍低比特量化落地，此前研究普遍将成因归因为RoPE或BOS令牌，但具体机制不明确，难以针对性优化。

### 方法关键点
- 拆解初始位置的三类影响因素：BOS令牌、RoPE位置编码、因果掩码下的强制自聚集，通过对照实验逐一隔离变量
- 定义Value-non-mixing状态：注意力输出仅由当前令牌自身的Value向量构成，无其他令牌Value的混合
- 采用两类干预实验：修改非初始位置的注意力权重强制自聚集、构造重复令牌序列人为制造Value不混合状态，验证因果关联

### 关键实验结果
在WikiText、GSM8K、SlimPajama三个数据集上测试Llama2-7B、Llama3.2-3B、Mistral-7B、Qwen2-7B、Pythia-1B共5款主流RoPE-based模型：
1. 修改初始令牌的RoPE编码后，AS强度下降不超过2%，证明RoPE不是主导因素
2. 在非初始位置强制自聚集后，该位置的Sink值从接近0提升到0.47~0.84，同时出现明显MAs
3. 仅在模型早期层施加自聚集干预，即可达到全层干预90%以上的AS强度

### 核心结论
Attention Sink和大规模激活的核心驱动是因果掩码带来的早期层Value不混合状态，而非RoPE或BOS令牌本身
