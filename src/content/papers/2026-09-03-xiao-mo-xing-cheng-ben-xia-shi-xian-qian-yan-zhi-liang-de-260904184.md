---
title: Toward Frontier-Quality Declarative UI Generation at Small-Model Cost
title_zh: 小模型成本下实现前沿质量的声明式UI生成
authors:
- Yingxiang Yang
- Weihang Xiao
- Ben Bullough
- Tushar Deshpande
- Niresh Agarwal
affiliations:
- Amazon
- Cornell University
arxiv_id: '2609.04184'
url: https://arxiv.org/abs/2609.04184
pdf_url: https://arxiv.org/pdf/2609.04184
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: 小模型调优 · 声明式UI生成
tags:
- SFT
- LoRA
- Small Language Model
- LLM-as-judge
- Data Augmentation
- Declarative UI
one_liner: 通过三组可控设计消融，用4B小模型实现接近前沿大模型的声明式UI生成效果，成本降10倍以上
practical_value: '- 做Agent工具调用/动态组件拼装类任务（如电商个性化推荐页生成、广告模板绑定）时，可复用Perturbed-catalog数据增强策略：训练时随机打乱、丢弃、重命名候选组件/工具条目，迫使模型学习读取当前可用候选集而非记忆固定词汇，提升OOD泛化能力

  - 若结构化输出的准确率是核心指标（如电商商品属性绑定、用户权益路径校验），优先选择Constrained-GT策略：限制输出复杂度、降低重命名率，可将OOD下的路径绑定准确率提升10pct以上，幻觉率降至1%以内

  - 小模型SFT落地时无需人为限制输出候选集（如商品库、组件库大小），实验显示哪怕0.8B小模型也能从~100量级的候选集中获得单调效果提升，无需为适配小模型削减业务能力

  - 成本敏感的生成类场景可参考其成本-质量权衡：4B量级LoRA微调小模型可达到前沿大模型97%以上的效果，成本降1个数量级，延迟降2-3倍，适合动态UI、个性化落地页等生产场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前声明式UI（如A2UI）是Agent输出交互界面的主流落地方案，具备安全、一致性高的优势，但前沿大模型调用成本高、延迟大，原生小模型质量不达标，行业缺乏针对该场景的SFT数据策略、模型尺寸、组件库大小三者的权衡参考，落地难度高。
### 方法关键点
- 对比三种SFT数据构造策略：Full-catalog基线（固定全量组件库）、Perturbed-catalog（训练时随机打乱/丢弃/20%重命名组件库，同步修改标签）、Constrained-GT（5%低重命名率，限制输出组件数量，降低目标复杂度）
- 覆盖Qwen 3.5 0.8B/2B/4B、SmolLM 3B共4款小模型，全部采用LoRA微调（r=8，lr=5e-5，4 epoch）
- 评估维度覆盖解析成功率、组件幻觉率、数据路径绑定准确率，搭配LLM-as-judge的语义/视觉质量打分，同时做跨模型校验和人工标注校准保证可信度
### 关键结果
- 实验覆盖两个业务域：任务管理场景（86组件库，1500条样本）、云管理控制台场景（47组件库），分别设置ID、OOD（新增未训练组件）测试集
- 4B参数Perturbed-catalog微调模型可恢复98%的教师模型语义质量、97%视觉质量，成本比前沿API低1个数量级，延迟比Claude Sonnet低2-3倍
- 两种增强策略均帕累托优于基线：Perturbed-catalog语义质量最优，Constrained-GT OOD下路径绑定准确率达98.1%，比基线高40pct以上
- 组件库从10个扩容到86个时，所有尺寸模型的质量均单调提升，0.8B小模型也能充分利用全量组件库
### 核心结论
小模型微调的落地效果上限很大程度由数据构造策略决定，针对场景特性做数据增强，远好过盲目堆模型参数
