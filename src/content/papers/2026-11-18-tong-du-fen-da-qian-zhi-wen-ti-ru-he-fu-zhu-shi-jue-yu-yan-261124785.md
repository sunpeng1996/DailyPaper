---
title: 'Read Together, Answer Apart: How Earlier Questions Help Vision-Language Models
  Look'
title_zh: 《同读分答：前置问题如何辅助视觉语言模型视觉感知》
authors:
- Xinyi Guo
- Kaile Huang
- Xitong Ling
- Mingyi He
- Chende Zheng
- Jianyu Xu
- Chao He
- Dongqing Song
affiliations:
- South China Normal University
- Tsinghua University
- Beijing University of Chemical Technology
- Xi'an Jiaotong University
arxiv_id: '2611.24785'
url: https://arxiv.org/abs/2611.24785
pdf_url: https://arxiv.org/pdf/2611.24785
published: '2026-11-18'
collected: '2026-11-19'
category: Multimodal
direction: 多模态大模型 · 同图多问推理优化
tags:
- VLM
- Multimodal Reasoning
- Attention Mask
- Decoding Optimization
- Zero Training Overhead
one_liner: 提出免训练同读分答解码掩码，大幅提升VLM同图多问场景的回答准确率
practical_value: '- 电商商品图多轮智能问答场景可直接复用该免训练解码掩码，无需微调即可提升同图多问题回答准确率，降低推理成本

  - 可借鉴「同预填充、分解码」的架构思路，优化多模态Agent处理同用户同主体多轮查询的推理流程，减少跨query干扰带来的幻觉

  - 多模态推荐场景中，对同商品生成多维度介绍文案/回答用户多维度问题时，可采用该掩码策略提升输出正确率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLM同图多问（co-asking）场景下现有评估结果矛盾，既存在准确率提升也存在幻觉，缺乏对单个回答变化的追踪与底层机制解释。
### 方法关键点
1. 测试22个1B-35B量级开源VLM，明确同问双向效应：可修复15.4%-29.8%的单问错误，但弱模型有30.8%正确答案变错，强模型该比例降至4.7%
2. 揭示作用机制：前置问题在prefill阶段早中层将视觉信息写入问题token，帮助后续问题聚焦目标区域，解码阶段解码器关注其他问题是错误核心来源
3. 提出免训练解码掩码：保留共享prefill阶段，隔离各答案生成与其他问题的注意力连接
### 关键结果
DCI数据集上12/14支持自定义注意力掩码的模型准确率最高提升4.71pp，填补70%与单问的效果差距；WebUI、FinTabNet、GQA数据集上分别有10、8、5个模型获得最高11.4pp、5.3pp、1.1pp的准确率提升
