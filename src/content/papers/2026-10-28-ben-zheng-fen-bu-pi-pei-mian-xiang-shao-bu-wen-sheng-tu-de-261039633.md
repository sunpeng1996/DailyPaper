---
title: Intrinsic Distribution Matching
title_zh: 本征分布匹配：面向少步文生图的分布对齐优化算法
authors:
- Deyuan Liu
- Yansen Han
- Kaiwen Zheng
- Jun Xie
- Jiacheng Liu
- Zhenglin Cheng
- Peng Sun
- Jintao Zhang
- Jianguo Li
- Tao Lin
affiliations:
- Inclusion AI
- Westlake University
- Tsinghua University
- Zhejiang University
- MBZUAI
arxiv_id: '2610.39633'
url: https://arxiv.org/abs/2610.39633
pdf_url: https://arxiv.org/pdf/2610.39633
published: '2026-10-28'
collected: '2026-10-31'
category: Multimodal
direction: 多模态生成 · 少步文生图分布对齐
tags:
- Text-to-Image
- Distribution Matching
- LoRA
- EMA
- Long-Text Rendering
one_liner: 提出无需外部特征编码器的IDM分布对齐方法，提升少步文生图的长文本渲染精度
practical_value: '- 电商广告/商品图少步生成场景可复用IDM的矩损失约束思路，在降低推理耗时的同时保证促销文案、商品参数等文本细节的渲染准确率

  - 对文生图模型做LoRA微调时，可引入生成器EMA副本做特征对齐，无需额外接入DINOv2等外部特征编码器，简化训练链路

  - 长文本渲染效果验证逻辑可直接复用在电商营销海报、商品详情图自动生成的效果评估环节'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
少步/单步文生图生成推理效率高，但难以精准还原prompt中的细节信息，现有DMD分布对齐方法缺乏显式矩约束，生成效果有待提升。
### 方法关键点
将反向KL场分解为高斯矩分量与非高斯残差，提出IDM算法，保留完整DMD校正能力的同时，仅通过生成器的EMA副本匹配特征均值与逐坐标标准差，无需引入外部特征编码器，支持全参数微调与LoRA微调两种模式。
### 关键结果
- 2次网络评估开销下，中文、英文LongText-Bench得分分别达94.25%、90.20%，为同算力预算下SOTA
- 生成器EMA特征在5项测试指标上效果与外部DINOv2编码器相当，新增的矩损失可带来稳定效果提升
