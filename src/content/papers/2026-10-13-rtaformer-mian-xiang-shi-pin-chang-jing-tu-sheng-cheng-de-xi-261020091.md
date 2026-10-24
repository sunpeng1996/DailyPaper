---
title: 'RTAformer: Relation-Transition-Aware Transformer for Video Scene Graph Generation'
title_zh: RTAformer：面向视频场景图生成的关系转移感知Transformer
authors:
- Jaeyeon Heo
- Geuntaek Lim
- Yukyung Choi
affiliations:
- Sejong University
arxiv_id: '2610.20091'
url: https://arxiv.org/abs/2610.20091
pdf_url: https://arxiv.org/pdf/2610.20091
published: '2026-10-13'
collected: '2026-10-24'
category: Multimodal
direction: 多模态视频理解 · 场景图生成
tags:
- VidSGG
- Transformer
- Spatio-Temporal Modeling
- Scene Graph
- Video Understanding
one_liner: 提出实体-关系分离建模的RTAformer，解决视频场景图生成的关系语义惯性问题
practical_value: '- 短视频电商内容理解场景可借鉴相邻帧关系差分注入方法，减少时序推理的语义惯性，提升动态商品-人物关系识别准确率

  - 具身Agent环境感知模块可复用跨帧实例对齐训练策略，降低跨帧表征漂移，提升连续动作决策的稳定性

  - 信息流时序推荐可参考实体与关系分离建模思路，同时兼顾用户兴趣持久性与场景跳转的突变性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频场景图生成（VidSGG）需同时建模实体身份持久性与关系突变特性，现有方法侧重跨帧时序信息聚合、强调一致性，易产生关系语义惯性——底层关系已变化但模型仍保留历史预测，无法适配关系跳转场景。
### 方法关键点
1. 单阶段RTAformer框架，对实体持久性和关系变化分开建模；
2. 推理阶段注入相邻帧关系查询的校准差值，引导谓词更新；
3. 训练阶段引入跨帧实例对齐机制，降低跨帧表征漂移。
### 关键结果
在Action Genome数据集上，recall与mean recall均优于现有方法，关系转移帧上的性能增益显著高于非转移帧，消融实验验证了各组件的有效性。
