---
title: Fine-Tuning Without Gradients? Closed-Form, LLM-Written Classifiers on a Frozen
  Encoder
title_zh: 无梯度微调？基于冻结编码器的LLM生成闭式分类器
authors:
- Md Nasir Uddin
- Musa Tur Farazi
- Soumik Bhattacharjee
- Tishna Sabrina
- Chowdhury Mohammad Rakin Haider
affiliations:
- Bangladesh University of Engineering and Technology (BUET)
- University of Asia Pacific, Dhaka
arxiv_id: '2611.33972'
url: https://arxiv.org/abs/2611.33972
pdf_url: https://arxiv.org/pdf/2611.33972
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: 无梯度微调 · 冻结编码器适配
tags:
- Gradient-free Fine-tuning
- Frozen Encoder
- Closed-form Classifier
- LoRA
- LLM-assisted Design
one_liner: 提出闭式权重空间编程框架，无需梯度适配冻结编码器，效果超全量微调与LoRA
practical_value: '- 电商评论情感分类、query意图识别等小样本分类场景可直接复用WSP框架，无需梯度训练，避免小样本下LoRA/全量微调的不稳定问题，标签量<128时效果领先3~5个点

  - 多任务部署场景下可共用一个冻结编码器，每个任务仅需存储KB级~MB级的闭式分类头，相比每个任务存储LoRA/全量微调权重大幅降低存储开销

  - 广告合规审核、内容治理等对可解释性、可复现性要求高的业务，WSP完全确定性无随机波动，不会出现微调崩溃问题，结果可严格复现'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
常规全量微调、LoRA等梯度适配方案依赖梯度训练、学习率搜索，小样本下易出现训练崩溃，且需为每个任务存储单独权重，多任务部署开销高；现有冻结编码器的线性探针效果远低于梯度微调方案，亟需无梯度、高性能的冻结编码器适配方法。
### 方法关键点
- 提出闭式权重空间编程（WSP）框架：LLM作为设计助手生成cloze prompt模板，从冻结RoBERTa编码器的12个上层、8种prompt、2种pooling方式提取共216种视图
- 候选分类头包含收缩线性判别分析、核岭回归、MLM标签词先验三类共113种，全部用闭式公式求解，全程无梯度计算、不修改编码器权重
- 通过5折交叉拟合从候选头中选择最优单头或头部集成，保证效果稳定性
### 关键实验
在11个开发数据集、6个未见过的held-out数据集上对比FT、LoRA、PFT三类基线：
- 标签量512~8192区间，WSP平均超过FT、LoRA 0.3~0.6个点，与PFT差距小于0.5个点
- 小样本下优势显著：64/128标签时领先LoRA 2.94/1.18个点，每类仅16标签的Few-shot场景下领先LoRA 3.79个点
- held-out数据集上仍稳定领先LoRA，与FT平均差距小于0.5个点，仅8192标签场景下落后PFT 1.3个点
### 核心结论
冻结编码器与微调的性能差距核心来自读出门槛，多视图+闭式分类头的组合可在无梯度前提下达到甚至超过常规梯度微调的效果，小样本场景下优势更突出
