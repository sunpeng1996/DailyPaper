---
title: 'PAWBench: How Far Are We from Probabilistically Aligned World Modeling?'
title_zh: PAWBench：我们距离概率对齐的世界建模还有多远？
authors:
- Yuandong Pu
- Le Zhuo
- Sayak Paul
- Gabriel Jorge Menezes
- Avram Đorđević
- Shiyang Li
- Yifan Zhou
- Bin Fu
- Wenlong Zhang
- Junjun He
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Krea AI
- Huggingface
- The University of Hong Kong
arxiv_id: '2608.27345'
url: https://arxiv.org/abs/2608.27345
pdf_url: https://arxiv.org/pdf/2608.27345
published: '2026-08-26'
collected: '2026-08-28'
category: Eval
direction: 世界模型评估 · 概率对齐
tags:
- World Model
- Evaluation Benchmark
- Probabilistic Alignment
- Video Generation
- Stochastic Sampling
one_liner: 提出概率对齐评估标准与PAWBench基准，量化现有世界模型的动态分布拟合差距
practical_value: '- 多模态交互Agent的动态轨迹预测可引入概率对齐思路，避免仅生成单条合理路径，拟合真实用户/场景的行为分布

  - 生成式内容推荐（如短视频、商品展示视频）的评估可复用PAWEval的分布级评估协议，替代现有单样本合理性评估，提升生成内容的多样性与真实度匹配

  - 大模型生成结果的不确定性校准可参考多次采样转经验分布的方法，优化生成结果的可控性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前视频生成模型常被用作世界模型，但现有评估仅校验单条生成视频的合理性，未验证相同初始条件下多次生成的行为分布是否与真实分布匹配，缺少分布级对齐的评估标准与基准。
### 方法关键点
1. 明确定义概率对齐作为世界模型的分布级评估准则；
2. 推出PAWBench基准，覆盖50种物理动态场景，可评估视频生成模型作为世界动态随机采样器的效果；
3. 提出PAWEval评估协议，将多次视频生成rollout转换为物理行为的经验分布，量化分布对齐程度。
### 关键结果
测试11个现有主流视频生成系统，无模型能在覆盖全部有效行为的同时匹配参考概率分布；验证了语言prompt、初始噪声采样、训练策略可一定程度调整模型的预测分布。
