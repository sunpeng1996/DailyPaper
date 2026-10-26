---
title: 'From Item Scores to Semantic Tokens: Test-Time Collaborative Adaptation for
  Generative Recommendation'
title_zh: 面向生成式推荐的测试时协同适配方法：从物品分数到语义令牌
authors:
- Xiongfeng Shan
- Xing Tang
- Hanchong Chen
- Fuyuan Lyu
- Lingjie Li
- Jingyan Jiang
- Duguang Liu
- Xiuqiang He
affiliations:
- Shenzhen Technology University
- McGill University
- Shenzhen University
arxiv_id: '2610.32098'
url: https://arxiv.org/abs/2610.32098
pdf_url: https://arxiv.org/pdf/2610.32098
published: '2026-10-23'
collected: '2026-10-26'
category: GenRec
direction: 生成式推荐 · 测试时自适应
tags:
- Generative Recommendation
- Test-time Adaptation
- Beam Search
- Semantic ID
- Collaborative Filtering
one_liner: 提出训练无关的测试时协同波束搜索适配方法，融合判别式信号缓解生成式推荐前缀过早剪枝问题
practical_value: '- 业务已落地成熟判别式召回/排序模型（如双塔、SASRec）的场景，可直接复用TCBSA框架对接语义ID类生成式推荐，无需重训两类模型，即可获得全场景效果提升，尤其适配用户兴趣漂移、新品冷启场景

  - 工程实现可复用「离线语义ID前缀-边映射预计算 + 测试时Top-R分数转边势能 + 置信门控调权」范式，仅需在生成模型beam pruning步骤前插入分数修正逻辑，对现有推理链路侵入性极低

  - 若生成式推荐latency预算有限，优先采用TCBSA+B=20配置，比单纯将原生beam宽度从20提升到50，NDCG@10高3.64%~26.94%，同时latency降低22%~32%，性价比显著更高

  - 针对用户新兴兴趣（如最近1-2次交互的新类目）的特殊召回需求，TCBSA相对原生生成式推荐NDCG@10最高提升103%，可直接用于大促流量倾斜、新品破圈等业务场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
语义ID类生成式推荐依赖自回归解码，beam search不可逆剪枝会过早过滤符合用户新兴兴趣的前缀路径；判别式推荐模型直接对全量物品打分，可捕捉生成式模型遗漏的弱兴趣信号，但二者预测空间不匹配（判别式输出完整物品分数，生成式做前缀token选择），此前的后融合方法无法修正已被剪枝的路径，也无无需重训模型的测试时适配方案。
### 方法关键点
- 离线预计算全量物品的Semantic ID到前缀-边的映射，跨用户全局复用
- 测试时用冻结的判别式模型对全物品打分，计算相对Top-R cutoff的分数margin，将margin聚合到对应语义边得到协同势能
- 新增置信门控：基于判别式分数的最大softmax值计算干预强度，判别置信低时降低势能权重，避免干扰原生生成效果
- 每次beam pruning前，将调权后的势能加到路径累积分上再筛选Top-B前缀，全程生成、判别模型均冻结无需修改
### 关键结果
在Amazon 3个领域+Yelp共4个全量目录数据集上，16个数据集-指标对全部最优，相对最强基线NDCG@10最高提升12.4%；新兴兴趣（仅1-2次最近交互的新类目）场景下，NDCG@10相对原生生成式最高提升103%；B=20的TCBSA配置比原生B=50的beam搜索NDCG@10高3.64%~26.94%，同时latency降低22%~32%；约5%的正确推荐来自判别式Top-500以外的物品，兼顾泛化性。
### 核心结论
生成式与判别式推荐的融合不要局限于最终列表后处理，在解码中间剪枝前介入，可在极低改造成本下获得显著效果收益。
