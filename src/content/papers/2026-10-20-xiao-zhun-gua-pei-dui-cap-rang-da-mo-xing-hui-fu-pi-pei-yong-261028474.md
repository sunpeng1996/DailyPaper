---
title: 'Answering in the User''s Variety: Calibrated Accommodation Pairs for Post-Training'
title_zh: 校准适配对（CAP）：让大模型回复匹配用户语言变体的后训练方法
authors:
- Zhizhuo Kou
- Heming Li
- Jian Yang
- Junyu Luo
- Jingshu Peng
- Sirui Han
- Yike Guo
affiliations:
- The Hong Kong University of Science and Technology
- The Hong Kong University of Science and Technology (Guangzhou)
- Peking University
arxiv_id: '2610.28474'
url: https://arxiv.org/abs/2610.28474
pdf_url: https://arxiv.org/pdf/2610.28474
published: '2026-10-20'
collected: '2026-10-22'
category: Training
direction: LLM对齐 · 方言适配偏好优化
tags:
- DPO
- post-training
- LLM alignment
- dialect adaptation
- preference tuning
one_liner: 提出校准适配对CAP，通过DPO微调实现LLM方言适配且不侵入标准英语用户回复
practical_value: '- 做面向多区域用户的电商客服Agent时，可借鉴CAP的校准思路，让回复适配不同区域用户的方言/用语习惯，同时不干扰标准语用户的体验，提升用户好感度

  - DPO阶段构造正负样本时，可复用CAP的三样本设计：同时惩罚适配不足、过度适配、语言侵入三类负面case，比单纯单边正负对效果更可控

  - 做LLM输出风格对齐时，可借鉴论文的novel spans-only评估方法，排除用户输入重复内容的干扰，更准确衡量模型主动适配的效果

  - 多语言/多方言推荐系统个性化文案生成场景，可参考论文的阶段诊断方法，定位SFT/DPO哪个环节引入风格偏差，针对性优化'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前大模型经过SFT、DPO等后训练流程后，无论用户输入何种方言（非裔英语、新加坡英语等），都会统一输出标准英语，这种统一输出隐藏了训练阶段对不同方言的选择性偏好偏差，无法通过常规输出审计发现；同时现有单边方言适配方案易出现过度适配、向标准英语用户错误输出方言的问题，平衡适配性与无侵入性是核心痛点。

### 方法关键点
- 构建双请求对比测试集：同内容生成标准英语与6种不同声望等级方言的请求对，排除内容干扰衡量模型适配性
- 设计匹配奖励（MB）诊断指标：通过相邻训练阶段输出的似然对数比，定位SFT/DPO各阶段对不同方言的偏好偏差
- 提出校准适配对（CAP）：DPO样本对同时惩罚三种错误：适配不足、过度适配、向标准用户输出方言，三类样本比例为2:1:1

### 关键结果
在10个开源LLM谱系（OLMo、Tülu、Zephyr等）上验证：CAP在OLMo-2-1B上实现0.173的域外方言特征适配度提升，是单边适配方案的4倍；标准英语用户的方言插入率仅提升0.001/100词，无用户感知；指令跟随能力下降小于2.1个百分点，无显著损失。

统一的标准化输出会隐藏训练阶段的选择性偏好偏差，大模型审计既要关注外部输出行为，也要评估训练更新的内在偏好。
