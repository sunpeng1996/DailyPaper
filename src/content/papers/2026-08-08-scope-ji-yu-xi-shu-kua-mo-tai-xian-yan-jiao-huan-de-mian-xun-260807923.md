---
title: 'SCoPE: Training-Free Audio-Visual Event Perception via Sparse Cross-Modal
  Prior Exchange'
title_zh: SCoPE：基于稀疏跨模态先验交换的免训练音视频事件感知框架
authors:
- Jaemo Jeong
- Junho Yoon
- Hyunju Kim
- Dongman Lee
affiliations:
- KAIST
arxiv_id: '2608.07923'
url: https://arxiv.org/abs/2608.07923
pdf_url: https://arxiv.org/pdf/2608.07923
published: '2026-08-08'
collected: '2026-08-13'
category: Multimodal
direction: 多模态事件感知 · 免训练跨模态对齐
tags:
- Multimodal Perception
- Training-Free
- Cross-Modal Alignment
- Audio-Visual Learning
- Zero-Shot Learning
one_liner: 提出免训练跨模态音视频事件感知框架SCoPE，通过标签竞争与模态互指导解决伪共激活问题
practical_value: '- 短视频/直播多模态内容理解场景（如商品事件识别、违规内容检测）可复用标签竞争消歧逻辑，解决语义相近标签误匹配问题

  - 跨模态分类/检索任务可借鉴模态间相互校验思路，无需微调预训练大模型即可提升下游任务准确率

  - 零样本类目拓展场景（如新品类短视频标签生成、新增事件检测）可参考无训练框架设计，大幅降低新增类目时的标注与训练成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有免训练音视频事件感知方法通过匹配冻结音、视觉特征与文本编码事件名实现零样本查询，但语义相近标签会共享特征证据产生伪共激活（FCA）问题，单一打分阈值或类别专属阈值都无法从根源消除FCA对底层打分向量的干扰。
### 方法关键点
提出SCoPE免训练框架：1. 让所有查询标签竞争共享特征证据，2. 音、视觉模态各自引导另一模态的事件选择，同时推导了双标签场景下竞争机制消除FCA的精确生效条件。
### 关键结果
基于相同冻结CLIP+CLAP backbone，在LLP数据集上Type@seg较AV²A提升7.45个百分点，Event@seg提升5.04个百分点，固定配置可直接迁移到OV-AVEBench、VGGSound-AVEL100k数据集无需调整。
