---
title: 'V-CoLA: Vision Token Compression with Linear Attention'
title_zh: V-CoLA：面向线性注意力的视觉Token压缩框架
authors:
- Hao Jiang
- Yiru Mao
- Tianpeng Bu
- Hao Zhou
- Hongtao Duan
- Wang Jing
- Bowen Xu
- Xin Chen
- Lulu Hu
- Bin Yang
affiliations:
- Alibaba Cloud Computing, Alibaba Group
arxiv_id: '2610.11251'
url: https://arxiv.org/abs/2610.11251
pdf_url: https://arxiv.org/pdf/2610.11251
published: '2026-10-07'
collected: '2026-10-09'
category: Multimodal
direction: 多模态大模型 · 线性注意力Token压缩
tags:
- Linear-Attention
- Vision-Token-Compression
- VLM
- Training-Free
- Inference-Optimization
one_liner: 针对线性注意力混合架构VLM，提出免训练视觉Token压缩方案，实现高保真实时推理加速
practical_value: '- 电商多模态商品理解、图文检索场景可直接复用V-CoLA方案，在Qwen3.5等线性注意力VLM上，50%Token保留率下仅损失0.5%性能，获得1.86~6.15×prefill加速，大幅降低推理成本

  - 做长序列Token压缩的团队可借鉴其重要度计算逻辑，从线性注意力状态更新特征中提取固有重要度信号，避免传统softmax依赖的方法在新架构上失效

  - 工程落地可复用其自适应分块合并+视觉Token早退出的组合优化策略，兼容线性注意力分块并行特性，额外开销仅占前向传播的1.6%，几乎无落地负担'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉Token压缩方法大多针对softmax注意力设计，随着Qwen3.5等融合线性注意力的混合架构VLM普及，原有方法性能暴跌甚至不如随机基线，核心原因是线性注意力的有限循环状态会破坏浅层注意力集中度与Token特征区分度，亟需适配新架构的压缩方案。
### 方法关键点
- 免训练框架，完全基于线性注意力固有特征设计，无需微调模型权重
- 提出uniqueness-aware重要度准则，同时衡量Token对最终状态的长期贡献与相对历史上下文的短期唯一性，避免冗余Token选中偏差
- 自适应分块合并策略：按重要度分布动态划分chunk，高重要度区域分配更细粒度分块，chunk内按重要度加权合并Token，减少关键信息损失
- 新增视觉Token早退出机制：深层模型推理时直接丢弃所有视觉Token，进一步降低计算量
### 关键实验
在Qwen3.5-9B/27B、InfiniteVL三个主流线性注意力混合架构VLM上，跨MME、MMB、GQA等8个多模态benchmark验证：50%视觉Token保留率下保留99.5%原性能，12.5%保留率下仍保留88%以上性能；prefill阶段加速1.86×~6.15×，压缩逻辑额外开销仅占前向传播成本的1.6%，显著优于FastV、DART、VisionZip等SOTA基线。
### 核心结论
线性注意力的循环状态更新过程本身就隐含了Token重要度信号，无需依赖softmax注意力分数或特征相似度即可实现高效精准的Token压缩
