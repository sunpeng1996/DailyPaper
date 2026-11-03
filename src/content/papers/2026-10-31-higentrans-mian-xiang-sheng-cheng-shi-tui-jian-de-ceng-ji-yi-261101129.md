---
title: 'HiGenTrans: Hierarchical LLM Knowledge Transfer for Generative Recommendation'
title_zh: HiGenTrans：面向生成式推荐的层级LLM知识迁移框架
authors:
- Zhuohang Jiang
- Yuxin Chen
- Haohao Qu
- ZeFei luo
- Yunlong Wang
- Xu Yuan
- Haojie Ding
- Boheng Zhang
- Fan Yang
- Hongyang Wang
affiliations:
- The Hong Kong Polytechnic University
- Kuaishou Technology
arxiv_id: '2611.01129'
url: https://arxiv.org/abs/2611.01129
pdf_url: https://arxiv.org/pdf/2611.01129
published: '2026-10-31'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · LLM知识迁移
tags:
- GenRec
- Semantic ID
- Knowledge Transfer
- LLM4Rec
- MoE
one_liner: 在输入、表征、决策三层向生成式推荐迁移LLM语义知识，兼顾效果与工业部署效率
practical_value: '- LLM知识注入不要局限于输入层拼接，可按Transformer相对深度对齐注入，搭配均值中心化+残差门控减少跨空间分布偏移，适配现有GenRec
  backbone的改造成本极低

  - 解决生成式推荐beam搜索排序错位问题，可新增轻量MoE校准模块，融合语义相似度、生成置信度、候选集上下文三类特征重排，NDCG增益显著

  - 工业部署可采用「冻结LLM离线提取特征+量化为Semantic ID存储+在线码本重建」方案，完全规避在线调用LLM的推理与带宽开销

  - 该框架对长尾商品、短/长历史用户均有稳定增益，尤其长尾商品NDCG@10提升可达40%+，适合电商长尾流量挖掘场景'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有生成式推荐（GenRec）仅依赖交互数据监督，未充分利用预训练LLM的层级语义知识，且beam搜索按序列似然排序与物品真实相关性存在天然错位，导致效果天花板低，工业落地性价比不足。

### 方法关键点
- **全局语义启动（GSP）**：将冻结LLM输出的用户历史全局语义表征投影后加到BOS嵌入，为SID生成提供语义先验
- **层级表征迁移（HRT）**：按相对深度对齐LLM中间层与GenRec backbone层，经均值中心化、投影、RMSNorm后通过可训练残差门控注入，保留协作信号的同时补充层级语义
- **多信号决策校准（MDC）**：用轻量MoE融合语义相关性、生成置信度、候选集上下文三类特征，对beam生成的候选重排，修正排序错位
- 工程优化：LLM特征全量离线计算，量化压缩为Semantic ID存储，在线仅通过码本重建，无额外LLM推理开销

### 关键结果
在Amazon Beauty、Sports、Toys三个公开数据集对比SASRec、TIGER、GRLM等SOTA基线，Recall@10最高提升12.9%，NDCG@10最高提升33.7%；电商工业场景下粗粒度SID预测准确率最高提升61.98个百分点，冷启动/长尾场景增益更显著。

**最值得记住的结论**：LLM语义知识向生成式推荐的迁移应覆盖输入、表征、决策全链路，而非仅做单阶段融合，可同时实现效果提升与工业级部署效率。
