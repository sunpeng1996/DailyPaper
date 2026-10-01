---
title: 'DuoOPD: Learning from Joint Teacher-Student Outcomes for Multi-Task On-Policy
  Distillation'
title_zh: DuoOPD：基于师生联合输出的多任务在路蒸馏方法
authors:
- Ao Yu
- Weibo Gao
- Heng Zhou
- Linan Yue
- Rui Li
- Suyi Liu
- Yu Yan
- Yizhong Zhang
- Qi Liu
affiliations:
- University of Science and Technology of China
- The Hong Kong Polytechnic University
- The University of Hong Kong
- Southeast University
arxiv_id: '2609.33711'
url: https://arxiv.org/abs/2609.33711
pdf_url: https://arxiv.org/pdf/2609.33711
published: '2026-09-26'
collected: '2026-10-01'
category: Training
direction: LLM训练 · 多任务在路知识蒸馏
tags:
- Knowledge Distillation
- On-Policy Distillation
- Multi-Task Learning
- LLM Training
one_liner: 基于师生联合输出的通用多任务在路蒸馏方案，无需任务配置效果远超基线
practical_value: '- 垂域小模型蒸馏（如电商文案生成、推荐理由生成模型）可复用四分支反馈规则，避免大模型teacher答错时擦除小模型已有的正确响应，保留小模型在垂域的特有优势

  - 多场景/多任务联合训练时，借鉴任务内共享权重的设计，对teacher答错学生答对的样本按场景分配独立正反馈权重，适配不同场景的输出分布差异

  - 工程实现时可预缓存teacher输出和验证结果，仅在teacher正确学生错误的场景下引入teacher参考上下文，仅增加不到10%的训练算力即可获得显著效果提升

  - 反馈权重计算用Softplus替代传统门控函数，解决正确样本反馈强度不足的问题，无需额外算力即可稳定提升蒸馏效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-Policy Distillation（OPD）未考虑师生模型输出的正确性差异，常出现压制学生正确响应、老师答错时提供错误反馈的问题；多任务场景下不同任务的师生正确率分布差异大，缺乏通用反馈规则适配所有任务。
### 方法关键点
- 统一四分支反馈规则：基于师生输出的二元验证结果组合（都对/都错/仅老师对/仅学生对）分别处理：师生同对时用Softplus加权正向反馈，同错时加权负向反馈，仅老师对时引入老师正确答案作为老师侧评分上下文修正学生错误，仅学生对时按任务共享正反馈权重强化学生正确响应
- 无任务特定配置，所有任务共用同一套规则，仅通过任务对应的验证器适配不同任务的输出校验需求
- 预缓存所有训练样本的老师输出和验证结果，仅在仅老师正确的场景下才引入参考上下文，降低额外算力开销
### 关键实验
跨Qwen3、Llama两个主流模型族，覆盖科学计算、指令遵循、代码生成3类异构任务混合场景，对比5种OPD基线方案：DuoOPD在Qwen3上比原生OPD宏观准确率高2.58个百分点，Llama上高5.98个百分点，在所有场景的最难任务上均取得最优效果；额外算力开销仅比原生OPD高0.7%（Qwen3）到7.3%（Llama）。
### 核心结论
蒸馏时由学生的输出正确性决定反馈方向，师生联合输出决定反馈的具体分配，既能充分学习老师的知识，又能保留学生自身已有的优势能力
