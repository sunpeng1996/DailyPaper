---
title: 'Thinking Inertia: LLMs Keep Thinking When Told Not To'
title_zh: 思维惯性：被要求停止推理时LLM仍会输出显性推导内容
authors:
- Dianqiao Lei
- Kevin Qinghong Lin
- Pan Lu
- Philip Torr
- James Zou
affiliations:
- 清华大学
- 牛津大学
- 斯坦福大学
arxiv_id: '2610.11765'
url: https://arxiv.org/abs/2610.11765
pdf_url: https://arxiv.org/pdf/2610.11765
published: '2026-10-07'
collected: '2026-10-13'
category: LLM
direction: LLM可控推理 · 无推理行为评估
tags:
- LLM
- Reasoning Control
- Instruction Following
- Evaluation
- Thinking Inertia
one_liner: 提出LLM无推理行为三层评估框架，发现思维惯性效应，无推理效果受答案空间约束
practical_value: '- 做Agent/LLM应用的Prompt工程时，要求直接返回结果的场景（比如召回候选ID、商品标签判定），优先将问题设计为布尔/多选闭集形式，比开放提问更容易让LLM遵守仅输出结果的要求，减少后处理成本。

  - 需严格控制输出格式的业务场景（如广告关键词提取、搜索Query改写结果输出），不要仅依赖模型自带的无推理开关，可叠加「仅输出结果不要解释」的强指令，或直接使用前缀强制（如`{"推荐商品ID":
  [`），注意开放生成类任务会存在合规性与准确率的trade-off。

  - 评估LLM指令遵循能力时，不要仅用输出长度、是否有<think>标签作为无推理的判断标准，可参考论文的三层指标：空推理率、前缀内容相关性、显性推理率，避免把短推理或无关话术误判为无推理。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM普遍配备推理模式开关，但用户要求直接输出答案时，现有判定无推理的表面指标（关闭推理开关、无<think>标签、输出长度短）不可靠，LLM仍会输出显性推理内容，既增加token成本，又提升后处理难度，亟需可量化的无推理行为评估体系，明确LLM停止输出推理的边界条件。

### 方法关键点
1. 将LLM输出拆分为答案前文本T和最终答案A，定义三层递进评估指标：①Empty-Thinking Rate (ETR)：严格仅输出答案的样本占比；②Question-Pre-answer Relevance (QRel.)：用指令感知的Qwen3-Embedding-4B计算T与问题的语义相似度；③Explicit Inference Rate (EIR)：通过盲审LLM judge判断T中是否存在显性推理步骤。
2. 设计6级干预梯度，覆盖开启推理、原生关推理、软/硬无推理指令、前缀强制等不同管控强度。
3. 对比三类答案空间任务：布尔判断、多选、开放生成，排除任务难度干扰。

### 关键实验结果
测试6款主流LLM（Qwen3全系列、DeepSeek-V4、GPT-5.4、Gemini-3），跨6个基准数据集，核心结论：
1. 原生关推理模式下，布尔任务ETR达80~100%，多选任务ETR为0~95%，开放生成任务ETR接近0，且开放生成任务EIR高达99.9%。
2. 严格无推理指令可将开放生成任务的ETR从0提升到40%，但平均准确率下降15个百分点，存在明确的合规性-准确率trade-off。
3. 同一道题改成布尔/多选形式，比开放生成的ETR提升50%以上，EIR下降50%以上。

**最值得记住的结论**：LLM的无推理能力不由开关单独决定，而是受任务答案空间约束，闭集答案更容易实现无推理输出，开放生成场景下强制无推理会显著降低准确率。
