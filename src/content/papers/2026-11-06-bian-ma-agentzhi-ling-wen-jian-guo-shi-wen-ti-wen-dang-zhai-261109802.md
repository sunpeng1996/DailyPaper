---
title: 'When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding
  Agents'
title_zh: 编码Agent指令文件过时问题：文档债务与隐性成本
authors:
- Tural Mehtiyev
- Biruk Tadesse
- Lawrence Arkoh
- Wesley Assunção
affiliations:
- North Carolina State University
arxiv_id: '2611.09802'
url: https://arxiv.org/abs/2611.09802
pdf_url: https://arxiv.org/pdf/2611.09802
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: 编码Agent · 文档债务成本评估
tags:
- CodingAgent
- DocumentationDebt
- StaleInstruction
- AgentTrajectory
- LLM4Code
one_liner: 通过732次受控实验证明编码Agent过时指令会产生隐性开销，且任务成功率无法识别该问题
practical_value: '- 企业内部业务Agent的system prompt/知识库文档需新增过期校验，尤其是高频访问的操作路径（如推荐系统埋点查询、AB实验提交脚本、广告素材审核规则），避免无效工具调用浪费算力

  - 评估Agent效果不能仅看最终任务成功率，需新增轨迹级指标（工具调用次数、无效请求占比、token消耗），才能发现隐性成本

  - 修正过时的Agent引导指令比直接删除效果更好，直接删除会导致Agent自行摸索路径，反而可能增加额外开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM编码Agent广泛依赖仓库根目录的AGENTS.md/CLAUDE.md等指令文件完成任务，但这类文档容易随代码迭代过时，现有评估体系仅关注最终任务成功率，完全无法发现这类文档债务带来的隐性成本，比如额外工具调用、无效操作、token浪费。

### 方法关键点
- 选取3个真实开源仓库的过时指令案例，分别对应测试命令、代码位置、组件添加流程三类常见引导
- 每个任务设置三组对照：指令保持过时、指令修正为当前正确路径、完全删除该条指令，代码和任务完全固定
- 测试Claude Haiku 5.5、Claude Sonnet 5.5两个模型，共采集732条Agent运行轨迹，逐工具调用分析行为

### 关键结果
- 任务成功率几乎不受过时指令影响，所有条件下bug修复率均接近100%
- Claude Sonnet 5.5面对过时测试命令时，单轮平均多产生2次工具调用，比修正指令场景开销高33%
- 过时指令仅当任务需要该指令对应能力时才会产生影响，三类案例的过时路径调用率分别为97.5%、68.75%、0%
- 所有Agent运行中均未主动修复过时指令文件，即使发现问题也仅自行绕过

**最值得记住的一句话：Agent的隐性成本藏在运行轨迹里，仅看最终输出的评估体系会忽略大量可优化的开销**
