---
title: Best-of-$N$ TTS Evaluation is Confounded by ASR Family Alignment
title_zh: 《Best-of-N TTS评估中的ASR家族对齐偏差问题》
authors:
- Taehyung Yu
- Seongjae Kang
affiliations:
- KAIST, Daejeon, South Korea
arxiv_id: '2607.08256'
url: https://arxiv.org/abs/2607.08256
pdf_url: https://arxiv.org/pdf/2607.08256
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 语音合成评估 · 偏差校正与集成
tags:
- TTS
- ASR
- Best-of-N
- Evaluation
- Ensemble
one_liner: 发现TTS Best-of-N评估存在ASR家族对齐偏差，提出跨家族排序集成方法降低WER
practical_value: '- 若业务涉及语音合成场景（如语音导购、有声商品介绍）的Best-of-N优化，需避免仅采用单ASR家族作为验证器，防止结果过拟合产生评估偏差

  - 跨模型家族的排序集成策略（秩平均、联合最大秩）可直接复用在多候选选优场景（如广告文案、商品标题多候选打分排序），降低单一评估模型的固有bias

  - 做模型效果离线/在线评估时，优先采用跨来源评估器三角验证作为默认流程，避免单评估器导致的结果虚高问题'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：零样本TTS的Best-of-N（BoN）推理通过ASR验证器从N个生成候选中选优，可大幅降低内容错误，但现有评估普遍采用单一固定ASR作为评估器，存在未被披露的系统性偏差。
**方法关键点**：1. 证实BoN评估存在ASR家族对齐混淆：即使不同ASR的线性CKA表征相似度达0.978，同家族的验证器-评估器组合可获得2-3倍于跨家族组合的oracle提升空间，跨家族组合甚至会出现验证器排名反转。2. 提出两种无训练开销的跨家族排序集成方案：秩平均、联合最大秩，提升评估鲁棒性。
**关键结果**：在LibriSpeech-PC测试集N=10时，跨家族集成方案平均WER达1.61%，相对F5-TTS基准降低12%；最优单验证器在官方F5-TTS评估器下WER从2.06%降至1.72%，相对下降16.5%，且SIM-o/UTMOS语音质量指标无明显退化。
