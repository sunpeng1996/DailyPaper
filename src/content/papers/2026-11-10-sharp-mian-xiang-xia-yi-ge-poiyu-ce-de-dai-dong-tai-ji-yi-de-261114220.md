---
title: 'SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with
  Dynamic Memory'
title_zh: SHARP：面向下一个POI预测的带动态记忆的语义分层Agent推理框架
authors:
- Yuhang Zhan
- Silin Zhou
- Zhuo Chen
- Haoxiang Lei
- Yunren Feng
- Lisi Chen
- Shuo Shang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2611.14220'
url: https://arxiv.org/abs/2611.14220
pdf_url: https://arxiv.org/pdf/2611.14220
published: '2026-11-10'
collected: '2026-11-11'
category: GenRec
direction: 生成式推荐 · Agent分层推理+Semantic ID
tags:
- Semantic ID
- POI Recommendation
- Agentic Reasoning
- Dynamic Memory
- RQ-VAE
one_liner: 提出分层Agent先预测POI类别再结合Semantic ID引导下游预测，兼顾推理效率与准确率
practical_value: '- 可复用「粗分类预测+细粒度item排序」的分层架构：在电商全品类推荐场景下，先让LLM预测用户接下来的消费类目，再引导下游SKU排序，大幅降低LLM输出空间，避免直接预测海量ID的语义对齐问题

  - 动态记忆库设计可直接迁移到LLM用户建模：将用户长期行为摘要为固定长度的profile，每次仅增量更新，无需全量输入历史行为，可降低80%+的token消耗，同时保留长周期行为规律

  - 多粒度时间感知转移图可复用到时序敏感推荐场景：针对不同时段（工作日/周末、早中晚）单独构建类目/品类转移概率，替代全局转移统计，更好捕捉不同时间的差异化行为规律

  - 基于RQ-VAE的Semantic ID学习方法可复用：编码时融合行为、品类、时空等多维度特征，让语义相似的item共享ID前缀，可同时用于生成式召回和排序任务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
下一个POI预测是本地生活、出行服务推荐的核心任务，现有方法存在三大痛点：一是LLM直接预测海量raw ID的POI时，语义对齐难度大，效果不佳；二是用户长周期行为全量输入LLM会快速超出上下文窗口，token成本极高；三是全局POI转移图会抹平不同时间维度的差异化类目转移规律，比如工作日早晨咖啡店→办公室、周末夜晚咖啡店→酒吧的规律会被全局统计抵消。
### 方法关键点
- 分层推理架构：先由Agent完成POI类目预测，再用类目结果引导下游细粒度POI排序，让LLM只做擅长的语义推理任务，降低输出空间
- 动态轨迹记忆库：由用户长期行为profile、近期状态、统计特征三部分构成，每次仅增量输入新行为更新记忆，无需全量喂入历史序列
- 多粒度时间感知类目转移图：构建全局、周类型、小时段、联合维度共21张转移图，预测时匹配目标时间对应的转移规则，保留时间特异的行为规律
- 语义POI表示：通过RQ-VAE融合POI的行为、类目、时空特征生成Semantic ID，相似POI共享ID前缀，与下游预测器端到端联合优化
### 关键实验
在NYC、TKY、CA三个真实POI数据集上对比12个基线方法，相比最强基线CoMaPOI，Acc@5平均提升5.29个百分点，Acc@10平均提升4.52个百分点；动态记忆相比全量输入历史的token消耗降低86.14%~91.86%，同时类目预测Acc@5相比仅用近期序列提升10.11~12.70个百分点。
### 核心结论
让LLM聚焦擅长的语义推理任务，专业的细粒度排序交给专门的推荐模型，分层协作可同时兼顾LLM的知识优势和推荐系统的效率与精度优势
