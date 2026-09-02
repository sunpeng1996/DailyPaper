---
title: 'SwapRec: Warming Up Cold Items Through Training-Time Swaps'
title_zh: SwapRec：训练阶段通过物品替换缓解推荐系统物品冷启动问题
authors:
- Marta Moscati
- Jan Malte Lichtenberg
- Davide Abbattista
- Antonio De Candia
- Laura Boggia
- Matteo Ruffini
affiliations:
- Albatross AI
- Johannes Kepler University Linz
arxiv_id: '2609.00913'
url: https://arxiv.org/abs/2609.00913
pdf_url: https://arxiv.org/pdf/2609.00913
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 序列推荐 · 物品冷启动优化
tags:
- ColdStart
- SequentialRecommendation
- SASRec
- BERT4Rec
- ID-basedRS
one_liner: 通过训练时按内容相似度随机替换物品，让ID型序列推荐适配推理时的冷启物品替换操作
practical_value: '- 现有已上线的ID型序列推荐（如SASRec/BERT4Rec）可直接复用当前物品相似度计算逻辑，无需修改模型架构，仅在训练时按概率p_swap随机替换序列物品为其最相似物品，即可大幅提升冷启场景性能，改造成本极低

  - 超参数可参考经验值设置：p_swap取0.1~0.3，单序列最大替换数M_swap设为序列长度的1/4（如40长度序列设为10），优先替换序列前部物品，既保留用户真实行为模式，又能让冷物品ID获得足够梯度更新

  - 推理时遇到严格冷启物品，直接用内容相似度最高的暖物品ID替换输入序列中的冷物品，结合SwapRec训练的模型，性能比随机初始化/丢弃冷物品的策略最高提升469%

  - 需扶持新商品的场景可直接复用该方案，可在不损失整体推荐精度的前提下，提升冷物品推荐占比约1pct，catalog覆盖率提升约9%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界ID型序列推荐系统处理冷物品交互时，常用推理时将冷物品替换为内容最相似暖物品的启发式策略，但原生模型未经过相关训练，对这类替换的鲁棒性极差，反而会导致推荐精度下降；同时冷物品ID在训练中梯度更新不足，很难被推荐出来，既影响用户体验也损害商家侧新物品曝光需求。

### 方法关键点
- 训练阶段基于物品侧信息（文本/音频/属性）预计算的余弦相似度最近邻映射φ，按概率p_swap随机替换序列中的物品为其最近邻，单序列最多替换M_swap个，优先替换序列前部物品，替换同时作用于输入序列和训练目标
- 推理阶段仅将输入序列中的冷物品替换为其最近邻暖物品，目标推荐物品不受替换影响
- 无需修改原有推荐模型架构，可无缝接入SASRec、BERT4Rec等任意ID型序列推荐模型

### 关键实验
在音乐、电商（Amazon美妆）、电影三个领域数据集测试，对比基线包括原生SASRec、BERT4Rec及MultVAE、Item-kNN、ALS等非序列模型：
1. 整体性能无损失：Amazon数据集上SwapRec+SASRec的HR@10和原生SASRec持平，ML-20M上反而提升1.4%
2. 冷启场景性能大幅提升：输入序列末尾为冷物品时，Onion数据集SwapRec+SASRec的swap后HR@10从0.1176涨到0.1849，提升57%；严格冷启场景下HR@10从0.0423涨到0.2405，提升469%
3. 冷物品曝光提升：Amazon数据集冷物品推荐占比从30.7%提升到31.8%，catalog覆盖率从0.5779提升到0.6322，涨幅9.4%

### 核心结论
工业界常用的冷启物品替换启发式策略只有在训练阶段也同步引入相同的替换逻辑，才能真正发挥作用，且几乎不需要额外的架构改造和资源投入
