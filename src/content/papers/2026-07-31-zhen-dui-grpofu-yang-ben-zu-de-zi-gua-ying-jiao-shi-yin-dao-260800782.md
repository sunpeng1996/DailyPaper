---
title: 'Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups
  from Adaptive Teacher Guidance'
title_zh: 针对GRPO负样本组的自适应教师引导学习信号恢复方法
authors:
- Zhuowen Han
- Jinwei Xiao
- Zhengxi Lu
- Renren Jin
- Zhiyuan Yao
- Yuxin Liu
- Hongyan Hao
- Yueqing Sun
- Yu Yang
- Qi GU
affiliations:
- Tianjin University
- Meituan Longcat Team
arxiv_id: '2608.00782'
url: https://arxiv.org/abs/2608.00782
pdf_url: https://arxiv.org/pdf/2608.00782
published: '2026-07-31'
collected: '2026-08-06'
category: Training
direction: 大语言模型 RLHF 训练优化
tags:
- GRPO
- OPD
- RLHF
- Knowledge Distillation
- SFT
one_liner: 通过样本/Token级蒸馏选择+辅助SFT实现GRPO与OPD高效融合，提升LLM推理性能
practical_value: '- 训练电商导购/广告文案生成/客服Agent的RL模型时，可复用这套GRPO+OPD融合框架，仅对学生全错的负零方差样本做蒸馏，大幅降低训练开销的同时提升效果

  - Token级蒸馏选择trick可直接迁移：仅对学生熵高/师生分布差异大的Token计算蒸馏损失，既避免过早收敛到教师能力上限，又减少梯度噪声，还能缓解OPD常见的回复长度膨胀问题

  - 可在GRPO训练的全负样本组上补充教师生成的正确轨迹做SFT，注入正向梯度信号，解决全负样本组无有效学习信号的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GRPO是当前LLM RLHF后训练的主流范式，但存在奖励稀疏问题：当同组rollout全对/全错时（零方差prompt）会完全丢失梯度。On-Policy Distillation（OPD）虽能提供token级稠密监督，但朴素结合GRPO与OPD会导致性能下降，根源在于三个问题：不是所有样本都适合蒸馏、过快拟合教师会破坏RL探索能力、OPD优势不对称会压制大部分token的学习信号。

### 方法关键点
- **样本级选择**：仅对学生全错的负零方差prompt应用OPD，并用教师在该prompt上的成功率作为权重加权蒸馏信号，仅用3.63%的全量数据就能取得比全量OPD更好的效果
- **Token级选择**：仅对学生熵高（不确定性高）或师生分布差异大的token计算蒸馏损失，通过Soft-OR公式计算选择得分，取Top k%的token更新，缓解过早收敛与梯度噪声
- **辅助SFT**：在负零方差样本上补充教师预生成的正确轨迹做SFT，注入正梯度信号，解决OPD优势不对称的问题

### 关键结果
在Qwen2.5、Qwen3系列的3组师生模型对上验证，覆盖数学、代码两个领域，对比GRPO、朴素GRPO+OPD、ReLIFT、RL-ZVP等基线，RSTG相对朴素GRPO+OPD在数学任务最高提升+4.02%，代码任务最高提升+3.05%，同时缓解OPD的长度膨胀问题，减慢学生向教师的收敛速度，保留RL探索空间。

最值得记住的一句话：蒸馏不需要全量做，只在学生做错、教师做对的场景下针对性做细粒度蒸馏，就能以极低 overhead 实现效果提升。
