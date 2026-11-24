---
title: 'Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?'
title_zh: Self-WSP：语言模型能否通过权重空间编程实现自我优化？
authors:
- Guoming Ling
- Shanshan Zhong
- Kaixuan Zhang
- Zhongzhan Huang
affiliations:
- Carnegie Mellon University
- MilkThink
arxiv_id: '2611.28833'
url: https://arxiv.org/abs/2611.28833
pdf_url: https://arxiv.org/pdf/2611.28833
published: '2026-11-20'
collected: '2026-11-24'
category: LLM
direction: LLM权重空间编程 · 递归自优化
tags:
- Weight-Space-Programming
- Self-Improvement
- LLM
- Gradient-Free-Optimization
- Recursive-Self-Improvement
one_liner: 验证0.8B LLM可通过自编辑权重实现性能跃升，同时揭示当前方案的核心局限性
practical_value: '- 针对小参数量域内模型的性能缺陷，可借鉴极小参数编辑思路：仅修改几十到上百个核心权重即可快速修复重复生成、输出卡死等常见问题，成本远低于全量/
  LoRA微调

  - 梯度-free的「模型提案+验证集筛选」框架可复用在业务模型快速迭代场景：比如针对搜索推荐的bad case，让LLM提出小范围权重修改方案，通过线上小流量AB测筛选有效编辑，无需重新训练

  - 任何自优化方案都必须设置随机搜索baseline做对比：大部分小权重编辑的收益来自运气而非模型理解，业务落地时要避免高估LLM的权重编辑能力，优先做随机对照'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM自优化方案多依赖数据生成、prompt迭代、代码改写等间接方式修改权重，Weight-Space Programming（WSP）虽已验证大模型可编辑小模型权重，但小模型能否编辑自身权重实现递归自优化尚未被验证，该研究填补了这一空白。

### 方法关键点
- Self-WSP循环框架：同个LLM同时担任编辑者和求解者，编辑者读取自身权重信息后提出编辑方案，求解者用修改后的权重回答验证题，只有双验证集准确率均不下降且总提升达标的编辑才会被保留，替换原权重进入下一轮循环
- 语法约束的权重编辑设计：支持归零、缩放、加减、方向移除等7种编辑操作，每次仅修改1-2个张量的局部块，过滤无效编辑
- 两套对照接口：乱序接口随机排列张量列表，有序接口按层排列张量列表，对比编辑顺序对效果的影响

### 关键结果
在GSM8K、MATH500两个数学推理数据集上测试，baseline包括原模型、随机搜索、GPT-6 Astra编辑方案；0.8B Qwen3.5自编辑后GSM8K准确率从11.8%最高提升到62.2%，MATH500准确率从7.0%最高提升到32.2%，部分有效编辑仅修改16个参数；但随机搜索在GSM8K上效果与Self-WSP相当，模型对编辑的可解释性极差，大部分收益来自运气筛选而非模型理解。

**最值得记住的一句话**：当前LLM自权重编辑的收益主要来自外部筛选的运气，而非模型对权重机制的理解，落地时必须搭配严格的验证机制。
