---
title: 'MidTool: Mid-training Data Synthesis for Agentic Tool Use'
title_zh: MidTool：面向智能体工具使用的训练中期数据合成方法
authors:
- Fengqing Jiang
- Yite Wang
- Boyi Liu
- Zhaoyang Wang
- Canwen Xu
- Zhewei Yao
- Radha Poovendran
- Yuxiong He
affiliations:
- University of Washington
- Snowflake
- University of North Carolina at Chapel Hill
arxiv_id: '2608.20314'
url: https://arxiv.org/abs/2608.20314
pdf_url: https://arxiv.org/pdf/2608.20314
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent工具使用 · 中期训练语料合成
tags:
- Tool Use
- Mid-training
- Data Synthesis
- LLM Agent
- Function Calling
one_liner: 构建20.3B token的通用工具使用中期训练语料，显著提升LLM下游工具调用与Agent能力
practical_value: '- 训练Agent工具调用能力时，可优先在中期训练阶段注入工具相关语料，而非仅依赖后续SFT/RL，能大幅降低后续微调的数据量需求与收敛难度。

  - 工具使用训练语料可复用双分支合成逻辑：从文档/代码等非结构化数据生成上下文锚定的轨迹，从真实API/MCP生成原生Agent轨迹，两者结合能同时提升工具调用准确率与跨域泛化性。

  - 语料构建可参考其分层过滤流程：先关键词/URL预筛，再轻量分类器做质量过滤，最后去重+基准泄漏校验，平衡语料规模与质量。

  - 小参数模型做工具调用优化时，可参考「中期训练注入通用工具能力→SFT对齐指令→RL强化交互能力」的流水线，小参数量级也能获得可观性能提升。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent的工具使用能力几乎完全依赖后期SFT/RL提升，不仅标注成本高，模型也很难从窄监督中同时习得工具识别、参数锚定、多步规划、错误恢复等原子能力。中期训练作为通用预训练到下游微调的中间阶段，已被证明能有效强化数学、代码等能力，但通用工具使用方向的专项中期训练方案仍处于空白。

### 方法关键点
- 数据源覆盖四类互补来源：网页、技术文档PDF、代码仓库、真实API/MCP技能，兼顾广度与结构化信息。
- 双分支轨迹合成：上下文锚定的轨迹增强分支从非结构化文档提取工具能力信息，生成QA与交互轨迹；原生Agent轨迹合成分支从可执行接口生成多轮交互轨迹，严格校验调用合法性、时序正确性、参数与返回一致性。
- 最终生成20.3B token的MidTool-Mix语料，网页占42%、PDF占23%、代码占26%、原生Agent轨迹占9%，统一为纯聊天模板无特殊控制符。

### 关键实验
在Qwen3-4B/8B Base模型上验证，基线为官方Qwen3模型、无中期训练直接SFT/RL的版本。结果显示：
- 相比无中期训练的基线，4B模型BFCLv3整体得分提升10.5个百分点，MCP-Universe通过率提升3.35个百分点，搭配RL后收益进一步扩大。
- 多轮工具调用场景收益最显著，4B模型BFCL多轮得分提升11.1个百分点，𝜏2-Bench整体Pass@1提升3.7个百分点。

### 核心结论
通用工具使用能力和其他LLM核心能力一样，能通过专项中期训练获得显著提升，而不需要完全依赖后期微调。
