---
title: 'From Passive Response to Proactive Correction: Enhancing LLM Robustness Against
  Input Fact Perturbations'
title_zh: 从被动响应到主动纠错：提升LLM对输入事实扰动的鲁棒性
authors:
- Ping Wang
- Xiangguo Sun
- Bingbing Xu
- Guocong Li
- Xiaofeng Meng
affiliations:
- Renmin University of China
- Southeast University
- Zhejiang University
arxiv_id: '2608.25894'
url: https://arxiv.org/abs/2608.25894
pdf_url: https://arxiv.org/pdf/2608.25894
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 大语言模型 · 输入事实扰动鲁棒性优化
tags:
- Hallucination Mitigation
- Fact Perturbation
- Proactive Correction
- LLM Robustness
- Benchmark
one_liner: 提出三阶段DEDUCE框架与MisFactQA基准，增强LLM对输入事实扰动的纠错与鲁棒性
practical_value: '- 电商客服/导购Agent可复用DEDUCE的原子事实拆解+校验逻辑，识别用户带错误前提的咨询（如误认产品参数），先纠正错误再回答，避免顺着错误内容翻车

  - 生成式推荐/商品问答场景可直接复用三角色（生成者/评审者/仲裁者）策略审议机制，无需额外训练即可降低被用户错误输入误导的概率

  - 搭建业务错误输入评估基准时，可参考MisFactQA的构建方法与MR/CR/CS三类指标，比单纯看回答准确率更全面衡量模型鲁棒性

  - 延迟不敏感场景优先用DEDUCE-Prompting零成本适配现有LLM，延迟敏感场景用DEDUCE-Tuning通过两阶段LoRA微调内化逻辑，兼顾效果与效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM幻觉缓解方案默认用户输入可靠，但实际场景中用户常因认知偏差输入带错误前提、内部矛盾、复合错误的内容，哪怕LLM本身具备正确知识，也会被误导生成错误回答。实验显示Qwen2.5-7B、Llama3.1-8B面对带事实扰动的输入时，准确率下降30~60个百分点，现有方案要么忽略错误传播错误信息，要么自校正时被输入带偏，同时缺乏对应评测基准与细粒度指标。

### 方法关键点
- 三阶段DEDUCE框架：①Detect：将输入拆解为最小可验证原子事实，逐一校验事实准确性、两两校验一致性，输出错误诊断摘要；②Devise：通过生成者（输出校正策略）、评审者（排查策略漏洞）、仲裁者（综合输出最终策略）三角色多视角审议，避免单模型校正偏差；③Correct：按策略分步执行，先明确指出输入错误，再给出校正依据，最后输出正确回答。
- 两种落地方案：DEDUCE-Prompting无需训练直接调用，DEDUCE-Tuning通过两阶段LoRA微调把校正逻辑内化到模型参数，降低推理成本。
- 构建MisFactQA基准，覆盖单错误前提、内部矛盾、复合错误三类输入，提出Misleading Rate（误导率）、Correction Rate（校正率）、Clarification Score（澄清得分）三类细粒度评测指标。

### 关键实验
在TruthfulQA、FalseQA、MisFactQA三个数据集上对比ICL、CoT、LoRA微调、IAQ-FA等基线，DEDUCE在各模型家族上均取得最优效果：Gemma3-12B上FalseQA准确率比最优基线高25.99个百分点，Llama3.1-8B上MisFactQA误导率从57.49%降到10.87%，校正率从36.23%提升到79.35%，且比CoT、IAQ-FA等方案token消耗更低，准确率-效率tradeoff更优。

**最值得记住的一句话**：哪怕LLM本身知识正确，用户输入的事实扰动也会大幅拉低回答准确率，仅靠优化模型生成端的幻觉缓解方案不足以解决问题，必须前置做输入事实校验与主动校正。
