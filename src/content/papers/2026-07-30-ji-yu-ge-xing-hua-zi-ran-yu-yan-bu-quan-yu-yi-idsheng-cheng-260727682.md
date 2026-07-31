---
title: Restoring Collaborative Signals in Semantic-ID Generative Recommendation via
  Personalized Natural Language
title_zh: 基于个性化自然语言补全语义ID生成式推荐的协同信号
authors:
- Changjiang Han
- Qingyang Li
- Yaqiang Zang
- Jikun Kang
- Pinghua Gong
- Xue Liu
- Bowei He
affiliations:
- MBZUAI
- JD.com
- Salesforce
- McGill University
- Mila – Quebec AI Institute
arxiv_id: '2607.27682'
url: https://arxiv.org/abs/2607.27682
pdf_url: https://arxiv.org/pdf/2607.27682
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · Semantic ID协同信号补全
tags:
- GenRec
- Semantic ID
- Collaborative Filtering
- LLM4Rec
- Training-free
one_liner: 无需重训冻结Semantic ID生成推荐模型，通过个性化自然语言桥接协同信号提升精度
practical_value: '- 不需要重训已上线的Semantic ID生成式推荐主干，仅通过推理阶段分层重排序即可引入协同信号，升级成本极低，适合业务快速迭代

  - 二阶item共现矩阵采用HPF因子分解的效果优于SVD、K-means方案，可直接复用在协同信号离线挖掘环节

  - 用户历史LLM摘要标签映射到协同因子空间的桥接方案，可实现语言层面的偏好干预，适配可解释推荐、自定义人群定向需求

  - 推理阶段分层处理Semantic ID的思路（粗码扩召回、中码重排序、细码控库存）可直接套用到电商分层语义ID生成流程中'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Semantic ID生成式推荐仅基于物品内容编码生成ID，无法同时承载内容与协同信号，导致用户协同行为规律丢失；直接添加CoT推理、prompt注入偏好反而会降低精度，根源是文本与SID嵌入空间不匹配，缺少可靠的协同信号传递通道。
### 方法关键点
- 离线构建二阶协同语义桥：统计item共现矩阵，用分层泊松因子分解（HPF）得到物品协同因子，按SID的sa、sb前缀聚合得到前缀签名
- 自然语言桥接：用LLM将用户交互历史总结为受众、行为风格标签，训练轻量映射模型把标签映射到协同因子空间，生成用户个性化查询向量
- 推理阶段分层重排序：冻结主干模型，sa层加协同得分扩展召回候选，sb层用用户向量重排序，sc层加库存过滤，不增加beam宽度与额外GPU推理成本
### 关键实验
基于RecIF基准的826个GT不重叠样本，在冻结的OneRec-1.7B/8B主干上测试，对比无干预基线、语义重排序基线；OneRec-8B上hit@10从11.14提升到15.50，相对提升39%，中码sb重排序贡献了大部分增益，普通语义重排序仅提升到11.86。
### 核心结论
Semantic ID的内容与协同信号冲突无需通过重训ID编码解决，推理阶段通过自然语言桥接协同信号即可低成本实现显著增益
