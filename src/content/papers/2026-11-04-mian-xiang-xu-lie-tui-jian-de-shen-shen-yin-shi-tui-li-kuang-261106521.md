---
title: Deliberate Latent Reasoning for Sequential Recommendation
title_zh: 面向序列推荐的审慎隐式推理框架DESRec
authors:
- Haobo Zhang
- Qiannan Zhu
- Yutao Zhu
- Zhicheng Dou
affiliations:
- Renmin University of China
- Beijing Normal University
- Engineering Research Center of Intelligent Technology and Educational Application,
  MOE
arxiv_id: '2611.06521'
url: https://arxiv.org/abs/2611.06521
pdf_url: https://arxiv.org/pdf/2611.06521
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 序列推荐 · 隐式推理增强
tags:
- Sequential Recommendation
- Latent Reasoning
- Self-Distillation
- User Preference Modeling
- Transformer
one_liner: 提出个性化隐式推理框架DESRec，无额外推理开销即可显著提升序列推荐效果
practical_value: '- 可直接复用「训练阶段最优推理步自蒸馏到固定推理步」的trick，无需修改推理部署逻辑，即可解决固定推理步带来的过/欠推理问题，拿到多步推理的性能收益

  - 长用户行为序列建模可借鉴渐进式偏好提取的滑动窗口里程碑设计，每个窗口取最后一个隐态作为阶段偏好表征，效果优于max/avg pooling，还可降低长序列推理开销

  - 隐式推理搭配KV cache优化后，10步推理单样本仅增加约0.09ms延迟，完全满足电商/内容推荐场景的线上实时吞吐要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于隐式推理的序列推荐方法采用统一固定的推理步数，对行为简单的用户易出现过推理引入冗余噪声，对行为复杂的用户易出现欠推理丢失关键偏好信息；若在推理侧动态选择最优推理步数，又会大幅增加部署复杂度和推理开销，无法适配线上高吞吐的推荐场景需求。
### 方法关键点
- 推理步选择模块（RESS）：训练阶段为每个用户序列计算各推理步表征与Ground Truth item的相似度，选最高的作为最优步，通过自蒸馏将最优步的全item排序分布压缩到最后一个固定推理步，推理时直接输出最后一步结果即可，无需动态调整
- 渐进式偏好提取模块（PPEM）：用固定大小滑动窗口切分用户行为序列，每个窗口取最后一个隐态作为该阶段的偏好里程碑，将里程碑序列作为推理输入的一部分，动态适配不同长度的用户行为序列，捕捉用户演化的兴趣
- 训练目标结合最优步的推荐交叉熵损失与蒸馏KL散度损失，平衡推荐精度和蒸馏效果
### 关键实验
在Yelp、Amazon 4个子数据集、MovieLens-1M共6个公开数据集上测试，适配SASRec、BERT4Rec等4个主流序列推荐backbone，对比8个基线模型；NDCG@10相对最强基线ReaRec最高提升13.94%，平均提升7%左右；搭配KV cache优化后，10步推理单样本延迟仅0.22ms，与基线推理开销基本持平。
### 核心结论
隐式推理增强推荐无需在推理侧做动态调整，通过训练侧最优步蒸馏即可在不增加部署复杂度的前提下获得稳定性能收益
