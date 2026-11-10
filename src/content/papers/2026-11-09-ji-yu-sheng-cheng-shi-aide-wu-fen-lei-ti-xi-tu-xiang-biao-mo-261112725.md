---
title: 'Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal'
title_zh: 基于生成式AI的无分类体系图像标注规模化方法：多模态搜索应用
authors:
- Zhenjie Zhang
- Sainan Chen
- Kshiteesh Hegde
- Mengze
- Li
- Pouya Rezazadeh Kalehbasti
- Munachim Ezema
- Karina Sobhani
affiliations:
- Pinterest, Inc.
arxiv_id: '2611.12725'
url: https://arxiv.org/abs/2611.12725
pdf_url: https://arxiv.org/pdf/2611.12725
published: '2026-11-09'
collected: '2026-11-10'
category: QueryRec
direction: 多模态搜索 Query 推荐优化
tags:
- Multimodal Search
- VLM
- Image Labeling
- Clustering
- Query Suggestion
one_liner: 提出GLOC聚类标注框架，大幅降低VLM图像标注成本，提升多模态搜索query推荐效果
practical_value: '- 高成本大模型打标场景可复用「聚类+打标簇中心」的降本思路：针对语义相似的物品/内容先聚类，仅对簇代表性样本用大模型生成标签/query，簇内所有样本复用结果，可将大模型打标成本降低2-3个数量级

  - 大规模聚类工程可直接采用分层K-means方案：先粗聚类拆分数据集到单GPU可承载的分片，再分片做细聚类，时间复杂度从O(N²)降到O(N)，适配十亿级样本的聚类需求

  - 多模态搜索query推荐可拆分descriptor（属性描述）和pivot（修改意图）两类，分别适配用户静态信息获取和动态意图跳转需求，实测可显著提升搜索点击率和后续feed
  engagement'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统图像标注依赖人工构建的固定分类体系，存在覆盖范围有限、迭代成本高、标注误差大的问题；直接用VLM做全量图像标注的推理成本高、延迟大，无法支撑十亿级图像的多模态搜索query推荐需求。
### 方法关键点
- 离线分层K-means聚类：先粗聚类将十亿级图像拆分为单GPU可承载的分片，再对每个分片做细粒度聚类，每个簇平均2000张语义高度相似的图像，选取距簇中心最近的图像作为代表样本
- 仅对簇代表样本输入VLM生成两类query：descriptor（图像属性描述短语，如风格、颜色）、pivot（可执行修改短语，如调整长度、更换颜色），将结果存入KV存储
- 在线服务：图像输入后先通过ANN或浅层神经网络查询所属簇ID，直接从KV存储读取预生成的query返回，延迟远低于实时VLM推理
### 关键实验
离线人工评估显示，pivot适用性得分3.5/4，descriptor相关性得分2.51/3，无关率仅4%；线上A/B测试对比无推荐的对照组，pivot CTR提升146%、对应feed engagement提升79%，descriptor对应feed engagement提升79%；对比基于文本GPT的基线方案，pivot CTR提升69.5%、对应feed engagement提升100%；标注成本仅为全量VLM打标的0.05%。
### 核心结论
大模型生成能力落地大规模业务的核心是找到合适的降本路径，通过语义聚类复用生成结果是兼顾效果、成本、延迟的可行方案
