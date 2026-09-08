---
title: 'HarvestBench: Measuring Whether LLM Agents Will Pay to Avoid Killing Animals'
title_zh: HarvestBench：衡量LLM Agent是否愿意为避免伤害动物付出成本
authors:
- Jasmine Brazilek
- Miles Tidmarsh
- Matthias Endres
- Anshuman Singh
- Jeremiah Miller
affiliations:
- Compassion Aligned Machine Learning (CaML)
- Department of Economics, University of Warwick
arxiv_id: '2609.04444'
url: https://arxiv.org/abs/2609.04444
pdf_url: https://arxiv.org/pdf/2609.04444
published: '2026-09-02'
collected: '2026-09-08'
category: Eval
direction: LLM Agent 道德对齐评估
tags:
- Agent
- Benchmark
- Alignment
- LLM
- Evaluation
one_liner: 首个量化LLM Agent为避免伤害生物支付意愿的可复现农场仿真评估基准
practical_value: '- Agent对齐/合规评估可参考「行为量化而非文本问答」的范式，直接统计环境交互日志的结果，避免LLM自评的偏差，结果可复现性更强

  - 电商/广告场景的Agent合规性测试可借鉴「隐藏约束+成本选项」的设计，测试Agent在任务描述未明确提及规范时的违规概率，更贴近真实业务场景

  - 设计Agent行为约束时可优先验证提示词引导效果，该研究显示明确的规则提示可将违规率从84%降至6%以下，提示工程的投入ROI极高'
score: 4
source: huggingface-daily
depth: abstract
---

**动机**：现有Agent副作用评估基准未量化规避副作用的成本，也未将伤害对象设定为生物，无法真实反映Agent在隐性约束下的决策偏好与道德对齐水平。
**方法关键点**：搭建农场网格仿真环境，LLM Agent控制拖拉机完成收割任务，遇到动物拦路时可选择无成本碾压、或支付燃油成本绕行；设置岩石（损坏设备）、干草堆（无生命无伤害）作为对照组，新增偷取邻地庄稼的次级道德测试；全程通过游戏日志自动统计结果，无LLM grader，完全可复现。
**关键结果数字**：9款模型共7201次定价决策中，动物杀伤率区间为0.4%~98.8%，与模型能力无正相关；4/6模型的杀伤率对绕行成本敏感，弹性范围0.09~1.69；所有模型碾压野生动物的概率高于养殖动物；明确加入道德提示后，6款推理模型中5款杀伤率降至6%以下，移除提示后所有模型杀伤率均超过84%。
