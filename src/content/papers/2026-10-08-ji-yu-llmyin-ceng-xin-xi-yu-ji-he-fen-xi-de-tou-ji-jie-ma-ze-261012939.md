---
title: 'Surfing the Activation Wave: Analyzing the Information and Geometry of LLM
  Hidden States for Speculative Decoding'
title_zh: 基于LLM隐层信息与几何分析的投机解码隐层选择框架
authors:
- Raghavv Goel
- Sudhanshu Agrawal
- Mukul Gagrani
- Risheek Garrepalli
- Mingu Lee
affiliations:
- Qualcomm AI Research
- Stanford University
arxiv_id: '2610.12939'
url: https://arxiv.org/abs/2610.12939
pdf_url: https://arxiv.org/pdf/2610.12939
published: '2026-10-08'
collected: '2026-10-12'
category: LLM
direction: LLM推理加速 · 投机解码隐层选择
tags:
- Speculative Decoding
- Hidden States
- Matrix Entropy
- CKA
- EAGLE3
one_liner: 基于矩阵熵与CKA的原则化隐层选择方案，提升EAGLE3式投机解码效率
practical_value: '- 搭建LLM驱动的Agent、生成式推荐推理服务时，若采用EAGLE类投机解码，可直接复用ELSI/ELSI-C算法替代默认固定层选择规则，无需增加计算量即可提升1.6%~7.3%的token接受率，降低推理延迟

  - 做隐层特征复用（如用户建模、RAG embedding提取、语义召回特征构建）时，可借鉴「矩阵熵衡量信息量+CKA衡量冗余」的方法，替代经验性选择最后几层的做法，提升特征质量

  - 训练基于LLM隐层的小模型时，可复用token-entropy过滤策略（保留top30%高熵token的隐层），降低跨样本特征方差，提升小模型训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有EAGLE系列投机解码方案依赖固定位置启发式选择目标模型隐层喂给draft模型，忽略了不同层的信息互补性与冗余性，且隐层组合选择是典型组合优化问题，穷举不可行，缺乏原则化的选择框架，导致推理加速效率未达最优。

### 方法关键点
- 核心准则：用矩阵熵量化隐层集合的信息量，用中心核对齐（CKA）量化隐层间的表征冗余，以此作为层选择的两大核心评估维度
- 层选择算法：设计ELSI算法，基于beam搜索以拼接隐层的矩阵熵为优化目标，高效筛选高信息量隐层组合；扩展ELSI-C算法，加入CKA过渡约束，进一步降低层间冗余
- 预处理优化：新增token-entropy过滤，预处理时仅保留预测熵前30%的token的隐层，降低跨prompt的熵方差，提升层选择统计的稳定性

### 关键实验
基于Qwen3-4B-Instruct、Llama3.1-8B-Instruct两个开源模型，用ShareGPT、Ultrachat数据训练draft模型，在SpecBench上对比EAGLE2、EAGLE3基线：
- Qwen3-4B场景下，ELSI选3层时比EAGLE3默认层选择平均提升1.6%~2.2%接受率，比EAGLE2提升6.1%~7.3%；仅选1层的效果就匹配EAGLE3选3层的性能
- Llama3.1-8B场景下，ELSI选1层即可达到EAGLE3 99%的效率，可降低1/3的隐层拼接计算量

### 核心结论
LLM隐层选择的质量远重要于选择的层数，基于信息量+冗余度的原则化选择可在不增加额外计算开销的前提下显著提升下游任务效率。
