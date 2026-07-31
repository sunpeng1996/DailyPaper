---
title: 'Beyond a Single Judge: Simulating Social Persona Panels for Generative UI
  Evaluation'
title_zh: 面向生成式UI评估的社会角色模拟评审面板方法
authors:
- Zheng Wu
- Yibo Luo
- Pu Zhang
- Cheng Yang
- Zhuosheng Zhang
affiliations:
- School of Computer Science, Shanghai Jiao Tong University
- ByteDance Inc
arxiv_id: '2607.28439'
url: https://arxiv.org/abs/2607.28439
pdf_url: https://arxiv.org/pdf/2607.28439
published: '2026-07-30'
collected: '2026-07-31'
category: Eval
direction: 大模型评估 · 多角色模拟评审
tags:
- LLM-as-judge
- Evaluation
- Persona
- Generative UI
- Alignment
one_liner: 三阶段ESPP多角色评审框架，大幅提升生成式UI评估与人类判断的匹配度
practical_value: '- 电商/广告生成素材、生成式活动页/商详页的自动评估场景，可直接复用ESPP三阶段框架替换单一LLM-as-judge，提升评估结果与真实用户感知的对齐度

  - 需要挖掘不同用户群对生成内容的偏好差异时，可保留各persona的单独评分，定位不同人群对内容/UI维度的偏好分歧，指导生成结果的人群定向优化

  - 语义门限bounded-confidence意见交互机制、Delphi权重聚合策略可直接迁移到多Agent评审、多LLM打分融合场景，降低单一模型的评估偏差'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
生成式UI（GenUI）可直接基于自然语言生成可渲染界面，但现有评估方案存在明显缺陷：人工评估成本高、标注差异大；单一LLM-as-judge仅能反映单一视角，无法匹配不同用户群体对同一款界面的感知差异。
### 方法关键点
三阶段ESPP评估框架流程：1）基于心理维度构建多样化、evidence-grounded的persona评审团独立打分；2）基于角色特质的语义门限bounded-confidence机制实现评审意见交互；3）参考Delphi法的社会权重聚合得到最终评分。
### 关键结果
与朴素单轮LLM评审相比，ESPP与人类判断的Pearson $r$从0.716提升至0.922；提示集成对照组仅能补全约1/3的效果差距，证明角色多样性和证据支撑是效果提升的核心来源；保留单评审员评分可挖掘用户子群的偏好分歧，为单一评审方法无法捕捉的关键信息。
