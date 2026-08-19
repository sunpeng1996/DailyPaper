---
title: 'ARASH: Adaptive Retrieval And Shot Selection for Tabular Prediction'
title_zh: ARASH：面向表格预测的自适应检索与样本选择方法
authors:
- Samirasadat Jamalidinan
- Yue Xu
- Kazem Cheshmi
affiliations:
- McMaster University
arxiv_id: '2608.17856'
url: https://arxiv.org/abs/2608.17856
pdf_url: https://arxiv.org/pdf/2608.17856
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: 表格大模型 · ICL样本选择优化
tags:
- ICL
- Tabular Prediction
- Few-shot Prompting
- Retrieval Augmented
- Foundation Model
one_liner: 结合特征局部性与标签纯度自适应选择ICL样本，降低表格大模型推理开销同时保持精度
practical_value: '- 电商用户标签预测、商品属性补全、用户风险判定等表格类任务，可直接复用ARASH框架，无需全量微调表格大模型，大幅降低推理成本

  - ICL/RAG的样本选择环节可借鉴「特征局部相似性+候选集标签纯度」双维度评估框架，替代固定k的kNN检索，既压缩prompt长度又避免低纯度样本带来的噪声

  - 可复用其离线-在线两级架构：离线一次性完成数据集聚类、簇难度打标并缓存，在线仅做查询路由和样本检索，端到端推理延迟可降低30%以上

  - 高吞吐的广告/推荐实时场景可落地短路推理逻辑，高纯度簇的查询直接返回统一标签跳过模型调用，20%+的请求可实现近零成本预测'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
表格大模型（TFM）全量上下文ICL推理存在内存开销大、延迟高的问题，固定k值的kNN样本选择方案未考虑局部区域的标签纯度，容易引入噪声导致精度下降，亟需兼顾精度与效率的自适应样本选择方法。
### 方法关键点
- 离线先对训练集做数据画像，自动选择适配的聚类算法划分特征空间的局部区域，计算每个簇的标签纯度、归一化熵得到簇难度得分
- 基于簇难度自适应分配样本配额，难度越高的簇样本配额越高，配额范围控制在预设的[k_min, k_max]区间内
- 在线查询时先路由到对应簇，根据数据集整体局部性、目标簇纯度选择4种检索策略：局部kNN、局部DPP多样性检索、混合局部+全局检索、全局DPP检索
- 新增短路推理逻辑：若检索到的所有样本标签完全一致，直接返回标签跳过模型推理
### 关键实验结果
在OpenML-CC18、Combo公开数据集上测试，对比TabPFN、TabDPT、XGBoost等20+基线：
1. ARASH+TabPFN相比全量上下文TabPFN，prompt长度降低1261.5×，VRAM占用降低2.56×，精度基本持平
2. 适配通用LLM（LLaMA-3.2、Qwen-2.5、FLAN-T5）时，相比最强检索基线，精度最高提升8.77个百分点，Macro-F1最高提升17个百分点
3. 22%的查询可走短路推理路径，准确率达98.9%，单query latency降低1.37×
### 核心结论
ICL样本选择不能仅依赖与查询的特征相似性，还要兼顾候选样本集的标签纯度，自适应样本配额比固定k的检索方案在精度和效率上都更优
