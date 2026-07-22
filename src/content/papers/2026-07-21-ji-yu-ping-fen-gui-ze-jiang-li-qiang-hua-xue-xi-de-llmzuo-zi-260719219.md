---
title: 'Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via
  Reinforcement Learning with Rubric Rewards'
title_zh: 基于评分规则奖励强化学习的LLM作文自动打分与反馈生成框架
authors:
- Xuefeng Jin
- Jiashuo Zhang
- Teng Cao
- Bin Yang
affiliations:
- Alibaba Cloud Computing, Alibaba Group
arxiv_id: '2607.19219'
url: https://arxiv.org/abs/2607.19219
pdf_url: https://arxiv.org/pdf/2607.19219
published: '2026-07-21'
collected: '2026-07-22'
category: LLM
direction: LLM下游优化 · 细粒度规则奖励RL
tags:
- Reinforcement Learning
- LLM Fine-tuning
- Automated Evaluation
- Reward Engineering
- Ordinal Classification
one_liner: 提出RLAES统一框架，通过细粒度评分规则奖励RL联合优化作文打分准确率与反馈质量
practical_value: '- 多目标RL优化可复用AGFO自适应门控思路：对评估成本高的目标（如LLM-judge评估的文案/推荐理由满意度）设置定期校验阈值，达标后暂停该目标的评估与优化，可大幅降低训练开销，同时避免单目标优化导致的副产物质量退化

  - 生成内容的自动化评估可复用RFE框架：将业务规则拆解为细粒度二元可校验项，用LLM-as-judge输出量化评分，相比语义相似度类指标，与专家偏好对齐度提升超40%，可直接作为RL奖励信号

  - 序数分类任务可复用ACR思路：在商品星级预测、用户满意度分层、内容质量分排序等场景，引导模型显式对比相邻等级的差异，可在零/少样本场景下降低相邻类混淆，提升分类准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM作文打分与反馈生成方案多依赖prompt工程或监督微调，RL后训练的优化方式探索不足；同时反馈质量缺乏可量化、可直接作为训练奖励的自动化评估方法，仅优化打分目标会导致反馈质量严重退化，序数分类固有的相邻分混淆问题也未得到有效解决。
### 方法关键点
- 构建RFE细粒度反馈评估框架：覆盖4个维度共166条二元可校验评分规则，通过LLM-as-judge输出可量化的反馈质量评分，可直接转换为RL训练的奖励信号
- 设计AGFO自适应门控优化机制：RL训练过程中定期触发LLM-as-judge评估反馈质量，若得分达标则暂时关闭反馈奖励，仅优化打分目标，大幅降低高成本的LLM-judge调用频次
- 提出ACR相邻对比推理策略：引导模型显式回答「为什么不打相邻更高/更低分」的问题，缓解序数分类的相邻等级混淆问题，零/少样本场景下效果提升显著
### 关键实验结果
在ASAP公开作文打分基准上，RLAES-AGFO的QWK得分达0.803，为当前LLM-based方法最优，接近人类打分员的0.805；反馈质量RFE得分达0.8399，与GPT-5.5的0.8334相当；RFE框架对好坏反馈的pairwise判别准确率达100%，远超BERTScore的51.3%，与专家偏好对齐度达93%。
> 最值得记住的一句话：多目标RL优化中，对评估成本高的目标设置自适应触发门控，可在几乎不损失效果的前提下大幅降低训练开销，同时避免单目标优化带来的副产物质量退化
