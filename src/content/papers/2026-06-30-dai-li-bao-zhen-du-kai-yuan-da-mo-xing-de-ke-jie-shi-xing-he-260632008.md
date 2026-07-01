---
title: 'Surrogate Fidelity: When Can Open LLMs Explain Closed Ones?'
title_zh: 代理保真度：开源大模型的可解释性结论何时可迁移至闭源模型
authors:
- Philippe Chlenski
- Zachariah Carmichael
- Ayush Warikoo
- Chia-Tse Shao
- Yingxiao Ye
- Aobo Yang
- Vivek Miglani
- Nehal Bandi
affiliations:
- Meta
arxiv_id: '2606.32008'
url: https://arxiv.org/abs/2606.32008
pdf_url: https://arxiv.org/pdf/2606.32008
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: 大模型可解释性 · 开源闭源模型迁移
tags:
- LLM Interpretability
- Surrogate Fidelity
- Model Attribution
- Black-box LLM
- Open LLM
one_liner: 跨11款大模型验证开源-闭源可解释性迁移边界，明确预测一致性不足以支撑归因结论迁移
practical_value: '- 调优基于闭源LLM的推荐/广告prompt时，不要直接复用同类型开源模型的白盒归因结论，优先用黑盒输入消融法做实际验证，避免归因错误影响业务效果

  - 若用开源模型做闭源LLM的预研验证，不能仅看预测准确率对齐，必须补充归因层面的一致性校验，确保推荐理由生成、广告投放归因等业务逻辑的可靠性

  - 对基于LLM的搜索推荐Agent做归因审计时，优先用API可获取的log-odds、leave-one-out消融归因做黑盒评估，无需强行获取模型白盒参数，降低对接与合规成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Mechanistic interpretability (MI)工具需访问模型内部参数，但主流商用LLM仅通过API暴露有限输出信息，开源模型的可解释性结论能否迁移到闭源模型缺乏定量验证标准。

### 方法关键点
搭建三级代理保真度评估框架，分别在预测层、归因层、表征层对比开源-闭源模型的一致性；针对二分类任务，采用API兼容的log-odds作为表征空间读出指标，用leave-one-out归因衡量模型行为逻辑；覆盖Llama、Qwen、GPT、Gemini四大模型家族共11款模型做验证。

### 关键结果
1. 预测保真度显著高估归因保真度，预测一致的样本中80%以上存在归因逻辑差异；
2. 注意力模式、扰动幅度等白盒信号跨模型稳定性达75%+，但对因果归因的预测性仅30%左右，黑盒输入消融法可更准确捕捉因果归因；
3. 仅预测层面的对齐不足以支撑可解释性结论跨模型迁移。
