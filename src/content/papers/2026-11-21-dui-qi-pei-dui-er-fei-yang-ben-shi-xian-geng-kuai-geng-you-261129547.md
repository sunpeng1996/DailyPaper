---
title: 'Align the Pair, Not the Sample: Representation Alignment for Faster and Better
  One-Step Generato'
title_zh: 对齐配对而非样本：实现更快更优一步生成器的表征对齐方法
authors:
- Mingxiao Li
- Xuantuo Huang
- Encheng Su
- Aoran Wang
- Han Zhang
- Jinouwen Zhang
- Shixiang Tang
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Peking University
- University of Science and Technology of China
- University of Oxford
arxiv_id: '2611.29547'
url: https://arxiv.org/abs/2611.29547
pdf_url: https://arxiv.org/pdf/2611.29547
published: '2026-11-21'
collected: '2026-11-25'
category: Other
direction: 一步生成器 · 表征对齐训练优化
tags:
- Representation Alignment
- One-step Generation
- Training Optimization
- Feature Matching
- Diffusion Model
one_liner: 通过对齐配对重建路径而非生成路径的表征，大幅提升一步生成器的训练效率与生成质量
practical_value: '- 训练生成式推荐/广告素材的一步生成模型时，优先对齐配对重建路径而非纯噪声生成路径的表征，可避免召回率大幅坍塌

  - 可复用「冻结预训练编码器+配对路径特征对齐」的训练范式，降低生成类业务模型的训练算力成本，同时提升生成内容质量

  - 当生成任务要求高实例级保真度（如商品图生成、个性化文案生成）时，禁止用同类随机样本作为对齐目标，必须使用输入对应的真实配对样本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
表征对齐可加速扩散模型训练，但一步生成器面临特有训练路径选择问题：纯噪声生成路径无对应真实样本，直接对齐该路径会导致效果劣化。
### 方法关键点
基于Priming一步生成器训练框架，选择对齐带真实配对的 corrupted 图像重建路径（而非生成路径），用冻结DINOv2编码器做特征对齐；验证不对称性根源：无实例信息的对齐目标会将生成结果拉向类原型，丢失实例细节。
### 关键结果
17组对照实验显示对齐生成路径会导致召回从0.45暴跌至0.15~0.25；ImageNet 256×256任务上，RePrime将Priming阶段训练epoch减少2倍即追平160epoch基线，后训练更新量减少4倍即超过基线效果；标准预算下FID低至1.30（Base版）、1.155（Large版），115M参数单阶段变体FID达1.22，较同效果模型算力降低24倍
