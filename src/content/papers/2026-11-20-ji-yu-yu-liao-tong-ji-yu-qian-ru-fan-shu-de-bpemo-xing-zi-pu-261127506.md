---
title: How Many Bytes Has a BPE Model Seen? Estimating Byte-Token Exposure in Pretraining
  from Corpus Statistics and Embedding Norms
title_zh: 基于语料统计与嵌入范数的BPE模型字节token预训练曝光量估计
authors:
- Liwei Zhang
- ZhiMing Tong
- Mochen Guan
- Linzhe Li
affiliations:
- Landi Lab
- Antiy
arxiv_id: '2611.27506'
url: https://arxiv.org/abs/2611.27506
pdf_url: https://arxiv.org/pdf/2611.27506
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM tokenizer 预训练质量评估
tags:
- BPE
- Tokenizer
- Embedding Norm
- Pretraining
- UTF-8
- LLM
one_liner: 用语料统计+嵌入范数两种方法估算BPE单字节token预训练暴露量，验证13个非法UTF-8字节未被训练
practical_value: '- 多语言电商/Agent业务可参考论文给出的不同语言BPE fallback率数据，选择适配小语种的tokenizer或设计针对性微调策略，降低小语种用户query、商品标题的编码误差。

  - 对开源LLM做字节级改造（如处理特殊编码的商品属性、代码类query）时，可先通过嵌入范数快速判断字节token训练充分度，优先补充曝光量低的字节对应训练数据，降低微调成本。

  - 排查LLM业务异常输出时，可复用论文的零曝光基线方法：用padding/未使用token的嵌入范数做基准，快速识别欠训练的glitch token，提升异常case排查效率。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
字节级BPE自带256个单字节fallback token，是纯字节模型改造的核心基础，但工业级LLM预训练语料不公开，无法直接统计这些字节的实际训练量；而字节token的训练充分度直接影响LLM对特殊字符、小语种、编码异常文本的处理效果，对业务侧LLM改造、多语言适配至关重要。

### 方法关键点
- 语料统计路线：用待分析模型的tokenizer分词540MB公开多领域多语言语料（覆盖33种语言、40个领域，含维基、网页、对话、代码、数学语料），结合6种主流预训练语料混合比例，估算单字节token的出现频率。
- 嵌入范数路线：提取LLM的token embedding和lm_head矩阵的行范数，用从未参与训练的padding/未使用token作为零曝光基线，用已知频率的普通token构建校准曲线，反推字节token的等效曝光频率。

### 关键结果数字
- 单字节token中ASCII占比13~36%，合法UTF-8高字节（0x80~0xFF）仅占总token的0.15~0.27%（主流混合比例下），加入10%长尾语言后占比提升至0.66%；Qwen3 36T预训练规模下，每个合法高字节平均被看到~7×10^8次。
- 4款开源LLM（Qwen3.8-27B、Qwen3.5-9B、MiniCPM5-2B、MiniMax-M3.1-Flash）中，恰好13个无法出现在合法UTF-8中的字节（0xC0、0xC1、0xF5~0xFF）的嵌入范数和初始化基线完全一致，从未被训练。
- 范数反推的频率和语料统计结果误差在4倍以内（Qwen3.8），最小误差可达0.05 dex（MiniMax）。

**最值得记住的一句话**：BPE的256个单字节token训练程度差异极大，13个非法UTF-8字节完全未训练，不同语言的fallback率最多可差4个数量级，直接决定LLM对小语种的处理能力。
