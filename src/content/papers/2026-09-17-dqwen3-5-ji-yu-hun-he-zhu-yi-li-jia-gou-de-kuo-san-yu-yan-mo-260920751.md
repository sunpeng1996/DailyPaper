---
title: 'dQwen3.5: Hybrid-Attention Diffusion Language Models'
title_zh: dQwen3.5：基于混合注意力架构的扩散语言模型
authors:
- Anton Xue
- Litu Rout
- Aditya Akella
- Adam Klivans
- Sujay Sanghavi
- Sanjay Shakkottai
affiliations:
- University of Texas at Austin
arxiv_id: '2609.20751'
url: https://arxiv.org/abs/2609.20751
pdf_url: https://arxiv.org/pdf/2609.20751
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 扩散语言模型 · 混合注意力适配优化
tags:
- Diffusion Language Model
- Hybrid Attention
- AR-to-DLM Adaptation
- Parallel Decoding
- Qwen3.5
one_liner: 将Qwen3.5混合注意力架构适配为扩散语言模型，训练token量减半且保留并行解码能力
practical_value: '- 做AR大模型到生成式模型适配时，无需将所有层改为双向注意力，仅修改部分注意力层、保留RNN因果结构即可将适配速度提升1倍以上，可大幅降低生成式推荐、Agent推理模型的改造训练成本

  - 扩散模型的高倍数并行解码能力可直接复用在电商商品标题、短文案、营销话术批量生成场景，dQwen3.5在16倍解码加速下仍能保留大部分生成质量，可显著提升内容生产效率

  - 大模型适配扩散目标时无需追求过长训练时长，9B级模型仅需50B训练token即可达到最优效果，继续训练反而会导致知识、数学类任务效果下降，可大幅降低适配阶段的算力投入'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前扩散语言模型（DLM）训练成本是同规模自回归（AR）模型的10倍，从预训练AR模型适配是主流低成本路线，但现有方案均基于全注意力Transformer，而当前主流AR模型已转向注意力+RNN混合架构，RNN天生因果结构无法直接双向化，存在架构适配 mismatch 问题。
### 方法关键点
- 仅将Qwen3.5中的注意力层改为双向，保留所有GDN（RNN变体）层的因果结构，无需修改RNN原生架构
- 沿用标准AR-to-DLM适配的token shifting、特殊令牌复用方案，不新增embedding层，降低适配复杂度
- 训练采用50%代码、35%通用文本、15%数学的混合数据，仅需50B~100B token即可完成全规模适配
### 关键结果
- 同参数量下，混合架构适配DLM的训练速度是全注意力架构的2.21倍，仅需一半token即可达到相同训练损失
- 9B规模dQwen3.5仅用50B训练token，性能超过训练了2.3T token的LLaDA-8B，在HumanEval等代码任务上16倍并行加速下仍领先同类DLM
- 保留DLM任意顺序解码能力，局部AR度0.636与全注意力DLM持平，全局解码符合自然语言左到右的生成规律

> 最值得记住：混合架构AR模型适配DLM时，保留大部分因果RNN层不仅不会阻碍扩散能力，反而能大幅降低适配成本，同时兼顾生成质量与并行解码效率
