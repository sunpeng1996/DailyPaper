---
title: 'DONDO: Open w2v-BERT Speech-Recognition Base Models for African Languages'
title_zh: 面向27种非洲语言的开源w2v-BERT语音识别基础模型DONDO
authors:
- Paul Azunre
affiliations:
- Khaya AI
arxiv_id: '2607.21540'
url: https://arxiv.org/abs/2607.21540
pdf_url: https://arxiv.org/pdf/2607.21540
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 低资源语言多语种ASR模型开源
tags:
- ASR
- w2v-BERT
- Low-Resource-NLP
- Multilingual-Model
- Open-Source
one_liner: 开源覆盖27种非洲语言的w2v-BERT ASR模型，配套轻量语言控制机制，Apache2.0许可
practical_value: '- 面向非洲小语种出海的电商语音搜索、智能客服Agent业务，可直接复用这批Apache-2.0许可的ASR模型二次微调，大幅降低冷启动成本

  - 低资源小语种场景下，选用版权清晰的公开规整语料（如宗教文本）作为微调数据源的思路，可解决标注数据稀缺问题

  - 两步学习率退火微调策略：先高学习率适配多语言底座再退火调优，可迁移到小语种多任务模型微调场景，提升小语种任务效果

  - 推理时在输入特征前拼接语言ID前缀帧的轻量控制方法，可复用在多语言统一模型的推理路由设计，减少多模型部署成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
高资源语言ASR技术已成熟，但非洲等低资源语言极度缺乏标注音频数据，无可用本地化语音交互技术，制约相关业务落地。

### 方法关键点
1. 基于w2v-BERT 2.0 构建DONDO系列模型，包含21个单语言、5个多语言模型，覆盖27种非洲语言变体，微调采用版权清晰、拼写一致的宗教文本朗读音频，解决标注数据不足问题
2. 采用两步（部分模型三步）学习率退火微调流程：先以高学习率适配多语言共享底座，再退火调优，效果追平甚至超过单语言基线
3. 设计轻量语言条件机制，在声学特征前拼接one-hot语言ID前缀帧，单个多语言checkpoint推理时可定向适配目标语言

### 关键结果数字
多语言模型平均WER达10~13%，接近单语言模型效果，所有模型以Apache-2.0许可开源，覆盖约1亿母语使用者
