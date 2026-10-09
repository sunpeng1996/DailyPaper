---
title: Predicting Alignment Generalization with Value Representations
title_zh: 基于值表示的大语言模型对齐泛化预测方法
authors:
- Andy Liu
- Mehar Bhatia
- Karolina Stanczak
- Mona Diab
- Vered Shwartz
- Daniel Fried
affiliations:
- Carnegie Mellon University
- Mila - Quebec AI Institute
- McGill University
- ETH Zurich
- University of British Columbia
arxiv_id: '2610.12410'
url: https://arxiv.org/abs/2610.12410
pdf_url: https://arxiv.org/pdf/2610.12410
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: LLM对齐 · 值表示与泛化预测
tags:
- LLM Alignment
- Value Representation
- Generalization Prediction
- Model Robustness
- Value Taxonomy
one_liner: 提出基于模型激活的值表示方法预测LLM对齐泛化，验证其在鲁棒性预测、值分类的有效性
practical_value: '- 做Agent角色/对齐设定时，不要仅靠文本描述定义特质，改用persona向量衡量不同特质的兼容性，可提前预判训练后的行为漂移，比如电商客服Agent训练"热情"特质前，先排查是否会触发过度承诺的负面泛化

  - 做多目标SFT/DPO训练时，用值表示的平均相似度计算对齐目标的一致性，优先选择一致性高的目标组合，可提升模型抗prompt注入/越狱的鲁棒性，比如电商导购Agent同时训练"专业""诚信""高转化"目标前先做一致性校验

  - 批量管理Agent行为边界时，可复用VALUEMAP聚类方法对自定义特质做分类，比文本语义聚类更贴合模型实际行为规律，降低特质冲突的排查成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM对齐训练依赖离散的价值观/行为目标清单，对单目标训练的跨目标泛化规律认知不足，常出现预期外的行为漂移（如训练共情导致支持阴谋论），且对齐目标设计依赖经验判断，全组合训练验证成本极高。
### 方法关键点
- 定义对齐泛化预测任务：预测微调某单一值时，模型对未训练值的依从度变化
- 对比5类值表示方法：文本描述嵌入、行为句子嵌入、权重差异、persona向量（模型对正反值响应的激活差）、梯度更新方向
- 构建2类值数据集：66个来自Anthropic宪法的对齐值（CONSTITUTION）、266个真实人机交互野生值（VITW）
- VALUEMAP值分类pipeline：基于persona向量聚类，生成贴合实际泛化规律的LLM值分类体系
### 关键结果
- 基于激活的persona向量预测泛化的Spearman ρ达0.45，远高于文本描述嵌入的0.05
- 对齐目标的persona向量平均相似度（一致性）与模型抗prefill注入鲁棒性的相关性ρ达0.43，文本描述相关性仅0.12
- VALUEMAP分类调整轮廓系数达2.61，远高于现有文本聚类方法的0.95
### 核心结论
LLM对齐泛化由行为层面的底层激活模式驱动，而非值的文本语义，量化激活表示可大幅降低对齐目标设计的试错成本
