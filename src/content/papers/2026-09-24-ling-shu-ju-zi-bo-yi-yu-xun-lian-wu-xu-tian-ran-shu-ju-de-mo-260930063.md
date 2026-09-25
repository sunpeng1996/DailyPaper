---
title: Self-Play Pretraining with Zero Data
title_zh: 零数据自博弈预训练：无需天然数据的通用模型预训练框架
authors:
- Aditya Cowsik
- Kfir Dolev
- Michael Y. Li
- G. Bruno De Luca
- Nourya Cohen
- Noah D. Goodman
- Yoav Levine
affiliations:
- Independent Researcher
- Tel Aviv University
- Stanford University
- LAPTh, USMB
arxiv_id: '2609.30063'
url: https://arxiv.org/abs/2609.30063
pdf_url: https://arxiv.org/pdf/2609.30063
published: '2026-09-24'
collected: '2026-09-25'
category: Training
direction: LLM预训练 · 自博弈零数据合成
tags:
- Self-Play
- Synthetic Data
- Pretraining
- Zero Data
- Scaling Law
- In-Context Learning
one_liner: 通过生成器-学习者自博弈生成可计算程序训练数据，零样本跨模态性能随算力幂律提升
practical_value: '- 可复用自适应学习进度奖励设计：用梯度与历史参数更新方向的对齐度作为合成数据筛选信号，避免生成无意义难例，适合推荐系统负样本生成、Agent训练数据自动构造场景

  - 可迁移自博弈双模型架构：生成器+学习者协同进化框架可用于小样本冷启动场景下的用户行为建模，无需大量真实标注数据即可习得通用序列预测规律

  - 合成数据跨模态迁移思路：无需与目标域分布完全一致的合成数据，只要包含递归、层次组合等通用结构就能提升下游任务性能，可用于电商多模态推荐预训练数据增强'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM预训练高度依赖大规模人工curated天然数据，数据获取成本随规模提升陡增，且存在质量、版权等瓶颈；若能让模型自主生成对自身提升最有用的训练数据，就能突破天然数据限制，实现仅靠算力的持续迭代。

### 方法关键点
- 双Transformer架构：随机初始化的生成器、学习者参数独立，前者输出类Brainf*ck的图灵完备程序，后者在程序执行生成的字节序列上做下一词预测训练
- 自适应奖励设计：生成器的RL奖励为学习者在当前程序输出上的梯度与历史参数更新方向的AdamW预条件对齐度，仅奖励处于学习者能力边界、可复用已习得结构的训练数据，避免无意义随机难例
- 训练流程：每轮迭代包含程序生成、执行、学习者更新、生成器RL+奖励加权SFT更新三步，加入程序突变、历史高价值程序回放机制缓解遗忘与探索不足

### 关键实验
在文本、图像、语音、旋律、代码、DNA等8类跨模态数据集上零样本评估，对比固定所罗门诺夫先验程序采样、PCFG预训练两个baseline：自博弈预训练的零样本损失随算力提升呈幂律下降，scaling exponent与天然数据预训练相当；在6类ICL任务上准确率最高达100%，远优于两个baseline；生成器能早于随机采样数万轮发现斐波那契、几何序列等通用数学结构。

### 核心结论
预训练中模型习得的通用预测结构（递归、层次组合等）与特定域的偶发信息可解耦，仅靠自博弈生成的通用结构就能实现跨模态零样本迁移。
