---
title: 'Alignment without Transfer: Tokenization Impacts Cross-lingual Representations
  during Multilingual Language Model Pretraining'
title_zh: 多语言大模型预训练中分词策略对跨语言表示的影响机制
authors:
- Jonathan von Rad
- Pontus Stenetorp
- Yao Lu
affiliations:
- University College London
arxiv_id: '2611.27491'
url: https://arxiv.org/abs/2611.27491
pdf_url: https://arxiv.org/pdf/2611.27491
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 多语言LLM · 分词与跨语言表示优化
tags:
- Multilingual-LLM
- Tokenizer
- Cross-lingual-Alignment
- Cross-lingual-Transfer
- Pretraining
one_liner: 通过受控训练39个1B规模多语言模型 揭示跨语言对齐与迁移的解离效应及分词的作用机制
practical_value: '- 跨境电商多语言Agent/推荐系统选型时，无需为了提升跨语言迁移效果额外投入资源优化分词策略，对齐提升不必然带来下游迁移收益

  - 做多语言商品知识问答/多语言Query理解场景时，优化目标语言词汇分配可提升FFN层知识共享度，降低多语言模型参数冗余，适合小部署场景

  - 跨脚本（如中英、中阿）跨境场景下，不要指望优化分词解决脚本屏障，需针对性采用音译、语言专属微调等方案适配

  - 做多语言小模型蒸馏时，采用公平分词的预训练模型知识更早出现在中低层，可选取浅层特征蒸馏，降低训练成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言LLM在低资源语言上表现普遍弱于英语，大多依赖高资源语言的跨语言迁移能力补全效果；此前研究发现分词的词汇分配不均会降低低资源语言性能，但分词如何影响跨语言表示对齐、参数知识共享与迁移效果三者的关系长期不明确，且多数研究仅关注输出层对齐，忽略模型全层的表示动态。

### 方法关键点
- 固定词表大小为64k，训练4种覆盖不同语言数量的分词器，控制其余变量完全一致，预训练39个1B参数的LLaMA风格单/双语模型，覆盖英、德、法、阿拉伯、中文5种语言，含同脚本、跨脚本两类语言对
- 采用MEXA指标测量全层跨语言表示对齐，设计FFN神经元消融实验量化跨语言参数知识共享率，使用bits-per-byte（BPB）作为损失指标避免分词差异对迁移效果评估的干扰

### 关键结果
- 更公平的目标语言词汇分配可使模型中低层（0-8层）跨语言对齐最高提升40%，知识解码层提前0.2~2层，但跨语言迁移效果波动不超过0.5个百分点，二者存在完全解离效应
- 跨脚本语言对的迁移效果比同脚本语言对低30%以上，且该差距不受分词优化影响，证明脚本屏障不是分词导致的伪影
- 公平分词可使同脚本语言的跨语言知识共享率最高提升65%，但中文等表意文字的提升效果有限

跨语言表示对齐的提升不必然带来跨语言迁移效果的提升，脚本差异是多语言迁移的核心瓶颈，无法仅通过优化分词解决。
