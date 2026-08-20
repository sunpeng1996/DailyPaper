---
title: A Theory of Post-hoc Debate Judgement
title_zh: 事后辩论判决的理论框架与实验验证
authors:
- Xiang Yin
- Adam Dejl
- Antonio Rago
- Lihu Chen
- Francesca Toni
affiliations:
- Imperial College London
- King's College London
arxiv_id: '2608.19002'
url: https://arxiv.org/abs/2608.19002
pdf_url: https://arxiv.org/pdf/2608.19002
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: Agent多智能体辩论判决优化
tags:
- Multi-Agent-Debate
- LLM-as-Judge
- Argumentation-Semantics
- QBAF
- DF-QuAD
one_liner: 提出辩论判决的7项形式化属性，验证计算论证语义相比LLM法官属性满足度更高且精度相当
practical_value: '- 做多智能体协同决策（如多Agent召回结果融合、商品内容真实性核验）时，可优先选用计算论证语义（如DF-QuAD）替代LLM直接作为法官，在精度相当的前提下大幅降低输出波动、位置偏差、幻觉问题

  - 辩论类Agent系统的评估不要只看准确率，可参考论文提出的7项形式化属性（确定性、排列独立性、鲁棒性等）做更全面的稳定性、可解释性校验

  - 电商场景下的评论立场聚合、虚假宣传判别等任务，可将用户/审核Agent的正反观点建模为QBAF结构，用DF-QuAD语义快速得到可解释的判决结果，算力成本远低于多次调用LLM'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多智能体辩论框架多聚焦辩论生成环节，对事后判决的研究较少，主流LLM-as-Judge方案存在输出不稳定、位置偏见、幻觉、无形式化可解释性等问题，高风险场景下仅靠准确率无法满足要求，亟需体系化的辩论判决评估标准与更可靠的判决方法。

### 方法关键点
- 定义7项辩论判决的通用形式化属性：确定性、排列独立性、输入鲁棒性、方法鲁棒性、无幻觉、一致性、可争议性，作为判决方法的评估维度
- 对比两类判决方法：1）GPT-4o作为LLM法官；2）基于量化双极论证框架（QBAF）的DF-QuAD语义法官，将辩论的正反观点建模为带基础分的支持/攻击节点，通过固定公式计算最终立场
- 覆盖单轮独立输出、多轮交互辩论两类场景，测试匿名/非匿名、观点单独输入/合并输入等多种配置

### 关键实验
采用500条真假平衡的公开声明验证数据集，用3个异构Agent（GPT-4o-mini、Llama-3.3-70B、Qwen3.5-9B）生成辩论内容。实验结果：两类法官精度相当，最高分别为75.00%（LLM）和76.00%（DF-QuAD）；DF-QuAD的属性满足度全面占优：100%满足确定性、排列独立性、可争议性，非幻觉率最高99.60%，一致性满足率最高99.39%，输入扰动下精度波动仅0.2%-0.4%，远低于LLM的1.6%-2.4%。

### 核心结论
计算论证语义是辩论驱动AI系统中原则化法官的理想候选，在精度相当的前提下可提供稳定、可解释、低幻觉的判决能力。
