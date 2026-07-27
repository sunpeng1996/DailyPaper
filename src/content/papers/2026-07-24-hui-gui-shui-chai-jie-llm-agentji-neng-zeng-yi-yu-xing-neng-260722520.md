---
title: 'The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents'
title_zh: 回归税：拆解LLM Agent技能增益与性能退化的底层原因
authors:
- Darshan Tank
- Baran Nama
affiliations:
- Sentient Labs
arxiv_id: '2607.22520'
url: https://arxiv.org/abs/2607.22520
pdf_url: https://arxiv.org/pdf/2607.22520
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent 技能可靠性优化
tags:
- LLM Agent
- Skill Library
- Agent Evaluation
- Skill Design
- Regression Tax
one_liner: 拆解LLM Agent技能的增益与退化效应，识别三类退化机制，量化回归抵消59%总增益
practical_value: '- 技能库评估不能仅看平均成功率，必须拆解增益、回归两类任务，避免上线后原本稳定的业务场景（如电商客服、运营自动化）出现不可预期的错误

  - 技能设计不要过度侧重中间执行流程，优先补充输入理解（grounding）校验、输出结果校验逻辑，比如电商报表Agent可加字段合法性校验、输出值与历史基线对比逻辑，大幅降低错误率

  - 需单独测试技能描述的上下文影响（osmosis效应），不要认为技能不被调用就不会影响结果，建议做无技能、仅放技能描述、完整技能库三组对照实验，排除不必要的描述干扰'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent技能库的评估仅依赖平均任务成功率，完全掩盖了技能引入会导致原本可完成的任务失败的「回归税」问题，既无法解释技能失效的底层原因，也无法指导高可靠技能库的设计，可能导致业务上线后出现大量不可预期的错误。
### 方法关键点
- 严格对照实验设计：固定任务集、模型、执行harness，仅变更技能库配置，将有无技能的配对任务结果分为四类：增益（无技能失败、有技能成功）、回归（无技能成功、有技能失败）、残留失败（均失败）、保留（均成功）
- 基于执行轨迹的归回退因框架，识别三类退化机制：skill-description osmosis（技能描述放入上下文即使不被调用也会偏移Agent行为）、grounding displacement（技能流程覆盖了Agent原本正确的输入理解）、verification displacement（技能流程抑制了Agent原本会执行的输出校验）
### 关键结果
在OfficeQA-Pro（94个金融文档问答）、SpreadsheetBench（392个真实Excel操作）两个基准上，覆盖3个模型-harness栈、4种技能库配置，共完成5832次运行。核心结果：
1. 总回归任务共324个，抵消了59%的总增益（553个），大多数技能库的性能优势来自更少的回归而非更多的增益
2. 72.8%的问答类回归来自grounding位移，17.3%来自osmosis效应
3. 给表格操作任务增加执行级输出校验，可恢复34%的公式类误判错误，大幅提升残留失败的修复率
### 最值得记住的结论
Agent技能的可靠性更多取决于输入理解和输出校验能力，而非中间执行流程的丰富度。
