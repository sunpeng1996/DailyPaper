---
title: 'Anchor and Check: Deterministic Cross-Prompt, Cross-Model Reconciliation for
  Auditable LLM Decisions'
title_zh: 锚定校验：面向可审计LLM决策的跨提示跨模型确定性对齐方案
authors:
- Sivakameswara Reddy Chejarla
arxiv_id: '2611.25818'
url: https://arxiv.org/abs/2611.25818
pdf_url: https://arxiv.org/pdf/2611.25818
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM可信决策 · 可审计校验
tags:
- LLM Hallucination Detection
- Auditable LLM
- Semantic Entropy
- Uncertainty Estimation
- Deterministic Guardrail
one_liner: 用锚定加跨路径贪心校验的轻量方案，实现可审计低成本的LLM决策错误检测
practical_value: '- 做LLM驱动的业务决策（如商品审核、营销文案合规校验、Agent动作决策）时，优先用跨模型/跨提示的贪心校验替代同模型多温度采样，错误检测AUROC可提6.5个百分点，成本降60%以上

  - 需要可审计的LLM业务流程（比如广告投放物料审核、用户申诉自动判定）可直接复用该契约框架：固定锚点+结构化校验规则+可重放审计日志，无需复杂阈值调优

  - 电商/推荐场景中做LLM召回结果校验时，可复用跨路径错误解耦思路：用小参数peer模型或改写prompt的校验替代多采样，既能降低幻觉，又能控制推理成本

  - 小参数量LLM部署（如端侧推荐理由生成）场景下，同模型多采样语义熵效果优于跨模型校验，不要盲目复用该方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于多采样的LLM置信度评估方案（如self-consistency、Semantic Entropy）推理成本高、决策随采样波动不可复现、无明确审计链路，无法满足需要自动执行、可追溯的LLM业务流水线需求。

### 方法关键点
- 锚定机制：固定目标模型贪心解码结果为唯一锚点，不随校验采样变动，确保决策输出稳定
- 校验设计：仅用1-2个贪心校验样本，分别来自同模型改写prompt、同量级异架构模型两条独立路径，避免同模型错误耦合
- 对齐契约：纯函数式对齐逻辑，按决策字段类型（数值/分类/短文本/结构化）预设归一化匹配规则，输出5种明确结果，仅全一致结果自动执行，其余转人工审核
- 审计链路：全链路记录原始样本、规则版本、决策结果，支持100%重放校验

### 关键实验
在GSM8K、MMLU、TriviaQA等6个基准任务共48000次模型调用上验证：3调用（锚点+改写prompt+异架构模型）方案错误检测AUROC达0.852，比单模型5采样Semantic Entropy高2.9个百分点，成本仅为其29%；严格自动放行策略下可覆盖70%请求，自动放行错误率仅5.4%，16%的错误会被漏放。

### 核心结论
LLM校验中，采样的来源多样性比采样数量重要得多，跨模型/跨路径的1次贪心校验效果远好于同模型的多次温度采样
