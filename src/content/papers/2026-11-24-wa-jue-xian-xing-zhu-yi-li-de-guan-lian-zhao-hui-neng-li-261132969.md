---
title: Eliciting the Recall Capacity of Linear Attention
title_zh: 挖掘线性注意力的关联召回能力
authors:
- Johan Lindqvist
- Antonio Orvieto
affiliations:
- ELLIS Institute Tübingen
- MPI-IS
- Tübingen AI Center
- KTH Royal Institute of Technology
arxiv_id: '2611.32969'
url: https://arxiv.org/abs/2611.32969
pdf_url: https://arxiv.org/pdf/2611.32969
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: 大语言模型 · 线性注意力召回优化
tags:
- Linear Attention
- Associative Recall
- Long Context
- Training Intervention
- Recall Optimization
one_liner: 通过上下文句子重复和损失重加权训练干预，无架构改动下缩小线性注意力与softmax的召回差距
practical_value: '- 做长上下文RAG/线性注意力Agent时，可直接复用训练trick：加入10%比例的上下文内句子重复+TLCE损失重加权，无需改动架构、不增加推理成本即可提升长程信息召回准确率，适配电商长商品描述解析、用户长行为序列召回场景

  - 线性注意力召回能力核心由recurrent state大小决定，与总参数量关联度极低，做轻量级端侧LLM/推荐排序模型时，优先分配参数给state维度，比盲目堆总参数量ROI更高

  - 做生成式推荐长序列用户建模时，可参考文中AR-hit定义，针对重复出现的罕见用户行为、商品关联对做损失上加权，能提升模型对用户个性化偏好的捕捉能力，减少推荐同质化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
线性注意力具备推理时KV cache固定大小、长序列下单token推理成本恒定的优势，是长上下文大模型的主流落地方向之一，但常规预训练下其关联召回（AR）能力远弱于softmax注意力，尤其长距离前缀匹配召回差距可达0.5nats以上，严重限制了其在需要长程信息检索的场景落地。

### 方法关键点
- 通过合成任务MQAR量化线性注意力召回能力的缩放规律，验证可召回的关联对数量与recurrent state大小近似线性正相关，与总参数量、头布局关联度极低
- 提出两种无架构改动的训练干预：1）上下文内插入10%比例的重复句子，提升AR-hit样本占比；2）Thresholded LongCE（TLCE）损失重加权，上加权可从长上下文获益的token预测
- 两种干预可单独或组合使用，仅需在训练最后20%阶段加入即可生效，全程启用可进一步优化效果

### 关键结果
- 组合干预下，4种主流线性注意力架构的长距离AR-hit损失差距缩小至与常规训练的softmax对齐，文档抽取准确率平均提升18.5pp，上下文QA准确率提升5.2pp，仅伴随LM困惑度2.0的小幅上升
- 全程启用干预的KDA模型，文档抽取准确率达48.9%，接近常规训练softmax的52.1%，QA准确率36.2%与干预后的softmax持平
- 单层面线性注意力在专用召回训练下，可从16k token上下文中检索到3000+个关联对，验证其底层召回潜力充足

**最值得记住的结论：线性注意力的长程召回短板并非来自架构固有容量限制，而是常规预训练的召回相关监督信号不足，针对性训练干预可在极小通用能力损失下释放其潜力**
