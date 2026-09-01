---
title: Dynamic Important Example Mining for Reinforcement Finetuning
title_zh: 面向强化学习微调的动态重要样本挖掘框架DIEM
authors:
- Haoru Tan
- Sitong Wu
- Yanfeng Chen
- Shizhen Zhao
- Yang-Tian Sun
- Tianjia Liu
- Chirui Chang
- Shaofeng Zhang
- Samm Sun
- Xiuzhe Wu
affiliations:
- HKU
- Tencent Hunyuan Team
- CUHK
- Stanford
arxiv_id: '2608.29252'
url: https://arxiv.org/abs/2608.29252
pdf_url: https://arxiv.org/pdf/2608.29252
published: '2026-08-28'
collected: '2026-09-01'
category: Training
direction: 大模型强化微调 · 动态样本选择优化
tags:
- RFT
- gradient alignment
- dynamic sample selection
- sample reweighting
- GRPO
- RLHF
one_liner: 提出基于梯度对齐的动态样本重加权框架，仅加1.2%训练开销即可提升RFT性能1%-6%
practical_value: '- 做LLM Agent、生成式推荐的RLHF/GRPO微调时，可直接集成DIEM，仅需在梯度反传后新增梯度对齐计算和重加权两步，以1.2%的极低额外开销换1%-6%的性能提升，性价比极高

  - 推荐系统多场景样本动态采样可复用梯度对齐思路：无需额外训练样本价值预估模型，直接复用现有反传梯度计算单样本对当前batch更新的贡献，实现自适应重加权，无额外数据依赖

  - 训练课程设计可复用DIEM的自组织curriculum机制：无需人工设计样本难度分层规则，动态重加权会自然形成从易到难的学习节奏，可迁移到用户/Item冷启动训练、多任务权重动态调整场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有强化学习微调（RFT）的样本选择方法多为静态预筛选或基于启发式难度、reward方差的动态策略，默认样本价值固定，忽略了策略学习的非平稳动态性，易导致优化次优；且多数动态方法需要额外训练样本价值预估模型，训练开销高，落地难度大。
### 方法关键点
- 梯度对齐重要性估计：每步训练时直接复用反传得到的单样本梯度与batch聚合梯度，计算两者内积作为样本边际贡献的代理指标，无额外模型开销，有理论误差边界保证
- 约束批量重加权：构造带约束的优化问题，最大化批量总效用的同时要求重加权后梯度的L2范数与原梯度一致，避免更新步长波动影响训练稳定性，给出准闭式解，计算量极低
- 负权重裁剪：对求解出的负权重直接置0，过滤当前步对优化有害的样本，实现自适应样本过滤
### 关键实验
在LLM数学推理（MATH、Gaokao、AIME等）、多模态推理（MathVista、MMMU、AI2D等）benchmark上测试，对比GRPO、LIMR、HVS、SPEED-RL等基线：仅增加1.2%的训练开销，性能比基线GRPO提升1%-6%；7B多模态模型平均得分61.8%，超过GPT-4o的60.9%；32B多模态模型比Vanilla RFT提升2.4个百分点，在所有6个测试集上均取得最优结果。
最值得记住的一句话：RFT阶段的样本价值是随训练动态变化的，基于梯度对齐的自适应重加权是低成本大幅提升训练效率和模型性能的有效路径
