---
title: 'On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models'
title_zh: 仅需主题引导的大模型无数据同策略自训练框架OPST
authors:
- Leon Sick
- Lukas Hoyer
- Yannick Strümpler
- Christian Reisswig
- Timo Ropinski
- Federico Tombari
affiliations:
- Google
- Ulm University
arxiv_id: '2610.32770'
url: https://arxiv.org/abs/2610.32770
pdf_url: https://arxiv.org/pdf/2610.32770
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: 大模型训练 · 无标注数据自提升
tags:
- Self-Training
- On-Policy Distillation
- Data-Free Training
- Multi-Modal
- Self-Improvement
one_liner: 仅用粗粒度主题描述生成训练数据，无需人工标注实现大模型多模态推理能力自提升
practical_value: '- 垂直领域LLM微调时，可复用「主题引导样本生成+伪验证/共识门双过滤」流程，低成本生成电商客服、商品文案等场景的训练数据，大幅降低人工标注成本

  - 用自生成数据做模型迭代时，优先采用EMA教师+特权信息不对称输入架构，将生成样本作为教师上下文而非学生模仿目标，抗噪性远高于直接SFT生成数据

  - 推荐系统的语义表征微调场景，可复用共识门机制自动筛选模型当前能力边界的训练样本，实现课程式学习，避免无效训练，提升表征迭代效率

  - 多模态商品问答、图文推荐场景，可复用视觉OPST框架，基于无标注商品图像生成训练数据，低成本提升多模态模型的推理准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型后训练方法（SFT、RLHF、同策略自蒸馏等）均依赖人工标注的问答对、问题集或监督信号，标注成本极高；现有自训练方案仍需人工 curated 问题集，无法完全摆脱人工干预，探索无外部标注的大模型自提升路径对降本增效具备极高工程价值。
### 方法关键点
- 仅输入粗粒度主题描述，由模型自行生成问题、推理过程、候选答案作为训练数据，无需任何人工标注的问题或答案
- 双层过滤机制：伪验证（重跑原问题、改写后问题答案一致）筛除歧义/无效样本，共识门（学生多次采样答案全一致则丢弃）筛除模型已掌握的简单样本，自动适配模型当前能力的课程
- 不对称特权信息训练架构：EMA教师可见生成的推理+答案，学生仅可见问题，学生通过匹配教师的token分布完成自蒸馏，而非直接模仿生成答案
- 支持多模态扩展：视觉OPST可基于无标注图像+视觉主题生成VQA训练数据，仅需无标注样本即可提升多模态能力
### 关键结果
在Gemma 4系列模型上测试，对比SFT、GRPO基线：
- 纯文本场景：Gemma 4 E2B无thinking模式下MMLU提升10.2pt，GPQA提升4.0pt，HellaSwag提升7.5pt，平均增益较同数据SFT高5.6pt；带thinking模式下GSM8K提升8.2pt
- 多模态场景：Gemma 4 E2B多模态版本VQAv2准确率提升6.9pt，POPE F1提升2.4pt
- 抗噪性：即使75%生成答案错误，OPST仅掉1.9pt，远优于SFT掉5.7pt的表现

最值得记住的一句话：大模型本身的参数知识远多于当前能激发的能力，仅需合适的自训练框架即可在无外部数据的情况下大幅释放已有能力
