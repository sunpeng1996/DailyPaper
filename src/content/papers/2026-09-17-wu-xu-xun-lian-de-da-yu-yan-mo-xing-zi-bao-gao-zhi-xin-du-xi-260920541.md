---
title: An Analysis of Training-Free Self-Reported Confidence in Language Models
title_zh: 无需训练的大语言模型自报告置信度效果分析
authors:
- Lukas Meyer
- Sofia Rossi
- Wei Chen
- Thomas Laurent
- Yiming Li
affiliations:
- DreamAI
arxiv_id: '2609.20541'
url: https://arxiv.org/abs/2609.20541
pdf_url: https://arxiv.org/pdf/2609.20541
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 大语言模型置信度评估 · 无训练方法
tags:
- LLM-confidence
- training-free
- black-box-evaluation
- factuality
- calibration
one_liner: 实测三类无需训练的LLM置信度信号效果，指出信号不可互换、多轮一致投票可能放大固有错误
practical_value: '- 用黑盒LLM生成商品文案、推荐理由、Agent回答时，优先选择输出同步生成的verbalized confidence做风险过滤，其正确性预测AUROC最高可达0.956，性价比远高于后验自评估、多轮采样一致方案

  - 不要将多轮采样一致性作为正确性唯一判定依据，同一LLM的多次生成可能重复共同错误，实测4/9的错误会获得3轮采样全票支持

  - 置信度决策阈值要与对应prompt绑定，等价语义的不同prompt会导致置信度平均偏移0.043~0.084，最高9%的样本会跨越0.8阈值，不可跨prompt复用阈值

  - 做LLM生成内容的事实性校验时，需先审计基准标签准确性，标签错误会导致置信度校准结果偏差可达3~4个百分点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：当前LLM生成内容被大量直接应用于电商文案、推荐理由、Agent交互等场景，置信度可用于分配有限的人工校验资源，但无训练的黑盒置信度信号的有效性、鲁棒性缺乏系统性实测，不同信号是否等价、是否受prompt干扰等问题没有明确结论。

**方法关键点**：
- 采用纯黑盒无训练设定，仅依赖prompt和少量采样，不访问logit、隐状态，不做任何微调
- 对比三类置信度信号：输出同步的verbalized confidence、固定答案后的后验P(True)、3次额外生成的一致性得分，以及两类信号的固定平均组合
- 覆盖两类任务：100条TriviaQA短问答、100条人物传记长文本claim级校验，所有标签均经过人工审计修正

**关键实验结果**：
短问答任务中，同步verbalized confidence的正确性预测AUROC达0.956（DeepSeek Flash）、0.937（Claude Sonnet 5），远高于3样本一致性的0.765、0.790；4/9的DeepSeek错误、2/8的Sonnet错误获得3次采样全票支持，一致性会放大模型固有误解；固定答案用等价prompt重提置信度，得分平均偏移0.043~0.084，4%~9%的样本跨越0.8决策阈值；标签审计可将模型准确率评估结果提升3~4个百分点，大幅修正校准偏差。

**最值得记住的结论**：置信度仅适合作为外部校验的触发信号，不能把单次置信度输出或模型生成一致性当作正确性的证明。
