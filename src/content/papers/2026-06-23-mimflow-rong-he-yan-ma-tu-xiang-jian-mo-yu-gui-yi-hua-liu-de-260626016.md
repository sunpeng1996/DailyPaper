---
title: 'MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End
  Image Generation'
title_zh: MIMFlow：融合掩码图像建模与归一化流的端到端图像生成
authors:
- Yang Chen
- Xiaowei Xu
- Shuai Wang
- Xinwen Zhang
- Qiushi Guo
- Tiezheng Ge
- Limin Wang
affiliations:
- Nanjing University
- Alibaba Group
- Shanghai AI Lab
arxiv_id: '2606.26016'
url: https://arxiv.org/abs/2606.26016
pdf_url: https://arxiv.org/pdf/2606.26016
published: '2026-06-23'
collected: '2026-06-30'
category: Multimodal
direction: 多模态图像生成 · 生成任务解耦
tags:
- Masked Image Modeling
- Normalizing Flows
- Image Generation
- End-to-End
- Task Decoupling
one_liner: 构建统一端到端生成框架，解耦语义建模与像素合成，解决归一化流容量瓶颈
practical_value: '- 生成任务解耦思路可迁移到电商商品图生成：将低频语义结构和高频像素细节分开建模，缓解大模型容量压力，降低训练成本

  - 少冗余token的设计思路可复用，能减少电商图文生成、多模态推荐的推理显存占用与时延

  - 掩码表征建模与生成任务统一端到端优化的方案，可用于电商多模态商品预训练，提升语义表征质量'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
Normalizing Flows (NFs) 作为生成模型支持精确密度估计与采样，但严格可逆性迫使模型容量消耗在底层像素细节上，难以捕获高层语义结构；Masked Image Modeling (MIM) 虽在表征学习表现出色，但此前和生成流程的结合始终为模块化分离，缺乏统一优化。

**方法关键点**  
构建统一端到端框架MIMFlow，联合优化 latent semantics、像素重建与生成流；采用VAE编码器从掩码图像推断语义隐变量，实现生成任务的原则性解耦：Normalizing Flow 专注建模简化的低频语义流形，专属解码器处理高频像素合成，解决NF的固有容量瓶颈，让模型优先保证全局结构一致性，而非冗余噪声。

**关键结果**  
在ImageNet 256×256数据集上，MIMFlow-L达到71.3%线性探测准确率，FID得分为2.50；模型仅使用128个token（比标准模型少50%），相对同规模NF基线实现32.8%的性能提升。
