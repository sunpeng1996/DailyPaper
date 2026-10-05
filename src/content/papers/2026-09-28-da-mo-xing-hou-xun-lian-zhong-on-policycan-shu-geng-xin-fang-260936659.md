---
title: On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training
title_zh: 大模型后训练中On-Policy参数更新方向是泛化能力的核心来源
authors:
- Shufan Shen
- Zhongni Hou
- Junshu Sun
- Yufei Zhang
- Wei Lin
- Guojun Yin
- Qingming Huang
- Shuhui Wang
affiliations:
- 中国科学院计算技术研究所
- 中国科学院大学
- 美团
arxiv_id: '2609.36659'
url: https://arxiv.org/abs/2609.36659
pdf_url: https://arxiv.org/pdf/2609.36659
published: '2026-09-28'
collected: '2026-10-05'
category: Training
direction: 大模型后训练 · 微调泛化性优化
tags:
- Supervised Fine-Tuning
- On-Policy Training
- Generalization
- Parameter Update
- LLM Post-Training
one_liner: 提出On-Policy方向约束的SFT方法OPSFT，兼顾SFT训练效率与on-policy范式的强泛化性
practical_value: '- 业务侧LLM微调（如商品文案生成、客服Agent、推荐理由生成）可先跑50~100步GRPO/OPD拿到更新方向，再用OPSFT做SFT，比直接SFT泛化性高2~8个百分点，比全量on-policy训练省50%以上时间

  - 已通过RLHF/on-policy训练完成的业务模型（如个性化文案生成模型），新增高质量标注数据时用OPSFT沿原有更新方向微调，不会破坏原有泛化能力，还可涨点2~3个百分点，避免重新跑全量RL流程

  - 垂直领域（如电商、游戏）小模型微调可复用同领域其他任务得到的on-policy更新方向，无需每个子任务单独跑on-policy训练，降低微调成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
SFT训练效率高、可直接利用高质量标注数据，但泛化性远弱于GRPO/OPD等on-policy后训练范式；现有研究多将on-policy的参数更新行为作为训练副产品，未挖掘其作为优化规则提升SFT泛化的潜力，需找到可迁移的on-policy优化特性打通两者优势。

### 方法关键点
- 理论+实验验证：SFT全程参数更新方向高度一致（不同阶段余弦相似度接近1.0），on-policy范式会持续调整更新方向（累计更新方向余弦相似度约0.5），该方向差异是两者泛化性差距的核心来源
- 设计OPSFT方法：首先用少量on-policy训练步骤得到累计更新的符号向量v∈{-1,0,1}^d，SFT训练时仅保留符号与v一致的梯度，优化器更新后再做二次方向校验，确保全程沿on-policy方向更新
- 支持两类落地场景：少量on-policy步骤锚定方向后做OPSFT提升训练效率；已完成on-policy训练的模型用OPSFT增量接入新高质量数据，避免能力退化

### 关键实验
基于Qwen3-1.7B/4B/8B、DeepSeek-R1等模型，在DeepMath数学推理、Eurus代码生成数据集测试，对比SFT、DFT、GRPO等基线：OPSFT比直接SFT平均涨点2~8个百分点，泛化性能匹配甚至超过全量GRPO，训练时间比GRPO减少50%以上（如Qwen3-8B上OPSFT耗时8.9h vs GRPO的19.3h，平均准确率41.67 vs 40.31）；已用GRPO训好的模型用OPSFT增量微调，比直接SFT避免了3~9个百分点的性能下降，还能进一步涨点；同领域内on-policy更新方向可跨数据集复用，跨域则不生效。

### 核心结论
只要约束更新方向匹配on-policy范式，SFT也能获得和on-policy相当的强泛化性，打破了“SFT只会记忆、RL才能泛化”的传统认知。
