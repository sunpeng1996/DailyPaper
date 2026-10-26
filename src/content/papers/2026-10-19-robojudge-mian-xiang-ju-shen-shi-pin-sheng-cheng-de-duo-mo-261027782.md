---
title: 'RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation'
title_zh: RoboJudge：面向具身视频生成的多模态大模型评判器
authors:
- Siyuan Ma
- Yu Qi
- Cheng Ye
- Ruotian Peng
- Xinyi Xu
- Zitiantao Lin
- Zedong Cai
- Yijian Huang
- Weiyang Liu
- Siyuan Wang
affiliations:
- The Chinese University of Hong Kong
- Westlake University
- Northeastern University
- University of California, San Diego
- Zhejiang University
arxiv_id: '2610.27782'
url: https://arxiv.org/abs/2610.27782
pdf_url: https://arxiv.org/pdf/2610.27782
published: '2026-10-19'
collected: '2026-10-26'
category: Eval
direction: 具身视频生成 · 多模态自动评估
tags:
- Multimodal LLM
- Video Generation
- Evaluation Benchmark
- Automatic Judge
- Embodied AI
one_liner: 构建具身视频生成评估基准，训练出与人类标注一致性最优的9B多模态评判模型
practical_value: '- 电商AI生成商品演示/种草视频的自动评估可复用双维度框架：物理合规性+指令对齐度，避免只匹配语义忽略操作合理性

  - 训练垂直领域自动评判模型可采用「监督微调+强化学习」两阶段范式，搭配模型辅助生成理由+人工校验的低成本标注方案

  - 跨场景复用通用评判模型时需做针对性微调，通用物理推理类评判模型无法直接迁移到具身/电商垂直操作类视频场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
具身视频生成作为世界模型基础需满足物理合规、指令对齐要求，现有多模态大模型作为自动评判器时和人类标注的一致性缺乏系统验证，通用物理推理评判模型也难以适配具身场景。
### 方法关键点
1. 构建RoboJudge-Bench评估基准，覆盖800条人工标注视频、10类生成器，从物理合规性、指令对齐度两个核心维度评测MLLM评判效果
2. 构建含12K条视频、25K个人工校验分数+标注理由的训练集RoboJudge-Train，采用监督微调+强化学习两阶段训练9B参数MLLM得到RoboJudge-9B
### 关键结果
RoboJudge-9B与人类标注的Pearson相关系数达0.719，较最优闭源基线Gemini-3.7-Flash提升0.089，同时在VideoPhy2、Physion-Eval等外部基准上取得效果提升，可直接用于下游视频生成模型的效果排序。
