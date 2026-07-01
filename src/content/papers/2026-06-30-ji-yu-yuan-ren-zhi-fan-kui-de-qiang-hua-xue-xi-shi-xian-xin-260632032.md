---
title: Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty
  Expression in LLMs
title_zh: 基于元认知反馈的强化学习实现LLM可信不确定性表达
authors:
- Gabrielle Kaili-May Liu
- Avi Caciularu
- Gal Yona
- Idan Szpektor
- Arman Cohan
affiliations:
- Yale University
- Google Research
arxiv_id: '2606.32032'
url: https://arxiv.org/abs/2606.32032
pdf_url: https://arxiv.org/pdf/2606.32032
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: LLM训练·元认知可信校准
tags:
- RLMF
- Metacognition
- Uncertainty Calibration
- Reinforcement Learning
- LLM Alignment
one_liner: 提出RLMF元认知反馈强化学习范式，实现LLM数值与语言级可信不确定性校准SOTA
practical_value: '- 电商导购/客服Agent场景可复用RLMF的元认知反馈思路，给RL优势项加自我评估准确率缩放系数，让Agent更清晰感知能力边界，降低高置信幻觉概率

  - 训练推荐/广告侧LLM生成模块时，可复用元认知数据选择方法，筛选模型自我评估分最高、最低的样本做训练，比随机/主动学习样本选择效果更好，提升小样本训练效率

  - 电商文案生成场景可复用「数值置信度→自然语言修饰词」的两步解耦架构，先训练模型输出句子级置信分，再根据场景灵活映射为不同风格的不确定表述，无需重复训练RL模块'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM普遍存在高置信幻觉、无法识别自身知识边界、内部不确定性与外在表达不一致的问题，在电商导购、医疗、法律等高风险场景会严重损害用户信任；现有可信校准方法仅覆盖语言层面不确定性，泛化性差、易降低任务准确率，且未实现数值+语言层面的全链路校准。

### 方法关键点
- 提出RLMF（元认知反馈强化学习）范式：在GRPO优势计算中，对任务表现高于平均的样本，额外用模型自我评估准确率Zg缩放置信校准的优势项，优先强化同时满足任务效果好、自我认知准的输出
- 提出元认知数据选择策略：筛选模型自我评估得分最高、最低的各一半样本做训练，效果优于随机、主动学习的样本选择方案
- 采用两步解耦校准架构：第一步用RLMF训练模型输出可靠的句子级数值置信分，第二步用轻量LLM将置信分映射为符合场景的自然语言模糊修饰词，支持灵活适配不同用户偏好无需重训RL模块

### 关键实验
在10个跨6+领域的任务上测试，对比MetaFaith、FUT等基线，以及GPT-5、Gemini-3.1-Pro等商用模型：RLMF比标准RL最高提升63%的可信校准效果，跨任务平均cMFG*达0.83以上，较基线方法最高提升29%；8B小模型的校准效果超过GPT-5等商用大模型37%，语言化不确定性的人类评估win率达96%以上，同时不损失任务准确率。

### 核心结论
基于模型元认知表现的内部反馈信号，比传统输出置信度类信号更适合作为RL训练的补充监督，能同时提升任务效果和模型的自我认知能力。
