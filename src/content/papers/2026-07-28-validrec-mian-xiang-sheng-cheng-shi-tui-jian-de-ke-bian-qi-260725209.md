---
title: 'VaLiDRec: Variable-Length LLM-Aligned Semantic IDs for Generative Recommendation'
title_zh: VaLiDRec：面向生成式推荐的可变长LLM对齐语义ID框架
authors:
- Shutong Qiao
- Wei Yuan
- Tong Chen
- Hao Wang
- Quoc Viet Hung Nguyen
- Hongzhi Yin
affiliations:
- University of Queensland
- Griffith University
- Computer Network Information Center, Chinese Academy of Sciences
arxiv_id: '2607.25209'
url: https://arxiv.org/abs/2607.25209
pdf_url: https://arxiv.org/pdf/2607.25209
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · Semantic ID 构建与推理优化
tags:
- Generative Recommendation
- Semantic ID
- LLM4Rec
- LoRA
- Cold Start
- Inference Optimization
one_liner: 提出基于LLM原生可变长语义ID的生成式推荐框架，推理效率较基线提升87.49倍
practical_value: '- Semantic ID构建可直接复用：用LLM原生token结合「上下文隐状态范数+IDF」计算token重要性，再用语义质量阈值做贪心剪枝，适配商品语义复杂度生成可变长ID，避免固定长度ID的语义压缩/冗余问题

  - 推理加速方案可落地：将生成式推荐从自回归SID生成改造成并行token预测+token级打分聚合，去掉beam search，同等LLM backbone下可实现几十倍推理提速，满足线上低延迟要求

  - 冷启动场景适配技巧：SID完全基于商品元数据生成，无需依赖交互数据，零样本冷启动场景下Recall@100较最优基线提升2.5%，电商新品推荐场景可直接复用该ID构造逻辑

  - 训练trick借鉴：用GraphSAGE生成的用户行为序列表征做软prompt注入LLM，结合LoRA微调+token集预测/排序/对比三类损失联合优化，兼顾语义对齐与推荐效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐普遍采用聚类/量化生成的固定长度语义ID（SID），存在三个核心痛点：一是人工编码语义与LLM原生词汇表错位，需额外做对齐训练；二是固定长度无法适配不同商品的语义复杂度，易出现语义过度压缩或冗余；三是自回归解码+beam search推理延迟过高，难以落地线上高吞吐推荐场景。

### 方法关键点
- **SID构造阶段**：从商品元数据的LLM分词结果出发，结合上下文隐状态范数与IDF计算token重要性，通过语义质量感知的贪心剪枝生成可变长SID，再经碰撞感知优化+后缀消歧义保证ID全局唯一，SID长度自适应商品语义复杂度。
- **推荐建模阶段**：用GraphSAGE对用户交互序列的商品转移图编码，生成graph-aware软prompt注入LLM输入，仅用LoRA微调LLM参数，训练时联合优化token集预测、item排序、对比对齐三类损失。
- **推理阶段**：LLM单次前向传播并行输出所有SID token的预测概率，按商品SID包含的token平均概率计算item打分，完全去掉自回归解码与beam search环节。

### 关键实验结果
在4个亚马逊公开数据集（美妆、科研器材、乐器、工艺）上对比8个主流基线（SASRec、BERT4Rec、LC-Rec、RPG等），所有评价指标均为最优：稀疏数据集Arts上NDCG@20较最优基线提升超22%，零样本冷启动场景Recall@100较最优基线提升2.5%，推理速度较LC-Rec提升87.49倍。

最值得记住的一句话：生成式推荐的SID不需要人工构造量化编码，直接用LLM原生词汇表的token生成可变长ID，不仅效果更优，还能大幅降低推理延迟。
