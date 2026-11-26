---
title: 'Agentic-Level Adversarial Purification: Revisiting Diffusion Purifiers on
  Native-Resolution Agentic Inputs'
title_zh: 面向原生分辨率智能体输入的对抗净化：重新审视扩散净化方法
authors:
- Yan Lin
- Zhongliang Guo
- Jingyu Lin
- Daizong Liu
affiliations:
- Newcastle University
- University of Aberdeen
- Monash University
- Wuhan University
arxiv_id: '2611.34181'
url: https://arxiv.org/abs/2611.34181
pdf_url: https://arxiv.org/pdf/2611.34181
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: VLM Agent 对抗鲁棒性优化
tags:
- VLM Agent
- Adversarial Purification
- Diffusion Model
- Robustness
- Native Resolution
one_liner: 首次提出VLM智能体原生分辨率对抗净化框架，鲁棒性较传统防御提升45个百分点
practical_value: '- 电商网页交互类VLM Agent可直接采用原生分辨率分块扩散净化方案，相比JPEG、高斯噪声等廉价变换，抗网页预处理的扰动鲁棒性提升45个点，仅带来3%左右的干净输入准确率损失

  - 可复用DC-4快速扩散净化流程，仅4步DDIM采样即可达到200步扩散的鲁棒性，单页处理耗时从45.57s降至1.05s，满足线上部署时延要求

  - 不需要复杂的输入注意力掩码、自适应噪声强度估计模块，固定全局噪声水平即可达到最优鲁棒性，大幅简化工程实现'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前VLM Agent广泛应用于电商网页商品选择、GUI交互等场景，第三方内容提供者可轻易添加对抗扰动误导Agent决策；现有扩散净化方案均针对分类任务的固定分辨率输入设计，直接resize会丢失大量文本、商品图片细节，导致干净输入准确率下降严重，且尚无针对Agent场景的标准化防御评估框架。

### 方法关键点
- 提出AgenticPure评估协议，分为三步：适配：将扩散净化改为对原生分辨率输入分256×256重叠块处理，羽化拼接还原；攻击：构建适配网页预处理的灰盒扰动库，包含抗JPEG、缩放、噪声的web-hardened扰动，以及自适应白盒攻击；评估：采用等干净损失对齐不同防御的阈值，固定采样读out策略保证公平对比
- 优化Divide-and-Conquer（DC）扩散净化方案，DC-4仅用4步DDIM采样，搭配vote-20读out策略，大幅降低推理耗时
- 对比基线覆盖JPEG压缩、位深降低、高斯噪声等廉价变换，以及SSNI、DiffCAP等现有扩散净化方案

### 关键结果
- 在TextVQA数据集上，传统resize到256×256的DC方案干净损失达35.7个点，原生分辨率分块处理的DC-4仅为4.0个点
- 在电商网页商品选择任务上，相同3.0个点干净损失下，DC-4的灰盒鲁棒准确率达85.0%，比最优廉价变换的40.0%高出45个点，在Qwen2.5-VL-7B上优势扩大到50个点
- 输入自适应的注意力掩码、噪声强度估计不会提升鲁棒性，固定全局噪声水平即可达到最优效果

最值得记住的一句话：面向VLM Agent的防御设计必须脱离分类任务的固定分辨率假设，针对原生分辨率多元素输入的决策核心区域做优化，才能兼顾低干净损失和高鲁棒性。
