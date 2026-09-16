---
title: Persistent Recurrent Memory Between Transformer Layers - Improves Language
  Model Generalization
title_zh: Transformer层间持久循环记忆模块提升语言模型泛化能力
authors:
- Eduardo Novaes Hering
affiliations:
- FITec Labs
- Ericsson São Paulo
arxiv_id: '2609.17251'
url: https://arxiv.org/abs/2609.17251
pdf_url: https://arxiv.org/pdf/2609.17251
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: LLM架构优化 · 层间循环记忆增强
tags:
- Transformer
- Recurrent Memory
- GRU
- Generalization
- Decoder-only
one_liner: 在Transformer层间插入轻量持久循环记忆模块，以3.7%参数开销换28.5%评测损失下降
practical_value: '- 落地小参数垂域LLM（如端侧推荐文案生成、Agent轻量推理模型）时，可直接在Transformer中间层插入PRM模块，仅3.7%参数开销即可获得大幅泛化提升，性价比远高于堆叠隐层维度或增加层数

  - 做长序列用户行为建模的推荐/广告排序模型时，可复用observe→update→influence拓扑，用GRU维护用户长期兴趣的持久状态，跨Transformer层传递压缩的全局用户信息，降低attention的计算与信息冗余负担

  - 小样本、数据受限的业务场景（如新品冷启动文案生成、垂域query改写）优先做架构拓扑优化，无需浪费精力调试复杂辅助损失，拓扑带来的归纳偏置增益远高于辅助损失的潜在收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
标准Decoder-only Transformer仅通过逐层传递隐层表示传递上下文信息，每层都需要重新从全序列推导全局语境，没有显式的跨层稳定信息维护机制，小参数模型极易过拟合，泛化能力差，在数据受限的垂域业务场景落地瓶颈明显。
### 方法关键点
- 将N层Transformer从中间切分为上下两半，中间插入Persistent Recurrent Memory（PRM）模块，仅增加3.7%参数开销
- PRM执行三步核心操作：1）Observe：持久状态向量对下层输出隐层做cross-attention抽取全局信息；2）Update：通过GRU迭代2次更新持久状态；3）Influence：通过可学习门控加法将状态向量调制到下层隐层，送入上层Transformer
- 训练仅使用标准next-token预测交叉熵损失，无需额外辅助损失
### 关键实验
- 数据集采用TinyStories，抽取1.5万条故事分词为64token序列，85/15拆分训练/验证集，基于6层22M参数的Decoder-only Transformer做对比
- 对比基线：标准Transformer、移除自预测损失的PRM拓扑、带随机辅助损失的标准Transformer
- 核心结果：PRM模型评测损失从2.438降至1.743，降幅28.5%；泛化gap从0.26降至0.12，过拟合程度减半；消融实验证明增益完全来自拓扑结构，与辅助损失无关；线性探测显示PRM持久状态编码叙事位置准确率达52%，远优于标准Transformer的33%随机水平。
### 核心结论
在数据受限的小模型场景，优化信息流动的拓扑结构带来的泛化增益，远高于增加辅助训练目标的收益。
