---
title: 'Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments'
title_zh: 工具调用参数校验的推导缺口问题及DEREF优化方案
authors:
- Linhai Ma
- Yan Wang
- Lingfei Qian
- Yupeng Cao
- Victor Gutierrez Basulto
affiliations:
- The Fin AI, USA
- Yale University, USA
- Cardiff University, UK
arxiv_id: '2610.18497'
url: https://arxiv.org/abs/2610.18497
pdf_url: https://arxiv.org/pdf/2610.18497
published: '2026-10-12'
collected: '2026-10-15'
category: Agent
direction: Agent工具调用正确性校验
tags:
- Agent
- Tool-Call
- LLM-Judge
- Evaluation
- Reference-Guided
one_liner: 发现LLM Agent工具调用参数校验的推导缺口，提出DEREF方案无需改动现有Judge即可大幅提升准确率
practical_value: '- 电商/广告 Agent 工具调用（如查库存、算优惠、调投放接口）的参数校验可直接复用 DEREF 架构：用独立模型读全量对话/请求历史预生成参数参考值，无需改动现有校验
  Judge，落地成本低收益高

  - 做 LLM 自动评估（如生成式推荐的文案/商品合理性校验、Agent 行为奖励建模）时，不要让 Judge 从截断上下文自行推导结果，优先喂显式参考结论，可大幅降低默认参数、历史截断取值场景的误判率

  - 长对话 Agent 系统中，不要盲目给 Judge 喂全量上下文，参考 DEREF 设计先用大模型预萃取关键信息再喂给小 Judge，比直接扩 Judge
  上下文窗口的成本更低、速度更快、效果更好'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent 依赖工具调用实现复杂业务逻辑，参数错误是最常见故障点。现有参数校验 Judge（奖励模型、执行前守卫）存在**推导缺口**：当正确参数来自截断的历史返回、schema 默认值、格式转换/逻辑推导，未在 Judge 输入中显式出现时，正确参数的接受率比显式可见参数低 22~50 个百分点，即使将 Judge 参数量从 4B 升到 27B 也无法消除缺口，甚至会优先采信显式出现的错误值，导致 AUROC 跌到随机水平。
### 方法关键点
- 定义5类参数推导路径：`VISIBLE`（输入中显式存在）、`HISTORY-ONLY`（仅全量历史存在、输入截断）、`FORMAT`（格式转换后匹配）、`DEFAULT`（schema 默认值）、`NO-SOURCE`（无匹配来源）
- 提出 DEREF 方案：用独立 Deriver 模型（论文用 Qwen3.8-27B）读取全量对话历史与函数 schema，全程看不到待校验候选参数，预生成每个参数的预期取值与来源说明，插入到 Judge 输入中
- 无需对现有 Judge 做任何微调或改动，完全兼容现有校验链路
### 关键结果
在 FCRB、CFB、FinTrace 3个工具调用基准上测试7款主流 Judge（CLM、Jev、Qwen/Llama/Mistral 系列）：
- DEREF 对所有 Judge 的 AUROC 均有显著提升，相比此前最优方案 RevisEval 平均提升 1~6 个百分点
- 在正确值来源被截断的受控测试中，将所有 Judge 的 AUROC 从随机水平（<50%）提升至 98.40~99.59%
- 默认参数的正确接受率最高提升 50 个百分点

所有 LLM Judge 本质上是参考匹配器而非逻辑推理器，给显式参考比提升 Judge 规模、开推理、扩上下文窗口的投入产出比高得多
