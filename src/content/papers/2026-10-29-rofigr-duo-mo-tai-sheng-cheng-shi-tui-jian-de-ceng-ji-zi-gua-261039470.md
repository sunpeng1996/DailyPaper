---
title: 'RoFiGR: Coarse Routing, Fine Refinement via Level-Adaptive Distillation in
  Multimodal Generative Recommendation'
title_zh: RoFiGR：多模态生成式推荐的层级自适应蒸馏粗路由-细优化框架
authors:
- Ji Dai
- Zhipeng Wei
- Zhuang Zhuang
- Rongfeng Guo
- Jie Chen
- Quan Fang
- Fei Pan
affiliations:
- Beijing University of Posts and Telecommunications
- Kuaishou Technology
arxiv_id: '2610.39470'
url: https://arxiv.org/abs/2610.39470
pdf_url: https://arxiv.org/pdf/2610.39470
published: '2026-10-29'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · 多模态Semantic ID
tags:
- Generative Recommendation
- Multimodal Recommendation
- Semantic ID
- Knowledge Distillation
- Sequential Recommendation
one_liner: 提出融合协同信息粗对齐与层级自适应蒸馏的多模态生成式推荐框架提升路由准确率
practical_value: '- Semantic ID构造可复用L1-L2粗编码与冻结CF item embedding的对比对齐方案，无需修改量化流程即可让粗聚类更贴合用户行为偏好，降低早期路由错误率

  - 序列编码侧可直接在Transformer第一层注意力添加item距离、来源层级偏置项，仅新增数百个参数即可解决扁平SID序列的结构信息丢失问题，落地成本极低

  - 蒸馏优化可借鉴固定粗层级锚点+需求自适应残差的权重分配策略，将传统SeqRec模型的item分数聚合为SID分支软标签，蒸馏过程无在线依赖，不影响推理性能

  - 推理阶段可复用多流beam search结果等权融合的方案，业务场景可根据延迟要求灵活选择2流（低延迟）或4流（高准确率）配置，适配不同等级的服务需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多模态生成式推荐基于层级Semantic ID（SID）自回归解码，早期L1-L2粗路由的决策错误会直接将相关item排除在候选池外，现有方案未显式区分SID不同层级的训练目标，粗路由阶段缺乏协同偏好引导，导致早期准确率低、候选召回范围偏差大。
### 方法关键点
- SID构造：对文本、图像双树的L1-L2累计编码向量，与冻结的协同过滤预训练item embedding做对比学习对齐，让粗聚类同时贴合内容语义和用户行为偏好，L3-L4保留细粒度语义不受约束
- 序列编码：在编码器第一层自注意力额外添加token距离、item距离、来源层级三类偏置项，解决扁平SID序列丢失item边界和层级信息的问题，无主模型结构改动
- 蒸馏优化：将冻结SeqRec教师的item分数聚合为各SID层级的合法分支软标签，蒸馏权重采用固定粗层级锚点（L1=0.1、L2=0.075、L3-L4=0）加需求自适应残差的分配策略，仅在教师信号优于学生和类目先验时增加对应层级权重
- 推理：支持2/4路beam search解码，各路结果归一化后等权融合，无在线教师依赖，可灵活平衡延迟和准确率
### 关键结果
在Amazon的Instruments、Arts、Games三个公开数据集上，对比TIGER、MACRec、SynGR等SOTA生成式推荐基线，所有5个排序指标（HR@1/5/10、NDCG@5/10）均最优，相对最强基线的NDCG@10提升6.2%~13.8%，平均相对增益9.4%，所有提升均通过Holm校正的显著性检验。
### 核心结论
生成式推荐的性能瓶颈很大概率在早期粗路由阶段，对Semantic ID的粗层级引入协同信息约束和定向蒸馏的收益远高于优化细层级解码。
