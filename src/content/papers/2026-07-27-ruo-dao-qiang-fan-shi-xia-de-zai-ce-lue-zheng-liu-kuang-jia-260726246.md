---
title: Weak-to-Strong On-Policy Distillation
title_zh: 弱到强范式下的在策略蒸馏框架W2S-OPD
authors:
- Fangxu Yu
- Zinan Lin
- Xiaodong Liu
- Weijia Xu
- Michael Xu
- Tianyi Zhou
- Jianfeng Gao
affiliations:
- University of Maryland, College Park
- Microsoft Research
- MBZUAI
arxiv_id: '2607.26246'
url: https://arxiv.org/abs/2607.26246
pdf_url: https://arxiv.org/pdf/2607.26246
published: '2026-07-27'
collected: '2026-08-04'
category: Training
direction: LLM训练 · 弱到强在策略蒸馏
tags:
- On-Policy Distillation
- Weak-to-Strong
- Knowledge Distillation
- LLM Training
- Logit Engineering
one_liner: 通过弱模型对比对的logit差构造代理教师，无需强教师即可提升大模型的推理与代码能力
practical_value: '- 生成式推荐/电商Agent领域可复用该框架降低训练成本：先在小参数模型上做领域RL（如商品属性理解、用户query意图识别、导购话术优化），再通过RL前后的小模型logit差构造代理教师蒸馏大模型，避免大模型全量RL的高昂算力开销

  - 跨场景推荐大模型的多能力融合可采用多对比对logit差加权方案，一次蒸馏即可整合多领域能力，无需依次微调避免旧能力遗忘，适配电商多品类、多业务线的能力整合需求

  - 工程落地可复用Top-K logit截断技巧降低通信开销，仅传输教师top-K token的索引与概率，整体训练耗时仅比普通OPD高20%，可快速接入现有蒸馏pipeline'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有在策略蒸馏（OPD）要求教师能力不弱于学生，主流范式要么是大模型蒸馏小模型，在前沿大模型优化场景下无更强教师可用，性能天花板明显；要么是训练多个同规模领域专家再蒸馏回学生，训练成本极高。直接用弱教师蒸馏还会因分布偏移拉低学生原有性能，无法实现能力突破。
### 方法关键点
- 核心思路是提取弱模型的能力增量方向而非直接模仿弱教师：构造正负弱模型对比对，计算两者logit差值隔离出能力提升方向，叠加到学生自身base logit上构造代理教师，既保留目标能力方向又保证与学生分布接近，避免性能退化
- 支持三种低成本对比对实现：①小模型RL前后的checkpoint对，隔离RL注入的领域能力；②不同规模的开源小模型对，隔离模型缩放带来的通用能力；③同一小模型加正确/错误提示的输出对，隔离实例级正确方向
- 蒸馏目标为在学生自身生成的rollout上最小化与代理教师的逐token反向KL，支持多对比对加权融合，一次蒸馏即可整合多领域能力
### 关键实验
在4个数学推理、3个代码生成基准上测试，对比普通OPD：①用4B RL专家蒸馏8B学生时，数学推理准确率相对提升11.4%，甚至超过4B教师本身；②仅用4B和0.6B两个弱于学生的开源模型蒸馏，8B学生数学准确率绝对提升6%，代码提升1.2%；③OOD测试中比OPD在GPQA基准上高2.1%，不会损失学生原有通用能力。
### 核心结论
弱到强学习的核心是提取能力增量方向而非直接模仿弱教师，海量现有弱信号可用来持续提升前沿模型性能，无需等待更强教师迭代。
