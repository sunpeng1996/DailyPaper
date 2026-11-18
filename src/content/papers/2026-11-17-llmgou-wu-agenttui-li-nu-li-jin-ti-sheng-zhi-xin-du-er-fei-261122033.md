---
title: 'Thinking Harder Doesn''t Lead to Better Choices: Reasoning Effort Increases
  the Confidence but Not the Correctness of LLM Shopping Agents'
title_zh: LLM购物Agent推理努力仅提升置信度而非决策准确率
authors:
- Adi Krishnamoorthy
- X. Y. Han
affiliations:
- University of Chicago
arxiv_id: '2611.22033'
url: https://arxiv.org/abs/2611.22033
pdf_url: https://arxiv.org/pdf/2611.22033
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: LLM 购物Agent 推理效果评估
tags:
- LLM Agent
- Shopping Agent
- Reasoning Effort
- Calibration
- E-commerce
one_liner: 在三个电商基准上验证提升LLM推理努力不提高选品准确率，仅增强模型自信
practical_value: '- 搭建电商购物Agent无需盲目开启高推理档位，大部分场景下低推理参数即可满足需求，既降低推理成本，也避免模型过度自信导致错误决策不触发人工回退

  - 购物Agent选型优先参考模型校准度而非推理能力，Claude系列校准效果显著优于其他主流模型，可有效降低过度自信问题

  - 不要依赖单模型置信度或多模型投票校验决策正确性，不同LLM错误相关性高达0.7-0.8，投票一致性无法证明决策无错

  - 评估Agent效果需同时上报校准指标（ECE/Brier）和多推理档位结果，且需做多重比较校正，避免误判假阳性的准确率提升'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM购物Agent已被广泛用于自主选品、下单等场景，过往认知认为推理努力越高（更多推理token、更长CoT）决策质量越好，这一结论在数学、编程任务中已被验证，但电商选品核心是读取商品信息而非多步逻辑推导，推理努力的增益尚未验证；同时模型置信度校准直接决定用户对Agent的信任度，其与推理努力的关系也缺乏实证。

### 方法关键点
- 固定10个商品的候选集（含1个正确商品），排除搜索、导航环节干扰，所有模型在完全相同的输入下完成决策
- 覆盖10个主流前沿LLM，通过OpenRouter API统一控制`reasoning.effort`为低/中/高三档，统一使用相同prompt要求输出选品结果和0-10分的置信度
- 核心指标包含选品成功率、置信度变化、校准指标（ECE、Brier、AUROC）、跨模型错误相关性

### 关键结果
在WebShop（亚马逊多模态）、Amazon SQID（亚马逊多模态搜索）、Wayfair WANDS（文本家具搜索）三个基准上测试得到：
1. 低→高推理努力切换时，30组模型-数据集对中仅2组成功率在Holm校正后显著提升，但有38组置信度显著上升，推理努力仅带来更高自信而非正确率
2. 校准度是模型固有属性，与推理努力无关：Claude系列ECE比其他模型低6-21个百分点，其余模型普遍过度自信10-30个百分点
3. 不同模型错误相关性达0.7-0.8，80%以上的错误集中在同一个近漏选商品上，多模型共识无校验价值

最值得记住的结论：电商购物Agent场景下，选择校准度好的模型比拉高推理努力的收益高得多，模型自信、多模型一致都不能代表决策正确。
