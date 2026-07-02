---
title: Real-Time Hard Negative Sampling via LLM-based Clustering for Large-Scale Two-Tower
  Retrieval
title_zh: 面向大规模双塔检索的基于LLM聚类的实时难负样本采样方法
authors:
- Ivan Ji
- Liuyi Hu
- Harrison
- Zhao
- Lei Huang
- Qunshu Zhang
- Max
- Fan
- Aameek Singh
affiliations:
- Meta
arxiv_id: '2607.00448'
url: https://arxiv.org/abs/2607.00448
pdf_url: https://arxiv.org/pdf/2607.00448
published: '2026-07-01'
collected: '2026-07-02'
category: RecSys
direction: 推荐系统 · 双塔召回负采样优化
tags:
- Two-Tower
- Hard Negative Sampling
- LLM Clustering
- Retrieval
- Popularity Debias
one_liner: 基于LLM语义聚类构建实时难负采样框架，大幅提升双塔检索效果同时缓解流行度偏差
practical_value: '- 负采样逻辑可直接复用：放弃高成本的ANN难负采样，改用同语义簇采样，无需修改模型结构，训练开销极低，效果提升显著

  - LLM聚类落地路径清晰：用业务场景微调的多模态LLM生成item语义簇，比传统类目划分更精准，适配电商多模态商品、短视频/内容推荐场景

  - GOOBS工程框架可直接复用：分簇item池+哈希映射的更新/采样逻辑，适配数十亿级训练数据，仅需对现有训练pipeline做轻量改造即可上线

  - 可同步解决业务痛点：该方案天然缓解流行度偏差，无需额外加纠偏逻辑，即可提升长尾商品/内容的曝光，打破推荐反馈环'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有双塔召回的负采样方案存在明显缺陷：in-batch负采样受batch size限制易引入偏差，随机out-of-batch（OOB）负样本区分度过低无法提供有效训练信号，同时长期反馈环会加剧推荐系统的流行度偏差，而现有难负采样方法（如ANCE）需要维护全局ANN索引，计算成本过高无法适配大规模工业生产场景。

### 方法关键点
- 基于微调的多模态LLM生成item的语义表示，做粒度适中的聚类，避免簇过细导致的假负样本问题
- 设计GOOBS实时采样框架：维护按簇划分的全局item池，训练时in-batch样本实时更新池内item特征，采样时直接从正样本所属簇内随机抽取OOB负样本
- 无需修改双塔模型结构与损失函数，可无缝嵌入现有生产训练链路

### 关键结果
- 公开数据集：对比in-batch baseline、DNS、ANCE等主流方案，在Amazon Electronics数据集上HR@50相对提升55.6%，优于所有基线
- 工业A/B测试：CTR相对提升53%，训练QPS仅下降1.4%，无推理性能损耗；top 100热门商品曝光占比从50%降至32%，千次曝光以上的长尾商品占比提升50%

**最值得记住的结论**：基于语义簇的难负采样落地成本远低于几何近邻难负方案，效果更优，同时可天然缓解流行度偏差，是工业级双塔召回的高性价比优化方向
