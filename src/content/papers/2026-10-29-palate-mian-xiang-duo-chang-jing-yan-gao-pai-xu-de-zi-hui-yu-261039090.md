---
title: 'PALATE: Pretrained Autoregressive LATent Embeddings'
title_zh: PALATE：面向多场景广告排序的自回归预训练隐式用户嵌入方法
authors:
- Sizhang Zhao
- Praveen Gondhi
- Bin Li
- Utsaw Kumar
affiliations:
- DoorDash
arxiv_id: '2610.39090'
url: https://arxiv.org/abs/2610.39090
pdf_url: https://arxiv.org/pdf/2610.39090
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 广告排序 · 预训练用户序列表示
tags:
- User Embedding
- Sequential Recommendation
- Ads Ranking
- Generative User Representation
- Pre-training
one_liner: 用轻量GPT风格序列模型生成可复用用户嵌入，作为特征提升多场景广告排序效果
practical_value: '- 可复用「预训练通用用户嵌入+下游排序直接消费特征」架构，避免每个业务场景单独建设序列建模模块，仅需一个离线日更任务生成嵌入即可降低多场景维护成本

  - 针对复购率高的本地生活/电商场景，训练序列模型时可添加探索权重，上调用户未交互新item的损失权重，避免模型仅拟合复购行为，提升新商家/新商品探索效果

  - 序列生成模型的负例可采用「热门item池+曝光未点击+随机/In-batch负例」的混合方案，相比纯随机负例大幅提升召回指标，同时用sampled softmax降低大vocabulary训练成本

  - 下游排序模型接入同空间的用户/物品嵌入时，可拼接原始向量、哈达玛积、余弦相似度三类衍生特征，最大化嵌入的信息利用率，效果优于直接喂入原始向量'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
DoorDash本地生活/外卖平台的广告排序此前仅依赖人工构造的统计特征、类别嵌入和无序池化的历史特征，缺乏端到端学习的用户序列表示；同时用户交互稀疏高基数，复购行为占比极高，常规序列模型容易偏向拟合已知复购行为，忽略新商家探索的核心需求，亟需一套通用用户表示同时适配浏览类Discovery场景和搜索类明确意图场景的排序需求。

### 方法关键点
- 输入为用户按时间排序的交互序列，每个位置拼接店铺ID、商家ID、5种上下文特征（时段、周末标识、当地时间、周几、是否广告）的嵌入后投影到模型主干维度
-  backbone为3层3头的轻量Decoder-only Transformer（GPT风格），上下文窗口200，输出最后一个token的256维隐藏态作为用户嵌入，softmax层输出的256维向量作为同空间的商家嵌入
- 两阶段训练：第一阶段用点击序列预训练覆盖广泛浏览行为，第二阶段用转化序列微调强化购买意图，采用暖启动避免预训练信息丢失
- 定制探索加权损失：用户未交互过的新商家目标权重设为0.9，复购商家权重设为0.1，倾斜模型对探索行为的拟合能力
- 负例混合构造：固定60K热门商家池+曝光未下单负例+随机/In-batch负例，配合sampled softmax降低10万级商家vocabulary的训练成本
- 下游DCNv2排序侧特征构造：拼接用户嵌入、商家嵌入、两者的哈达玛积、余弦相似度作为输入特征

### 关键结果
离线Eval-AUC相对提升Discovery场景+0.59%、搜索场景+0.57%，是单特征带来的最大增益，额外加入DIN序列模块仅带来0.03%的微小提升；线上A/B测试中，Discovery场景收入+0.79%、CVR+1.17%，搜索场景收入+0.94%、CVR+1.50%，所有核心指标均统计显著。

### 核心结论
预训练生成的通用冻结用户嵌入是性价比极高的大规模个性化落地路径，一套表示可同时适配多个意图差异极大的业务场景，收益远高于单场景重复建设序列建模模块。
