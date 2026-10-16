---
title: 'CoTranslator: Reverse to Forward Chain-of-Thought Translator for Reasoning
  Distillation'
title_zh: CoTranslator：面向推理蒸馏的反向到正向思维链翻译器
authors:
- Zinan Tang
- Zhuoshi Pan
- Kairui Chen
- Ze Yan
- Shaomian Zheng
- Yukun Zhang
- Gang Wang
- Biqing Huang
affiliations:
- Tsinghua University
- Ant Group
- Xiaomi Corporation
arxiv_id: '2610.20828'
url: https://arxiv.org/abs/2610.20828
pdf_url: https://arxiv.org/pdf/2610.20828
published: '2026-10-13'
collected: '2026-10-16'
category: Reasoning
direction: 推理蒸馏 · 思维链分布对齐优化
tags:
- Chain-of-Thought
- Reasoning Distillation
- Knowledge Distillation
- LLM Training
- Distribution Alignment
one_liner: 基于小样本配对正反CoT训练翻译器，低成本生成高质量推理蒸馏训练数据
practical_value: '- 做Agent/导购大模型的推理能力蒸馏时，可复用该方案替代全量正向CoT拒绝采样，仅用35k左右小样本配对数据训练4B翻译器，即可节省64%的推理数据生成算力，同时保留95%的正向采样效果

  - 反向生成内容（如给定结果生成解释、给定商品卖点生成导购话术）的事后合理化问题，都可以参考该翻译对齐范式，用小样本正向优质数据做分布对齐，无需反复迭代prompt，跨场景迁移性强

  - 业务冷启动推理能力时，无需准备大量标注推理数据，复用预训练好的同领域翻译器即可快速生成适配性强的训练数据，无需重训练即可跨数据集、跨基模型迁移'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
推理蒸馏依赖带正确答案的高质量Chain-of-Thought（CoT）数据，现有两种生成路径均有明显缺陷：正向CoT生成+拒绝采样可产出符合推理逻辑的验证数据，但难问题需多次调用大模型，算力成本极高；反向CoT生成（输入问题+已知答案生成推理路径）成本低，但易出现事后合理化问题，生成的推理路径依赖答案前置信息，和学生模型无答案推理的部署场景存在分布mismatch，现有语义抑制、结构引导等方法无法从根本上解决该问题。

### 方法关键点
- 将反向CoT到验证正向CoT的分布对齐问题建模为翻译任务，训练CoTranslator完成路径转换
- 仅需35.7k小样本配对数据（同问题下的反向CoT为源、拒绝采样验证的正向CoT为目标）微调翻译器，训练时屏蔽问题与答案输入，避免模型学习答案捷径
- 全量数据生成阶段仅需1次反向CoT调用+1次翻译器调用，无需额外拒绝采样，大幅降低算力成本

### 关键结果
在6个数学基准、6款不同参数（4B~8B）、不同架构的学生模型上验证：比语义抑制基线最高提升5.82个百分点准确率；4B学生模型可保留拒绝采样95.0%的平均准确率，仅消耗其35.9%的算力；无需重训练即可直接迁移到新数学数据集、新教师模型、STEM领域，STEM场景下4B、8B学生平均准确率分别提升4.88、4.31个百分点。

### 核心结论
用翻译范式对齐反向/正向CoT分布，是兼顾推理蒸馏效率、效果、迁移性的低成本落地方案。
