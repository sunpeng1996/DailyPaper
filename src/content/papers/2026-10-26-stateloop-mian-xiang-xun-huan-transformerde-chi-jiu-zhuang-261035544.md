---
title: 'StateLoop: Persistent State for Looped Transformers'
title_zh: StateLoop：面向循环Transformer的持久状态优化机制
authors:
- Feichen Song
- Boyi Zeng
- He Li
- Shixiang Song
- Yiqin Hao
- Zitong Wang
- Yizhou Yang
- Yifan Liu
- Ziwei He
- Zhouhan Lin
affiliations:
- Shanghai Jiao Tong University
- Sun Yat-sen University
- Shanghai Innovation Institute
arxiv_id: '2610.35544'
url: https://arxiv.org/abs/2610.35544
pdf_url: https://arxiv.org/pdf/2610.35544
published: '2026-10-26'
collected: '2026-10-27'
category: LLM
direction: 循环Transformer · 持久状态架构优化
tags:
- Looped Transformer
- Persistent State
- Selective SSM
- Mamba-2
- Language Modeling
one_liner: 为循环Transformer每个token新增独立持久状态，低开销提升语言建模与下游任务性能
practical_value: '- 电商垂域小参数LLM（文案生成、Agent推理等场景）可引入StateLoop机制，仅增加1%左右参数量就能提升多轮迭代推理效果，性价比远高于单纯叠加Transformer层

  - 多步推理场景（商品多属性抽取、长序列用户行为理解）可复用其门控状态更新逻辑，用selective SSM/GRU保留跨迭代信息，延迟仅增加2%以内，远低于新增一层骨干的开销

  - 长序列推荐场景可参考Token级独立持久状态设计，为每个用户行为item单独维护跨步状态，降低全序列注意力的计算成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Looped Transformer通过共享骨干网络反复迭代实现参数高效的语言建模，但原生方案仅靠单隐层状态传递跨迭代信息，早期迭代产生的有效信息容易在多轮迭代中丢失，限制了深层循环的性能增益。

### 方法关键点
- 为每个token新增独立的持久状态向量，跨所有循环迭代传递信息，不替换原有的骨干输出直连路径，仅作为补充信息叠加到下一轮输入和最终预测层
- 采用selective SSM门控更新逻辑，每轮迭代根据当前骨干输出动态计算保留门、写入门权重，控制旧状态保留比例和新信息写入比例，也可替换为GRU实现类似效果
- 可选增加token维度混合层，支持因果注意力或Mamba-2实现跨token信息交互，进一步提升下游任务效果
- 所有状态更新、混合层、投影层参数跨迭代共享，参数量 overhead 极低

### 关键结果
在Pile数据集上训练410M、1.4B参数模型，对比Vanilla Looped、Hyperloop、MeSH等基线：1.4B规模下基础版StateLoop将Pile困惑度降低0.18，8个零样本任务平均准确率提升0.97pct；增加Mamba-2混合层后准确率提升达1.44pct，仅增加3.26%参数量，推理延迟仅提升1.79%，远低于增加1轮骨干迭代带来的25%延迟提升。循环深度从3提升到7时，StateLoop相对基线的困惑度优势从0.14扩大到0.3，迭代越深增益越明显。

### 核心结论
给循环Transformer增加独立的轻量持久状态，比单纯增加迭代次数或扩宽骨干网络的性价比高得多
