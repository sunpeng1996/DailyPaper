---
title: 'Reasoning Quality Matters: Combating Reasoning Collapse in LLM-based Embedding
  Learning'
title_zh: 解决LLM嵌入学习推理崩溃问题的CoFree双阶段优化框架
authors:
- Zihan Gong
- Xiaohan Ye
- Jiangchao Yao
- Jinsong Lan
- Xiaoyong Zhu
- Xu Chen
affiliations:
- Alibaba Group
- Taobao
- Wuhan University
- Shanghai Jiao Tong University
arxiv_id: '2609.20563'
url: https://arxiv.org/abs/2609.20563
pdf_url: https://arxiv.org/pdf/2609.20563
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: LLM 嵌入学习 · 推理增强检索
tags:
- LLM Embedding
- Reasoning Collapse
- Dual-stage Training
- Retrieval
- Reinforcement Learning
one_liner: 提出双阶段CoFree框架缓解LLM嵌入学习的推理崩溃问题，显著提升检索性能且已落地电商搜索
practical_value: '- 做推理增强嵌入时可复用双阶段训练范式：先SFT用参考模型锚定原始嵌入能力+恢复推理生成，再RL用双 reward 同时优化检索效果和推理相关性，避免推理崩溃

  - RL阶段可借鉴嵌入空间MSE正则设计，仅靠生成侧的KL惩罚不足以避免嵌入能力退化，增加与SFT后参考模型的 embedding MSE 损失能稳定效果

  - 电商搜索/推荐召回场景可直接落地CoFree增强的语义嵌入，论文验证其作为新增召回通道能带来CTR+0.02、CVR+0.12、订单相对+13.56%、GMV相对+8.15%的显著增益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的推理增强嵌入方法存在「推理崩溃」问题：要么为优化嵌入目标抑制生成能力，出现空输出、重复、不通顺的生成崩溃；要么推理文本语义无关、缺乏判别性，出现语义崩溃，反而劣化检索效果，亟需在保留原有嵌入能力的前提下提升推理质量。
### 方法关键点
- 第一阶段推理恢复SFT：联合优化三类损失，语言建模损失恢复推理生成能力，对比损失保证嵌入判别性，参考引导损失用冻结的原始嵌入骨干做锚，对齐推理增强后嵌入与原始嵌入，避免能力退化
- 第二阶段推理增强RL：基于GRPO优化，设计双奖励机制，嵌入导向 reward 用正负样本相似度差保障检索效果，推理导向 reward 用独立重排模型的正负分差保障推理内容与检索相关，额外增加嵌入空间MSE正则避免嵌入漂移
- 构建3.6M规模的RTED数据集，覆盖多领域检索场景，用于推理增强嵌入训练
### 关键实验
在22个公开数据集（10个MTEB检索子集、12个BRIGHT推理密集检索子集）上测试，CoFree-4B较基线Qwen3-Embedding-4B的nDCG@10绝对提升2.8点，CoFree-1.5B较同规模最强基线提升3.2点；电商搜索线上A/B测试作为新增召回通道，获得CTR+0.02、CVR+0.12、订单相对提升13.56%、GMV相对提升8.15%的收益，已全量部署。
> 最值得记住：推理增强嵌入的核心不是是否加推理，而是如何保证推理对检索忠实有用，避免双重崩溃
