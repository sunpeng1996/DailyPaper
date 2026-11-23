---
title: 'Felid: A Flexible and Efficient Design for Transformer Fine-Tuning over Encrypted
  Data'
title_zh: FELID：加密数据下Transformer微调的灵活高效设计
authors:
- Linru Zhang
- Jun Jie Sim
- Xiangning Wang
- Jiahao Zhong
- Kaiyu Zhou
- Huanyi Ye
- Yongsen Zheng
- Lushan Song
- Xiaojian Liang
- Yingting Liu
affiliations:
- Nanyang Technological University
- Ant International, Ant Group
arxiv_id: '2611.27175'
url: https://arxiv.org/abs/2611.27175
pdf_url: https://arxiv.org/pdf/2611.27175
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 隐私计算 · LLM密态微调效率优化
tags:
- FHE
- LoRA
- Transformer
- Fine-tuning
- Privacy-Preserving ML
one_liner: 优化FHE下Transformer微调的密文运算 较SOTA实现8倍速度提升
practical_value: '- 涉及用户敏感数据的电商/广告个性化LLM微调场景，可直接复用灵活列优先打包策略，适配4~64可变批量的密态计算需求，避免固定批量的槽位浪费

  - 密态模型计算的矩阵运算优化可复用列优先打包思路，相比传统行打包减少最高213倍的密文旋转开销，大幅降低计算成本

  - 功能Bootstrapping融合激活计算的trick可直接迁移到所有FHE场景的LLM推理/微调，将Bootstrapping调用次数降低2.5倍

  - 面向B端的LLM微调SaaS服务可基于该框架实现数据可用不可见的能力，8倍的性能提升已接近落地可用门槛'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
随着AI服务化普及，金融、电商等强监管场景对用户数据隐私要求极高，FHE支持非交互式密态计算无需客户端在线，但现有FHE下Transformer微调方案要么仅支持分类头微调，要么受限于密文旋转、重线性化、Bootstrapping的极高开销，完全无法落地。

### 方法关键点
- 灵活列优先批量打包：支持4~64可变批量输入加密，按列交错跨样本元素，相比传统行打包避免矩阵乘法的内部旋转开销，密文槽位利用率接近100%
- 全链路矩阵运算优化：针对注意力、LoRA、分类头等四类核心矩阵运算定制优化，最高减少213倍密文旋转，乘法层级最高降低4层，大幅减少Bootstrapping触发次数
- 激活与Bootstrapping融合：采用功能Bootstrapping将元素级激活（ReLU、GELU等）计算与密文刷新合并，省去单独的激活计算步骤，无额外开销

### 关键实验
基于2层BERT+LoRA在GLUE的MRPC、RTE、STSB三个任务测试，对比SOTA Rho et al. 2025方案：密文旋转与重线性化总次数降低30×，Bootstrapping调用次数降低2.5×，批量大小16下单批次微调时间从5238s降至650s，实现8×加速，密态微调精度相比明文损失小于1%。

> 最值得记住：FHE下Transformer优化的核心优先级是底层密文运算的打包、层级优化，而非修改模型架构，可在无精度损失的前提下实现数量级效率提升
