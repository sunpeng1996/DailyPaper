---
title: What If Chain-of-Thought Is Not Enough?
title_zh: 当思维链效果不足时：基于QOC结构化决策的LLM推理优化
authors:
- Marc Jansen
affiliations:
- University of Applied Sciences Ruhr West, Germany
arxiv_id: '2611.26282'
url: https://arxiv.org/abs/2611.26282
pdf_url: https://arxiv.org/pdf/2611.26282
published: '2026-11-19'
collected: '2026-11-20'
category: Reasoning
direction: 结构化推理 · QOC替代CoT优化决策效果
tags:
- Chain-of-Thought
- QOC
- Structured Reasoning
- Fine-tuning
- LLM Reasoning
- Explainable AI
one_liner: 通过微调让LLM内化QOC结构化决策逻辑，效果与可解释性均优于同尺寸CoT基线
practical_value: '- 电商推荐/广告多目标排序场景可复用QOC框架，将决策问题、候选集、评估指标（转化率、毛利率、用户满意度等）拆解为结构化推理步骤，提升排序可解释性，同时便于业务规则直接干预

  - 端侧小模型推理优化可参考分层适配结论：10B以下小模型适合用轻量化QOC结构（仅核心排序输出，无需额外解释层），可在不增加推理延迟的前提下提升效果，实测同尺寸小模型QOC微调后偏好率较基线提升66%~98%

  - Agent决策模块可直接替换原有CoT推理逻辑为QOC结构，将候选动作、评价维度、权重配置显式化，降低Agent决策幻觉，同时便于后续审计决策过程'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前CoT推理多为自由形式，决策过程不透明，在需要可解释性、可审计性的决策支持场景（如电商选品、广告投放、用户权益决策）中难以满足业务合规与干预需求，且小模型执行CoT的稳定性差、效果天花板低，亟需更适配决策场景的结构化推理范式。

### 方法关键点
- 提出Question-Option-Criteria（QOC）结构化决策框架，将推理拆分为明确决策问题、枚举候选选项、定义评估准则、给准则分配权重、给每个选项按准则打分、加权求和选最优6个步骤，全程可追溯可校验
- 设计三代迭代架构：Gen1仅输出最优选项，Gen2增加自然语言解释层，Gen3额外加入统计指标（如得分标准差）提升解释丰富度
- 训练流程：先用大模型生成带QOC结构的合成监督数据，再对目标LLM做微调，让模型内化QOC推理逻辑

### 关键实验
- 数据集：100条跨领域决策类benchmark，基线为同尺寸未微调的Qwen3.5系列模型（0.8B~27B）
- 内部一致性：27B微调模型QOC计算正确率达95%，9B达87%，4B达65%，<2B小模型计算正确率不足15%
- 效果对比：同尺寸对比下，QOC微调模型被LLM-as-a-Judge偏好的比例分别为0.8B 98%、2B 87%、4B 82%、9B 79%、27B 61%，全部统计显著；4B QOC微调模型效果与27B基线无显著差异

### 核心结论
LLM的内部推理范式不是固定的，可通过微调针对任务特性定制结构化思考模型，小模型适配轻量化结构、大模型适配复杂结构的分层设计能实现效果与成本的最优平衡
