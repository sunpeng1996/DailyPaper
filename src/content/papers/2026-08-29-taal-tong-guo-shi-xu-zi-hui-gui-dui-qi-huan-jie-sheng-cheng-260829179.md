---
title: 'TAAL: Mitigating Early Beam Pruning in Generative Recommendation via Temporal
  Autoregressive Alignment'
title_zh: TAAL：通过时序自回归对齐缓解生成式推荐的早期剪枝问题
authors:
- Lianjie Li
- Zhiying Tu
- Dianhui Chu
- Hongliang Sun
affiliations:
- 哈尔滨工业大学
arxiv_id: '2608.29179'
url: https://arxiv.org/abs/2608.29179
pdf_url: https://arxiv.org/pdf/2608.29179
published: '2026-08-29'
collected: '2026-09-01'
category: GenRec
direction: 生成式推荐 · 解码剪枝优化
tags:
- Generative Recommendation
- Semantic ID
- Beam Search
- Temporal Alignment
- PMI Calibration
one_liner: 针对生成式推荐Semantic ID解码早期不可逆剪枝 提出训练推理双阶段优化框架显著提升推荐效果
practical_value: '- 落地基于Semantic ID的生成式推荐时，优先统计解码前2步的ground truth剪枝率，若90%左右的召回错误集中于此，可直接复用TAAL的双阶段优化逻辑，无需改动原有的LLM骨干与SID体系

  - 训练侧可低成本叠加(c1,c2)联合前缀的前向KL对齐损失：仅采样Kmc=2个分支计算，计算量几乎可忽略，α取0.2-0.3即可适配多数场景，能直接提升真实候选的beam留存率

  - 推理侧可加O(B)复杂度的PMI校准：无需修改beam search流程，仅对Top-B候选rerank时减去全局前缀流行度偏差，β统一取0.02泛用性强，无额外latency即可获得稳定的NDCG提升

  - 针对线上低延迟要求、只能用窄波束（B=5~10）的场景，该方法收益更高，ground truth全SID留存率相对提升可达27%~39%，特别适配电商实时推荐场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐采用分层Semantic ID（SID）对物品编码，通过自回归解码生成下一个交互物品，但标准next-token预测目标没有显式建模交互序列中的多模态转移，导致beam search早期（前2步）就会不可逆剪除掉真实样本的前缀。三个公开数据集统计发现，91.9%~96.6%的召回错误都发生在前两步解码，直接决定最终推荐效果，现有优化方法大多只针对单个正样本路径，未利用语料级时序转移分布做覆盖性监督。

### 方法关键点
- 训练阶段：基于历史交互的指数衰减聚合构造(c1,c2)联合前缀软目标，通过链式法则分解为前向KL损失，仅采样Kmc=2个分支做无偏估计，无需枚举所有候选，保证模式覆盖，避免模型坍缩到少数高频路径
- 推理阶段：用点互信息（PMI）校准候选得分，减去全局前缀的边际频率消除流行度偏差，仅对Top-B候选rerank，复杂度O(B)，无需修改解码流程

### 关键实验结果
在Amazon Beauty、Amazon Instruments、Yelp三个公开数据集上，对比LETTER、DIGER、APAO等SOTA生成式推荐基线，TAAL的NDCG@10分别比标准基线提升39.5%、6.7%、28.6%，真实样本全SID留存率提升3.9%~16.6%；当beam width缩小到5时，全SID留存率相对提升可达39.4%，波束越窄收益越高。

### 最值得记住的结论
生成式推荐的召回错误90%以上集中在SID解码前2步，针对该环节做轻量优化的收益远高于盲目堆叠复杂的骨干或编码方案。
