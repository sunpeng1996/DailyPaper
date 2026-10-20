---
title: 'Joint, Decoupled, or Agent: When Each Multimodal Alignment Paradigm Wins'
title_zh: 联合、解耦与Agent范式：多模态对齐场景下的最优选型规律
authors:
- Yi Fang
- Gaurav Srivastava
- Sirui Ding
- Xuan Wang
affiliations:
- Virginia Tech
- Stanford University
arxiv_id: '2610.24108'
url: https://arxiv.org/abs/2610.24108
pdf_url: https://arxiv.org/pdf/2610.24108
published: '2026-10-16'
collected: '2026-10-20'
category: Agent
direction: Agent 多模态对齐范式选型
tags:
- Multimodal Alignment
- LLM Agent
- Model Selection
- Fusion Paradigm
- Transfer Learning
one_liner: 对比三类多模态对齐范式适用边界，提出预训练前选型路由，准确率71.4%
practical_value: '- 电商多模态推荐（图文/短视频+文本）场景可直接复用选型规律：小样本标注下优先选AGENT范式，标注充足时候选匹配类QA（如商品问答推荐）选JOINT范式，分类任务（如商品类目预测）若单模态5-NN准确率高选DECOUPLED范式，省掉反复试错成本

  - 可复用两步级联路由框架，先判断用AGENT还是融合范式，再选JOINT/DECOUPLED，基于少量标注数据的表征诊断即可提前锁定最优架构，无需全量训练所有候选范式

  - 搭建电商多模态Agent时，优先给LLM喂原始文本（如商品标题、用户Query），再补充单模态readout输出，部分场景纯LLM效果优于带readout的完整AGENT架构，可大幅降低推理成本'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
多模态系统已广泛应用于推荐、QA等业务场景，但从业者缺乏明确的范式选型依据，只能靠试错选择联合预训练、解耦融合还是LLM Agent对齐方案，时间和算力成本极高，亟需明确不同范式的适用边界和可复用的选型方法。

### 方法关键点
- 定义三类对齐范式：JOINT（基于联合预训练的冻结双塔+任务融合头）、DECOUPLED（独立预训练的单模态冻结编码器+任务融合头）、AGENT（冻结LLM+单模态readout+推理时多源信息组合）
- 控制变量：所有范式匹配编码器架构和规模，仅改变对齐阶段，覆盖5个领域16个数据集、多种标注预算场景
- 提出两步级联选型路由：第一步基于文本诊断、任务元数据判断选AGENT还是融合范式，第二步基于单模态5-NN准确率等诊断特征选JOINT/DECOUPLED，可在训练候选模型前完成选型

### 关键结果
144组数据集-预算组合下三类范式各有优劣：DECOUPLED赢54次，JOINT赢44次，AGENT赢46次，无通用最优范式；标注量提升时ScienceQA、MELD等任务会从AGENT切换为融合范式，QA类任务普遍优先选JOINT，分类任务单模态5-NN准确率越高越适合DECOUPLED（Spearman ρ=-0.67）；路由模型在leave-one-group-out评估下选型准确率达71.4%，相对后悔度仅0.028，远优于仅用元数据的54.2%准确率、0.057后悔度。

### 核心结论
多模态对齐没有万能范式，可通过任务格式、标注预算、单模态表征可分性三个维度快速锁定最优方案，无需盲目试错。
