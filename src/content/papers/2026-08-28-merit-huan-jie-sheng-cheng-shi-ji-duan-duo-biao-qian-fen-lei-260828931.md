---
title: 'MERIT: Mitigating Exposure Bias in Generative XMC for User-Interest Propensity
  Modeling'
title_zh: MERIT：缓解生成式极端多标签分类曝光偏差的用户兴趣倾向建模框架
authors:
- Abhinav Mahajan
- Arindam Sarkar
- Prakash Mandayam Comar
affiliations:
- Carnegie Mellon University
- Amazon
arxiv_id: '2608.28931'
url: https://arxiv.org/abs/2608.28931
pdf_url: https://arxiv.org/pdf/2608.28931
published: '2026-08-28'
collected: '2026-09-01'
category: GenRec
direction: 生成式推荐 · 用户兴趣倾向建模
tags:
- Generative XMC
- Exposure Bias
- User Interest Modeling
- Hard Negative Mining
- Recommendation System
one_liner: 通过离线硬负挖掘+排列不变多目标损失缓解生成式XMC曝光偏差，提升用户兴趣召回与线上转化
practical_value: '- 生成式多标签任务（如用户兴趣打标、商品标签生成）可复用离线硬负+混合前缀的自校正训练范式，无需RL/调度采样即可低成本缓解曝光偏差，避免关联标签过生成

  - 用户长序列压缩可借鉴按时间远近的自适应patching策略，老交互做池化压缩、新交互保留全量，既能容纳长周期历史又不丢关键信号，还能严格控制token预算

  - 生成模型标签起始位的隐状态天然对齐用户兴趣倾向，可直接蒸馏到小参数打分模型，实现双向检索，兼顾生成模型的泛化性和排序模型的线上效率

  - 上游召回类任务可主动接受少量精度损失换更高召回，下游规则过滤的成本远低于漏召回的业务损失，该tradeoff在电商人群圈选、个性化召回场景通用'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商平台用户兴趣标签空间达数十万级、长尾性强且动态迭代，生成式极端多标签分类（XMC）是用户兴趣倾向建模的理想方案，但teacher-forcing微调带来的曝光偏差会触发关联标签生成 cascade：一旦早期生成某类标签，后续会持续输出同类关联标签，漏召回用户的独立真实兴趣，严重影响下游召回、人群圈选效果。现有缓解曝光偏差的RL、调度采样等方法训练成本过高，无法落地极端大标签场景。

### 方法关键点
- 离线硬负挖掘：先用普通交叉熵训练初始生成器，温度采样生成可信错误标签，过滤与金标语义相似度>0.6的近同义词，构成混合标签集
- 自校正训练目标：金标+硬负标签打乱后做teacher-forcing单步前向，标签起始分类位只计算金标首词的排列不变损失，遇到错误前缀仍强制生成完整合理标签，既暴露错误场景又不学习错误输出
- 自适应patching：用户长序列中老交互做10倍池化压缩、新交互保留全量token，在固定预算下装下全年用户交互历史
- 轻量倾向打分模型：取生成器分类位的倾向对齐隐状态，蒸馏到230M小参数模型，输出跨用户可比的打分，支持双向检索

### 关键结果
在亚马逊291k兴趣标签的私有电商数据集上，对比XLGen、GROOV、双编码器等SOTA基线，全局召回提升至少11.9%，平均Hit@k提升6.1%，线上A/B测试用户转化率平均提升0.26%。

### 核心结论
生成式多标签任务的曝光偏差核心是关联标签 cascade 导致的召回损失，通过低成本的混合前缀自校正训练即可大幅缓解，无需引入复杂的RL训练流程。
