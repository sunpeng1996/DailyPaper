---
title: Concept-Level Risk and Calibration for Governance in Diffusion Foundation Models
title_zh: 扩散基础模型治理中的概念级风险评估与校准
authors:
- Kun Xu
- Yushu Zhang
- Tao Wang
- Shuren Qi
- Barbara Carminati
- Elena Ferrari
- Yuming Fang
affiliations:
- Nanjing University of Aeronautics and Astronautics
- Jiangxi University of Finance and Economics
- City University of Hong Kong
- University of Insubria
arxiv_id: '2609.08517'
url: https://arxiv.org/abs/2609.08517
pdf_url: https://arxiv.org/pdf/2609.08517
published: '2026-09-08'
collected: '2026-09-11'
category: Other
direction: 扩散生成模型 · 安全治理与评估
tags:
- Diffusion Model
- Risk Assessment
- Model Governance
- Calibration
- Safety Audit
one_liner: 提出概念级概率审计校准框架，支持跨模型跨渠道的扩散生成系统统一安全治理评估
practical_value: '- 电商AIGC商品图/营销素材生成场景，可复用Concept Risk Operator框架，对敏感肖像、违规内容、品牌侵权风险做统一检测，覆盖prompt、embedding等多输入渠道的安全隐患

  - 可借鉴样本级事后校准方法，对AIGC内容审核的政策临界阈值做校正，减少误判漏判，降低合规风险

  - pooled多协议校准器可直接复用在生成式内容生产管线的后置审核模块，提升跨SD系列模型生成内容的安全评估可靠性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
扩散模型已成为多媒体生成核心范式，但其语义控制覆盖自然语言prompt、学习嵌入、干预管线等多渠道后，安全敏感、身份关联等隐私相关概念的安全治理缺乏统一评估方案，现有启发式审计、对抗探测等方法无法支持跨模型、跨渠道、跨部署条件的系统比对。
### 方法关键点
提出概念级概率审计校准框架CLRC：将治理相关概念行为形式化为随机生成诱导的伯努利语义事件，定义Concept Risk Operator映射模型-渠道配置到结构化风险画像，支持跨prompt接口、嵌入渠道、模型、部署条件的风险比对；配套样本级事后校准、配置级风险聚合策略。
### 关键结果
在SD1.5、SD2.1、SDXL上实验验证：嵌入访问、混淆prompt带来的风险常被标准prompt评估低估；pooled多协议校准器可提升留存集概率可靠性，仅用标准prompt训练的校准器无跨场景迁移性。
